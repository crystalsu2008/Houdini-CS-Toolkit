import os
import sys
cstk_file_path = os.path.dirname(sys.argv[0])

## Install CS-Toolkit shelf.
# Judge whether there is a 'inst_cs_toolkit' tool, if it exist then delete it.
if hou.shelves.tool('inst_cs_toolkit'):
    hou.shelves.tools()['inst_cs_toolkit'].destroy()

# Judge whether there is a 'cs_toolkit_shelf' shelf, if it exist then delete it.
if 'cs_toolkit_shelf' in hou.shelves.shelves():
    hou.shelves.shelves()['cs_toolkit_shelf'].destroy()

## Copy CS-Toolkit shelf file.
# Get source and target file.
sourceFile = cstk_file_path+'/csToolkit.shelf'
targetFile = hou.hscriptExpression('$HOUDINI_USER_PREF_DIR')+'/toolbar/csToolkit.shelf'

# Writhe the target file.
fsou = open(sourceFile, 'r')
ftar = open(targetFile, 'w')

part=()
for line in fsou:
    if line.find('houdini-cs-toolkit_path') != -1:
        # Replace 'houdini-cs-toolkit_path' to specified file path.
        part = line.partition('houdini-cs-toolkit_path')
        line = part[0]+cstk_file_path+part[2]
    ftar.write(line)

ftar.close()
fsou.close()

# Install CS-Toolkit shelf frome shelf file.
hou.shelves.loadFile(targetFile)

# Get CS-Toolkit shelf instance.
cstk_shelf = hou.shelves.shelves()['cs_toolkit_shelf']

# Get 'shelf_set_1' instance.
shelf_set1 = hou.shelves.shelfSets()['shelf_set_1']

# Add 'cs_toolkit_shelf' shelf to 'shelf_set_1'.
new_shelves_list = list(shelf_set1.shelves())
new_shelves_list.append(cstk_shelf)
shelf_set1.setShelves(new_shelves_list)


# hou.shelves.shelfSets() -- get all shelfSets list.
# hou.shelves.shelves() -- get all shelves list.
# hou.shelves.tools() -- get all tools list.
# shelfSet1.shelves() -- get all shelves list under the 'shelf_set_1' shelfSet.
