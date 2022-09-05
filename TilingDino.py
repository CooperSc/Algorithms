# CS4102 Spring 2022 -- Unit D Programming
#################################
# Collaboration Policy: You are encouraged to collaborate with up to 3 other
# students, but all work submitted must be your own independently written
# solution. List the computing ids of all of your collaborators in the comment
# at the top of your java or python file. Do not seek published or online
# solutions for any assignments. If you use any published or online resources
# (which may not include solutions) when completing this assignment, be sure to
# cite them. Do not submit a solution that you are unable to explain orally to a
# member of the course staff.
#################################
# Your Computing ID: cms4ub
# Collaborators: 
# Sources: Introduction to Algorithms, Cormen
#################################
import networkx as nx
from networkx.algorithms.flow import edmonds_karp
# import matplotlib.pyplot as plt


class TilingDino:
    def __init__(self):
        return

    # This is the method that should set off the computation
    # of tiling dino.  It takes as input a list lines of input
    # as strings.  You should parse that input, find a tiling,
    # and return a list of strings representing the tiling
    #
    # @return the list of strings representing the tiling
    def compute(self, lines):
        tiling = [[0 for x in range(len(lines[0]))] for y in range(len(lines))]
        #tiling = [[0 for x in range(6)] for y in range(len(lines))]
        lineIndex = 0
        tilingSum = 0
        for line in lines:
            stringIndex = 0
            for string in line:
                # if (stringIndex == 7):
                #     break
                if(string == "."):
                    tiling[lineIndex][stringIndex] = 0
                if (string == "#"):
                    tiling[lineIndex][stringIndex] = 1
                    tilingSum = tilingSum + 1
                stringIndex = stringIndex + 1
            lineIndex = lineIndex + 1


        # plt.imshow(tiling, cmap='hot', interpolation='nearest')
        # plt.show()

        G = nx.Graph()
        coeff = 0
        #coff2 = 2
        nodeCount = 0
        for x in range(len(tiling)):
            for y in range(len(tiling[0])):
                AddedStartNode = False
                AddedEndNode = False
                if (tiling[x][y] == 0):
                    G.add_node(nodeCount, xVal=x, yVal=y, bipartite=2)
                elif (tiling[x][y] == 1):
                    startNodeCheck = True
                    if (x != 0):
                        startNodeCheck = (G.nodes[nodeCount - len(tiling[0])]['bipartite'] != 0)
                    if (y != 0 and startNodeCheck):
                        startNodeCheck = (G.nodes[nodeCount - 1]['bipartite'] != 0)
                    # if(y != len(tiling[0]) - 1 and startNodeCheck):
                    #     if (tiling[x][y + 1] == 1):
                    #         G.add_node(nodeCount, xVal=x, yVal=y, bipartite=0)
                    #         AddedStartNode = True
                    # if (x != len(tiling) - 1 and AddedStartNode == False and startNodeCheck):
                    #     if (tiling[x + 1][y] == 1):
                    #         G.add_node(nodeCount, xVal=x, yVal=y, bipartite=0)
                    #         AddedStartNode = True
                    #if (startNodeCheck and (x != len(tiling) - 1 or y != len(tiling[0]) - 1)):
                    if startNodeCheck:
                        G.add_node(nodeCount, xVal=x, yVal=y, bipartite=0)
                        AddedStartNode = True
                    if (y != 0 and AddedStartNode == False):
                        if (tiling[x][y - 1] == 1):
                            G.add_node(nodeCount + len(tiling) * len(tiling[0]) * coeff, xVal=x, yVal=y, bipartite=1)
                            AddedEndNode = True
                    if (x != 0 and AddedEndNode == False and AddedStartNode == False):
                        if (tiling[x - 1][y] == 1):
                            G.add_node(nodeCount + len(tiling) * len(tiling[0]) * coeff, xVal=x, yVal=y, bipartite=1)
                    #if(AddedEndNode and AddedStartNode):
                        #G.add_node(nodeCount + len(tiling) * len(tiling[0]) * coeff * 2, xVal=x, yVal=y, bipartite=1)
                        #G.add_edge(nodeCount, nodeCount + len(tiling) * len(tiling[0]) * coeff, capacity=1)
                        #G.add_edge(nodeCount + len(tiling) * len(tiling[0]) * coeff, nodeCount + len(tiling) * len(tiling[0]) * coeff * 2, capacity=1)
                nodeCount = nodeCount + 1

        endDict = {}
        startDict = {}
        #print(nodeCount)
        G.add_node(nodeCount,xVal=0, yVal=0, bipartite=2)
        G.add_node(nodeCount + 1,xVal=0, yVal=0, bipartite=2)
        for x in range(len(tiling)):
            for y in range(len(tiling[0])):
                if (x != len(tiling) - 1 and y != len(tiling[0]) - 1 and tiling[x][y] == 1):
                    if (tiling[x + 1][y] == 1 and G.nodes[x * len(tiling[0]) + y]['bipartite'] == 0):
                        G.add_edge(x * len(tiling[0]) + y, (x + 1) * len(tiling[0]) + y + len(tiling) * len(tiling[0]) * coeff, capacity = 1)
                        startDict[x * len(tiling[0]) + y] = 1
                        endDict[(x + 1) * len(tiling[0]) + y + len(tiling) * len(tiling[0]) * coeff] = 1
                    if (tiling[x][y + 1] == 1  and G.nodes[x * len(tiling[0]) + y]['bipartite'] == 0):
                        G.add_edge(x * len(tiling[0]) + y, x * len(tiling[0]) + y + 1 + len(tiling) * len(tiling[0]) * coeff, capacity = 1)
                        startDict[x * len(tiling[0]) + y] = 1
                        endDict[x * len(tiling[0]) + y + 1 + len(tiling) * len(tiling[0]) * coeff] = 1
                    if (x != 0):
                        if (tiling[x - 1][y] == 1 and G.nodes[x * len(tiling[0]) + y]['bipartite'] == 0):
                            G.add_edge(x * len(tiling[0]) + y, (x - 1) * len(tiling[0]) + y + len(tiling) * len(tiling[0]) * coeff, capacity=1)
                            startDict[x * len(tiling[0]) + y] = 1
                            endDict[(x - 1) * len(tiling[0]) + y + len(tiling) * len(tiling[0]) * coeff] = 1
                    if (y != 0):
                        if (tiling[x][y - 1] == 1 and G.nodes[x * len(tiling[0]) + y]['bipartite'] == 0):
                            G.add_edge(x * len(tiling[0]) + y,x * len(tiling[0]) + y - 1 + len(tiling) * len(tiling[0]) * coeff, capacity=1)
                            startDict[x * len(tiling[0]) + y] = 1
                            endDict[x * len(tiling[0]) + y - 1 + len(tiling) * len(tiling[0]) * coeff] = 1
                if (x == len(tiling) - 1 and y != len(tiling[0]) - 1 and tiling[x][y] == 1):
                    if (tiling[x][y + 1] == 1  and G.nodes[x * len(tiling[0]) + y]['bipartite'] == 0):
                        G.add_edge(x * len(tiling[0]) + y, x * len(tiling[0]) + y + 1 + len(tiling) * len(tiling[0]) * coeff, capacity = 1)
                        startDict[x * len(tiling[0]) + y] = 1
                        endDict[x * len(tiling[0]) + y + 1 + len(tiling) * len(tiling[0]) * coeff] = 1
                    if (x != 0):
                        if (tiling[x - 1][y] == 1 and G.nodes[x * len(tiling[0]) + y]['bipartite'] == 0):
                            G.add_edge(x * len(tiling[0]) + y, (x - 1) * len(tiling[0]) + y + len(tiling) * len(tiling[0]) * coeff, capacity=1)
                            startDict[x * len(tiling[0]) + y] = 1
                            endDict[(x - 1) * len(tiling[0]) + y + len(tiling) * len(tiling[0]) * coeff] = 1
                    if (y != 0):
                        if (tiling[x][y - 1] == 1 and G.nodes[x * len(tiling[0]) + y]['bipartite'] == 0):
                            G.add_edge(x * len(tiling[0]) + y,x * len(tiling[0]) + y - 1 + len(tiling) * len(tiling[0]) * coeff, capacity=1)
                            startDict[x * len(tiling[0]) + y] = 1
                            endDict[x * len(tiling[0]) + y - 1 + len(tiling) * len(tiling[0]) * coeff] = 1
                if (x != len(tiling) - 1 and y == len(tiling[0]) - 1 and tiling[x][y] == 1):
                    if (tiling[x + 1][y] == 1 and G.nodes[x * len(tiling[0]) + y]['bipartite'] == 0):
                        G.add_edge(x * len(tiling[0]) + y, (x + 1) * len(tiling[0]) + y + len(tiling) * len(tiling[0]) * coeff, capacity = 1)
                        startDict[x * len(tiling[0]) + y] = 1
                        endDict[(x + 1) * len(tiling[0]) + y + len(tiling) * len(tiling[0]) * coeff] = 1
                    if (x != 0):
                        if (tiling[x - 1][y] == 1 and G.nodes[x * len(tiling[0]) + y]['bipartite'] == 0):
                            G.add_edge(x * len(tiling[0]) + y, (x - 1) * len(tiling[0]) + y + len(tiling) * len(tiling[0]) * coeff, capacity=1)
                            startDict[x * len(tiling[0]) + y] = 1
                            endDict[(x - 1) * len(tiling[0]) + y + len(tiling) * len(tiling[0]) * coeff] = 1
                    if (y != 0):
                        if (tiling[x][y - 1] == 1 and G.nodes[x * len(tiling[0]) + y]['bipartite'] == 0):
                            G.add_edge(x * len(tiling[0]) + y,x * len(tiling[0]) + y - 1 + len(tiling) * len(tiling[0]) * coeff, capacity=1)
                            startDict[x * len(tiling[0]) + y] = 1
                            endDict[x * len(tiling[0]) + y - 1 + len(tiling) * len(tiling[0]) * coeff] = 1
                if (x == len(tiling) - 1 and y == len(tiling[0]) - 1 and tiling[x][y] == 1):
                    if (tiling[x - 1][y] == 1 and G.nodes[x * len(tiling[0]) + y]['bipartite'] == 0):
                        G.add_edge(x * len(tiling[0]) + y, (x - 1) * len(tiling[0]) + y + len(tiling) * len(tiling[0]) * coeff, capacity=1)
                        startDict[x * len(tiling[0]) + y] = 1
                        endDict[(x - 1) * len(tiling[0]) + y + len(tiling) * len(tiling[0]) * coeff] = 1
                    if (tiling[x][y - 1] == 1 and G.nodes[x * len(tiling[0]) + y]['bipartite'] == 0):
                        G.add_edge(x * len(tiling[0]) + y,x * len(tiling[0]) + y - 1 + len(tiling) * len(tiling[0]) * coeff, capacity=1)
                        startDict[x * len(tiling[0]) + y] = 1
                        endDict[x * len(tiling[0]) + y - 1 + len(tiling) * len(tiling[0]) * coeff] = 1
        for key in startDict.keys():
            G.add_edge(nodeCount,key,capacity = 1)

        #counter = 0

        for key in endDict.keys():
            #print(counter)
            #counter = counter + 1
            G.add_edge(key,nodeCount + 1,capacity = 1)
        #print(G.edges)

        top_nodes = {n for n, d in G.nodes(data=True) if d["bipartite"] == 0}

        selected_nodes = []
        count = 0
        for node in G.nodes(data=True):
            if (node[1]['bipartite'] != 2):
                selected_nodes.append(count)
            count = count + 1
        H = G.subgraph(selected_nodes)
        # labels = nx.get_edge_attributes(G, 'flow')
        # pos = pos = nx.spring_layout(G)
        # nx.draw(H, with_labels=True, node_size=300)
        # nx.draw_networkx_edge_labels(H, pos, edge_labels=labels)
        # plt.savefig("filename.png")
        dict = nx.bipartite.maximum_matching(H,top_nodes=top_nodes)
        # print(dict)
        # print(len(dict))

        #R = edmonds_karp(G,nodeCount,nodeCount + 1)
        flow_dict = {}
        flow, flow_dict = nx.maximum_flow(G,nodeCount,nodeCount + 1)
        # print("sum", tilingSum)
        # print("flow", flow)


        dominoes = [""] * int((tilingSum/2))
        dominoDict = {}


        if (flow != tilingSum / 2):
            return ["impossible"]

        count = 0
        # endKeys = flow_dict[nodeCount + 1].keys()
        # startKeys = flow_dict[nodeCount].keys()
        # print(endKeys)
        # print(startKeys)
        if (flow == tilingSum/2):
            count = 0
            for key in dict.keys():
                # if G.nodes[node]['bipartite'] != 2:
                #     for key in flow_dict[node].keys():
                #         if G.nodes[key]['bipartite'] != 2:
                #             if ((node in endKeys and key in startKeys) or (node in startKeys and key in endKeys)) and key!= nodeCount + 1 and flow_dict[node][key] == 1:
                #                 dominoes[count] = str(G.nodes[node]['yVal']) + " " + str(G.nodes[node]['xVal']) + " " + str(G.nodes[key]['yVal']) + " " + str(G.nodes[key]['xVal'])
                #                 count = count + 1
                if (dict[key] > key):
                    node = dict[key]
                    dominoes[count] = str(G.nodes[node]['yVal']) + " " + str(G.nodes[node]['xVal']) + " " + str(G.nodes[key]['yVal']) + " " + str(G.nodes[key]['xVal'])
                    count = count + 1
        # print(G.nodes(data=True))
        # print("count",count)
        #  count = 0
        # print(selected_nodes)

        return dominoes









