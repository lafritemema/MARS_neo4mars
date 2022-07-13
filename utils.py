from neomodel.relationship import StructuredRel
from neomodel.properties import StringProperty, IntegerProperty

class DependanceRelationship(StructuredRel):
  __TYPE = {
    'UPSTREAM':'UPSTREAM',
    'DOWNSTREAM':'DOWNSTREAM'
  }
  type=StringProperty(choices=__TYPE)

class PreconditionRelationShip(StructuredRel):
  relation=StringProperty()
  state=StringProperty()
  priority=IntegerProperty()

class ResultRelationShip(StructuredRel):
  state=StringProperty()
  relation=StringProperty()
  description=StringProperty()