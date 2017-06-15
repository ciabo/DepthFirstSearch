
time=0

def DFS(nodeList):
    for node in nodeList:
        node.setParent(None)
    for node in nodeList:
        if node.getColor()=="white":
            DFSVisit(node)


def DFSVisit(u):
    global time
    time+=1
    u.setD(time)
    u.setColor("gray")
    for node in u.getSons():
        c=node.getColor()
        if node.getColor() is "white":
            node.setParent(u)
            DFSVisit(node)
    u.setColor("black")
    time+=1
    u.setEndTime(time)