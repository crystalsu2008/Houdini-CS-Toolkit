import os
import sys
cstk_file_path = os.path.dirname(sys.argv[0])

# hou.shelves.shelfSets() -- get all shelfSets list.
# hou.shelves.shelves() -- get all shelves list.
# hou.shelves.tools() -- get all tools list.

# hou.shelves.loadFile('C:/Users/Administrator/Documents/houdini15.5/toolbar/csToolkit.shelf')
sourceFile = cstk_file_path+'/csToolkit.shelf'
targetFile = hou.hscriptExpression('$HOUDINI_USER_PREF_DIR')+'/toolbar/csToolkit.shelf'

fsou = open(sourceFile, 'r')
ftar = open(targetFile, 'w')

for line in fsou:
    print line

ftar.close()
fsou.close()
'''
# Judge whether there is a 'inst_cs_toolkit' tool, if it exist then delete it.
if hou.shelves.tool('inst_cs_toolkit'):
    hou.shelves.tools()['inst_cs_toolkit'].destroy()

# Judge whether there is a 'cs_toolkit_shelf' shelf, if it exist then delete it.
if 'cs_toolkit_shelf' in hou.shelves.shelves():
    hou.shelves.shelves()['cs_toolkit_shelf'].destroy()

# Create a new shelf named 'cs_toolkit_shelf'.
cstk_shelf = hou.shelves.newShelf(file_path='$HOUDINI_USER_PREF_DIR/toolbar/csToolkit.shelf', name='cs_toolkit_shelf', label='CS Toolkit')

# Create a new tool name 'inst_cstk_tool'.
inst_cstk_script = ("hou.hda.installFile('"+cstk_file_path+"/cs_simpleStar.otl')")
inst_cstk_tool = hou.shelves.newTool(file_path='$HOUDINI_USER_PREF_DIR/toolbar/csToolkit.shelf', name='inst_cs_toolkit', label='Install CS Toolkit', script=inst_cstk_script)

# Add 'inst_cstk_script' tool to 'cs_toolkit_shelf' shelf.
tools = list(cstk_shelf.tools()) if len(cstk_shelf.tools()) else []
tools.append(inst_cstk_tool)
cstk_shelf.setTools(tools)

# Get 'shelf_set_1' instance.
shelf_set1=hou.shelves.shelfSets()['shelf_set_1']
# shelfSet1.shelves() -- get all shelves list under the 'shelf_set_1' shelfSet.

# Add 'cs_toolkit_shelf' shelf to 'shelf_set_1'.
new_shelves_list = list(shelf_set1.shelves())
new_shelves_list.append(cstk_shelf)
shelf_set1.setShelves(new_shelves_list)

inst_cstk_tool.setFilePath('$HOUDINI_USER_PREF_DIR/toolbar/csToolkit.shelf')
cstk_shelf.setFilePath('$HOUDINI_USER_PREF_DIR/toolbar/csToolkit.shelf')
#HOUDINI_USER_PREF_DIR
'''
