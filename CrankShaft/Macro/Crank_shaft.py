# -*- coding: utf-8 -*-

# Macro Begin: /home/alok/Desktop/program/python course/Crank_shaft.FCMacro +++++++++++++++++++++++++++++++++++++++++++++++++
import FreeCAD
import PartDesign
import PartDesignGui
import Sketcher
import Part

App.activeDocument().addObject('PartDesign::Body','Body')
#Gui.activeView().setActiveObject('pdbody', App.activeDocument().Body)
#Gui.Selection.clearSelection()
#Gui.Selection.addSelection(App.ActiveDocument.Body)
App.ActiveDocument.recompute()
App.activeDocument().Body.newObject('Sketcher::SketchObject','Sketch')
App.activeDocument().Sketch.Support = (App.activeDocument().YZ_Plane, [''])
App.activeDocument().Sketch.MapMode = 'FlatFace'
App.ActiveDocument.recompute()

geoList = []
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(-0.131254,-35.346539,0),App.Vector(0,0,1),26.519026),3.141593,0.000000))
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(-0.131254,23.525703,0),App.Vector(0,0,1),26.519026),0.000000,3.141593))
geoList.append(Part.LineSegment(App.Vector(26.387772,-35.346539,0),App.Vector(26.387772,23.525703,0)))
geoList.append(Part.LineSegment(App.Vector(-26.650279,-35.346539,0),App.Vector(-26.650279,23.525703,0)))
App.ActiveDocument.Sketch.addGeometry(geoList,False)
conList = []
conList.append(Sketcher.Constraint('Tangent',0,1,3,1))
conList.append(Sketcher.Constraint('Tangent',0,2,2,1))
conList.append(Sketcher.Constraint('Tangent',2,2,1,1))
conList.append(Sketcher.Constraint('Tangent',3,2,1,2))
conList.append(Sketcher.Constraint('Vertical',2))
conList.append(Sketcher.Constraint('Equal',0,1))
App.ActiveDocument.Sketch.addConstraint(conList)

App.ActiveDocument.Sketch.addConstraint(Sketcher.Constraint('PointOnObject',0,3,-2)) 
App.ActiveDocument.Sketch.addConstraint(Sketcher.Constraint('Distance',3,58.872233)) 
App.ActiveDocument.Sketch.setDatum(7,App.Units.Quantity('40.000000 mm'))
App.ActiveDocument.Sketch.addConstraint(Sketcher.Constraint('Radius',1,26.650142)) 
App.ActiveDocument.Sketch.setDatum(8,App.Units.Quantity('27.500000 mm'))
App.ActiveDocument.Sketch.addGeometry(Part.Circle(App.Vector(0.000000,-17.326187,0),App.Vector(0,0,1),22.857844),False)
App.ActiveDocument.Sketch.addConstraint(Sketcher.Constraint('Coincident',4,3,0,3)) 
App.ActiveDocument.Sketch.addConstraint(Sketcher.Constraint('Radius',4,22.857844)) 
App.ActiveDocument.Sketch.setDatum(10,App.Units.Quantity('25.000000 mm'))
App.ActiveDocument.Sketch.setDatum(8,App.Units.Quantity('30.000000 mm'))

App.getDocument('Unnamed').recompute()
App.activeDocument().Body.newObject("PartDesign::Pad","Pad")
App.activeDocument().Pad.Profile = App.activeDocument().Sketch
App.activeDocument().Pad.Length = 10.0
App.ActiveDocument.recompute()


App.ActiveDocument.Pad.Length = 22.000000
App.ActiveDocument.Pad.Length2 = 100.000000
App.ActiveDocument.Pad.Type = 0
App.ActiveDocument.Pad.UpToFace = None
App.ActiveDocument.Pad.Reversed = 0
App.ActiveDocument.Pad.Midplane = 0
App.ActiveDocument.Pad.Offset = 0.000000
App.ActiveDocument.recompute()

