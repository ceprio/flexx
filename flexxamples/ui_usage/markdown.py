"""
Simple use of a the markdown widget,
using a custom widget that is populated in its ``init()``.
"""

from flexx import app, event, ui, flx
from httpx import _content

class Example(flx.Widget):
    def init(self):
        content = "# Welcome\n\n" \
            "Hello.  Welcome to my **website**."
        ui.Markdown(content=content)
        
if __name__ == '__main__':
    m = flx.launch(Example, 'default-browser')
    flx.run()
