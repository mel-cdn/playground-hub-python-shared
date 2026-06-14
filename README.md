# Playground Hub Python Shared Utilities

This repository is a supplement to a **DEV.to** article about **automating Python package releases to AWS CodeArtifact**
with **auto version bumping via Bitbucket pipelines**.

If you are into deployment pipelines, check it
out [here](https://dev.to/melcdn/automate-python-package-releases-semantic-release-aws-codeartifact-poetry-and-bitbucket-pipelines-95m).

## 🚀 Getting Started

### Prerequisites

- **Python**
    - Install [Python 3.12](https://www.python.org/)
- **Python Poetry**
    - Install [Poetry](https://python-poetry.org/docs/#installation)
- **Amazon Web Services (AWS) Account**
    - Install [AWS CLI](https://aws.amazon.com/cli/)

## 🧪 Development

```bash
# Clone project
$ git clone git@bitbucket.org:mello-world/phub-python-shared.git
$ cd phub-python-shared

# Install and activate Poetry
$ pip install poetry
$ eval $(poetry env activate)

# Install dependencies
$ poetry install --no-root

# Run unit tests
$ poetry run python -m pytest
```

## ✨ How to Commit

This project uses **Automated Semantic Versioning**. Version bumps, changelog generations, and deployments to AWS
CodeArtifact are entirely driven by your git commit messages.

You can refer to [Semantic Version](https://semver.org/) for more details.

### Commit Message Format

```text
type: Description of your changes
```

Must be one of the following lowercase structural keywords:

- `feat` -> Triggers a Minor version bump (e.g., 0.1.0 to 0.2.0). Use for new features.
- `fix` -> Triggers a Patch version bump (e.g., 0.1.0 to 0.1.1). Use for bug fixes.
- `chore`, `docs`, `style`, `refactor`, `test` -> Triggers a Patch version bump.
- `ci` -> Does not trigger any version bump.

See `pyproject.toml`: `tool.semantic_release.commit_parser_options` section for more details.

### Check Next Version

If ran locally this will bump the pyroject.toml version and add commit message and create tag

```bash
$ semantic-release version --print-tag
0.0.1
```