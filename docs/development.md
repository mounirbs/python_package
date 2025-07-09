## Setting up a development environment

```sh
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -e .[test]
```

## Linting

```sh
python -m pip install .[sca]
python -m pylint src/mypackage
```

## Building the Package (output in dist folder)

```sh
python -m pip install build
python -m build
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

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
