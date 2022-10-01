# Contributing to Brawl Box

Thanks for being interested in contributing to the Brawl Box project! There are two different ways of contributing, which are explained in further detail below.

Details about the tech stack, instructions for environment setup and configuration keys can be found in the [README file][readme-file].

There is a `#development` channel in the support server at [https://discord.gg/bXQaeFM][discord-support-server] dedicated to communication about the development process. For more information about contributing to Brawl Box, check in over there.

## Feature Request

While the feature set of Brawl Box is fairly complete, there are still ways improve the experience. For example, a command interface could be made more intuitive and user-friendly. Or, a background process that's responsible for fetching the required data could be optimised significantly.

The code in this version of Brawl Box is mainly designed and implemented by [Robin Mahieu][github-robinmahieu], nicknamed Papier. This causes a very opinionated approach throughout the source code, which may not always be the best one. A fresh look on things is always welcome!

## Bug Report / Fix

Upon discovering a bug, please [create an issue][github-issue]. This way, a core maintainer can confirm the problem and swiftly implement a fix. Alternatively, feel free to [submit a pull request][github-pull-request] with a short description of the bug and your proposed solution.

Please try to include

- the version number of Python, Brawl Box and dependency packages;
- the type and version of the operating system;
- instructions to reproduce the issue.

## Code Style

The Brawl Box project adheres to the [PEP 8][pep-8] code style guidelines, utilising [`black`][black] and [`flake8`][flake8] to enforce this. In particular, the usage of double quotes and a maximum line length of 79 characters is required.

Furthermore, the usage of full sentences and British English is preferred where applicable.

[black]: <https://black.readthedocs.io/en/stable/>
[discord-support-server]: <https://discord.gg/bXQaeFM>
[flake8]: <https://flake8.pycqa.org/en/stable/>
[github-issue]: <https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-an-issue>
[github-pull-request]: <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request>
[github-robinmahieu]: <https://github.com/robinmahieu>
[pep-8]: <https://www.python.org/dev/peps/pep-0008/>
[readme-file]: <https://github.com/nielsvv08/brawlbox/blob/main/README.md>
