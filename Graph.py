import Node
import AdjacencyMatrix
import numpy as np

def createGraph(vertices, edges):
    nodeList=[]
    for i in range(0,vertices):
        nodeList.append(Node.Node())
    adjMatrix=AdjacencyMatrix.createMatrix(vertices,edges)
    #adjMatrix=np.array([[0,1,0],[0,0,1],[1,0,0]])
    for i in range(0, vertices):
        for j in range(0,vertices):
            if adjMatrix[i][j]==1:
                nodeList[i].addSon(nodeList[j])
    returnList=[adjMatrix,nodeList]
    return returnList

def transpose(matrix):
    nodeList = []
    for i in range(0,len(matrix)):
        nodeList.append(Node.Node())
    transposedMatrix=AdjacencyMatrix.traspose(matrix)
    for i in range(0, len(matrix)):
        for j in range(0,len(matrix)):
            if transposedMatrix[i][j]==1:
                nodeList[i].addSon(nodeList[j])
    returnList=[transposedMatrix,nodeList]
    return returnList