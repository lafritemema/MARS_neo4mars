from ._resource import Resource
from neomodel.properties import StringProperty

class Asset(Resource):
  interface=StringProperty()

class Carrier(Asset):
  pass

class EndEffector(Asset):
  pass
  