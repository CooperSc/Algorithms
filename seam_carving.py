# CS4102 Spring 2022 -- Unit C Programming
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

import math
import numpy as np

class SeamCarving:

    def __init__(self):
        self.seam = []
        return

    # This method is the one you should implement.  It will be called to perform
    # the seam carving.  You may create any additional data structures as fields
    # in this class or write any additional methods you need.
    # 
    # @return the seam's weight
    def run(self, image):
        self.seam = [0 for x in range(len(image))]
        energies = [[0 for x in range(len(image[0]))] for y in range(len(image))]
        for j in range(len(image)):
            for i in range(len(image[0])):
                sum = 0
                if (i != 0 and i != len(image[0]) - 1 and j != 0 and j != len(image) - 1):
                    sum += self.dist(image[j][i],image[j + 1][i]) + self.dist(image[j][i],image[j + 1][i + 1]) + self.dist(image[j][i],image[j + 1][i - 1]) + self.dist(image[j][i],image[j][i + 1]) + self.dist(image[j][i],image[j][i - 1]) + self.dist(image[j][i],image[j - 1][i]) + self.dist(image[j][i],image[j - 1][i + 1]) + self.dist(image[j][i],image[j - 1][i - 1])
                    energies[j][i] = sum / 8
                if (i == 0 and j != 0 and j != len(image) - 1):
                    sum += self.dist(image[j][i],image[j + 1][i]) + self.dist(image[j][i],image[j + 1][i + 1]) + self.dist(image[j][i],image[j][i + 1]) + self.dist(image[j][i],image[j - 1][i + 1]) + self.dist(image[j][i],image[j - 1][i])
                    energies[j][i] = sum / 5
                    continue
                if (i == len(image[0]) - 1 and j != 0 and j != len(image) - 1):
                    sum += self.dist(image[j][i],image[j - 1][i]) + self.dist(image[j][i],image[j - 1][i - 1]) + self.dist(image[j][i],image[j][i - 1]) + self.dist(image[j][i],image[j + 1][i]) + self.dist(image[j][i],image[j + 1][i - 1])
                    energies[j][i] = sum / 5
                    continue
                if (j == 0 and i != 0 and i != len(image[0]) - 1):
                    sum += self.dist(image[j][i],image[j + 1][i]) + self.dist(image[j][i],image[j + 1][i + 1]) + self.dist(image[j][i],image[j + 1][i - 1]) + self.dist(image[j][i],image[j][i + 1]) + self.dist(image[j][i],image[j][i - 1])
                    energies[j][i] = sum / 5
                if (j == len(image) - 1 and i != 0 and i != len(image[0]) - 1):
                    sum += self.dist(image[j][i],image[j][i + 1]) + self.dist(image[j][i],image[j][i - 1]) + self.dist(image[j][i],image[j - 1][i]) + self.dist(image[j][i],image[j - 1][i - 1]) + self.dist(image[j][i],image[j - 1][i + 1])
                    energies[j][i] = sum / 5
                    continue
                if (i == 0 and j == 0):
                    sum += self.dist(image[j][i],image[j + 1][i]) + self.dist(image[j][i],image[j + 1][i + 1]) + self.dist(image[j][i],image[j][i + 1])
                    energies[j][i] = sum / 3
                    continue
                if (i == len(image[0]) - 1 and j == 0):
                    sum += self.dist(image[j][i],image[j + 1][i]) + self.dist(image[j][i],image[j + 1][i - 1]) + self.dist(image[j][i],image[j][i - 1])
                    energies[j][i] = sum / 3
                    continue
                if (i == 0 and j == len(image) - 1):
                    sum += self.dist(image[j][i],image[j - 1][i]) + self.dist(image[j][i],image[j - 1][i + 1]) + self.dist(image[j][i],image[j][i + 1])
                    energies[j][i] = sum / 3
                    continue
                if (i == len(image[0]) - 1 and j == len(image) - 1):
                    sum += self.dist(image[j][i],image[j - 1][i]) + self.dist(image[j][i],image[j - 1][i - 1]) + self.dist(image[j][i],image[j][i - 1])
                    energies[j][i] = sum / 3
                    continue
        seams = [[0 for x in range(len(image[0]))] for y in range(len(image))]
        #energies2 = np.array(energies.copy())
        seams[0][0:] = energies[0][0:]



        for j in range(1,len(image)):
            for i in range(len(image[0])):
                if (j == 0):
                    seams = energies[j][i]
                    continue
                if (i == 0):
                    seams[j][i] = energies[j][i] + min(seams[j - 1][i:i + 2])
                    continue
                elif (i == len(image[0]) - 1):
                    seams[j][i] = energies[j][i] + min(seams[j - 1][i - 1:i + 1])
                    continue
                else:
                    seams[j][i] = energies[j][i] + min(seams[j - 1][i - 1:i + 2])

        self.seam[len(image) - 1] = int(seams[len(image) - 1][:].index(min(seams[len(image) - 1][:])))
        # print(min(seams[len(image) - 1][:]))
        # print(seams[len(image) - 1][:])
        # print(len(seams[len(image) - 1][:]))
        # print(seams)
        for i in reversed(range(len(image) - 1)):

            if (self.seam[i + 1] == 0):
                #print(seams[int(self.seam[i + 1]): int(self.seam[i + 1]) + 2,i])
                self.seam[i] = int(self.seam[i+1] + seams[i][int(self.seam[i + 1]): int(self.seam[i + 1]) + 2].index(min(seams[i][int(self.seam[i + 1]): int(self.seam[i + 1]) + 2])))
            elif (self.seam[i + 1] == len(image) - 1):
                #print(seams[int(self.seam[i + 1]) - 1: int(self.seam[i + 1] + 1), i])
                self.seam[i] = int(self.seam[i+1] - 1 + seams[i][int(self.seam[i + 1]) - 1: int(self.seam[i + 1]) + 1].index(min(seams[i][int(self.seam[i + 1]) - 1: int(self.seam[i + 1]) + 1])))
            else:
                #print(seams[int(self.seam[i+1]) - 1 : int(self.seam[i+1]) + 2,i])
                self.seam[i] = int(self.seam[i + 1] - 1 + seams[i][int(self.seam[i+1]) - 1 : int(self.seam[i+1]) + 2].index(min(seams[i][int(self.seam[i+1]) - 1 : int(self.seam[i+1]) + 2])))
        return min(seams[len(image) - 1][:])

    def dist(self,val1,val2):
        return math.sqrt((val1[0] - val2[0])**2 + (val1[1] - val2[1])**2 + (val1[2] - val2[2])**2)
    # Get the seam, in order from top to bottom, where the top-left corner of the
    # image is denoted (0,0).
    #
    # Since the y-coordinate (row) is determined by the order, only return the x-coordinate
    # 
    # @return the ordered list of x-coordinates (column number) of each pixel in the seam
    #         as an array
    def getSeam(self):
        return self.seam

