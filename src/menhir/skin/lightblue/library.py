import grok
import megrok.resourcelibrary
from zope.interface import Interface
from dolmen.app.layout.master import DolmenHeader
from menhir.library.jquery import JQueryBase
from menhir.skin.lightblue import ILightblueLayer


class LightblueDolmenLibrary(megrok.resourcelibrary.ResourceLibrary):
    grok.name("menhir.skin.lightblue")
    grok.layer(ILightblueLayer)
    megrok.resourcelibrary.depend(JQueryBase)
    megrok.resourcelibrary.directory('resources')
    megrok.resourcelibrary.include('lightblue.css')
    megrok.resourcelibrary.include('lightblue.dropdown.js')


class LightBlueResourceViewlet(grok.Viewlet):
    grok.viewletmanager(DolmenHeader)
    grok.layer(ILightblueLayer)
    grok.context(Interface)

    def render(self):
        LightblueDolmenLibrary.need()
        return u""
    
