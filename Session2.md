# Macro

## Definition

In reference to computers, a macro (which stands for "macroinstruction") is a programmable pattern which translates 
a certain sequence of input into a preset sequence of output. 
Macros can be used to make tasks less repetitive by representing a complicated sequence of keystrokes, 
mouse movements, commands, or other types of input.

In computer programming, macros are a tool which allow a developer to re-use code.

## Macros in FreeCAD

While it looks easier to use the GUI to create 3D objects in FreeCAD, 
the process becomes time consuming and tedious when the object is complex and of repetitive nature.
Macros are a convenient way to create complex actions in FreeCAD. 
You simply record actions as you do them, then save that under a name, and replay them whenever you want. 
Since macros are in reality a list of python commands, you can also edit them, and create very complex scripts.

### How it works

If you enable console output (Menu Edit -> Preferences -> General -> Macros -> Show scripts commands in python console), 
you will see that in FreeCAD, every action you do, such as pressing a button, outputs a python command. 
Those commands are what can be recorded in a macro. The main tool for making macros is the macros toolbar:

![Macro Toolbar](https://www.freecadweb.org/wiki/images/0/09/Macros_toolbar.jpg)

On it you have 4 buttons: Record, stop recording, edit and play the current macro.

It is very simple to use: Press the record button, you will be asked to give a name to your macro, then perform some actions. 
When you are done, click the stop recording button, and your actions will be saved.
