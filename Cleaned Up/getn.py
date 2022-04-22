
import numpy 
import getneighbourof
def mainfunc(input, TDA):

    cellx = numpy.where(TDA == input)
    cellx = cellx[0]
    celly = numpy.where(TDA == input)
    celly = celly[1]
    neigboors = []
    ncordsx = int(cellx)
    ncordsy = int(celly + 1)
    try:
        trailclass = TDA[ncordsx, ncordsy]
        

        isavalid = getneighbourof.main(trailclass, input, TDA)
        if (isavalid == True):

            neigboors.append(trailclass)
    except:
        pass
    ncordsx = int(cellx)
    ncordsy = int(celly - 1)
    try:
        trailclass = TDA[ncordsx, ncordsy]
        


        isavalid = getneighbourof.main(trailclass, input,TDA)
        if(isavalid == True):
            neigboors.append(trailclass)

    except:
        pass
    ncordsx = int(cellx + 1)
    ncordsy = int(celly)
    try:
        trailclass = TDA[ncordsx, ncordsy]
        

        isavalid = getneighbourof.main(trailclass, input,TDA)
        if (isavalid == True):
            neigboors.append(trailclass)
    except:
        pass
    ncordsx = int(cellx - 1)
    ncordsy = int(celly)
    try:
        trailclass = TDA[ncordsx, ncordsy]
        

        isavalid = getneighbourof.main(trailclass, input,TDA)
        if (isavalid == True):
            neigboors.append(trailclass)
    except:
        pass
    
    return neigboors
