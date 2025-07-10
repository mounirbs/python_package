# Documentation Generation

## Generating Documentation using Sphinx
To generate HTML documentation using [Sphinx](https://www.sphinx-doc.org).

### Install Sphinx and Dependencies
Install Sphinx and its dependencies for documentation generation:

```sh
python -m pip install .[doc]
```

### Prepare mypackage API documentation
the `mypackage` API documentation is generated from the docstrings in the `mypackage` source code.
This will create a `mypackage.rst` file in the `docs/api` directory:

```sh
sphinx-apidoc -o docs/api src/mypackage
```

### Build the full HTML documentation based on the index.rst file
Make sure the `index.rst` file is in the `docs` directory and contains the necessary configuration to include the generated API documentation.

```sh
cp ./sphinx/index.rst ./docs/
sphinx-build --conf-dir sphinx -b html docs docs/_site
```
The generated HTML documentation will be available in the `docs/_site` directory.

## Generating Documentation using Quarto

To generate HTML documentation from the `docs` folder using [Quarto](https://quarto.org), adjust _quarto.yml file.

### Install Quarto and Dependencies
Uncomment Quarto dependencies on the `pyproject.toml` file under the `[project.optional-dependencies][doc]` section.
Install Quarto and its dependencies for documentation generation:

```sh
python -m pip install .[doc]
```

Generates reference qmd files from docstrings:
```sh
quartodoc build 
```

Render docs folder and qmd files for docstrings:
```sh
quarto render 
```

Preview the rendered documentation:
```sh
quarto preview 
```

The generated HTML documentation will be available in the `docs/_site` directory.