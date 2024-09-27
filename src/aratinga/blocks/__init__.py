"""
Blocks module entry point. Used to cleanly organize blocks into
individual files based on purpose, but provide them all as a
single `blocks` module.
"""

from django.utils.translation import gettext_lazy as _
from wagtail import blocks


# Collections of blocks commonly used together.

HTML_STREAMBLOCKS = [

]

CONTENT_STREAMBLOCKS = HTML_STREAMBLOCKS + [
   
]

LAYOUT_STREAMBLOCKS = [
]

STREAMFORM_BLOCKS = []