App.activeDocument().Body.newObject('Sketcher::SketchObject','Sketch001')
App.activeDocument().Sketch001.Support = (App.activeDocument().XZ_Plane, [''])
App.activeDocument().Sketch001.MapMode = 'FlatFace'
App.ActiveDocument.recompute()

App.getDocument('Unnamed').recompute()
App.activeDocument().Body.newObject("PartDesign::Pad","Pad001")
App.activeDocument().Pad001.Profile = (App.activeDocument().Pad, ["Edge15"])
App.activeDocument().Pad001.Length = 10.0
App.ActiveDocument.recompute()
App.ActiveDocument.recompute()

App.ActiveDocument.Sketch.movePoint(1,0,App.Vector(-15.593932,65.541344,0),0)
App.ActiveDocument.Sketch.movePoint(3,0,App.Vector(0.000000,-3.455574,0),1)
App.ActiveDocument.Sketch.addConstraint(Sketcher.Constraint('Coincident',-1,1,0,3)) 
App.ActiveDocument.Sketch.delGeometry(4)
App.getDocument("Unnamed").recompute()

App.getDocument('Unnamed').recompute()
App.getDocument("Unnamed").removeObject("Sketch001")
App.getDocument("Unnamed").recompute()
App.activeDocument().Body.newObject('Sketcher::SketchObject','Sketch001')
App.activeDocument().Sketch001.Support = (App.activeDocument().YZ_Plane, [''])
App.activeDocument().Sketch001.MapMode = 'FlatFace'
App.ActiveDocument.recompute()

App.ActiveDocument.Sketch001.addGeometry(Part.Circle(App.Vector(0.005833,0.015285,0),App.Vector(0,0,1),53.105447),False)
App.ActiveDocument.Sketch001.addConstraint(Sketcher.Constraint('Coincident',0,3,-1,1)) 
App.ActiveDocument.Sketch001.addConstraint(Sketcher.Constraint('Radius',0,53.105447)) 
App.ActiveDocument.Sketch001.setDatum(1,App.Units.Quantity('25.000000 mm'))

App.getDocument('Unnamed').recompute()
App.activeDocument().Body.newObject("PartDesign::Pad","Pad001")
App.activeDocument().Pad001.Profile = App.activeDocument().Sketch001
App.activeDocument().Pad001.Length = 10.0
App.ActiveDocument.recompute()

App.ActiveDocument.recompute()

App.ActiveDocument.Pad001.Length = 67.000000
App.ActiveDocument.Pad001.Length2 = 100.000000
App.ActiveDocument.Pad001.Type = 0
App.ActiveDocument.Pad001.UpToFace = None
App.ActiveDocument.Pad001.Reversed = 0
App.ActiveDocument.Pad001.Midplane = 0
App.ActiveDocument.Pad001.Offset = 0.000000

App.ActiveDocument.recompute()

App.activeDocument().Body.newObject('PartDesign::Boolean','Boolean')
App.activeDocument().Boolean.addObjects([App.activeDocument().Pad001,App.activeDocument().Pad,])
App.ActiveDocument.recompute()

App.activeDocument().Body.newObject('PartDesign::Boolean','Boolean')
App.activeDocument().Boolean.addObjects([App.activeDocument().Pad001,App.activeDocument().Pad,])
App.ActiveDocument.recompute()

App.ActiveDocument.Boolean.setObjects( [App.ActiveDocument.Pad,App.ActiveDocument.Sketch,App.ActiveDocument.Pad001,App.ActiveDocument.Sketch001,App.ActiveDocument.Pad,App.ActiveDocument.Sketch,])
App.ActiveDocument.Boolean.Type = 0
App.ActiveDocument.recompute()

App.activeDocument().Body.newObject('PartDesign::Boolean','Boolean')
App.activeDocument().Boolean.addObjects([App.activeDocument().Pad001,])
App.ActiveDocument.recompute()

App.ActiveDocument.Boolean.setObjects( [App.ActiveDocument.Pad001,App.ActiveDocument.Sketch001,App.ActiveDocument.Pad,App.ActiveDocument.Sketch,])
App.ActiveDocument.Boolean.Type = 0
App.ActiveDocument.recompute()

