# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
sys.path.insert(0, os.path.abspath('../src/mypackage'))

project = 'mypackage'
copyright = '2025, myName'
author = 'myName'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc', # Automatically generate documentation from docstrings
    'sphinx.ext.napoleon',  # For Google style docstrings
    'sphinx.ext.viewcode', # Include source code in the documentation
    'sphinx_autodoc_typehints',  # Improves type hint rendering in docstrings
    'sphinx.ext.autosectionlabel', # Allows linking to sections by their titles
    'sphinx.ext.todo', # Support for todo items
    'myst_parser', # For parsing Markdown files
]

# The master toctree document.
root_doc = "index"

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#https://sphinx-themes.readthedocs.io/en/latest/
html_theme = 'alabaster'

html_file_suffix = '.html'

# Add custom static files (like style sheets)
#html_static_path = ['_static']
#html_css_files = ["_static/custom.css"]
#html_logo = "_static/logo.png"
