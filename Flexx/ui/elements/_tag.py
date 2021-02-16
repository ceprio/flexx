""" TagWidget

A simple tag. Example:

.. UIExample:: 150

    from flexx import app, event, ui

    class Example(ui.GroupWidget):
        def init(self):
            self.set_title('A silly panel')
            with ui.VBox():
                self.progress = ui.ProgressBar(min=0, max=9,
                                               text='Clicked {value} times')
                self.but = ui.Button(text='click me')

        @event.reaction('but.pointer_down')
        def _button_pressed(self, *events):
            self.progress.set_value(self.progress.value + 1)
"""

from . import Widget
from ... import flx, app, event
from pscript import RawJS

class TagWidget(Widget):
    """ Generic tag widget to create elements in the DOM.
    """
    def __init__(self, tag, *init_args, **kwargs):
        """
            TagWidget(tag, options, children) # children may be a list
            
            Note to devs:
                For the TagWidget widget to work in place of a dict element (see the return type of 
                create_element), the TagWidget widget must implement type, props and children member 
                variables.
        """ 
        self.type = tag
        if init_args:
            self.props = init_args[0] 
            self.children = init_args[1] if 1 < len(init_args) else kwargs.get('children', '')
        else:
            self.props = kwargs.get('options', {})
            del kwargs["options"]
            self.children = kwargs.get('children', '')
            del kwargs["children"]

        init_args = []
        super().__init__(*init_args, **kwargs)

    def _create_dom(self):
        return flx.create_element(self.type)
    
    def _render_dom(self):
        node = flx.create_element(self.type, self.props, self.children)
        return node  
