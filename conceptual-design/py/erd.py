# Entity-Relationship Diagram (ERD) Definition

import networkx as nx
import matplotlib.pyplot as plt
from functools import reduce
import math

# An Entity-Relationship Diagram as a type of networkx graph
#
# The vertex set includes all entity sets, relationships,
# attributes, and collections of entity sets
# The edge set connects entity sets to relationships, attributes,
# and/or collections of other entity sets. It also may connect
# attributes to relationships (i.e., the graph has a min colouring of 3)
#
# The class also contains a mapping from every entity set to one identifier.
# These are not drawn by the plotting library due to the complexity of support
# for weak entity sets.
class ERD:
    def __init__(self):
        self.graph = nx.Graph()
        self.identifiers = {}
    def add_entity_set(self, es):
        self.graph.add_node(es, s='s')
    def add_relationship(self, rel):
        self.graph.add_node(rel, s='d')
    def add_attribute(self, att):
        self.graph.add_node(att, s='o')
    def add_identifier(self, es, attributes):
        self.identifiers[es] = attributes
    def add_generalisation(self, generalisation, specialisations, style):
        self.add_entity_set(generalisation)
        isA = reduce(lambda x, y: x + " " + y, specialisations)
        self.graph.add_node(isA, s='^')
        self.graph.add_edges_from([(generalisation, isA, {"style":style})])
        self.graph.add_edges_from([(specialisation, isA) for specialisation in specialisations])
    def connect(self, es, rel, min_card, max_card):
        self.graph.add_edges_from([(es, rel, {"min": min_card, "max" : max_card})])
    def attach(self, att, es):
        self.graph.add_edge(att, es)
    def draw(self):
        # TODO: Draw edge and vertex labels
        # From https://stackoverflow.com/a/31195070/2769271
        nodePos = nx.layout.spring_layout(self.graph)
        nodeShapes = set((aShape[1]["s"] for aShape in self.graph.nodes(data = True)))
        for aShape in nodeShapes:
             nx.draw_networkx_nodes(self.graph,nodePos,node_shape = aShape, \
                nodelist = [sNode[0] for sNode in filter(lambda x: x[1]["s"]==aShape,self.graph.nodes(data = True))])
        nx.draw_networkx_edges(self.graph,nodePos)
        plt.show()

def test():
    erd = ERD()
    erd.add_entity_set("A")
    erd.add_attribute("a")
    erd.add_entity_set("B")
    erd.add_attribute("b")
    erd.add_relationship("R")
    erd.connect("A", "R", 0, 1)
    erd.connect("B", "R", 1, 100)
    erd.attach('a', "A")
    erd.attach('b', "B")
    erd.add_generalisation("C", ["A","B"], "(t,e)")
    erd.draw()

# test()
