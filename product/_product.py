from neomodel.core import StructuredNode
from neomodel.properties import StringProperty, UniqueIdProperty

class Product(StructuredNode):
  uid = UniqueIdProperty()
  description = StringProperty()

  @classmethod
  def get_by_uid(cls, uid:str):
    return cls.nodes.get(uid=uid)
  