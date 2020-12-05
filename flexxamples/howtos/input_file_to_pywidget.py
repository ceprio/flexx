# based on https://www.webcodegeeks.com/html5/html5-file-upload-example/

from flexx import flx, event, ui
from flexx.ui._widget import Widget, create_element


class FileInput(Widget):
    """ Abstract button class.
    
    The html structure of this Widget is the following:
    <input name="file1" type="file", accept="image/png, image/jpeg">
    
    accept can be:
    image: "image/png, image/jpeg"
    excel sheet: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    """

    DEFAULT_MIN_SIZE = 10, 24

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

    filename = event.StringProp('', settable=True, doc="""
        The name of the file.
        """)

    filetype = event.StringProp('', settable=True, doc="""
        The type of file.
        """)

    filesize = event.IntProp(0, settable=True, doc="""
        The size of the file.
        """)

    filecontent = event.StringProp('', settable=True, doc="""
        The content of the file in byte64 format.
        """)

    def _init_events():
        pass  # just don't use standard events

    def _create_dom(self):
        global window
        outer = window.document.createElement('div')
        self.input = window.document.createElement('input')
        self.input.id = self.id + ".0"
        self.input.type = "file"
        self.input.accept = "image/png, image/jpeg"
        self.message = window.document.createElement('div')
        self.message.id = self.id + ".1"
        outer.appendChild(self.input)
        outer.appendChild(self.message)
        self._addEventListener(self.input, 'change', self.change, 0)
        return outer

    @event.emitter
    def change(self, e):
        global FileReader
        file = self.input.files[0];
        if file:
            self.set_filename(file.name)
            self.set_filetype(file.type)
            self.set_filesize(file.size)
            reader = FileReader()
            def onload(evt):
                self.set_filecontent(evt.target.result)
                self.message.innerHTML = ""
            def onerror(evt):
                self.message.innerHTML = "Error Reading File"
            reader.onload = onload
            reader.onerror = onerror
            reader.readAsDataURL(file)
        return dict(orange="black")


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
        self.input = FileInput()
        self.img = Image()

    @event.reaction('input.filecontent')
    def __source_changed(self, *events):
        if "allow_reconnect" not in events[0]: # skip the first one
            self.img.set_source(self.input.filecontent)

if __name__ == '__main__':
    m = flx.launch(Example, 'default-browser')
    flx.start()
