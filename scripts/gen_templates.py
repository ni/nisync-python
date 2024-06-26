"""Extracts metadata from header files and generates Python API."""

import logging
import pathlib

import black
import CppHeaderParser
from mako.lookup import TemplateLookup

_logger = logging.getLogger(__name__)
_logger.addHandler(logging.NullHandler())


ROOT_DIR = pathlib.Path(__file__).parent.parent


def main():
    """Main function to generate templates based on specified input files."""
    # Template inputs
    errors_path = ROOT_DIR / "includes" / "errors.nimxl"
    headers = {"nisync.h": None, "internal.h": None}
    merged_defines = []
    merged_functions = []

    for header_name in headers:
        _logger.info("Processing header {}", header_name)
        parsed_header = CppHeaderParser.CppHeader(ROOT_DIR / "includes" / header_name)
        headers[header_name] = parsed_header
        merged_defines += parsed_header.defines
        merged_functions += parsed_header.functions

    input_data = dict(
        errors_path=str(errors_path),
        headers=headers,
        merged_defines=merged_defines,
        merged_functions=merged_functions,
    )

    templates_dir = ROOT_DIR / "templates"
    templates_metadata_dir = templates_dir / "_metadata"
    templates_nisync_dir = templates_dir / "nisync"

    for template_dir in [templates_metadata_dir, templates_nisync_dir]:
        for template in template_dir.glob("*.mako"):
            _logger.info("Generating template {}", template)
            output = ROOT_DIR / template.parent.name / template.stem
            output.parent.mkdir(exist_ok=True)
            lookup = TemplateLookup([template_dir])
            output.write_bytes(
                lookup.get_template(template.name).render(**input_data).encode("utf-8")
            )

            black.format_file_in_place(
                src=output,
                fast=False,
                mode=black.Mode(line_length=100),
                write_back=black.WriteBack.YES,
            )


if __name__ == "__main__":
    main()
