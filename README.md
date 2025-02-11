# SQLAlchemy playground

This is a playground for SQLAlchemy.

## Setup and dependencies

You only need `uv`!
Refer to [this page](https://docs.astral.sh/uv/getting-started/installation/) for installation instructions.

If you have MacOS and `brew` installed, you can install `uv` with the following command:

```bash
brew install uv
```

## Running the tests

Tests are run with pytest, and are located in the `tests` directory.
You don't need to install pytest separately, it will be installed automatically
to your virtual environment when you run `uv run pytest` when missing.

```bash
uv run pytest
```


