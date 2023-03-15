



#%%
import sys
from time import perf_counter

sys.setrecursionlimit(500000)

from graph import Graph, graph_from_file, time_min_power, kruskal, build_oriented_tree, min_power_tree
# construire le fichier temps.min.power
file = r"C:\Users\keteb\OneDrive\Bureau\ensae-prog23\delivery_network\temps.min_power"
f = open(file, 'w')
f.write("temps de calcul : min_power Q6\n")

for x in range(1, 11):
    network = "network."+str(x)+".in"
    t = time_min_power(network)
    f.write("routes"+str(x)+": "+str(t)+"sec = "+str(t/60)+"min"+"\n")

f.close()


#%%
import sys
from time import perf_counter

sys.setrecursionlimit(500000)
from graph import Graph, graph_from_file, time_min_power, kruskal, build_oriented_tree, min_power_tree, level, min_power_lca, process

g = graph_from_file(r"C:\Users\keteb\OneDrive\Bureau\ensae-prog23\input\network.2.in")
tree = kruskal(g)
ot = build_oriented_tree(tree)
print(1)
print(level(tree))
print(process(ot))


# %%
