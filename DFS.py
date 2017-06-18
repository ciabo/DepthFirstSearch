
time=0
nodeAndTimes = {} #Yep, it is and not end

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
        if node.getColor() is "white":
            node.setParent(u)
            DFSVisit(node)
    u.setColor("black")
    time+=1
    u.setEndTime(time)
    nodeAndTimes[time] = u #Saves the the end time of each node (node as index)


def stronglyConnected(nodes):
    scc_list = []

    def dfswrap(node):
        scc = []

        def Scc(u):
            u.setColor("gray")
            for node in u.getSons():
                if node.getColor() is "white":
                    node.setParent(u)
                    Scc(node)
            u.setColor("black")
            scc.append(u)

        Scc(node)
        return scc

    def DFStrasposed(nodelist):
        global nodeAndTimes
        reversenode = []
        for endtime, node in reversed(sorted(nodeAndTimes.iteritems())): #.iteritems(): Return an iterator over the dictionary’s (key, value) pairs.
            reversenode.append(node)
        for node in nodelist:
            node.setColor("white")
        for node in reversenode:
            if node.getColor() == "white":
                scc_list.append(dfswrap(node))

    DFStrasposed(nodes)
    return scc_list
