from flexx import flx
from flexx import event


class DynamicWidgetContainer(flx.PyWidget):
    """ Widget container to allow dynamic insertion and disposal of widgets.
    """

    DEFAULT_MIN_SIZE = 0, 0

    CSS = """

    .flx-FileInputBase {
        white-space: nowrap;
        padding: 0.2em 0.4em;
        border-radius: 3px;
        color: #333;
    }
    .flx-FileInputBase, .flx-FileInputBase > input {
        margin: 2px; /* room for outline */
    }
    .flx-FileInputBase:focus, .flx-FileInputBase > input:focus  {
        outline: none;
        box-shadow: 0px 0px 3px 1px rgba(0, 100, 200, 0.7);
    }
    """

    pagename = event.StringProp('', settable=True, doc="""
        The name of the page.
        """)

    def init(self, *init_args, **property_values):
        super().init()
        # the page
        self.page = None
        
    def _init_events(self):
        pass  # just don't use standard events

    @event.reaction("clear")
    def __clear(self, *events):
        if self.page:
            self.page.dispose()
            self.page._jswidget.dispose()  # <-- added
            self.page = None

    @event.emitter
    def clear(self):
        return dict()
    
    @event.reaction("instantiate")
    def __instantiate(self, *events):
        if self.page:
            return
        with self:
            with events[0]['klass'](events[0]['style']) as self.page:
                self.page.parent = self

    @event.emitter
    def instantiate(self, klass, options={'style':None}):
        return dict(klass=klass, style=options['style'])

class CustomPyWidget1(flx.PyWidget):
    frame = None

    def init(self, additional_style="width: 100%; height: 100%; border: 3px solid green"):
        with flx.VFix(flex=1, style=additional_style) as self.frame:
            with flx.VFix(flex=1) as self.page:
                self.custom = flx.VFix(flex=1, style="width: 100%; height: 100%; border: 5px solid green;")
                self.but = flx.Button(text="swap it")

    def dispose(self):
        self.frame.dispose()
        self.frame = None
        super().dispose()
        
    @flx.reaction("but.pointer_click")
    def delete_function(self, *events):
        self.parent.clear()
        self.parent.instantiate(CustomPyWidget2, dict(style="width: 100%; height: 100%; border: 5px solid blue;"))

class CustomPyWidget2(flx.PyWidget):
    frame = None

    def init(self, additional_style="width: 100%; height: 100%; border: 3px solid blue"):
        with flx.VFix(flex=1, style=additional_style) as self.frame:
            with flx.VFix(flex=1) as self.page:
                self.but = flx.Button(text="swapped it")
                self.custom = flx.VFix(flex=1, style="width: 100%; height: 100%; border: 5px solid blue;")

    def dispose(self):
        self.frame.dispose()
        self.frame = None
        super().dispose()
        
    @flx.reaction("but.pointer_click")
    def delete_function(self, *events):
        self.parent.clear()
        self.parent.instantiate(CustomPyWidget1, dict(style="width: 100%; height: 100%; border: 5px solid green;"))

class Example(flx.PyWidget):
    def init(self):
        with flx.VFix(flex=1) as self.frame_layout:
            self.dynamic = DynamicWidgetContainer(
                "width: 100%; height: 100%; border: 5px solid black;", flex=1
            )
            self.but = flx.Button(text="instanciate")

    @flx.reaction("but.pointer_click")
    def click(self, *events):
        self.dynamic.instantiate(CustomPyWidget1)

m = flx.launch(Example)
flx.run()