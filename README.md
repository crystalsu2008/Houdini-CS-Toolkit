# Houdini-CS-Toolkit
This is a practice of Houdini Digital Asset study.

__Procedure Name__ : Houdini-CS-Toolkit<br>
__Update__ : August 9, 2016<br>
__Author__ : Chris Su<br>
__Contact__ : crystalsu2008@gmail.com<br>

## History:
* v0.0

## How to use:
#### Install
1. Download all files in a folder, put it anywhere.
* In the Houdini, choose File ▸ Run script...
* At the "Run Command" dialog, pick the "Install_startup.cmd" or "Install_shelf.cmd" file and run it.

>&emsp;*Of course you can just download some otls to use.
But the install way is more easily and security.
There are three scripts for install and uninstall CS-Toolkit HDAs.*

* Install_startup.cmd<br>
<font size=2>*This script add snippets to "456.cmd" or "456.py" file to loading CS-Toolkit HDAs whenever a scene file is loaded(including when Houdini starts up with a scene file).<br>
And you can edit it to choose the startup file type is "HScript" or "Python". To do this, just put an argument after the "python $instpy startup" command. For example:*<br>
&emsp;python $instpy startup python<br>
*This command will add loading HDA snippets to "456.py", default is hscript.*
* Install_shelf.cmd<br>
<font size=2>*This script will create "CS-Toolkit" shelf and "Install CS-Toolkit" tool, you can use this tool to loading CS-Toolkit HDAs.*
* Uninstall.cmd<br>
<font size=2>*This will clean all startup snippets and remove "CS-Toolkit" shelf.*

## Functions:
* CS SimpleStar<br>
This is a simple star generator.
