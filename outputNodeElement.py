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
def main(modelname,instancename,nodeY,elementY,filen,filel,useset,nodeset,elementset):  
    if useset==True:
        nodesett=mdb.models[modelname].rootAssembly.sets[nodeset]
        nodematrix = np.zeros((len(nodesett.nodes), 4))
        for i in range(len(nodesett.nodes)):
            nodematrix[i, :] =np.hstack((nodesett.nodes[i].label,nodesett.nodes[i].coordinates))
        elementsett=mdb.models[modelname].rootAssembly.sets[elementset]
        esize=size(elementsett.elements[0].connectivity)
        elementmatrix=np.zeros((len(elementsett.elements), esize+1))
        for i in range(len(elementsett.elements)):
            elementmatrix[i, :] =np.hstack((elementsett.elements[i].label,elementsett.elements[i].connectivity))
        if nodeY==True:
            np.savetxt(filen, np.c_[nodematrix],fmt='%f',delimiter='\t')
            print('The node file has been output')
        if elementY==True:
            np.savetxt(filel, np.c_[elementmatrix],fmt='%f',delimiter='\t')
            print('The element file has been output')
    else:
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