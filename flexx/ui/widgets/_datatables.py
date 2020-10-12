"""
Simple example:

.. UIExample:: 200

    # Define options. See datatables.net for full options documentation.
    columns = [{"title": "GDP Year"}, {"title": "Australia"}, {"title": "New Zealand"}]
    data = [["1952", 10039.59564, 10556.57566],
            ["1957", 10949.64959, 12247.39532]]
    options = {'pageLength': 100, 'data':data, 'columns':columns}

    # Show
    p = ui.DataTableWidget(options=options)

Also see examples: :ref:`datatables_from_js.py`.
"""

from . import Widget
from ... import flx, app, event

# Associate datatables's assets with this module so that Flexx will load
# them when (things from) this module is used.
app.assets.associate_asset(__name__, "https://code.jquery.com/jquery-2.2.4.js")
datatables_base_url = 'https://cdn.datatables.net/1.10.21/'
app.assets.associate_asset(__name__, datatables_base_url + 'css/jquery.dataTables.css')
app.assets.associate_asset(__name__, datatables_base_url + 'js/jquery.dataTables.js')

class DataTableWidget(Widget):
    """ A DataTableWidget widget based on datatables.
    """

    options = flx.DictProp(settable=True, doc="""
        Options of the datatable
        args:
        columns: Minimum format: [{{"title": "Column 1"}},]
        data: list of list (list of rows)
        """)

    CSS = """
        .flx-DataTableWidget tr:nth-child(even) {
            background: #99BCDB;
        }
         
        .flx-DataTableWidget tr:nth-child(odd) {
            background: #EBF2F8;
        }
        .flx-DataTableWidget tr td {
            padding-top: 0px;
            padding-bottom: 0px;
        }
    """
    @event.reaction('!tableify')
    def on_tableify(self, *events):
        global jQuery
        jQuery('#' + self.id).dataTable(self.options)

    def _render_dom(self):
        self.emit('tableify', {})
        return [flx.create_element('table', {'id': self.id }, ''),]
