"""

Simple example:

.. UIExample:: 200
        self.overlay = ui.Div(text="Text in the middle of the window", style='''
            position: fixed;
            top: 0;
            left: 0;
            height: 100%;
            width: 100%;
            z-index: 1001;
            background-color: rgba(33,33,33,0.5);
            display: flex;
            justify-content: center;
            align-items: center;
            ''')
"""

from ... import app, event
from . import Widget

class Div(Widget): 
    """ A basic div widget with html content.
    This is the swiss knife for html insertions.
    """

    text = event.StringProp('', doc="""
        The text shown in the label (HTML is shown verbatim).
        """)

    html = event.StringProp(settable=True, doc="""
        The html content to be inserted in the div.
        """)
    
    style = event.StringProp(settable=True, doc="""
        The style of the div.
        """)
    
    def init(self):
        if self.text:
            self.set_text(self.text)
        elif self.html:
            self.set_html(self.html)

    def _init_events():
        pass  # just don't use standard events?

    @event.action
    def set_text(self, text):
        """ Setter for the text property.
        """
        if not self.node:
            self._mutate_text(text)
            return
        self.node.textContent = text
        self._mutate_text(self.node.textContent)
        self._mutate_html(self.node.innerHTML)

    @event.action
    def set_html(self, html):
        """ Setter for the html property. Use with care.
        """
        if not self.node:
            self._mutate_html(html)
            return
        self.node.innerHTML = html
        self._mutate_text(self.node.textContent)
        self._mutate_html(self.node.innerHTML)

    @event.action
    def set_style(self, sz):
        """ Setter for the style property.
        """
        if not self.node:
            self._mutate_style(sz)
            return
        self.node.style['word-wrap'] = 'normal'
        self._mutate_style(self.node.style)
