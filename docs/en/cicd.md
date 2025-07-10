# CI/CD Pipeline

## Linting (Static Code Analysis)

```sh
python -m pip install .[sca]
python -m pylint src/mypackage
```

## Building the Package (output into dist/ folder)
This will generate a `.whl` file in the `dist/` directory:
```sh
python -m pip install build
python -m build
```

## Install from Wheel
install the package from the generated wheel file in the `dist/` folder:
```sh
python -m pip install dist/mypackage-*.whl
```

## Running Tests
Running tests located in the `tests/` folder:
```sh
python -m pip install .[test]
python -m pytest
```

## Code Coverage
To measure test coverage, you can use the `pytest-cov`:
```sh
python -m pytest --cov=src/mypackage
```

## Upload Code Coverage to Codecov
Test coverage can be automatically reported to [Codecov](https://codecov.io/) via the CI/CD pipeline.
To run coverage locally and upload (requires CODECOV_TOKEN):

```sh
python -m pytest --cov=src/mypackage --cov-report=xml
python -m codecov --file=coverage.xml
```
