from flexx import flx

class Example(flx.PyWidget):

    count = flx.IntProp()

    def _render_dom(self):
        # This method automatically gets called when any of the used
        # properties (only count, in this case) changes.
        return flx.create_element('div', {'className':'myDiv'},
            flx.create_element('button',
                               {'onclick': self.increase_count},
                               '+'),
            flx.create_element('span',
                               {'style.background': '#afa'},
                               str(self.count)),
            )

    @flx.action
    def increase_count(self):
        self._mutate_count(self.count + 1)
        
if __name__ == '__main__':
     m = flx.launch(Example, 'default-browser')
     flx.start()
