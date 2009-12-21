import grok
from megrok import resource
from zope.interface import Interface
from dolmen.app.layout.master import Header
from menhir.library.jquery import jquery
from menhir.skin.lightblue import ILightblueLayer


class LightblueLibrary(resource.Library):
    resource.path('resources')
    resource.name("menhir.skin.lightblue")
    grok.layer(ILightblueLayer)

bluejs = resource.ResourceInclusion(
    LightblueLibrary, 'lightblue.dropdown.js', depends=[jquery])

bluecss = resource.ResourceInclusion(
    LightblueLibrary, 'lightblue.css')

lightblue = resource.GroupInclusion([bluejs, bluecss])


class LightBlueResourceViewlet(grok.Viewlet):
    grok.viewletmanager(DolmenHeader)
    grok.layer(ILightblueLayer)
    grok.context(Interface)

    def render(self):
        lightblue.need()
        return u""
    
