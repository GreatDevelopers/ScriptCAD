# Functions supporting building.py:

## def span_process(span_string):
This function process span input (from config file) and then returns a list of lengths.

Remove leading and trailing whitespaces, and put in "span_st" variable.
(e.g- span_st = "2@8+9+1@10+2@12")

```python
	span_st=string.strip(span_string)
```
	
Split string contained in "span_st", where the "+" is encountered and put in span_sp array.
(e.g- span_sp =  ['2@8', '9', '1@10', '2@12'])

```python
	span_sp = string.split(span_st, '+')
```

Let's take a varibale which will hold the record of the index:

```python
	index=0	
```

Then an empty array has been taken.

```python
	list=[]
```

Then we start a loop which runs till the end of list:

```python
	while index < len(span_sp):
```

find function inside the string moudule will find "@" recursively in span_sp array. If not found, append the index value to "list" array:
(e.g- span_sp[1] = '9', then list = [9.0] )

```python 
		if string.find(span_sp[index], '@')==-1:
			list.append(float(span_sp[index]))
```

If found, split the index value, where "@" is encountered, and put in in_sp array.
(e.g- span_sp[0] = '2@8' then) 
```python
		else:	
			in_sp=string.split(span_sp[index], '@')
```
			
Append the value written after "@" to "list" array for no. of times equal to the value written before "@".
(in_sp = ['8', '8'] then, list = [8.0, 8.0])

```python
			count=0	
			while count < int(in_sp[0]):
				list.append(float(in_sp[1]))
				count+=1
		index+=1
```

Following statement will return the list of span inputs.

```python
	return list
```

## def make_box(name, length, width, height, base_vector, base_rotation):

This function creates "box" shape, which is used to create columns and beams.

```python
def make_box(name, length, width, height, base_vector, base_rotation):
	ac_doc = FreeCAD.ActiveDocument
	ac_doc.addObject("Part::Box",name)
	getattr(ac_doc, name).Length = length
	getattr(ac_doc, name).Width = width
	getattr(ac_doc, name).Height = height
	getattr(ac_doc, name).Placement=Base.Placement(Base.Vector(base_vector[0],base_vector[1],base_vector[2]),Base.Rotation(base_rotation[0],base_rotation[1],base_rotation[2],base_rotation[3]))
```


## def make_cylinder(name, radius, height, base_vector, base_rotation):

This function creates circular columns.

```python
def make_cylinder(name, radius, height, base_vector, base_rotation):
	ac_doc = FreeCAD.ActiveDocument
	ac_doc.addObject("Part::Cylinder",name)
	getattr(ac_doc, name).Radius = radius
	getattr(ac_doc, name).Height= height
	getattr(ac_doc, name).Placement=Base.Placement(Base.Vector(base_vector[0],base_vector[1],base_vector[2]),Base.Rotation(base_rotation[0],base_rotation[1],base_rotation[2],base_rotation[3]))
```


## def plane(start, l, w):

This function is used to show ground level and plinth level. It takes three inputs: 4 corners coordinates, length and breadth.

```python
def plane(start, l, w):
	p1 = FreeCAD.Vector(start[0],start[1],start[2])
	p2 = FreeCAD.Vector(start[0]+l,start[1],start[2])
	p3 = FreeCAD.Vector(start[0]+l,start[1]+w,start[2])
	p4 = FreeCAD.Vector(start[0],start[1]+w,start[2])
	pointslist = [p1, p2, p3, p4, p1]
	mywire = Part.makePolygon(pointslist)
	myface = Part.Face(mywire)
	Part.show(myface)	
```

## def z_sum(i):

```python
def z_sum(i):
	zsum = 0
	index = 0
	while index <= i-1 and i!=0:
		zsum = zsum + clear_height[index] + dep_slab - dep_beam/2.0 + ((dep_beam/2.0) * index)
		index = index + 1	 
	return zsum
```

## def x_sum(i):
This function sums the total length of all spans, building's length wise.

```python
def x_sum(i):
	xsum = 0
	index = 0
	while index <= i-1 and i!=0:
		xsum = xsum + dis_span_len[index]
		index = index + 1
	return xsum
```

## def y_sum(i):

This function sums the total length of all spans, building's width wise.

```python
def y_sum(i):
	ysum = 0
	index = 0
	while index <= i-1 and i!=0:
		ysum = ysum + dis_span_len[index]
		index = index + 1
	return ysum
```