App.activeDocument().addObject("Part::Fuse","Fusion")
App.activeDocument().Fusion.Base = App.activeDocument().Pad
App.activeDocument().Fusion.Tool = App.activeDocument().Pad001

App.getDocument("Unnamed").removeObject("Fusion")
App.getDocument("Unnamed").recompute()

App.activeDocument().Body.newObject('Sketcher::SketchObject','Sketch002')
App.activeDocument().Sketch002.Support = (App.activeDocument().YZ_Plane, [''])
App.activeDocument().Sketch002.MapMode = 'FlatFace'
App.ActiveDocument.recompute()

App.ActiveDocument.Sketch002.addGeometry(Part.Circle(App.Vector(0.007813,39.965527,0),App.Vector(0,0,1),23.407400),False)
App.ActiveDocument.Sketch002.addConstraint(Sketcher.Constraint('PointOnObject',0,3,-2)) 
App.ActiveDocument.Sketch002.addConstraint(Sketcher.Constraint('Radius',0,23.407400)) 
App.ActiveDocument.Sketch002.setDatum(1,App.Units.Quantity('22.500000 mm'))

App.getDocument('Unnamed').recompute()
App.activeDocument().Body.newObject("PartDesign::Pad","Pad002")
App.activeDocument().Pad002.Profile = App.activeDocument().Sketch002
App.activeDocument().Pad002.Length = 10.0
App.ActiveDocument.recompute()
#Gui.activeDocument().hide("Sketch002")
App.ActiveDocument.recompute()

App.ActiveDocument.Pad002.Length = 35.000000
App.ActiveDocument.Pad002.Length2 = 100.000000
App.ActiveDocument.Pad002.Type = 0
App.ActiveDocument.Pad002.UpToFace = None
App.ActiveDocument.Pad002.Reversed = 1
App.ActiveDocument.Pad002.Midplane = 0
App.ActiveDocument.Pad002.Offset = 0.000000

App.ActiveDocument.recompute()

App.activeDocument().Body.newObject('Sketcher::SketchObject','Sketch003')
App.activeDocument().Sketch003.Support = (App.activeDocument().YZ_Plane, [''])
App.activeDocument().Sketch003.MapMode = 'FlatFace'
App.ActiveDocument.recompute()

App.getDocument('Unnamed').recompute()

geoList = []
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(0.565040,69.651154,0),App.Vector(0,0,1),30.462538),0.000000,3.141593))
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(0.565040,-48.242851,0),App.Vector(0,0,1),30.462538),3.141593,0.000000))
geoList.append(Part.LineSegment(App.Vector(-29.897498,69.651154,0),App.Vector(-29.897498,-48.242851,0)))
geoList.append(Part.LineSegment(App.Vector(31.027577,69.651154,0),App.Vector(31.027577,-48.242851,0)))
App.ActiveDocument.Sketch003.addGeometry(geoList,False)
conList = []
conList.append(Sketcher.Constraint('Tangent',0,1,3,1))
conList.append(Sketcher.Constraint('Tangent',0,2,2,1))
conList.append(Sketcher.Constraint('Tangent',2,2,1,1))
conList.append(Sketcher.Constraint('Tangent',3,2,1,2))
conList.append(Sketcher.Constraint('Vertical',2))
conList.append(Sketcher.Constraint('Equal',0,1))
App.ActiveDocument.Sketch003.addConstraint(conList)

App.ActiveDocument.Sketch003.addConstraint(Sketcher.Constraint('PointOnObject',0,3,-2)) 
App.ActiveDocument.Sketch003.addConstraint(Sketcher.Constraint('Distance',2,117.893977)) 
App.ActiveDocument.Sketch003.setDatum(7,App.Units.Quantity('80.000000 mm'))
App.ActiveDocument.Sketch003.movePoint(2,0,App.Vector(-0.791243,-12.659758,0),1)
App.ActiveDocument.Sketch003.addConstraint(Sketcher.Constraint('Radius',0,30.689903)) 
App.ActiveDocument.Sketch003.setDatum(8,App.Units.Quantity('30.000000 mm'))
App.ActiveDocument.Sketch003.movePoint(0,0,App.Vector(1.877507,69.865219,0),0)

