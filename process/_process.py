from neomodel.core import StructuredNode
from neomodel.properties import StringProperty, UniqueIdProperty

class Process(StructuredNode):
  uid = UniqueIdProperty()
  description = StringProperty()

