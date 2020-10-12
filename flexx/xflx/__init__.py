"""
The Flexx widgets.
"""

import logging
logger = logging.getLogger(__name__)
del logging

# flake8: noqa

# We follow the convention of having one module per widget class (or a
# small set of closely related classes). In order not to pollute the
# namespaces, we prefix the module names with an underscrore.

from ._element import Element, PyElement, HTML_str
#from .layouts import *  # todo
from .elements import *
#from .pyelements import *  # todo
