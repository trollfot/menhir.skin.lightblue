# -*- coding: utf-8 -*-

import grok
from megrok.z3cform import FormLayer
from zope.publisher.interfaces import browser


class ILightblueLayer(FormLayer):
    """Base layer for lightblue components
    """


class ILightBlueSkin(ILightblueLayer, browser.IBrowserSkinType):
    """A skin with light-blue tones. Very sober yet effective.
    """
    grok.skin("lightblue")
