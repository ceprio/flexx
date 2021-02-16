"""
Simple use of a group,
using a custom widget that is populated in its ``init()``.
"""

from flexx import app, event, ui, flx

class Example(ui.Widget):

    def init(self):
        with ui.Overlay():
            ui.TagWidget('h1',{},"allo")
            ui.TagWidget('h1',{},"police")

if __name__ == '__main__':
    m = flx.launch(Example, 'default-browser')
    flx.start()
