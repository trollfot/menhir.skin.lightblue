# -*- coding: utf-8 -*-

from dolmen.forms.crud import ApplicationForm
from dolmen.app.layout import master, DefaultView
from megrok import pagetemplate as pt
from menhir.skin.lightblue import ILightblueLayer


class BlueMaster(master.Master):
    pt.layer(ILightblueLayer)


class DolmenFormTemplate(pt.PageTemplate):
    """Template for a layout aware form.
    """
    pt.view(ApplicationForm)
    pt.layer(ILightblueLayer)


class DolmenViewFormTemplate(pt.PageTemplate):
    """Template for a layout aware form.
    """
    pt.view(DefaultView)
    pt.layer(ILightblueLayer)
