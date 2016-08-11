# Houdini-CS-Toolkit
This is a practice of Houdini Digital Asset study.

__Procedure Name__ : Houdini-CS-Toolkit<br>
__Update__ : August 9, 2016<br>
__Author__ : Chris Su<br>
__Contact__ : crystalsu2008@gmail.com<br>

## History:
* v0.0

## How to use:
Download all files in a folder, put it anywhere.<br>
In the Houdini, choose File ▸ Run script...<br>
At the "Run Command" dialog, pick the "Install_startup.cmd" or "Install_shelf.cmd" file and run it.

Of course you can just download some otls to use.
But the install way is more easily and security.
There are two install scripts and one uninstall script.
Running the "Install_startup.cmd" will add snippets to "456.cmd" or "456.py" file to install CS-Toolkit whenever a scene file is loaded(including when Houdini starts up with a scene file).
Running the "Install_shelf.cmd" will create "CS-Toolkit" shelf and "Install CS-Toolkit" tool, you can use this tool to loading CS-Toolkit HDAs.
Running the "Uninstall.cmd" will clean all startup snippets and remove "CS-Toolkit" shelf.

If you run "Install_startup.cmd" to install CS-Toolkit HDAs at Houdini starts up, you can edit the "Install_startup.cmd" file to decide the startup file type.
You can put a argument after the "python $instpy startup" command.
This argument accept two keyword, "hscript" and "python", default type is "hscript".
For example: "python $instpy startup python" will 


## Functions:
* CS SimpleStar<br>
This is a simple star generator.
