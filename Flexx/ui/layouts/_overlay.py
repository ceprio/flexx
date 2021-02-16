""" StackLayout

Show all childs overlaying each others. Example:

.. UIExample:: 200

    from flexx import app, event, ui

    class Example(ui.Widget):

        def init(self):
            with ui.HBox():
                with ui.VBox():
                    self.buta = ui.Button(text='red')
                    self.butb = ui.Button(text='green')
                    self.butc = ui.Button(text='blue')
                    ui.Widget(flex=1)  # space filler
                with ui.StackLayout(flex=1) as self.stack:
                    self.buta.w = ui.Widget(style='background:#a00;')
                    self.butb.w = ui.Widget(style='background:#0a0;')
                    self.butc.w = ui.Widget(style='background:#00a;')

        @event.reaction('buta.pointer_down', 'butb.pointer_down', 'butc.pointer_down')
        def _stacked_current(self, *events):
            button = events[-1].source
            self.stack.set_current(button.w)
"""

from ... import event
from . import Layout


class Overlay(Layout):
    """ A layout widget which shows all its children on top of each others.
    
    The ``node`` of this widget is a
    `<div> <https://developer.mozilla.org/docs/Web/HTML/Element/div>`_.
    """

    CSS = """
        .flx-Overlay {
            width: 100%;
            height: 100%;
            position: relative !important;
        }
        .flx-Overlay > * { 
            position: absolute !important;
            width: 100%;
            height: 100%;
            top: 0 !important;
            left: 0 !important;
        }
    """
