from ._process import Process
from neomodel.properties import StringProperty

class Area(Process):
  type=StringProperty()
  reference=StringProperty()