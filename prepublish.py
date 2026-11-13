#!/usr/bin/env python3
"""Check the latest published version before publishing."""

import json
import os
import subprocess
import sys
import tomllib
from functools import cache
from pathlib import Path
from typing import Any
from urllib.request import urlopen


# @todo Configure a pipeline to publish the package automatically after version checks, refer to:
#       https://github.com/ni/nisyscfg-python/blob/main/.github/workflows/publish.yml
ROOT_DIR = Path(__file__).resolve().parent
VENV_DIR = ROOT_DIR / ".venv"


@cache
def _load_project_metadata() -> dict[str, Any]:
    """Load project metadata from pyproject.toml."""
    with (ROOT_DIR / "pyproject.toml").open("rb") as pyproject_file:
        return tomllib.load(pyproject_file)


def get_project_metadata(key: str) -> str:
    """Read a value from the Poetry project section in pyproject.toml."""
    try:
        value = _load_project_metadata()["tool"]["poetry"][key]
    except (KeyError, TypeError) as error:
        raise ValueError(f"Could not find the project {key} in [tool.poetry]") from error
    return value


def get_project_name() -> str:
    """Read the Poetry project name from pyproject.toml."""
    return get_project_metadata("name")


def get_project_version() -> str:
    """Read the Poetry project version from pyproject.toml."""
    return get_project_metadata("version")


def get_latest_published_version(project_name: str) -> str:
    """Query PyPI for the latest published project version."""
    url = f"https://pypi.org/pypi/{project_name}/json"
    with urlopen(url, timeout=10) as response:
        payload = json.load(response)

    try:
        version = payload["info"]["version"]
    except (KeyError, TypeError) as error:
        raise ValueError("PyPI returned a response without a project version") from error

    return version


def prepare_virtual_environment() -> None:
    """Create .venv if needed, upgrade publishing tools, and build the package."""
    venv_python = VENV_DIR / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
    if not venv_python.is_file():
        print("Creating .venv...")
        subprocess.run([sys.executable, "-m", "venv", str(VENV_DIR)], check=True)
    else:
        print("Using existing .venv...")

    for package in ("pip", "build", "twine"):
        print(f"Upgrading {package} in .venv...")
        subprocess.run(
            [str(venv_python), "-m", "pip", "install", "--upgrade", package],
            check=True,
        )

    print("Building package in .venv...")
    subprocess.run([str(venv_python), "-m", "build"], cwd=ROOT_DIR, check=True)


def print_publish_instructions(project_name: str, project_version: str) -> None:
    """Show how to activate .venv if needed and upload the built distributions."""
    if Path(sys.prefix).resolve() != VENV_DIR.resolve():
        print()
        print("Activate the project .venv before publishing:")
        if os.name == "nt":
            print(r"  PowerShell: .\.venv\Scripts\Activate.ps1")
            print(r"  Command Prompt: .venv\Scripts\activate.bat")
        else:
            print("  source .venv/bin/activate")

    print("Publish with:")
    print(f"  python -m twine upload dist/{project_name}-{project_version}* --verbose")


def main() -> int:
    """Check the published version and prepare the publishing environment."""
    try:
        project_name = get_project_name()
        project_version = get_project_version()
        version = get_latest_published_version(project_name)
    except (OSError, ValueError) as error:
        print(f"Unable to check the latest published version: {error}", file=sys.stderr)
        return 1

    if project_version == version:
        print(f"The current version {project_version} has already been published.", file=sys.stderr)
        return 1

    print(f"Latest published version of {project_name}: {version}")
    print(f"Preparing to publish version {project_version}...")
    try:
        prepare_virtual_environment()
    except (OSError, subprocess.CalledProcessError) as error:
        print(f"Unable to prepare the publishing environment: {error}", file=sys.stderr)
        return 1

    print_publish_instructions(project_name, project_version)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
