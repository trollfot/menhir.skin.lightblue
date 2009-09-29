# -*- coding: utf-8 -*-

import grok
from dolmen.app.layout import skin
from zope.publisher.interfaces import browser


class ILightblueLayer(skin.IDolmenBaseLayer):
    """Base layer for lightblue components
    """


class ILightBlueSkin(ILightblueLayer, browser.IBrowserSkinType):
    """A skin with light-blue tones. Very sober yet effective.
    """
    grok.skin("lightblue")
