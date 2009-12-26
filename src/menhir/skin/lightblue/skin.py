# -*- coding: utf-8 -*-

import grokcore.viewlet as grok
from dolmen.app import layout
from zope.publisher.interfaces import browser


class ILightblueLayer(layout.IBaseLayer):
    """Base layer for lightblue components
    """


class ILightBlueSkin(ILightblueLayer, browser.IBrowserSkinType):
    """A skin with light-blue tones. Very sober yet effective.
    """
    grok.skin("lightblue")