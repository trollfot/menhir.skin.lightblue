# -*- coding: utf-8 -*-

import grokcore.viewlet as grok

from dolmen.app.layout.master import Header
from hurry.jquery import jquery
from megrok import resource
from menhir.skin.lightblue import ILightblueLayer
from zope.interface import Interface


class LightblueLibrary(resource.ResourceLibrary):
    grok.layer(ILightblueLayer)
    grok.path('resources')
    grok.name("menhir.skin.lightblue")
    resource.resource('lightblue.css')
    resource.resource('lightblue.dropdown.js', depends=[jquery])


class LightBlueResourceViewlet(grok.Viewlet):
    grok.viewletmanager(Header)
    grok.layer(ILightblueLayer)
    grok.context(Interface)

    def render(self):
        LightblueLibrary.need()
        return u""
    
