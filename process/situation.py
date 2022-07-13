from ._process import Process
from neomodel.properties import IntegerProperty

class StateObject(Process):
  priority=IntegerProperty()
