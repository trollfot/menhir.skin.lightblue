# -*- coding: utf-8 -*-

import grok
from zope.i18n import translate
from xml.sax import saxutils
from zope.component.hooks import getSite
from zope.interface import Interface
from dolmen.app.site import IDolmen
from dolmen.app.layout.master import Header
from zope.i18nmessageid import MessageFactory

_ = MessageFactory("menhir.skin.lightblue")


class Metadatas(grok.Viewlet):
    grok.viewletmanager(Header)
    grok.context(Interface)

    title = _(u'Untitled content')
    description = u""

    def update(self):
        title = getattr(self.context, 'title', None)
        if title is None:
            title = translate(grok.title.bind(self.title).get(self.view),
                              context=self.request)
        self.title = title
            
        if not IDolmen.providedBy(self.context):
            site = getSite()
            if IDolmen.providedBy(site):
                self.title = u"%s \u2014 %s" % (self.title, site.title)

    def render(self):
        return '''<title>%s</title>\n''' % saxutils.escape(self.title)
