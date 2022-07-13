from random import choices
from tokenize import String

from ._process import Process
from neomodel.properties import StringProperty
from neomodel.relationship_manager import RelationshipTo, RelationshipFrom
from ..utils import PreconditionRelationShip, ResultRelationShip

class Operation(Process):
  __TYPES = {
    'DRILL':'drilling',
    'FASTEN':'fastening',
    'TMPDRILLING':'temporary drilling',
    'TMPFASTENING':'temporary fastening'
  }
  type = StringProperty(choices=__TYPES)

class Class(Operation):
  pass

class Instance(Operation):
  mother_class = RelationshipTo('Class', 'INSTANCE_OF')
  preconditions = RelationshipFrom('neo4mars.product.assembly.Assembly', 'PRECONDITION', model=PreconditionRelationShip)
  results = RelationshipTo('neo4mars.product.assembly.Assembly', 'RESULT', model=ResultRelationShip)
  # assembly = RelationshipTo('neo4mars.product.assembly.Assembly', 'PERFORM_ON')