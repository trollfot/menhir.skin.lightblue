# -*- coding: utf-8 -*-

from dolmen.forms.crud import ApplicationForm
from megrok import pagetemplate as pt
from menhir.skin.lightblue import ILightblueLayer


class DolmenFormTemplate(pt.PageTemplate):
    """Template for a layout aware form.
    """
    pt.view(ApplicationForm)
    pt.layer(ILightblueLayer)
