"""

.. moduleauthor:: Martí Congost <marti.congost@whads.com>
"""
from cocktail.persistence import migration_step
from woost.models import BlocksCatalog


@migration_step
def preserve_woost2_data(e):

    from woost.models import Website

    catalog = BlocksCatalog.require_instance(
        qname="woost.extensions.notices.blocks_catalog"
    )

    for website in Website.select():
        blocks = set()
        try:
            value = website._notices
        except AttributeError:
            pass
        else:
            del website._notices
            if value:
                catalog.blocks.extend(value)

