## Generating Documentation

To generate HTML documentation from the `docs` folder using [Quarto](https://quarto.org):
Adjust _quarto.yml file under docs folder.

```sh
python -m pip install .[doc]
# See the _quarto.yml file for configuration
quartodoc build # generates reference qmd files from docstrings
quarto render # render docs folder and qmd files for docstrings
quarto preview # preview the rendered documentation
```

The generated HTML documentation will be available in the `_site` directory.