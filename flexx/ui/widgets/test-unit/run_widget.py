from flexx import flx


class Example(flx.Widget):
    def _render_dom(self):
        node = flx.create_element('div', {}, flx.HTML_str("<b>nothing</b>"))
        return node


if __name__ == "__main__":
    app = flx.App(Example, title='Test')
    app.launch('default-browser')
    flx.start()