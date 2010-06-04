# -*- coding: utf-8 -*-

import grokcore.viewlet as grok

from hurry.jquery import jquery
from megrok import resource, resourceviewlet
from menhir.skin.lightblue import ILightblueLayer
from zope.interface import Interface


class LightblueLibrary(resource.ResourceLibrary):
    grok.layer(ILightblueLayer)
    grok.path('resources')
    grok.name("menhir.skin.lightblue")
    resource.resource('lightblue.css')
    resource.resource('lightblue.dropdown.js', depends=[jquery])


class LightBlueResourceViewlet(resourceviewlet.ResourceViewlet):
    grok.context(Interface)
    grok.layer(ILightblueLayer)
    resources = [LightblueLibrary]
