#-*- coding: utf-8 -*-
"""

.. moduleauthor:: Martí Congost <marti.congost@whads.com>
"""
from woost.models import ExtensionAssets, BlocksCatalog


def install():
    """Creates the assets required by the notices extension."""

    assets = ExtensionAssets("notices")

    assets.require(
        BlocksCatalog,
        "blocks",
        title = assets.TRANSLATIONS
    )

