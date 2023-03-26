# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'EVECelery'
copyright = '2023, Nat'
author = 'Nat'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['autoapi.extension']

# autoapi config
autoapi_dirs = ['../EVECelery']
autoapi_add_toctree_entry = False

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output


html_theme = "pydata_sphinx_theme"
html_static_path = ['_static']

html_title = "EVECelery Docs"
html_context = {
    "default_mode": "dark",
    "github_user": "NullsecSpace",
    "github_repo": "EVECelery",
    "github_version": "main",
    "doc_path": "docs",
}
html_theme_options = {
    "use_edit_page_button": True,
    "show_nav_level": 2,
    "navigation_depth": 4,
    "announcement": "This library is in development and may rapidly change or have breaking bugs until the v1.0 release is ready.",
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/NullsecSpace/EVECelery",
            "icon": "fa-brands fa-square-github",
            "type": "fontawesome",
        },
        {
            "name": "PyPI",
            "url": "https://pypi.org/project/EVECelery",
            "icon": "fa-solid fa-box",
            "type": "fontawesome",
        },
        {
            "name": "NullsecSpace",
            "url": "https://nullsec.space",
            "icon": "fa-solid fa-star",
            "type": "fontawesome",
        }
    ]
}
