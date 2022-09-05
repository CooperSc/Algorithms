# CS4102 Spring 2022 - Unit A Programming 
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
# Your Computing ID: Cms4ub
# Collaborators: N/A
# Sources: Introduction to Algorithms, Cormen, Wikipedia page on Quicksort
#################################
import numpy as np
def dataToVar(file_data):
        x = np.zeros(len(file_data))
        y = np.zeros(len(file_data))
        count = 0
        for points in file_data:
            nums = points.split()
            x[count] = float(nums[0])
            y[count] = float(nums[1])
            count = count + 1
        return np.vstack((x,y)).T

def quicksort(Arr,first,last,coord):
        if first >= last or first < 0:
            return
        
        index = partition(Arr,first,last,coord)
        quicksort(Arr,first,index-1,coord)
        quicksort(Arr,index+1,last,coord)
        return 
        
def partition(Arr,first,last,coord):
        pivot = Arr[last,coord]
        
        temp = first - 1
        
        for i in range(first,last):
            if (Arr[i,coord] <= pivot):
                temp = temp + 1
                tempVal = Arr[i].copy()
                Arr[i] = Arr[temp]
                Arr[temp] = tempVal
        temp = temp + 1
        tempVal = Arr[temp].copy()
        Arr[temp] = Arr[last]
        Arr[last] = tempVal
        return temp

def closestPoints(Arr,first,last):
        #print("first",first,last)
        if last - first == 0:
            return 10**9
        if last - first == 1:
            return dist(Arr[last],Arr[first])
        if last - first == 2:
            vals = np.zeros(3)
            vals[0] = dist(Arr[last],Arr[first])
            vals[1] = dist(Arr[last-1],Arr[first])
            vals[2] = dist(Arr[last-1],Arr[last])
            return np.sort(vals)[0:2]
        if last - first == 3:
            vals = np.zeros(6)
            vals[0] = dist(Arr[last],Arr[first])
            vals[1] = dist(Arr[last-1],Arr[first])
            vals[2] = dist(Arr[last-1],Arr[last])
            vals[3] = dist(Arr[last-1],Arr[last - 2])
            vals[4] = dist(Arr[last-2],Arr[first])
            vals[5] = dist(Arr[last-2],Arr[last])
            return np.sort(vals)[0:2]
                
                
        
        median = int(first + (last-first)/2)
        if 
        medianVal = Arr[median,0]
        #print("median:",median,medianVal)
        mins = np.concatenate((closestPoints(Arr,first,median),closestPoints(Arr,median,last)))
        mins = np.sort(mins) 
        min2 = mins[1]
        min1 = mins[0]
        
        runLeft = -1
        runRight = last + 1
        for i in range(first,last):
            if (medianVal - Arr[i,0] < mins[1]):
                #print("Arr",Arr[i,0],i)
                runLeft = i
                break
        for i in range(last,first,-1):
            if (Arr[i,0] - medianVal < mins[1]):
                runRight = i
                break

        #print("Left",runLeft)
        #print("Right",runRight)
        if (runLeft != -1 and runRight != last + 1):
            tempArr = Arr[runLeft:runRight+1,:].copy()
            tempArr = tempArr[np.argsort(tempArr[:,1])]
            numCompare = 15
            for i in range(runRight - runLeft):
                for j in range(i+1,min(i + numCompare + 1,runRight-runLeft)):
                    if (i < median and j > median):
                        distance = dist(tempArr[i],tempArr[j])
                        if distance < min2:
                            min2 = distance
                        if min2 < min1:
                            temp = min1.copy()
                            min1 = distance
                            min2 = temp
        #print("Out",np.array([min1,min2]))
        return np.array([min1,min2])
                    
                    
def dist(point1,point2):
        return np.sqrt((point2[1]-point1[1])**2 + (point2[0]-point1[0])**2)
                    
                           


class ClosestPair:
    
    def __init__(self):
        return

    # This is the method that should set off the computation
    # of closest pair.  It takes as input a list containing lines of input
    # as strings.  You should parse that input and then call a
    # subroutine that you write to compute the closest pair distances
    # and return those values from this method
    #
    # @return the distances between the closest pair and second closest pair
    # with closest at position 0 and second at position 1 
      
    def compute(self, file_data):
        Arr = dataToVar(file_data)
        Arr2 = dataToVar(file_data)
        #quicksort(Arr,0,Arr.shape[0] - 1,0)
        #quicksort(Arr2,0,Arr.shape[0] - 1,1)
        Arr = Arr[np.argsort(Arr[:,0])]
        closest,secondClosest = closestPoints(Arr,0,len(Arr)-1)
        return [closest, secondClosest]
    
    
        
                
        
