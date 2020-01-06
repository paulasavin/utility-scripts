'''
Created on Oct 10, 2018

@author: uidq8546
'''
import sys, os, stat
from os.path import splitext, abspath
from shutil import move

class Organiser:
   def __init__(self, path):
      self.currentPath = path
      self.standardFolders = {'.exe':'Executables', '.jpg':'Pictures', '.png':'Pictures', '.doc':'Documents', '.pdf':'Documents', '.docx':'Documents', '.txt':'Documents', '.py':'Source files', '.pyc':'Source files', '.cs':'Source files', '.cpp':'Source files'}
      self.filesCounter = {'.exe': 0 , '.jpg': 0, '.png': 0, '.doc': 0, '.pdf': 0, '.docx': 0, '.txt': 0, '.py': 0, '.pyc': 0, '.cs': 0, '.cpp': 0}
   
   def getExtension(self, filePath):
      fileName, ext = splitext(filePath)
      return ext
   
   def getParentDirectoryName(self, path):
      return os.path.basename(os.path.dirname(path))
      
   def createFolder(self, folderPath, folderName):
      newFolder = os.path.join(folderPath, folderName)
      if not os.path.exists(newFolder):
         os.mkdir(newFolder)
         os.chmod(newFolder, stat.S_IREAD | stat.S_IWRITE)
         print('New folder created: %s\n' % newFolder)
         
   def organise(self):
      for subdir, dirs, files in os.walk(self.currentPath):
         for file in files:
            #Get extension and create specific directory
            folderName = 'Others'
            filePath = os.path.join(subdir, file)
            extension = self.getExtension(filePath)
            
            if extension in self.standardFolders:
               folderName = self.standardFolders[extension]
               
            if self.getParentDirectoryName(filePath) != folderName: #if the folder is not already there
               dest = os.path.join(subdir, folderName)   
               self.createFolder(subdir, folderName)
               
               move(filePath, dest)
               self.filesCounter[extension] = self.filesCounter[extension] + 1
               print('File %s moved to destination %s\n\n' % (filePath, dest))