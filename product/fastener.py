from ._product import Product
from neomodel.properties import StringProperty, FloatProperty
from neomodel.relationship_manager import RelationshipTo, Traversal, INCOMING

class Fastener(Product):
  reference=StringProperty()

class Class(Fastener):
  diameter=FloatProperty()
  type=StringProperty()

  def get_instances(self):
    definition = dict(node_class=Instance,
                      direction=INCOMING,
                      relation_type='INSTANCE_OF',
                      model=None)
    traversal = Traversal(self,
                          Instance.__label__,
                          definition)
    return traversal.all()

class Instance(Fastener):
  mother_class = RelationshipTo('Class', 'INSTANCE_OF')
  
  def get_class(self):
    return self.mother_class.get()