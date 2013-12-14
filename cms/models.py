from django.db import models
from django.utils.translation import ugettext_lazy as _

from feincms.module.page.models import Page
from feincms.content.richtext.models import RichTextContent
from feincms.content.medialibrary.models import MediaFileContent

Page.register_extensions('feincms.module.extensions.datepublisher',) # Example set of extensions

Page.register_templates({
    'title': _('Standard template'),
    'path': 'cms_base.html',
    'regions': (
        ('main', _('Main content area')),
        # ('sidebar', _('Sidebar'), 'inherited'),
        ),
    })

Page.create_content_type(RichTextContent)