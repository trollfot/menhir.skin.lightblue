# -*- coding: utf-8 -*-

import grokcore.viewlet as grok

from fanstatic import Resource, Library
from js.jquery import jquery
from megrok import resourceviewlet
from menhir.skin.lightblue import ILightblueLayer
from zope.interface import Interface


LightblueLibrary = Library("menhir.skin.lightblue", 'resources')
    
lightblue_css = Resource(LightblueLibrary, 'lightblue.css')
lightblue_js = Resource(LightblueLibrary,
                        'lightblue.dropdown.js', depends=[jquery])


class LightBlueResourceViewlet(resourceviewlet.ResourceViewlet):
    grok.context(Interface)
    grok.layer(ILightblueLayer)
    resources = [lightblue_css, lightblue_js]