App.getDocument('Unnamed').recompute()

App.getDocument('Unnamed').recompute()
App.activeDocument().Body.newObject("PartDesign::Pad","Pad003")
App.activeDocument().Pad003.Profile = App.activeDocument().Sketch003
App.activeDocument().Pad003.Length = 10.0
App.ActiveDocument.recompute()

App.ActiveDocument.recompute()

App.ActiveDocument.Pad003.Length = 22.000000
App.ActiveDocument.Pad003.Length2 = 100.000000
App.ActiveDocument.Pad003.Type = 0
App.ActiveDocument.Pad003.UpToFace = None
App.ActiveDocument.Pad003.Reversed = 0
App.ActiveDocument.Pad003.Midplane = 0
App.ActiveDocument.Pad003.Offset = 0.000000

App.ActiveDocument.recompute()

App.ActiveDocument.Sketch003.MapReversed = False
App.ActiveDocument.Sketch003.Support = [(App.getDocument('Unnamed').YZ_Plane,'')]
App.ActiveDocument.Sketch003.MapMode = 'Deactivated'
App.ActiveDocument.recompute()
)
App.getDocument("Unnamed").Sketch003.Placement=App.Placement(App.Vector(57,0,0), App.Rotation(App.Vector(0.57735,0.57735,0.57735),120), App.Vector(0,0,0))
App.getDocument("Unnamed").Sketch003.Placement=App.Placement(App.Vector(-57,0,0), App.Rotation(App.Vector(0.57735,0.57735,0.57735),120), App.Vector(0,0,0))
App.getDocument("Unnamed").Sketch003.Placement=App.Placement(App.Vector(-57,0,0), App.Rotation(App.Vector(0.57735,0.57735,0.57735),120), App.Vector(0,0,0))

App.activeDocument().Body.newObject('Sketcher::SketchObject','Sketch004')
App.activeDocument().Sketch004.Support = (App.activeDocument().YZ_Plane, [''])
App.activeDocument().Sketch004.MapMode = 'FlatFace'
App.ActiveDocument.recompute()

App.ActiveDocument.Sketch004.addGeometry(Part.Circle(App.Vector(0.023649,-40.027302,0),App.Vector(0,0,1),26.231807),False)
App.ActiveDocument.Sketch004.addConstraint(Sketcher.Constraint('PointOnObject',0,3,-2)) 
App.ActiveDocument.Sketch004.addConstraint(Sketcher.Constraint('Radius',0,26.231807)) 
App.ActiveDocument.Sketch004.setDatum(1,App.Units.Quantity('22.500000 mm'))

App.getDocument('Unnamed').recompute()

App.ActiveDocument.recompute()
#Gui.getDocument("Unnamed").getObject("Pad003").Visibility=True
App.ActiveDocument.Sketch004.MapReversed = False
App.ActiveDocument.Sketch004.Support = [(App.getDocument('Unnamed').YZ_Plane,'')]
App.ActiveDocument.Sketch004.MapMode = 'Deactivated'
App.ActiveDocument.recompute()

App.getDocument("Unnamed").Sketch004.Placement=App.Placement(App.Vector(-57,0,0), App.Rotation(App.Vector(0.57735,0.57735,0.57735),120), App.Vector(0,0,0))
App.activeDocument().Body.newObject("PartDesign::Pad","Pad004")
App.activeDocument().Pad004.Profile = App.activeDocument().Sketch004
App.activeDocument().Pad004.Length = 10.0
App.ActiveDocument.recompute()

App.ActiveDocument.recompute()

App.ActiveDocument.Pad004.Length = 35.000000
App.ActiveDocument.Pad004.Length2 = 100.000000
App.ActiveDocument.Pad004.Type = 0
App.ActiveDocument.Pad004.UpToFace = None
App.ActiveDocument.Pad004.Reversed = 1
App.ActiveDocument.Pad004.Midplane = 0
App.ActiveDocument.Pad004.Offset = 0.000000

