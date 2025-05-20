# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'FactorLib Dashboard'
copyright = '2025, 黃天瑜'
author = '黃天瑜'
release = '2.3.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser'
    ]

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_TW'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']

#-- Options for latex output ----------------------------
latex_engine = 'xelatex'
latex_use_xindy = False
latex_elements = {
    'preamble': r'''
    \usepackage{xeCJK}
    \setCJKmainfont[BoldFont=Noto Sans CJK TC, ItalicFont=Noto Serif CJK TC]{Noto Sans CJK TC}
    \setCJKsansfont{Noto Sans CJK TC}
    \setCJKmonofont{Noto Sans Mono CJK TC}
    \XeTeXlinebreaklocale "zh"
    \XeTeXlinebreakskip = 0pt plus 1pt
    ''',
}