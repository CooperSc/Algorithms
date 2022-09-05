# CS4102 Spring 2022 - Unit B Programming
#################################
# Collaboration Policy: You are encouraged to collaborate with up to 3 other
# students, but all work submitted must be your own independently written
# solution. List the computing ids of all of your collaborators in the
# comments at the top of each submitted file. Do not share written notes,
# documents (including Google docs, Overleaf docs, discussion notes, PDFs), or
# code. Do not seek published or online solutions, including pseudocode, for
# this assignment. If you use any published or online resources (which may not
# include solutions) when completing this assignment, be sure to cite them. Do
# not submit a solution that you are unable to explain orally to a member of
# the course staff. Any solutions that share similar text/code will be
# considered in breach of this policy. Please refer to the syllabus for a
# complete description of the collaboration policy.
#################################
# Your Computing ID: cms4ub
# Collaborators:
# Sources: Introduction to Algorithms, Cormen
#################################

import numpy as np

class Supply:
    def __init__(self):
        return

    # This is the method that should set off the computation
    # of the supply chain problem.  It takes as input a list containing lines of input
    # as strings.  You should parse that input and then call a
    # subroutine that you write to compute the total edge-weight sum
    # and return that value from this method
    #
    # @return the total edge-weight sum of a tree that connects nodes as described
    # in the problem statement
    def compute(self, file_data):
        edgeWeightSum = 0

        line = file_data[0].split()
        nodesCount = int(line[0])
        linkCount = int(line[1])

        nodes = np.zeros(nodesCount)
        nodeNames = []
        nodeListByName = {}
        nodeListByIndex = {}
        links = np.zeros((linkCount,3))
        distCenter = -1
        for i in range(nodesCount):
            line = file_data[i + 1].split()
            nodes[i] = i
            nodeNames.append(line[0])
            type = 0
            if (line[1] == "rail-hub"):
                type = 1
            elif (line[1] == "dist-center"):
                type = 2
                distCenter = i
            elif (line[1] == "store"):
                type = 3
            nodeListByName[line[0]] = [i,type, distCenter]
            nodeListByIndex[i] = [i,type, distCenter]

        for i in range(linkCount):
            line = file_data[i + nodesCount + 1].split()
            node1 = nodeListByName[line[0]]
            node2 = nodeListByName[line[1]]

            validLink = False
            if (((node1[1] == 0 or node1[1] == 1) and (node2[1] == 1 or node2[1] == 2)) or ((node2[1] == 0 or node2[1] == 1) and (node1[1] == 1 or node1[1] == 2)) or (node1[1] == 2 and node2[1] == 3 and node2[2] == node1[0]) or (node1[1] == 3 and node2[1] == 2 and node1[2] == node2[0]) or (node1[1] == 3 and node2[1] == 3)):
            #if (((node1[1] == 0 or node1[1] == 1) and (node2[1] == 1 or node2[1] == 2)) or ((node2[1] == 0 or node2[1] == 1) and (node1[1] == 1 or node1[1] == 2)) or (node1[1] == 2 and node2[1] == 3) or (node1[1] == 3 and node2[1] == 2) or (node1[1] == 3 and node2[1] == 3)):
                validLink = True

            if validLink:
                links[i][0] = node1[0]
                links[i][1] = node2[0]
                links[i][2] = int(line[2])
            else:
                links[i][0] = -1
                links[i][1] = -1
                links[i][2] = -1


        links = np.delete(links,np.argwhere(links[:,0] == -1),axis=0)
        links = links[np.argsort(links, axis = 0)[:,2]]

        edgeWeightSum = self.kruskal(links, nodeListByIndex, nodes, nodesCount, linkCount)

        # your function to compute the result should be called here

        return edgeWeightSum

    def kruskal(self, links, nodeListByIndex, nodes, nodesCount, linkCount):
        disjointsets = nodes
        edgesAccepted = 0
        edgeWeightSum = 0
        print(nodeListByIndex)
        while (edgesAccepted < nodesCount - 1):
            print(edgesAccepted)
            print(links)
            print(nodes)
            #print(links[0][0])
            #print(nodeListByIndex)
            node1List = nodeListByIndex[links[0][0]]
            node1 = node1List[0]
            node2List = nodeListByIndex[links[0][1]]
            node2 = node2List[0]
            #if ((nodeListByIndex[node1][2] != -1 and nodeListByIndex[node2][1] != 3) or (nodeListByIndex[node2][2] != -1 and nodeListByIndex[node1][1] != 3)): #or (nodeListByIndex[node1][2] != -1 and nodeListByIndex[node2][2] != -1)):
               # links = np.delete(links, 0, axis = 0)
                #continue
            if (nodes[node1] == nodes[node2]):
                links = np.delete(links, 0, axis=0)
                continue
            #if (nodeListByIndex[node1][1] == 3):
               # nodeListByIndex[node1][1] = node2
            #if (nodeListByIndex[node2][1] == 3):
                #nodeListByIndex[node2][1] = node1
            #print(nodes)
            #print(node1,node2)
            nodes = self.union(node1,node2,nodes)
            #links = np.delete(links, 0, axis=0)
            #print(nodes)
            edgeWeightSum += links[0][2]
            edgesAccepted += 1

        return edgeWeightSum

    def union(self,node1Index,node2Index,nodes):
        #setIndices1 = np.argwhere(nodes == node1[0])
        setIndices2 = np.argwhere(nodes == nodes[node2Index])
        for i in setIndices2:
            nodes[i] = nodes[node1Index]
        return nodes


