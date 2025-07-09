# mypackage

[![codecov](https://codecov.io/gh/yourusername/mypackage/branch/main/graph/badge.svg)](https://codecov.io/gh/yourusername/mypackage)

Basic arithmetic operations on pandas DataFrames.

## File Structure

```
package-template/
├── docs/
│   ├── index.md
│   └── installation.md
│   └── development.md
│   └── api.md
│   └── usage.md
├── src/
│   └── mypackage/
│       ├── __init__.py
│       └── math_ops.py
│
├── tests/
│   ├── __init__.py
│   └── test_math_ops.py
│
├── example/
│   └── example_usage.py
│
├── README.md
├── LICENSE
├── pyproject.toml
├── setup.cfg
└── MANIFEST.in
```

## Linting (Static Code Analysis)

```sh
python -m pip install .[sca]
python -m pylint src/mypackage
```

## Build (Wheel)

```sh
python -m pip install build
python -m build
```

This will generate a `.whl` file in the `dist/` directory.

## Install from Wheel

```sh
python -m pip install dist/mypackage-*.whl
```

## Testing

```sh
python -m pip install .[test]
python -m pytest
```

## Documentation

To generate HTML documentation from the `docs` folder using [Quarto](https://quarto.org):
Adjust _quarto.yml file under docs folder.

```sh
python -m pip install quarto-cli  # or follow Quarto installation instructions for your OS
quarto render docs
```

The generated HTML documentation will be available in the `docs/_site` directory.

## Example

You can run the example script without installing the package:

```sh
python -m example/example_usage.py
```

## Usage

```python
import pandas as pd
from mypackage import add, subtract, multiply, divide

df1 = pd.DataFrame([[1, 2], [3, 4]])
df2 = pd.DataFrame([[5, 6], [7, 8]])

print(add(df1, df2))
print(subtract(df1, df2))
print(multiply(df1, df2))
print(divide(df1, df2))
```

## CI/CD

A GitLab/GitHub CI/CD pipeline is provided to run static code analysis, build, test, and measure test coverage.

## Test Coverage with Codecov

Test coverage is automatically reported to [Codecov](https://codecov.io/) via the CI/CD pipeline.
To run coverage locally and upload (requires CODECOV_TOKEN):

```sh
python -m pytest --cov=src/mypackage --cov-report=xml
python -m codecov --file=coverage.xml
```
