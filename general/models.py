from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.core.models import Page


class GiroPage(Page):
    content = models.TextField()
    content_panels = Page.content_panels + [
        FieldPanel('content')
    ]


class InfrastrukturPage(Page):
    content = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('content')]


class DokumentePage(Page):
    content = StreamField([
        ('Mitgliedsantrag', blocks.RichTextBlock()),
        ('Misc', blocks.RichTextBlock()),
        ('Protokoll', blocks.RichTextBlock())
    ])
    content_panels = Page.content_panels + [
        StreamFieldPanel('content')]


class ImpressumPage(Page):
    content = StreamField([
        ('Used', blocks.RichTextBlock())
    ])
    content_panels = Page.content_panels + [
        StreamFieldPanel('content')]


class MitmachPage(Page):
    content = StreamField([
        ('Introduction_for_Homepage', blocks.CharBlock(max_length=200)),
        ('Text', blocks.RichTextBlock()),
    ])
    content_panels = Page.content_panels + [
        StreamFieldPanel('content')
    ]


class LandingPage(Page):
    content = blocks.CharBlock()