App.ActiveDocument.recompute()

App.activeDocument().addObject('PartDesign::Body','Body001')

App.ActiveDocument.recompute()
App.getDocument("Unnamed").getObject("Body001").removeObjectsFromDocument()
App.getDocument("Unnamed").removeObject("Body001")
App.getDocument("Unnamed").recompute()

App.activeDocument().Body.newObject('Sketcher::SketchObject','Sketch005')
App.activeDocument().Sketch005.Support = (App.activeDocument().YZ_Plane, [''])
App.activeDocument().Sketch005.MapMode = 'FlatFace'
App.ActiveDocument.recompute()

geoList = []
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(0.036703,-69.919510,0),App.Vector(0,0,1),31.106646),3.141593,0.000000))
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(0.036703,9.737137,0),App.Vector(0,0,1),31.106646),0.000000,3.141593))
geoList.append(Part.LineSegment(App.Vector(31.143349,-69.919510,0),App.Vector(31.143349,9.737137,0)))
geoList.append(Part.LineSegment(App.Vector(-31.069942,-69.919510,0),App.Vector(-31.069942,9.737137,0)))
App.ActiveDocument.Sketch005.addGeometry(geoList,False)
conList = []
conList.append(Sketcher.Constraint('Tangent',0,1,3,1))
conList.append(Sketcher.Constraint('Tangent',0,2,2,1))
conList.append(Sketcher.Constraint('Tangent',2,2,1,1))
conList.append(Sketcher.Constraint('Tangent',3,2,1,2))
conList.append(Sketcher.Constraint('Vertical',2))
conList.append(Sketcher.Constraint('Equal',0,1))
App.ActiveDocument.Sketch005.addConstraint(conList)

App.ActiveDocument.Sketch005.addConstraint(Sketcher.Constraint('PointOnObject',0,3,-2)) 
App.ActiveDocument.Sketch005.addConstraint(Sketcher.Constraint('Distance',3,79.656647)) 
App.ActiveDocument.Sketch005.setDatum(7,App.Units.Quantity('40.000000 mm'))
App.ActiveDocument.Sketch005.movePoint(1,0,App.Vector(6.824884,18.713516,0),0)
App.ActiveDocument.Sketch005.movePoint(2,0,App.Vector(-0.177763,6.932732,0),1)
App.ActiveDocument.Sketch005.addConstraint(Sketcher.Constraint('Coincident',1,3,-1,1)) 
App.ActiveDocument.Sketch005.addConstraint(Sketcher.Constraint('Radius',1,30.363362)) 
App.ActiveDocument.Sketch005.setDatum(9,App.Units.Quantity('30.000000 mm'))

App.getDocument('Unnamed').recompute()

App.ActiveDocument.recompute()

App.ActiveDocument.Sketch005.MapReversed = False
App.ActiveDocument.Sketch005.Support = [(App.getDocument('Unnamed').YZ_Plane,'')]
App.ActiveDocument.Sketch005.MapMode = 'Deactivated'
App.ActiveDocument.recompute()

App.getDocument("Unnamed").Sketch005.Placement=App.Placement(App.Vector(-90,0,0), App.Rotation(App.Vector(0.57735,0.57735,0.57735),120), App.Vector(0,0,0))
App.getDocument("Unnamed").Sketch005.Placement=App.Placement(App.Vector(-90,0,0), App.Rotation(App.Vector(0.57735,0.57735,0.57735),120), App.Vector(0,0,0))
App.activeDocument().Body.newObject("PartDesign::Pad","Pad005")
App.activeDocument().Pad005.Profile = App.activeDocument().Sketch005
App.activeDocument().Pad005.Length = 10.0
App.ActiveDocument.recompute()

App.ActiveDocument.recompute()

