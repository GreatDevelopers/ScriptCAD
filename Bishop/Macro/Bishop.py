
#this script is a raw script and is only changed tillbase of the bishop.
#rest collar of tha bishop is not ready yet.


import FreeCAD as App
import Part


R= 30 #radius of Sphere

H= 150 #height of the neck of the bisshop

W= 20 #Thickness of the neck of the bishop


#for water drop shape -----------------------------------------------------------------------------------------------------------------------------------

#creaition of sphere
App.ActiveDocument.addObject("Part::Sphere","Sphere")
App.ActiveDocument.ActiveObject.Label = "Sphere"
App.ActiveDocument.recompute()
#providing the radius
App.ActiveDocument.getObject("Sphere").Radius = R


#creation of cone
App.ActiveDocument.addObject("Part::Cone","Cone")
App.ActiveDocument.ActiveObject.Label = "Cone"
App.ActiveDocument.recompute()
#providing the dimensions to the cone
App.ActiveDocument.getObject("Cone").Height = 1.5*R 
App.ActiveDocument.getObject("Cone").Radius2 = '0 mm'
App.ActiveDocument.getObject("Cone").Radius1 = R*0.866
#placement of cone
App.activeDocument().Cone.Placement=App.Placement(App.Vector(0,0,R*0.5), App.Rotation(App.Vector(0,0,1),0), App.Vector(0,0,0))

#--------------------------------------------------------------------------------------------------------------------------------------------------------

#fusion(union) of the two solids i.e. sphere and cone
App.activeDocument().addObject("Part::Fuse","Fusion")
App.activeDocument().Fusion.Base = App.activeDocument().Sphere
App.activeDocument().Fusion.Tool = App.activeDocument().Cone

#--------------------------------------------------------------------------------------------------------------------------------------------------------

##for Joker nose shape
#Creation of small sphere (Joker nose shape)
App.ActiveDocument.addObject("Part::Sphere","Sphere")
App.ActiveDocument.ActiveObject.Label = "Sphere"
App.ActiveDocument.recompute()
#dimensioning
App.ActiveDocument.getObject("Sphere001").Radius = 0.25*R
#placement
App.activeDocument().Sphere001.Placement=App.Placement(App.Vector(0,0,2*R), App.Rotation(App.Vector(0,0,1),0), App.Vector(0,0,0))

#fusion(union) of "Joker nose" and "water drop" shapes 
App.activeDocument().addObject("Part::Fuse","Fusion001")
App.activeDocument().Fusion001.Base = App.activeDocument().Fusion
App.activeDocument().Fusion001.Tool = App.activeDocument().Sphere001

#--------------------------------------------------------------------------------------------------------------------------------------------------------

##creation of Neck
App.ActiveDocument.addObject("Part::Cone","Cone")
App.ActiveDocument.ActiveObject.Label = "Cone"
App.ActiveDocument.recompute()
#dimensioning
App.ActiveDocument.getObject("Cone001").Radius1 = W*1.3
App.ActiveDocument.getObject("Cone001").Radius2 = W*0.7
App.ActiveDocument.getObject("Cone001").Height = H
#placement of the neck
App.activeDocument().Cone001.Placement=App.Placement(App.Vector(0,0,-H), App.Rotation(App.Vector(0,0,1),0), App.Vector(0,0,0))

#-------------------------------------------------------------------------------------------------------------------------------------------------------

##creation of base

App.ActiveDocument.addObject("Part::Cone","Cone")
App.ActiveDocument.ActiveObject.Label = "Cone"
App.ActiveDocument.recompute()
#dimensioning
App.ActiveDocument.getObject("Cone002").Radius1 = W*2.3
App.ActiveDocument.getObject("Cone002").Radius2 = W*1.7
App.ActiveDocument.getObject("Cone002").Height = H*0.17
#placement
App.activeDocument().Cone002.Placement=App.Placement(App.Vector(0,0,-H), App.Rotation(App.Vector(0,0,1),0), App.Vector(0,0,0))

