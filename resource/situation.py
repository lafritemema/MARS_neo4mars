from ._resource import Resource
from neomodel.properties import IntegerProperty

class StateObject(Resource):
  priority=IntegerProperty()