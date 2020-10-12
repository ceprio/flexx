# doc-export: DataTableWidgets
"""
This example demonstrates a table widget based on datatables (see datatables.js). 
"""

from flexx import flx

columns = [{"title": "Country"}, {"title": "Australia"}, {"title": "New Zealand"}]
data = [["gdpPercap_1952", 10039.59564, 10556.57566],
["gdpPercap_1957", 10949.64959, 12247.39532],
["gdpPercap_1962", 12217.22686, 13175.67800],
["gdpPercap_1967", 14526.12465, 14463.91893],
["gdpPercap_1972", 16788.62948, 16046.03728],
["gdpPercap_1977", 18334.19751, 16233.71770],
["gdpPercap_1982", 19477.00928, 17632.41040],
["gdpPercap_1987", 21888.88903, 19007.19129],
["gdpPercap_1992", 23424.76683, 18363.32494],
["gdpPercap_1997", 26997.93657, 21050.41377],
["gdpPercap_2002", 30687.75473, 23189.80135],
["gdpPercap_2007", 34435.36744, 25185.00911]]

class DataTableDemo(flx.HBox):

    def init(self):
        flx.DataTableWidget(options = {"pageLength": 100, 'data':data, 'columns':columns})


if __name__ == '__main__':
    flx.launch(DataTableDemo, 'default-browser')
    # flx.run() # runs once
    flx.start()
