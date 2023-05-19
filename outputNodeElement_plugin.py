from abaqusGui import *
from abaqusConstants import ALL
import osutils, os


###########################################################################
# Class definition
###########################################################################

class OutputNodeElement_plugin(AFXForm):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, owner):
        
        # Construct the base class.
        #
        AFXForm.__init__(self, owner)
        self.radioButtonGroups = {}

        self.cmd = AFXGuiCommand(mode=self, method='main',
            objectName='outputNodeElement', registerQuery=False)
        pickedDefault = ''
        self.modelnameKw = AFXStringKeyword(self.cmd, 'modelname', True, 'Model-1')
        self.nodesetKw = AFXStringKeyword(self.cmd, 'nodeset', True, 'NSet-1')
        self.instancenameKw = AFXStringKeyword(self.cmd, 'instancename', True, 'Part-1-1')
        self.elementsetKw = AFXStringKeyword(self.cmd, 'elementset', True, 'ESet-1')
        self.usesetKw = AFXBoolKeyword(self.cmd, 'useset', AFXBoolKeyword.TRUE_FALSE, True, False)
        self.nodeYKw = AFXBoolKeyword(self.cmd, 'nodeY', AFXBoolKeyword.TRUE_FALSE, True, True)
        self.filenKw = AFXStringKeyword(self.cmd, 'filen', True, 'node.txt')
        self.elementYKw = AFXBoolKeyword(self.cmd, 'elementY', AFXBoolKeyword.TRUE_FALSE, True, True)
        self.filelKw = AFXStringKeyword(self.cmd, 'filel', True, 'element.txt')

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def getFirstDialog(self):

        import outputNodeElementDB
        return outputNodeElementDB.OutputNodeElementDB(self)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def doCustomChecks(self):

        # Try to set the appropriate radio button on. If the user did
        # not specify any buttons to be on, do nothing.
        #
        for kw1,kw2,d in self.radioButtonGroups.values():
            try:
                value = d[ kw1.getValue() ]
                kw2.setValue(value)
            except:
                pass
        return True

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def okToCancel(self):

        # No need to close the dialog when a file operation (such
        # as New or Open) or model change is executed.
        #
        return False

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Register the plug-in
#
thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)

toolset = getAFXApp().getAFXMainWindow().getPluginToolset()
toolset.registerGuiMenuButton(
    buttonText='Output Node&Element', 
    object=OutputNodeElement_plugin(toolset),
    messageId=AFXMode.ID_ACTIVATE,
    icon=None,
    kernelInitString='import outputNodeElement',
    applicableModules=ALL,
    version='N/A',
    author='N/A',
    description='N/A',
    helpUrl='N/A'
)
