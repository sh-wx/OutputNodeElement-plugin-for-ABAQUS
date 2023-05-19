from abaqusConstants import *
from abaqusGui import *
from kernelAccess import mdb, session
import os

thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)


###########################################################################
# Class definition
###########################################################################

class OutputNodeElementDB(AFXDataDialog):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, form):

        # Construct the base class.
        #

        AFXDataDialog.__init__(self, form, 'Output Node&Element',
            self.OK|self.APPLY|self.CANCEL, DIALOG_ACTIONS_SEPARATOR)
            

        okBtn = self.getActionButton(self.ID_CLICKED_OK)
        okBtn.setText('OK')
            

        applyBtn = self.getActionButton(self.ID_CLICKED_APPLY)
        applyBtn.setText('Apply')
            
        l = FXLabel(p=self, text='Generate node and element information for assembled instances', opts=JUSTIFY_LEFT)
        l.setFont( getAFXFont(FONT_BOLD) )
        l = FXLabel(p=self, text='Different elements with different numbers of nodes are not supported', opts=JUSTIFY_LEFT)
        VFrame_1 = FXVerticalFrame(p=self, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        HFrame_3 = FXHorizontalFrame(p=VFrame_1, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        VAligner_1 = AFXVerticalAligner(p=HFrame_3, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        AFXTextField(p=VAligner_1, ncols=18, labelText='Model name:', tgt=form.modelnameKw, sel=0)
        self.nset1=AFXTextField(p=VAligner_1, ncols=18, labelText='NodeSet:', tgt=form.nodesetKw, sel=0)
        VAligner_2 = AFXVerticalAligner(p=HFrame_3, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        AFXTextField(p=VAligner_2, ncols=18, labelText='Instancename:', tgt=form.instancenameKw, sel=0)
        self.eset1=AFXTextField(p=VAligner_2, ncols=18, labelText='ElementSet:', tgt=form.elementsetKw, sel=0)
        HFrame_7 = FXHorizontalFrame(p=VFrame_1, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        FXCheckButton(p=HFrame_7, text='Use set', tgt=form.usesetKw, sel=0)
        
        self.addTransition(form.usesetKw, AFXTransition.EQ,
            False,self.nset1,
            MKUINT(FXWindow.ID_DISABLE, SEL_COMMAND), None)
        self.addTransition(form.usesetKw, AFXTransition.EQ,
            True,self.nset1,
            MKUINT(FXWindow.ID_ENABLE, SEL_COMMAND), None)    
        self.addTransition(form.usesetKw, AFXTransition.EQ,
            False,self.eset1,
            MKUINT(FXWindow.ID_DISABLE, SEL_COMMAND), None)
        self.addTransition(form.usesetKw, AFXTransition.EQ,
            True,self.eset1,
            MKUINT(FXWindow.ID_ENABLE, SEL_COMMAND), None)    
        
        l = FXLabel(p=HFrame_7, text='Node set and element set need to be built in assembly', opts=JUSTIFY_LEFT)
        l.setFont( getAFXFont(FONT_BOLD) )
        HFrame_5 = FXHorizontalFrame(p=self, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        HFrame_2 = FXHorizontalFrame(p=HFrame_5, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        FXCheckButton(p=HFrame_2, text='Output node', tgt=form.nodeYKw, sel=0)
        self.nodefile=AFXTextField(p=HFrame_2, ncols=7, labelText='Filename:', tgt=form.filenKw, sel=0)
        if isinstance(HFrame_2, FXHorizontalFrame):
            FXVerticalSeparator(p=HFrame_2, x=0, y=0, w=0, h=0, pl=2, pr=2, pt=2, pb=2)
        else:
            FXHorizontalSeparator(p=HFrame_2, x=0, y=0, w=0, h=0, pl=2, pr=2, pt=2, pb=2)
        HFrame_1 = FXHorizontalFrame(p=HFrame_5, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        FXCheckButton(p=HFrame_1, text='Output elem', tgt=form.elementYKw, sel=0)
        self.elefile=AFXTextField(p=HFrame_1, ncols=7, labelText='Filename:', tgt=form.filelKw, sel=0)
        
        self.addTransition(form.nodeYKw, AFXTransition.EQ,
            False,self.nodefile,
            MKUINT(FXWindow.ID_DISABLE, SEL_COMMAND), None)
        self.addTransition(form.nodeYKw, AFXTransition.EQ,
            True,self.nodefile,
            MKUINT(FXWindow.ID_ENABLE, SEL_COMMAND), None)    
        self.addTransition(form.elementYKw, AFXTransition.EQ,
            False,self.elefile,
            MKUINT(FXWindow.ID_DISABLE, SEL_COMMAND), None)
        self.addTransition(form.elementYKw, AFXTransition.EQ,
            True,self.elefile,
            MKUINT(FXWindow.ID_ENABLE, SEL_COMMAND), None)    
        
