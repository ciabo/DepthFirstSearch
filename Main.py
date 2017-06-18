import Graph
import DFS
import Tests
'''
vals=Graph.createGraph(3,2)
matrix=vals[0]
nodeList=vals[1]
DFS.DFS(nodeList)
transposedVals=Graph.transpose(matrix)
transposedMatrix=transposedVals[0]
transposedNodeList=transposedVals[1]
print(matrix)
print(transposedMatrix)
scclist = DFS.stronglyConnected(transposedNodeList)
'''
Tests.test()