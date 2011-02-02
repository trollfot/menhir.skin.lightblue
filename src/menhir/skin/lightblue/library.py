# -*- coding: utf-8 -*-

import grokcore.viewlet as grok

from fanstatic import Resource, Library
from js.jquery import jquery
from megrok import resourceviewlet
from menhir.skin.lightblue import ILightblueLayer
from zope.interface import Interface
from js.jquery_tablesorter import tablesorter


LightblueLibrary = Library("menhir.skin.lightblue", 'resources')
    
style = Resource(LightblueLibrary, 'lightblue.css')
dropdown = Resource(LightblueLibrary, 'dropdown.js', depends=[jquery])
table = Resource(LightblueLibrary, 'table.js', depends=[jquery, tablesorter])


class LightBlueResourceViewlet(resourceviewlet.ResourceViewlet):
    grok.context(Interface)
    grok.layer(ILightblueLayer)
    resources = [style, dropdown, table]