App.ActiveDocument.Pad005.Length = 22.000000
App.ActiveDocument.Pad005.Length2 = 100.000000
App.ActiveDocument.Pad005.Type = 0
App.ActiveDocument.Pad005.UpToFace = None
App.ActiveDocument.Pad005.Reversed = 1
App.ActiveDocument.Pad005.Midplane = 0
App.ActiveDocument.Pad005.Offset = 0.000000

App.ActiveDocument.recompute()

App.activeDocument().Body.newObject('Sketcher::SketchObject','Sketch006')
App.activeDocument().Sketch006.Support = (App.activeDocument().YZ_Plane, [''])
App.activeDocument().Sketch006.MapMode = 'FlatFace'
App.ActiveDocument.recompute()

App.ActiveDocument.Sketch006.addGeometry(Part.Circle(App.Vector(0.590197,0.507617,0),App.Vector(0,0,1),23.637180),False)
App.ActiveDocument.Sketch006.addConstraint(Sketcher.Constraint('Coincident',0,3,-1,1)) 
App.ActiveDocument.Sketch006.addConstraint(Sketcher.Constraint('Radius',0,23.637180)) 
App.ActiveDocument.Sketch006.setDatum(1,App.Units.Quantity('25.000000 mm'))

App.getDocument('Unnamed').recompute()
App.ActiveDocument.Sketch006.MapReversed = False
App.ActiveDocument.Sketch006.Support = [(App.getDocument('Unnamed').YZ_Plane,'')]
App.ActiveDocument.Sketch006.MapMode = 'Deactivated'
App.ActiveDocument.recompute()

App.getDocument("Unnamed").Sketch006.Placement=App.Placement(App.Vector(-112,0,0), App.Rotation(App.Vector(0.57735,0.57735,0.57735),120), App.Vector(0,0,0))
App.getDocument("Unnamed").Sketch006.Placement=App.Placement(App.Vector(-112,0,0), App.Rotation(App.Vector(0.57735,0.57735,0.57735),120), App.Vector(0,0,0))
App.activeDocument().Body.newObject("PartDesign::Pad","Pad006")
App.activeDocument().Pad006.Profile = App.activeDocument().Sketch006
App.activeDocument().Pad006.Length = 10.0
App.ActiveDocument.recompute()

App.ActiveDocument.Pad006.Length = 22.500000
App.ActiveDocument.Pad006.Length2 = 100.000000
App.ActiveDocument.Pad006.Type = 0
App.ActiveDocument.Pad006.UpToFace = None
App.ActiveDocument.Pad006.Reversed = 1
App.ActiveDocument.Pad006.Midplane = 0
App.ActiveDocument.Pad006.Offset = 0.000000

App.ActiveDocument.recompute()

import PartDesignGui
App.activeDocument().addObject("Part::Fuse","Fusion")
App.activeDocument().Fusion.Base = App.activeDocument().Pad
App.activeDocument().Fusion.Tool = App.activeDocument().Pad001

App.activeDocument().addObject("Part::Fuse","Fusion001")
App.activeDocument().Fusion001.Base = App.activeDocument().Pad002
App.activeDocument().Fusion001.Tool = App.activeDocument().Pad003

App.activeDocument().addObject("Part::Fuse","Fusion002")
App.activeDocument().Fusion002.Base = App.activeDocument().Pad004
App.activeDocument().Fusion002.Tool = App.activeDocument().Pad005

App.activeDocument().addObject("Part::Fuse","Fusion003")
App.activeDocument().Fusion003.Base = App.activeDocument().Fusion
App.activeDocument().Fusion003.Tool = App.activeDocument().Fusion001

App.activeDocument().addObject("Part::Fuse","Fusion004")
App.activeDocument().Fusion004.Base = App.activeDocument().Fusion002
App.activeDocument().Fusion004.Tool = App.activeDocument().Fusion003

App.activeDocument().addObject("Part::Fuse","Fusion005")
App.activeDocument().Fusion005.Base = App.activeDocument().Pad006
App.activeDocument().Fusion005.Tool = App.activeDocument().Fusion004


# Macro End: /home/alok/Desktop/program/python course/Crank_shaft.FCMacro +++++++++++++++++++++++++++++++++++++++++++++++++
