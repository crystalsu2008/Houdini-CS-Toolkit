# hou.shelves.shelfSets() -- get all shelfSets list.
# hou.shelves.shelves() -- get all shelves list.
# hou.shelves.tools() -- get all tools list.

# Create a new shelf named 'csToolkit'.
csToolkitShelf=hou.shelves.newShelf(file_path='$HFS/houdini/toolbar/csToolkit.shelf', name='csToolkit', label='CS Toolkit')

# Get 'shelf_set_1' instance.
shelfSet1=hou.shelves.shelfSets()['shelf_set_1']
# shelfSet1.shelves() -- get all shelves list under the 'shelf_set_1' shelfSet.

# Add 'csToolkit' shelf to 'shelf_set_1'.
newShelvesList=list(shelfSet1.shelves())
newShelvesList.append(csToolkitShelf)
shelfSet1.setShelves(newShelvesList)
