import random

import networkx as nx
import matplotlib.pyplot as plt

N = 10

G = nx.grid_2d_graph(N, N)
pos = dict((n,n) for n in G.nodes() ) # This function is used to find the location of nodes in 2D plane
labels = dict(((i,j), i*10+j) for i, j in G.nodes())
def display_graph(G):
    nodes_g = nx.draw_networkx_nodes(G,pos, node_color='green', nodelist= type1_node_list)
    nodes_r = nx.draw_networkx_nodes(G,pos, node_color='red', nodelist= type2_node_list)
    nodes_w = nx.draw_networkx_nodes(G,pos, node_color='white', nodelist= empty_cells)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos,labels= labels)
    plt.show()
def get_boundary_nodes(G):
    get_boundary_nodes_list = []
    if ((u,v),d) in G.nodes(data = True):
        if ((u,v), d) in G.nodes(data = True):
            if u ==0 or u == N-1 or v == 0 or v == N-1:
                get_boundary_nodes_list.append((u,v))
                print(get_boundary_nodes_list)
#Add diagonal edges
    return get_boundary_nodes_list


def get_neigh_for_internal(u, v):
    return [(u-1, v),(u+1, v),(u, v-1),(u, v+1),(u-1, v+1),(u+1, v-1),(u-1, v-1),(u+1, v+1)]


def get_neigh_for_boundary(u, v):
    # global N
    # print 'uv', u, v
    if u == 0 and v == 0:
        return [(0, 1),(1, 1), (1, 0)]
    elif u == N-1 and v == N-1:
        return [(N-2, N-2), (N-1, N-2), (N-2, N-1)]
    elif u == N-1 and v == 0:
        return [(u-1, v), (u,v+1), (u-1, v+1)]
    elif u == 0 and v == N-1:
        return [(u+1, v), (u+1, v-1), (u, v-1)]
    elif u == 0:
        return [(u, v-1), (u, v+1), (u+1, v), (u+1, v-1), (u+1, v+1)]
    elif u == N-1:
        return [(u-1, v), (u, v-1), (u, v+1), (u-1, v+1), (u-1, v-1)]
    elif v == N-1:
        return [(u, v-1), (u-1, v), (u+1, v), (u-1, v-1), (u+1, v-1)]
    elif v == 0:
        return [(u-1, v), (u+1, v), (u, v+1), (u-1, v+1), (u+1, v+1)]


def get_unsatified_nodes_list(G, internal_nodes, boundary_nodes):
    unsatified_nodes_list = []
    for u, v in G.nodes():
        type_of_this_node = G.node[(u, v)]['type']
        if type_of_this_node == 0:
            continue
        else:
            similar_nodes = 0
            if (u, v) in internal_nodes:
                neigh = get_neigh_for_internal(u, v)
            elif (u, v) in boundary_nodes:
                neigh = get_neigh_for_boundary(u, v)

            for each in neigh:
                if G.node[each]['type'] == type_of_this_node:
                    similar_nodes += 1

            if similar_nodes <= t:
                unsatified_nodes_list.append((u, v))

    return unsatified_nodes_list


for ((u,v),d) in G.nodes(data = True):
        if u+1 <= N-1:
               if v+1 <= N-1:

                  G.add_edge((u,v), (u+1,v+1))

               if v-1 >= 0:

                    G.add_edge((u,v), (u+1,v-1))


plt.show()
G.nodes()

for n in G.nodes():
    G.node[n]['type'] = random.randint(0,2)
type1_node_list = [n for (n,d) in G.nodes(data = True) if d['type'] == 1]
type2_node_list = [n for (n,d) in G.nodes(data = True) if d['type'] == 2]

empty_cells = [n for (n,d) in G.nodes(data = True) if d['type'] == 0]
#print (type1_node_list)
#print (type2_node_list)
#print (empty_cells)



nx.draw(G,pos)
plt.show()
display_graph(G)

get_boundary_nodes_list = get_boundary_nodes(G)
internal_nodes_list = list(set(G.nodes())- set(get_boundary_nodes_list))
print(get_boundary_nodes_list)
print(internal_nodes_list)