#------------------------------------------------------------------------------------------------------------------------------------------------------

#fusion(union) neck and base
App.activeDocument().addObject("Part::Fuse","Fusion002")
App.activeDocument().Fusion002.Base = App.activeDocument().Cone001
App.activeDocument().Fusion002.Tool = App.activeDocument().Cone002

##collar------------------------------------------------------------------------------------------------------------------------------------------------

#cone1
App.ActiveDocument.addObject("Part::Cone","Cone")
App.ActiveDocument.ActiveObject.Label = "Cone"
App.ActiveDocument.recompute()
#dimensioning
App.ActiveDocument.getObject("Cone003").Radius1 = W*1.4
App.ActiveDocument.getObject("Cone003").Radius2 = W*0.9
App.ActiveDocument.getObject("Cone003").Height = H*0.03
App.activeDocument().Cone003.Placement=App.Placement(App.Vector(0,0,-H*0.25), App.Rotation(App.Vector(0,0,1),0), App.Vector(0,0,0))
#cone2
App.ActiveDocument.addObject("Part::Cone","Cone")
App.ActiveDocument.ActiveObject.Label = "Cone"
App.ActiveDocument.recompute()
#dimensioning
App.ActiveDocument.getObject("Cone004").Radius1 = W*1.4
App.ActiveDocument.getObject("Cone004").Radius2 = W*0.9
App.ActiveDocument.getObject("Cone004").Height = H*0.013
#placement
App.activeDocument().Cone004.Placement=App.Placement(App.Vector(0,0,-H*0.25), App.Rotation(App.Vector(1,0,0),180), App.Vector(0,0,0))
#fusion(union) upper cone and downward cone
App.activeDocument().addObject("Part::Fuse","Fusion003")
App.activeDocument().Fusion003.Base = App.activeDocument().Cone003
App.activeDocument().Fusion003.Tool = App.activeDocument().Cone004

#--------------------------------------------------------------------------------------------------------------------------------------------------------


#fusion(union) collar and neck
App.activeDocument().addObject("Part::Fuse","Fusion004")
App.activeDocument().Fusion004.Base = App.activeDocument().Fusion002
App.activeDocument().Fusion004.Tool = App.activeDocument().Fusion003


#fusion(union) upper part and lower part
App.activeDocument().addObject("Part::Fuse","Fusion005")
App.activeDocument().Fusion005.Base = App.activeDocument().Fusion001
App.activeDocument().Fusion005.Tool = App.activeDocument().Fusion004

##creation of cut out slot-------------------------------------------------------------------------------------------------------------------------------
App.ActiveDocument.addObject("Part::Box","Box")
App.ActiveDocument.ActiveObject.Label = "Cube"
App.ActiveDocument.recompute()
#dimensioning
App.ActiveDocument.getObject("Box").Length = R*2
App.ActiveDocument.getObject("Box").Width = R*0.25
App.ActiveDocument.getObject("Box").Height = R*2
#placement
App.activeDocument().Box.Placement=App.Placement(App.Vector(-R,0,0), App.Rotation(App.Vector(1,0,0),45), App.Vector(0,0,0))

##cut (difference) cuboid and the raw bishop-------------------------------------------------------------------------------------------------------------
App.activeDocument().addObject("Part::Cut","Cut")
App.activeDocument().Cut.Base = App.activeDocument().Fusion005
App.activeDocument().Cut.Tool = App.activeDocument().Box

Gui.activeDocument().hide("Fusion005")
Gui.activeDocument().hide("Box")
Gui.ActiveDocument.Cut.ShapeColor=Gui.ActiveDocument.Fusion005.ShapeColor
Gui.ActiveDocument.Cut.DisplayMode=Gui.ActiveDocument.Fusion005.DisplayMode

#Script Ends here.
