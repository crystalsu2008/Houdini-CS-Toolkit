import os
import sys

class CSToolkitInstall(object):
    'This class is use for install CS-Toolkit HDA.'

    def getCutKeywords(self):
        return [self.getInstallPath(), 'CS-Toolkit', 'cs_simpleStar']

    def getInstallPath(self):
        return os.path.dirname(sys.argv[0])

    def getLoadHDACmds(self, fileType=''):
        if fileType=='':
            fileType = self.getStartupType()
        startupCmds = ''
        if fileType=='hscript':
            startupCmds = '# Install CS-Toolkit HDAs\n' + "otload " + self.getInstallPath() + "/cs_simpleStar.otl"
            return startupCmds
        elif fileType=='python':
            startupCmds = '# Install CS-Toolkit HDAs\n' + "hou.hda.installFile('" + self.getInstallPath() + "/cs_simpleStar.otl')"
            return startupCmds
        else:
            return

    def getUnloadHDACmds(self, fileType=''):
        if fileType=='':
            fileType = self.getStartupType()
        startupCmds = ''
        if fileType=='hscript':
            startupCmds = "otunload " + self.getInstallPath() + "/cs_simpleStar.otl"
            return startupCmds
        elif fileType=='python':
            startupCmds = "hou.hda.uninstallFile('" + self.getInstallPath() + "/cs_simpleStar.otl')"
            return startupCmds
        else:
            return

    def getInstallMode(self):
        install_mode = 'Startup'
        try:
            install_mode = sys.argv[1]
        except:
            pass
        return install_mode

    def getStartupType(self):
        startup_type = 'hscript'
        try:
            startup_type = sys.argv[2]
        except:
            pass
        return startup_type

    def getStartupFileName(self, fileType=''):
        if fileType=='':
            fileType = self.getStartupType()
        if fileType=='hscript':
            return( hou.hscriptExpression('$HFS')+'/houdini/scripts/456.cmd' )
        elif fileType=='python':
            return( hou.hscriptExpression('$HFS')+'/houdini/scripts/456.py' )
        else:
            return

    def getStartupFileContent(self, fileType=''):
        if fileType=='':
            fileType = self.getStartupType()
        cmds = ''
        noClean = True
        cutKeywords = self.getCutKeywords()

        # Get the 456 file.
        startupfile = self.getStartupFileName(fileType=fileType)
        try:
            f = open(startupfile, 'r')
        except:
            return

        # Read 456 content.
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

    def deleteShelf(self):
        # Judge whether there is a 'inst_cs_toolkit' tool, if it exist then delete it.
        if hou.shelves.tool('inst_cs_toolkit'):
            hou.shelves.tools()['inst_cs_toolkit'].destroy()

        # Judge whether there is a 'cs_toolkit_shelf' shelf, if it exist then delete it.
        if 'cs_toolkit_shelf' in hou.shelves.shelves():
            hou.shelves.shelves()['cs_toolkit_shelf'].destroy()

    def uninstall(self):
        ext={'hscript':'cmd', 'python':'py'}
        cutKeywords = self.getCutKeywords()
        startupfileDir = os.path.dirname(self.getStartupFileName())

        # Cleaning the 456.cmd file.
        startupfile = self.getStartupFileName(fileType='hscript')
        cmds = self.getStartupFileContent(fileType='hscript')
        if cmds!=None:
            if len(cmds)==0:
                os.remove(startupfile)
            else:
                f = open(startupfile, 'w')
                f.write(cmds)
                f.close()

        # Cleaning the 456.py file.
        startupfile = self.getStartupFileName(fileType='python')
        cmds = self.getStartupFileContent(fileType='python')
        if cmds!=None:
            if len(cmds)==0:
                os.remove(startupfile)
            else:
                f = open(startupfile, 'w')
                f.write(cmds)
                f.close()

        # Delete CS-Toolkit Shelf.
        self.deleteShelf()

        # Unloading CS-Toolkit HDAs.
        # ??? eval( self.getUnloadHDACmds(fileType='python') )
        # ??? hou.hda.uninstallFile(self.getInstallPath() + '/cs_simpleStar.otl')
        # ??? hou.hscript( self.getUnloadHDACmds(fileType='hscript') )

    def installShelf(self):
        # Cleaning CS-Toolkit shelf.
        self.deleteShelf()

        # Copy CS-Toolkit shelf file.
        # Get source and target .shelf file.
        install_path = self.getInstallPath()
        sourceFile = install_path+'/csToolkit.shelf'
        targetFile = hou.hscriptExpression('$HOUDINI_USER_PREF_DIR')+'/toolbar/csToolkit.shelf'

        # Writhe the target file.
        fsou = open(sourceFile, 'r')
        ftar = open(targetFile, 'w')

        part=()
        for line in fsou:
            if line.find('__CS-TOOLKIT_INSTALL_PATH__') != -1:
                # Replace '__CS-TOOLKIT_INSTALL_PATH__' to specified CS-Toolkit HDA install path.
                part = line.partition('__CS-TOOLKIT_INSTALL_PATH__')
                line = part[0] + install_path + part[2]
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

    def installStartup(self):
        # Get the 456 file content and cleaning CS-Toolkit related lines.
        cmds = self.getStartupFileContent()

        # Add CS-Toolkit related commands.
        if not cmds:
            cmds = ''
        cmds = cmds + self.getLoadHDACmds()

        # Rewrite the 456 file.
        f = open(self.getStartupFileName(), 'w')
        f.write(cmds)
        f.close()

csti = CSToolkitInstall()

if csti.getInstallMode() == 'startup':
    # Add install CS-Toolkit action when the Houdini first starts up.
    csti.installStartup()

elif csti.getInstallMode() == 'shelf':
    # Install CS-Toolkit shelf.
    csti.installShelf()

else:
    #Uninstall CS-Toolkit.
    csti.uninstall()

# Loading CS-Toolkit HDAs.
eval( csti.getLoadHDACmds(fileType='python') )
