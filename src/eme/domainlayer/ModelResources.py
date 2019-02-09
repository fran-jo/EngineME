'''
Created on 13 apr 2014
Access to the names and paths for the simulation resources. This resources are the 
names and path of the models to be simulated, and libraries supporting this models.
This information is stored in the correspondence .properties file 
@author: Francis Gomez
'''

import EngineProperties

class ModelResources(EngineProperties):
    '''
    classdocs
    cimPath= ''
    modelPath=''
    modelFile=''
    modelName=''
    libraryPath=''
    libraryFile=''
    '''
    
    def __init__(self, settingfile="setting.properties", settingpath=""):
        '''
        Constructor
        '''
        self.path= settingpath.replace('\\','/')
        self.name= settingfile
        super(ModelResources,self).__init__(self.path+ self.name)
        self._properties= {'cimPath':'','modelPath':'','modelFile':'',\
                          'libraryPath':'','libraryFile':'','modelName':'',\
                          'outputPath':'','outputFile':''}
    
    def load_Resources(self):
        self.__load_Properties__()
        self._properties['cimPath']= self._properties['cimPath'][:-1] if '\n' in self._properties['cimPath'] else self._properties['cimPath']
        self._properties['modelPath']= self._properties['modelPath'][:-1] if '\n' in self._properties['modelPath'] else self._properties['modelPath']
        self._properties['modelFile']= self._properties['modelFile'][:-1] if '\n' in self._properties['modelFile'] else self._properties['modelFile']
        self._properties['modelName']= self._properties['modelName'][:-1] if '\n' in self._properties['modelName'] else self._properties['modelName']
        self._properties['libraryPath']= self._properties['libraryPath'][:-1] if '\n' in self._properties['libraryPath'] else self._properties['libraryPath']
        self._properties['libraryFile']= self._properties['libraryFile'][:-1] if '\n' in self._properties['libraryFile'] else self._properties['libraryFile']
        self._properties['outputPath']= self._properties['outputPath'][:-1] if '\n' in self._properties['outputPath'] else self._properties['outputPath']
        self._properties['outputFile']= self._properties['outputFile'][:-1] if '\n' in self._properties['outputFile'] else self._properties['outputFile']
        
    @property
    def cimFolder(self):
        return self._properties['cimPath']
    @cimFolder.setter
    def cimFolder(self, value):
        cimfolder= value.rstrip('\n') if '\n' in value else value
        self._properties['cimPath']= cimfolder
        
    @property
    def modelFolder(self):
        return self._properties['modelPath']
    @modelFolder.setter
    def modelFolder(self, value):
        modelfolder= value.rstrip('\n') if '\n' in value else value
        self._properties['modelPath']= modelfolder
        
    @property
    def modelFile(self):
        return self._properties['modelFile']
    @modelFile.setter
    def modelFile(self, value):
        modelfile= value.rstrip('\n') if '\n' in value else value
        self._properties['modelFile']= modelfile
       
    @property
    def modelName(self):
        return self._properties['modelName']
    @modelName.setter
    def modelName(self, value):
        ''' path is the full path of the file '''
        modelname= value.rstrip('\n') if '\n' in value else value
        self._properties['modelName']= modelname
        
    @property
    def libraryFolder(self):
        return self._properties['libraryPath']
    @libraryFolder.setter
    def libraryFolder(self, value):
        libraryfolder= value.rstrip('\n') if '\n' in value else value
        self._properties['libraryPath']= libraryfolder
        
    @property
    def libraryFile(self):
        return self._properties['libraryFile']
    @libraryFile.setter
    def libraryFile(self, value):
        libraryfile = value.rstrip('\n') if '\n' in value else value
        self._properties['libraryFile']= libraryfile
        
    @property
    def outputPath(self):
        return self._properties['outputPath']
    @libraryFolder.setter
    def libraryFolder(self, value):
        libraryfolder= value.rstrip('\n') if '\n' in value else value
        self._properties['outputPath']= libraryfolder
        
    @property
    def outputFile(self):
        return self._properties['outputFile']
    @libraryFile.setter
    def libraryFile(self, value):
        libraryfile = value.rstrip('\n') if '\n' in value else value
        self._properties['outputFile']= libraryfile
        
