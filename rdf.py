from rdflib import Graph
import graphviz

import random


def read_graph_render():
    with open('./renders/graph.gv.png', 'rb') as f:
        image = f.read()

    return image


def create_graph(turtle_input):
    dot = graphviz.Digraph('graph', comment='Turtle Graph', format='png')
    graph = Graph()

    graph.parse(data=turtle_input)

    for subj, pred, obj in graph:
        # Naming nodes after URIs causes issues with backslashes and
        # colons. Nodes are given the last part of the URI as a name
        # and the node label gets the full URI.
        subj_node = subj.split("/")[-1]
        obj_node = obj.split("/")[-1]
        dot.node(subj_node, subj)
        dot.node(obj_node, obj)

        # Give each edge a random color
        rand_color = "#%06x" % random.randint(0, 0xFFFFFF)
        dot.edge(subj_node, obj_node, label=pred,
                 color=rand_color, fontcolor=rand_color)

    dot = dot.unflatten(stagger=3)
    dot.render(directory='./renders/')
