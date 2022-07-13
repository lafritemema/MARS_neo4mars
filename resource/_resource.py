from neomodel.core import StructuredNode
from neomodel.properties import StringProperty, UniqueIdProperty

class Resource(StructuredNode):
  uid = UniqueIdProperty()
  description = StringProperty()
