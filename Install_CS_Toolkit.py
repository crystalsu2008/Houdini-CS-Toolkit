import os
import sys

class CSToolkitInstall(object):
    'This class is use for install CS-Toolkit HDA.'

    def getInstallPath(self):
        return( os.path.dirname(sys.argv[0]) )

    def getStartupFile(self, fileType='HScript'):
        if fileType=='HScript':
            return( hou.hscriptExpression('$HFS')+'/houdini/scripts/123.cmd' )
        elif fileType=='Python':
            return( hou.hscriptExpression('$HFS')+'/houdini/scripts/123.py' )
        else:
            return

    def getStartupCommand(self, fileType='HScript', cutKeywords=[]):
        cmds = ''
        noClean = True

        # Get the 123 file.
        startupfile = self.getStartupFile(fileType)
        try:
            f = open(startupfile, 'r')
        except:
            #f = open(startupfile, 'w')
            #f.write('# 123.' + ext[fileType] + ' : Houdini Master startup script\n#\n')
            #f.write('# This file gets sourced whenever Houdini Master starts up\n#\n')
            #f.close()
            return

        # Read 123 content.
        for line in f:
            # To judge whether or not need to clear CS-Toolkit related content.
            if len(cutKeywords)>0:
                # To judge if this line contain any CS-Toolkit related keyword.
                for word in cutKeywords:
                    noClean = noClean and (line.find(word) == -1)
                    if not noClean:
                        break
                # If this line doesn't include any CS-Toolkit related keyword, then add it to content.
                if noClean:
                    cmds = cmds + line
            else:
                cmds = cmds + line
        f.close()
        return cmds

    def uninstall(self):
        ext={'HScript':'cmd', 'Python':'py'}
        cstk_file_path = self.getInstallPath()
        cutKeywords=[cstk_file_path, 'CS-Toolkit', 'cs_simpleStar']

        startupfile = self.getStartupFile(fileType='HScript')
        cmds = self.getStartupCommand(fileType='HScript', cutKeywords=cutKeywords)
        if cmds!=None:
            f = open(startupfile, 'w')
            f.write(cmds)
            f.close()

        startupfile = self.getStartupFile(fileType='Python')
        cmds = self.getStartupCommand(fileType='Python', cutKeywords=cutKeywords)
        if cmds!=None:
            f = open(startupfile, 'w')
            f.write(cmds)
            f.close()






cstk_file_path = os.path.dirname(sys.argv[0])

install_mode = 'Startup'
try:
    install_mode = sys.argv[1]
except:
    pass

def cs_get_123_content(clearnKeywords=[]):
    # Get the 123.cmd file.
    f = open(hou.hscriptExpression('$HFS')+'/houdini/scripts/123.cmd', 'r')
    content = ''
    noClean = True
    # Get the 123.cmd content.
    for line in f:
        if len(clearnKeywords)>0:
            for text in clearnKeywords:
                noClean = noClean and (line.find(text) == -1)
                if not noClean:
                    break
            if noClean:
                content = content + line
        else:
            content = content + line
    f.close()
    return content


if install_mode == 'Startup':
    ## Add install CS-Toolkit action when the Houdini first starts up.
    # Get the 123.cmd content and cleaning CS-Toolkit related lines.
    text = cs_get_123_content(clearnKeywords=[cstk_file_path, 'CS-Toolkit', 'cs_simpleStar'])

    # Add CS-Toolkit related commands.
    text = text + '# Install CS-Toolkit HDAs\n'
    text = text + "otload "+cstk_file_path+"'/cs_simpleStar.otl'"

    # Rewrite the 123.cmd file.
    f = open(hou.hscriptExpression('$HFS')+'/houdini/scripts/123.cmd', 'w')
    f.write(text)
    f.close()

elif install_mode == 'Shelf':
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

else:
    #Uninstall CS-Toolkit
    print('#\nIt\'s in the uninstall procedure!\n#\n')
    cst = CSToolkitInstall()
    cst.uninstall()

# hou.shelves.shelfSets() -- get all shelfSets list.
# hou.shelves.shelves() -- get all shelves list.
# hou.shelves.tools() -- get all tools list.
# shelfSet1.shelves() -- get all shelves list under the 'shelf_set_1' shelfSet.
