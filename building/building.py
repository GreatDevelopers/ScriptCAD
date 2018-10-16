from config import *
import string
import FreeCAD, Part, PartGui
from FreeCAD import Base
ac_doc = FreeCAD.ActiveDocument

# Process span input (from config file).
def span_process(span_string):

	# Remove leading and trailing whitespaces, and put in "span_st" variable.
	span_st = string.strip(span_string)
	
	# Split string contained in "span_st", where the "+" is encountered and put in span_sp array.
	span_sp = string.split(span_st, '+')
	index = 0	
	# Empty Array.
	list = []
	while index < len(span_sp):

		# Find "@" recursively in span_sp array. If not found, append the index value to "list" array. 
		if string.find(span_sp[index], '@') == -1:
			list.append(float(span_sp[index]))
		else:	

		# If found, split the index value, where "@" is encountered, and put in in_sp array.
			in_sp=string.split(span_sp[index], '@')
			
			# Append the value written after "@" to "list" array for no. of times equal to the value written before "@".
			count=0	
			while count < int(in_sp[0]):
				list.append(float(in_sp[1]))
				count += 1
		index += 1

	# Following statement will return the list of span inputs.
	return list

# Common function to create "box" shape that will be used for columns and beams.
def make_box(name, length, width, height, base_vector, base_rotation):
	ac_doc = FreeCAD.ActiveDocument
	ac_doc.addObject("Part::Box",name)
	getattr(ac_doc, name).Length = length
	getattr(ac_doc, name).Width = width
	getattr(ac_doc, name).Height = height
	getattr(ac_doc, name).Placement=Base.Placement(Base.Vector(base_vector[0],base_vector[1],base_vector[2]),Base.Rotation(base_rotation[0],base_rotation[1],base_rotation[2],base_rotation[3]))

# Function to create circular columns.
def make_cylinder(name, radius, height, base_vector, base_rotation):
	ac_doc = FreeCAD.ActiveDocument
	ac_doc.addObject("Part::Cylinder",name)
	getattr(ac_doc, name).Radius = radius
	getattr(ac_doc, name).Height= height
	getattr(ac_doc, name).Placement=Base.Placement(Base.Vector(base_vector[0],base_vector[1],base_vector[2]),Base.Rotation(base_rotation[0],base_rotation[1],base_rotation[2],base_rotation[3]))

# "dis_span_len" array contains list of "spans" length wise.	
dis_span_len = span_process(rep_span_len)

# "dis_span_wid" array contains list of "spans" length wise.
dis_span_wid = span_process(rep_span_wid)

# Number of spans building's length wise.
no_spans_len = len(dis_span_len)

# Number of spans building's width wise.
no_span_wid = len(dis_span_wid)

# Function to show ground level and plinth level. It takes three inputs: 4 corners coordinates, length and breadth
def plane(start, l, w):
	p1 = FreeCAD.Vector(start[0],start[1],start[2])
	p2 = FreeCAD.Vector(start[0]+l,start[1],start[2])
	p3 = FreeCAD.Vector(start[0]+l,start[1]+w,start[2])
	p4 = FreeCAD.Vector(start[0],start[1]+w,start[2])
	pointslist = [p1, p2, p3, p4, p1]
	mywire = Part.makePolygon(pointslist)
	myface = Part.Face(mywire)
	Part.show(myface)	

def z_sum(i):
	zsum = 0
	index = 0
	while index <= i-1 and i!=0:
		zsum = zsum + clear_height[index] + dep_slab - dep_beam/2.0 + ((dep_beam/2.0) * index)
		index = index + 1	 
	return zsum

# Sums the total length of all spans, building's length wise.
def x_sum(i):
	xsum = 0
	index = 0
	while index <= i-1 and i!=0:
		xsum = xsum + dis_span_len[index]
		index = index + 1
	return xsum

# Sums the total length of all spans, building's width wise.
def y_sum(i):
	ysum = 0
	index = 0
	while index <= i-1 and i!=0:
		ysum = ysum + dis_span_len[index]
		index = index + 1
	return ysum


i = 0
j = 0
k = 0
nodes = []
z = 0
#Drawing ground plane to depict ground level
plane([-3, -3, plinth_lev - 2 * plinth_lev], x_sum(no_spans_len) + 6, y_sum(no_span_wid) + 6)

#Drawing plinth plane to depict plinth level
plane([0, 0, 0], x_sum(no_spans_len), y_sum(no_span_wid))

while z <= stories:
	x = 0
	while x <= no_spans_len:
		y = 0
		while y <= no_span_wid:
			coords = [x_sum(x), y_sum(y), z_sum(z)]
			nodes.append(coords)		
			
			# If building is 0 storey, height will be equal to ground level
			if z == 0:
				col_name = "Column" + str(i)
				i = i + 1
				
				# If column is rectangular
				if col_type == 1:
				 	make_box(col_name, len_col, wid_col, dep_of_foun + plinth_lev, [coords[0] - len_col / 2.0, coords[1] - wid_col / 2.0, dep_of_foun + plinth_lev - 2 * (dep_of_foun + plinth_lev)], [0.00, 0.00, 0.00, 1.00])
				
				# If column is cylinderical
				else:
				 	make_cylinder(col_name, radius_col, dep_of_foun + plinth_lev, [coords[0], coords[1], dep_of_foun + plinth_lev - 2 * (dep_of_foun + plinth_lev)], [0.00, 0.00, 0.00, 1.00])
			else:
				col_name = "Column" + str(i)
				i = i + 1
				if col_type == 1:			
					make_box(col_name, len_col, wid_col, z_sum(z) - z_sum(z-1), [coords[0] - len_col/2.0, coords[1] - wid_col/2.0, z_sum(z-1)], [0.00, 0.00, 0.00, 1.00])
				else:
					make_cylinder(col_name, radius_col, z_sum(z) - z_sum(z-1), [coords[0], coords[1], z_sum(z-1)], [0.00, 0.00, 0.00, 1.00])

			# Creating beams width wise.
			if y != 0 and z != 0:
				beam_name = "Beam" + str(j)
				j = j + 1			
				make_box(beam_name, wid_beam, y_sum(y) - y_sum(y - 1), dep_beam, [coords[0] - wid_beam / 2.0, y_sum(y - 1), z_sum(z) - dep_beam / 2.0], [0.00, 0.00, 0.00, 1.00])
				
			# Creating beams length wise.
			if x != 0 and z != 0:
				beam_name = "Beam" + str(j)
				j = j + 1			
				make_box(beam_name, x_sum(x) - x_sum(x - 1), wid_beam, dep_beam, [x_sum(x - 1), coords[1] - wid_beam / 2.0, z_sum(z) - dep_beam / 2.0], [0.00, 0.00, 0.00, 1.00])
				
			y = y + 1
		x = x + 1

	# If building has some height, i.e. "z != 0", only then slab can come into existance.
	if z != 0:
		slab_name = "Slab" + str(k)
		k = k + 1			
		make_box(slab_name, x_sum(no_spans_len), y_sum(no_span_wid), dep_slab, [0, 0, z_sum(z) + dep_beam / 2.0 - dep_slab], [0.00, 0.00, 0.00, 1.00])
		
	z = z + 1
FreeCAD.Gui.SendMsgToActiveView("ViewFit")
FreeCAD.Gui.activeDocument().activeView().viewAxometric()
#print nodes[1][1]

