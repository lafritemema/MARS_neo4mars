from ._resource import Resource
from neomodel.properties import StringProperty
from neomodel.relationship_manager import RelationshipTo, RelationshipFrom
from ..utils import PreconditionRelationShip, ResultRelationShip

class Action(Resource):
  __TYPE = {
    'MOVE.STATION.HOME' : 'STATION',
    'MOVE.STATION.TOOL': 'STATION',
    'LOAD.EFFECTOR' : 'EFFECTOR',
    'UNLOAD.EFFECTOR' : 'EFFECTOR',
    'LOAD.TOOL' : 'TOOL',
    'UNLOAD.TOOL': 'TOOL',
    'MOVE.STATION.WORK' : 'STATION',
    'MOVE.TCP.APPROACH': 'APPROACH',
    'MOVE.TCP.CLEARANCE': 'APPROACH',
    'MOVE.TCP.WORK' : 'WORK',
    'WORK.DRILL' : 'DRILL',
    'WORK.FASTEN' : 'FASTEN',
    'WORK.PROBE': 'PROBE'
  }

  type=StringProperty(choices=__TYPE)
  preconditions = RelationshipFrom('neo4mars.resource.situation.StateObject',
                                 'PRECONDITION',
                                 model=PreconditionRelationShip)
  results=RelationshipTo('neo4mars.resource.situation.StateObject',
                         'RESULT',
                         model=ResultRelationShip)
  # dependence = RelationshipTo('Action', 'DEPENDENCE', model=DependanceRelationship)
  assets = RelationshipTo('neo4mars.resource.asset.Asset', 'PERFORMED_BY')
  areas = RelationshipTo('neo4mars.process.area.Area', 'TO_REACH')
  operations = RelationshipTo('neo4mars.process.operation.Operation', 'DESCRIBE')
  collection = StringProperty()