"""

Simple example:

.. UIExample:: 200

    # Define data. This can also be generated with the plotly Python library
    data = [{'type': 'bar',
             'x': ['giraffes', 'orangutans', 'monkeys'],
             'y': [20, 14, 23]}]

    # Show
    p = ui.PlotlyWidget(data=data)

Also see examples: :ref:`plotly_gdp.py`.

"""

from ... import app, event
from . import Widget

class HTMLContent(Widget):
    """ A widget that shows a rendered Markdown content.
    """

    content = event.StringProp(settable=True, doc="""
        The html content to be inserted.
        """)

    @event.reaction
    def __content_change(self):
        self.node.innerHTML = self.content
