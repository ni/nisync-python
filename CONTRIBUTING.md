# Contributing to nisync-python 

Contributions to nisync-python are welcome from all!

nisync-python is managed via [git](https://git-scm.com), with the canonical upstream
repository hosted on [GitHub](https://github.com/ni/nisync-python/).

nisync-python follows a pull-request model for development.  If you wish to
contribute, you will need to create a GitHub account, fork this project, push a
branch with your changes to your project, and then submit a pull request.

Please remember to sign off your commits (e.g., by using `git commit -s` if you
are using the command line client). This amends your git commit message with a line
of the form `Signed-off-by: Name Lastname <name.lastmail@emailaddress.com>`. Please
include all authors of any given commit into the commit message with a
`Signed-off-by` line. This indicates that you have read and signed the Developer
Certificate of Origin (see below) and are able to legally submit your code to
this repository.

See [GitHub's official documentation](https://help.github.com/articles/using-pull-requests/) for more details.

# Getting Started

To contribute to this project, it is recommended that you follow these steps:

1. Ensure you have [poetry](https://python-poetry.org/) [installed](https://python-poetry.org/docs/#installation)
2. Fork the repository on GitHub.
3. Install **nisync** dependencies using ``poetry install``
4. Run the unit tests on your system (see Testing section). At this point, if any tests fail, do not
begin development. Try to investigate these failures. If you're unable to do so, report an issue
through our [GitHub issues page](http://github.com/ni/nisync-python/issues).
5. Write new tests that demonstrate your bug or feature. Ensure that these new tests fail.
6. Make your change.
7. Once the necessary changes are done, update the auto-generated code using ``poetry run python scripts/gen_templates.py``. This will ensure that the all code generated files are fresh.
8. Run all the unit tests again (including the tests you just added), and confirm that they all
pass.
9. Send a GitHub Pull Request to the main repository's master branch. GitHub Pull Requests are the
expected method of code collaboration on this project.

# Testing

In order to be able to run the **nisync** unit tests, your setup should meet the following minimum
requirements:

- Machine has a supported version of CPython or PyPy installed.
- Machine has [poetry](https://python-poetry.org/) installed.

To run the **nisync** unit tests in a specific version of Python, run the following command in the
root of the distribution:

```sh
$ poetry run pytest
```

# Developer Certificate of Origin (DCO)

   Developer's Certificate of Origin 1.1

   By making a contribution to this project, I certify that:

   (a) The contribution was created in whole or in part by me and I
       have the right to submit it under the open source license
       indicated in the file; or

   (b) The contribution is based upon previous work that, to the best
       of my knowledge, is covered under an appropriate open source
       license and I have the right under that license to submit that
       work with modifications, whether created in whole or in part
       by me, under the same open source license (unless I am
       permitted to submit under a different license), as indicated
       in the file; or

   (c) The contribution was provided directly to me by some other
       person who certified (a), (b) or (c) and I have not modified
       it.

   (d) I understand and agree that this project and the contribution
       are public and that a record of the contribution (including all
       personal information I submit with it, including my sign-off) is
       maintained indefinitely and may be redistributed consistent with
       this project or the open source license(s) involved.

(taken from [developercertificate.org](https://developercertificate.org/))

See [LICENSE](https://github.com/ni/nisync-python/blob/main/LICENSE)
for details about how nisync-python is licensed.
