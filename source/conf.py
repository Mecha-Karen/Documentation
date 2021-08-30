import pydata_sphinx_theme
import datetime
import sys
import os
import re

sys.path.insert(0, os.path.abspath('..'))
sys.path.append(os.path.abspath('extensions'))

project = 'Mecha Karen'
copyright = '2021, Seniatical'
author = 'Seniatical'
release = '1.9.2a'

templates_path = ['_templates']

exclude_patterns = ['*.md', '*.template']

extensions = [
   'builder',
   'sphinx.ext.autodoc',
   'sphinx.ext.extlinks',
   'sphinx.ext.intersphinx',
   'sphinx.ext.napoleon',
   'sphinxcontrib_trio',
   'details',
   'exception_hierarchy',
   'attributetable',
   'resourcelinks',
   'nitpick_file_ignorer',
]
autodoc_member_order = 'bysource'
autodoc_typehints = 'none'
source_suffix = '.rst'

rst_prolog = """
.. |coro| replace:: This function is a |coroutine_link|_.
.. |maybecoro| replace:: This function *could be a* |coroutine_link|_.
.. |coroutine_link| replace:: *coroutine*
.. _coroutine_link: https://docs.python.org/3/library/asyncio-task.html#coroutine
"""

html_theme = 'pydata_sphinx_theme'
html_logo = "_static/karen.png"

html_theme_options = {
   "favicons": [
      {
         "rel": "icon",
         "sizes": "16x16",
         "href": "karen.png",
      },
      {
         "rel": "icon",
         "sizes": "32x32",
         "href": "karen.png",
      },
      {
         "rel": "apple-touch-icon",
         "sizes": "180x180",
         "href": "karen.png"
      },
   ],

   "icon_links": [
      {
         "name": "GitHub",
         "url": "https://github.com/Seniatical/Mecha-Karen/",
         "icon": "fab fa-github",
      },
      {
         "name": "Discord",
         "url": "https://discord.com/invite/Q5mFhUM",
         "icon": "fab fa-discord"
      },
      {
         "name": "Dashboard",
         "url": "https://mechakaren.xyz/dashboard",
         "icon": "fas fa-box"
      }
    ],

   "use_edit_page_button": True,
   "collapse_navigation": False,
   "navigation_depth": 3,
   "search_bar_text": "Search the docs ...",
   "footer_items": ["copyright", "sphinx-version", "last-updated"],
}

html_context = {
    "github_url": "https://github.com",
    "github_user": "Seniatical",
    "github_repo": "Mecha-Karen",
    "github_version": "main",
    "doc_path": "Documentation",
    "last_updated": datetime.datetime.utcnow().strftime('%d/%m/%Y'),
}

html_sidebars = {
    "**": ["search-field", "sidebar-nav-bs", "arc"],
    "index": ["search-field", "home-navbar", "arc"]
}

html_static_path = ['_static']
html_css_files = [
    'css/custom.css',
]

html_title = "Mecha Karen"

suppress_warnings = [
   "image.not_readable"
]

html_static_path = ['_static']
