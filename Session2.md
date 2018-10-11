---
Title : Session-2
---

<link rel = "stylesheet" href = "style/intro.css">
 
<link rel = "stylesheet" href = "https://www.w3schools.com/w3css/4/w3.css">

<div class="w3-bar w3-light-grey">
<a href="https://greatdevelopers.github.io/ScriptCAD" class="w3-bar-item w3-button">Home</a>
<a href="https://goo.gl/forms/YeDk8IqOeDLKQOtB2" class="w3-bar-item w3-button" target="_blank">Register Here</a>
<div class="w3-dropdown-hover">
<button class="w3-button">Menu</button>
<div class="w3-dropdown-content w3-bar-block w3-card-4">
<a href="https://goo.gl/forms/YeDk8IqOeDLKQOtB2" class="w3-bar-item w3-button" target="_blank">Register Here</a>
<a href="https://groups.google.com/forum/#!forum/greatbim" class="w3-bar-item w3-button" target="_blank">Mailing List</a>
<a href="https://greatdevelopers.github.io/ScriptCAD/Payment.html" class="w3-bar-item w3-button">Transaction Details</a>
<a href="https://greatdevelopers.github.io/ScriptCAD/FAQ.html" class="w3-bar-item w3-button">FAQs</a>
<a href="https://greatdevelopers.github.io/ScriptCAD/Terms.html" class="w3-bar-item w3-button">Terms & Conditions</a>
</div>
</div>

<div class="w3-dropdown-hover">
<button class="w3-button">Sessions</button>
<div class="w3-dropdown-content w3-bar-block w3-card-4">
<a href="https://greatdevelopers.github.io/ScriptCAD/Session0/Session0.html" class="w3-bar-item w3-button">Session-0</a>
<a href="https://greatdevelopers.github.io/ScriptCAD/Bishop_Tutorial.html" class="w3-bar-item w3-button">Session-1</a>
<a href="https://greatdevelopers.github.io/ScriptCAD/Session2.html" class="w3-bar-item w3-button">Session-2</a>
</div>
</div>

</div>

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
