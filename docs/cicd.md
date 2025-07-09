## Linting (Static Code Analysis)

```sh
python -m pip install .[sca]
python -m pylint src/mypackage
```

## Building the Package (output in dist folder)

```sh
python -m pip install build
python -m build
```
This will generate a `.whl` file in the `dist/` directory.

## Install from Wheel

```sh
python -m pip install dist/mypackage-*.whl
```

## Running Tests

```sh
python -m pip install .[test]
python -m pytest
```

## Code Coverage

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
