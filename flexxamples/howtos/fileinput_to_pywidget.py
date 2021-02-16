# based on https://www.webcodegeeks.com/html5/html5-file-upload-example/
"""
This example shows the use of a file input widget used to select and upload 
a file.

"""

from flexx import flx, event, ui
from flexx.ui._widget import Widget, create_element

class Image(flx.Widget):
    DEFAULT_MIN_SIZE = 10, 24
    
    source = event.StringProp('', settable=True, doc="""
        The image src.
        """)
    
    def _init_events():
        pass  # just don't use standard events

    def _create_dom(self):
        global window
        outer = window.document.createElement('img')
        return outer
    
    @event.reaction('source')
    def __source_changed(self, *events):
        if "allow_reconnect" not in events[0]: # skip the first one
            self.node.src = self.source


class Example(flx.PyWidget):

    def init(self):
        self.input = flx.FileInput(accept="image/png, image/jpeg")
        self.img = Image()

    @event.reaction('input.filecontent')
    def __source_changed(self, *events):
        if "allow_reconnect" not in events[0]: # skip the first one
            self.img.set_source(self.input.filecontent)

if __name__ == '__main__':
    m = flx.launch(Example, 'default-browser')
    flx.start()
