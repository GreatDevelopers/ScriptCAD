#Chess Bishop In FreeCAD. (GUI only)

Before getting started, lets devide the bishop in 3 basic part.
1) Head
2) Lower part(neck and base)
3) collar and cut-out slot.

![](Chess%20Bishop%20in%20FreeCAD%20%E2%80%93%20mechaAk_files/capture9.png)

our bishop will be something what like this

**The Head:**

Open FreeCAD and select part workbench as there we can easily and
directly create our basic solids shapes that are required for our chess
bishop.

![](Chess%20Bishop%20in%20FreeCAD%20%E2%80%93%20mechaAk_files/1.jpg)

From “1. Basic shapes” as the image we can create different shapes like
cube, sphere, cylinder, cone etc. From the “2. Basic settings” we can
change the dimensions and position/placement of the solid.

**Step 1: The sphere**

Click on to the sphere icon to create the sphere, now change the radius
of the sphere to 20, we are going to keep this sphere at the center itself.

**Step 2: The cone**

Now click on to the cone to create it. When you will do that you will see
that no cone was created, but it is actually there. Because of its small
dimensions it is hidden inside the sphere we made.

![](Chess%20Bishop%20in%20FreeCAD%20%E2%80%93%20mechaAk_files/2.png)

From the image you may see that “2” shows that a cone is present. “4” is
the dimension of the cone, change it as we did in OpenSCAD. “5” is an
area where the cone or I may say frustum is there but hidden inside the
sphere.

![](Chess%20Bishop%20in%20FreeCAD%20%E2%80%93%20mechaAk_files/4.png)

After changing the dimensions accordingly we may see that the shape is
not at all like a water-drop, so as we did last time we will place the
bishop accordingly by clicking the placement.

![](Chess%20Bishop%20in%20FreeCAD%20%E2%80%93%20mechaAk_files/3.png)

After placing correctly the shape looks something what like the below
image.

![](Chess%20Bishop%20in%20FreeCAD%20%E2%80%93%20mechaAk_files/4-1.png)

**Step 3: Union of solids**

Now it time to unite the two solids we created, the same thing we also
did in OpenSCAD right.

![](Chess%20Bishop%20in%20FreeCAD%20%E2%80%93%20mechaAk_files/4-2.png)

In the image above from “1” we can perform ‘union’, ‘difference’ etc.

Clicking to that it will as you to select the two solids. Select them
and click “Union” and then “Apply” and then “close”.

![](Chess%20Bishop%20in%20FreeCAD%20%E2%80%93%20mechaAk_files/4-32.png)

**Step 4: Dollop/Joker nose**

Now the procedure for other solids are also going to be same.

Going to the Dollop shape or we can say Jokers nose shape.

![](Chess%20Bishop%20in%20FreeCAD%20%E2%80%93%20mechaAk_files/5.png)

Create a sphere, change its dimensions and placement accordingly.

Then unite it with the water drop shape and we are done with the head
part.

**Neck And Base:**

**Step 1:**

To create neck click on cone and change its radius1 and radius2 change
it’s height to create a frustum and place it correctly.

![](Chess%20Bishop%20in%20FreeCAD%20%E2%80%93%20mechaAk_files/6.png)

**Step 2:**

Click on cone again change its radius1 and radius2 also it’s height and
place it to the bottom and that will create the base.

![](Chess%20Bishop%20in%20FreeCAD%20%E2%80%93%20mechaAk_files/7.png)

**Step 3:**

Unite the neck and base.

Now it’s the turn for collar of the bishop.

**Collar:**

Creating the collar is simple just we have to do is to create a cone
change its radius1 and radius2 and place it little upper to its neck,
now create another cone do the same and rotate it by 180°, and unite the
two frustum.

After doing this unite “collar” and “neck-base”.

Also unite the head and lower part to create the “raw bishop”

The collar is also done. Now it’s time for the final step i.e. the cut
out slot

**Cut out slot:**

**Step 1:**

To do that create a cube change its height and length accordingly and
also it’s width. Place it accordingly and also rotate it 45°.

![](Chess%20Bishop%20in%20FreeCAD%20%E2%80%93%20mechaAk_files/8.png)

Which will look something what like the above image.

**Step 2:**

Now we have to cut the cuboid from the raw bishop that we had created.

![](Chess%20Bishop%20in%20FreeCAD%20%E2%80%93%20mechaAk_files/9.png)

For that the procedure is same as Union just we have to click the
difference Boolean operation.

![](Chess%20Bishop%20in%20FreeCAD%20%E2%80%93%20mechaAk_files/10.png)

Which will look something what like this.

Now we are done with the bishop and it just took 30-35 minutes to make
it. Isn’t it simple to make complex shapes using basic and simple
shapes?

Our final Chess bishop will look like this

![](Chess%20Bishop%20in%20FreeCAD%20%E2%80%93%20mechaAk_files/bishop.jpg)

Follow the blog for Chess_Bishop

https://akmecha.wordpress.com/2018/09/15/chess-bishop-in-freecad/


