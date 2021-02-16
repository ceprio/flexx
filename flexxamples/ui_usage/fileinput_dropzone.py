"""
Simple use of a fileinput

see also: input_file_to_pywidget.py
"""

from flexx import app, event, ui, flx


class Example(ui.Widget):

    def init(self):
        self.input = ui.FileInputBase(accept=".xlsx")


if __name__ == '__main__':
     m = flx.launch(Example, 'default-browser')
     flx.run()
