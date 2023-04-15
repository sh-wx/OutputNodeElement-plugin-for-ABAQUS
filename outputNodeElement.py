from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup
from numpy import *
import regionToolset
import numpy as np
import os
import time
import shutil
import math
def main(modelname,instancename,nodeY,elementY,filen,filel):  
    lnode=len(mdb.models[modelname].rootAssembly.instances[instancename].nodes)
    nodematrix = np.zeros((lnode, 4))
    b=mdb.models[modelname].rootAssembly.instances[instancename]
    for i in range(lnode):
        nodematrix[i, :] =np.hstack((b.nodes[i].label,b.nodes[i].coordinates))
    if nodeY==True:
        np.savetxt(filen, np.c_[nodematrix],fmt='%f',delimiter='\t')
        print('The node file has been output')
    if elementY==True:
        lelement=len(b.elements)
        esize=size(b.elements[0].connectivity)
        elementmatrix=np.zeros((lelement, esize+1))
        for i in range(lelement):
            elementmatrix[i, :] =np.hstack((b.elements[i].label,b.elements[i].connectivity))
        elementmatrix[:,1:]=elementmatrix[:,1:]+1
        np.savetxt(filel, np.c_[elementmatrix],fmt='%f',delimiter='\t')
        print('The element file has been output')
    print('All done! Enjoy!')