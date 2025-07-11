# mypackage

[![codecov](https://codecov.io/gh/mounirbs/python_package/branch/main/graph/badge.svg?token=36IFV7Z311)](https://codecov.io/gh/mounirbs/python_package)

Basic arithmetic operations on pandas DataFrames.

## File Structure

```
package-template/
├── docs/
│   ├── index.md
│   └── installation.md
│   └── usage.md
│   └── cicd.md
│   └── doc_generation.md
├── src/
│   └── mypackage/
│       ├── __init__.py
│       └── math_ops.py
│
├── tests/
│   ├── __init__.py
│   └── test_math_ops.py
│
├── examples/
│   └── example_usage.py
│
├── README.md
├── LICENSE
├── pyproject.toml
├── _quarto.yml
└── MANIFEST.in
```

## Contents

- [Installation](docs/en/installation.md)
- [Usage](docs/en/usage.md)
- [CI/CD](docs/en/cicd.md)
- [Generating Documentation](docs/en/doc_generation.md)

## CI/CD

A GitLab/GitHub CI/CD pipeline is provided to run static code analysis, build, test, measure test coverage, generate documentation, and deploy documentation to GitLab Pages or GitHub Pages.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
