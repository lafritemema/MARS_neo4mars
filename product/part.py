from ._product import Product
from .assembly import Assembly, AssembleRS
from neomodel.properties import StringProperty
from neomodel.relationship_manager import RelationshipTo, Traversal, INCOMING

class Part(Product):
  reference=StringProperty()

class Class(Part):
  def get_instances(self):
    definition = dict(node_class=Instance,
                      direction=INCOMING,
                      relation_type='INSTANCE_OF',
                      model=None)
    traversal = Traversal(self,
                          Instance.__label__,
                          definition)
    return traversal.all()

class Instance(Part):
  mother_class = RelationshipTo('Class', 'INSTANCE_OF')

  def get_assemblies(self):
    definition = dict(node_class=Assembly,
                      direction=INCOMING,
                      relation_type='ASSEMBLE',
                      model=AssembleRS)

    traversal = Traversal(self,
                          Assembly.__label__,
                          definition)
    return traversal.all()

  def get_class(self):
    return self.mother_class.get()