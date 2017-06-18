import Graph
from timeit import default_timer as timer
import matplotlib.pyplot as mp

def createGraph(nodeNumber):
    edgeNumber = 0
    endit = nodeNumber * nodeNumber
    list=[]
    while edgeNumber <= endit:
        start = timer()
        Graph.createGraph(nodeNumber, edgeNumber)
        end = timer()
        time=end-start
        #print("Graph with ",nodeNumber," nodes and ",edgeNumber," edges ---> Time: ",time)
        edgeNumber += 1
        list.append(time)
    return list

def test():
    list2=createGraph(2)
    list8=createGraph(8)
    list20=createGraph(20)
    list50=createGraph(50)
    list100=createGraph(100)
    xAxis=[]
    for i in range(0,len(list2)):
        xAxis.append(i)
    mp.plot(xAxis, list2)

    mp.xlabel('Number of edges')
    mp.ylabel('Creation time')
    mp.title("Graph with 2 vertices")
    mp.show()

    xAxis = []
    for i in range(0, len(list8)):
        xAxis.append(i)
    mp.plot(xAxis, list8)

    mp.xlabel('Number of edges')
    mp.ylabel('Creation time')
    mp.title("Graph with 8 vertices")
    mp.show()

    xAxis = []
    for i in range(0, len(list20)):
        xAxis.append(i)
    mp.plot(xAxis, list20)

    mp.xlabel('Number of edges')
    mp.ylabel('Creation time')
    mp.title("Graph with 20 vertices")
    mp.show()

    xAxis = []
    for i in range(0, len(list50)):
        xAxis.append(i)
    mp.plot(xAxis, list50)

    mp.xlabel('Number of edges')
    mp.ylabel('Creation time')
    mp.title("Graph with 50 vertices")
    mp.show()

    xAxis = []
    for i in range(0, len(list100)):
        xAxis.append(i)
    mp.plot(xAxis, list100)

    mp.xlabel('Number of edges')
    mp.ylabel('Creation time')
    mp.title("Graph with 100 vertices")
    mp.show()