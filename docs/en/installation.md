# Installation

## Create and Activate a Virtual Environment

It is recommended to use a virtual environment for development:

```sh
python -m venv .venv
# On Linux/macOS:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate
```

## From Source

```sh
python -m pip install .
```

## From Wheel

First, build the wheel:

```sh
python -m pip install build
python -m build
```

Then install:

```sh
python -m pip install dist/mypackage-*.whl
```
