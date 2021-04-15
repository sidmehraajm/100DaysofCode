import math, sys
    
import maya.OpenMaya as om
import maya.OpenMayaMPx as omx

kPluginNodeTypeName = "AutoWheel"
kPluginNodeId = om.MTypeId(0x87055)

#Node
class Wheel(omx.MPxNode):
    #vars
    aInput = om.MObject()
    bInput = om.MObject()
    bInputX = om.MObject()
    bInputY = om.MObject()
    bInputZ = om.MObject()
    aOutput = om.MObject()

    def __init__(self):
        omx.MPxNode.__init__(self)


    def compute(self,plug,data):
        if(plug == Wheel.aOutput):
            inputTransform = data.inputValue(Wheel.aInput)
            axis = data.inputValue(Wheel.bInput)
            print(inputTransform,axis)
            result = 10
            a = data.outputValue(Wheel.aOutput)
            a.setFloat(result)
            data.setClean(plug)
        else:
            print('Hey')


def nodeCreator():
    return omx.asMPxPtr(Wheel())

def nodeInitializer():
    nAttr = om.MFnNumericAttribute()
    cAttr = om.MFnCompoundAttribute()
   

    Wheel.bInput = cAttr.create('Direction','Dirc')
    

    uAttrX = om.MFnUnitAttribute()
    Wheel.bInputX = uAttrX.create('DirectionX','DircX',om.MFnUnitAttribute.kDistance)
    uAttrX.setKeyable(True)
    uAttrX.setStorable(True)
    uAttrX.setWritable(True)
    cAttr.addChild(Wheel.bInputX)
    
    uAttrY = om.MFnUnitAttribute()
    Wheel.bInputY = uAttrY.create('DirectionY','DircY',om.MFnUnitAttribute.kDistance)
    uAttrY.setKeyable(True)
    uAttrY.setStorable(True)
    uAttrY.setWritable(True)
    cAttr.addChild(Wheel.bInputY)

    uAttrZ = om.MFnUnitAttribute()
    Wheel.bInputZ = uAttrZ.create('DirectionZ','DircZ',om.MFnUnitAttribute.kDistance)
    uAttrZ.setKeyable(True)
    uAttrZ.setStorable(True)
    uAttrZ.setWritable(True)
    cAttr.addChild(Wheel.bInputZ)


    Wheel.aInput = nAttr.create("Transform", "in", om.MFnNumericData.kFloat, 0.0)
    nAttr.setStorable(True)


    Wheel.aOutput = nAttr.create("sineOutput", "so", om.MFnNumericData.kFloat, 0.0)
    nAttr.setWritable(False)
    nAttr.setStorable(False)

    Wheel.addAttribute(Wheel.aInput)
    
    Wheel.addAttribute(Wheel.bInput)

    Wheel.addAttribute(Wheel.aOutput)  

    Wheel.attributeAffects(Wheel.aInput, Wheel.aOutput)
    Wheel.attributeAffects(Wheel.bInput, Wheel.aOutput)

'''

cAttr = OpenMaya.MFnCompoundAttribute()

uAttrX = OpenMaya.MFnUnitAttribute()

node.old = cAttr.create('oldValue', 'old')
*
node.oldX =uAttrX.create('oldValueX', 'oldX', OpenMaya.MFnUnitAttribute.kDistance)
uAttrX.setKeyable(True)
uAttrX.setStorable(True)
uAttrX.setWritable(True)
cAttr.addChild(node.oldX)

uAttrY = OpenMaya.MFnUnitAttribute()
node.oldY =uAttrX.create('oldValueY', 'oldY', OpenMaya.MFnUnitAttribute.kDistance)
uAttrY.setKeyable(True)
uAttrY.setStorable(True)
uAttrY.setWritable(True)
cAttr.addChild(node.oldY)

uAttrZ = OpenMaya.MFnUnitAttribute()
node.oldZ =uAttrX.create('oldValueZ', 'oldZ', OpenMaya.MFnUnitAttribute.kDistance)
uAttrZ.setKeyable(True)
uAttrZ.setStorable(True)
uAttrZ.setWritable(True)
cAttr.addChild(node.oldZ)

node.addAttribute(node.old)
'''



def initializePlugin(mobject):
    vendor = 'Sid'
    mplugin = omx.MFnPlugin(mobject,vendor)
    try:
        mplugin.registerNode(kPluginNodeTypeName,kPluginNodeId, nodeCreator,nodeInitializer)

    except:
        sys.stderr.write( "Failed to register node: %s" % kPluginNodeTypeName )

        raise

def uninitializePlugin(mobject):
    mplugin = omx.MFnPlugin(mobject)
    try:
        mplugin.deregisterNode(kPluginNodeId)

    except:
        sys.stderr.write( "Failed to De-register node: %s" % kPluginNodeTypeName )

        raise

