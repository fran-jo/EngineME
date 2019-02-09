'''
Created on 4 apr 2014

@author: fragom
'''
import os
from eme.logiclayer.engine.modelicaengine import ModelicaEngine
from eme.logiclayer.command.commandDYM import SimulatorDY
from modelicares.simres import SimRes

'''
so the engine uses setting.object, domainlayer.modelresources, domainlayer.compilerresult
and defines the methods to use the compiler

def setUp(self):
        pass 
    
def timeDomain(self, netmodel= None):
    pass

def linearization(self, netmodel= None):
    pass
'''

class EngineDYM(ModelicaEngine):
    
    def __init__(self, resources= None, settings= None):
        super(EngineDYM,self).__init__(resources, settings)

        
    @property
    def timeout(self):
        return self._configuration["timeout"].rstrip('\n')
    @timeout.setter
    def timeout(self, value):
        self._configuration["timeout"]= value.rstrip('\n') if '\n' in value else value
        
    def updateModelicaResources(self, resources, linearlibPath= ''):
        os.environ["MODELICAPATH"]= resources.modelFolder
        for carpeta in os.walk(resources.modelFolder):
            os.environ["MODELICAPATH"] += os.pathsep + str(carpeta[0]) 
        os.environ["MODELICAPATH"]+= os.pathsep + resources.libraryFolder
        if linearlibPath!= '':
            os.environ["MODELICAPATH"]+= os.pathsep+ linearlibPath
        print os.environ["MODELICAPATH"]
    
    def simulate(self):
#         tic= timeit.default_timer()
        os.chdir(self._resources.modelFolder)
        
        s= SimulatorDY([self._resources.modelName, self._resources.modelFile,
                        self._resources.libraryFolder+ '/'+ self._resources.libraryFile, 
                        self._resources.modelFolder, self._resources.outputPath])
    #     s.showGUI(True)
    #     s.exitSimulator(False)
    #     s.addParameters({'vf1': 0.2, 'pm1': 0.02})
        s.setStopTime(self._configuration.stopTime)
        s.setNumberOfIntervals(self._configuration.numberOfIntervals)
        s.setTolerance(self._configuration.tolerance)
        ''' setTimeOut kill the process if it does not finish in specific time'''
        s.setTimeOut('60')
        s.setSolver(self._configuration.method)
        s.showProgressBar(False)
    #     s.printModelAndTime()
        s.simulate()
#         print os.getcwd()
        os.chdir(self._resources.outputPath)
        outputFile= self._resources.modelName+'.mat'
        try:
            if os.path.exists(outputFile):
                self._configuration["resultFile"]= outputFile
        except OSError as e:
            print "Result file not found '" + outputFile + "' : " + e.strerror
        
#         toc= timeit.default_timer()
#         print 'Simulation time ', toc- tic

    def linearize(self):
        os.chdir(self._resources.modelFolder)
        s= SimulatorDY([self._resources.modelName, self._resources.modelFile,
                        self._resources.libraryFolder+ '/'+ self._resources.libraryFile, 
                        self._resources.modelFolder, self._resources.outputFolder])
        s.setStopTime(self._configuration.stopTime)
        s.setNumberOfIntervals(self._configuration.numberOfIntervals)
        s.setTolerance(self._configuration.tolerance)
        ''' setTimeOut kill the process if it does not finish in specific time'''
        s.setTimeOut('60')
        s.setSolver(self._configuration.method)
        s.showProgressBar(False)
        s.linearize()
#         print os.getcwd()
        os.chdir(self._resources.outputFolder)
        outputFile= 'dslin.mat'
        try:
            if os.path.exists(outputFile):
                self._configuration["resultFile"]= outputFile
        except OSError as e:
            print "Result file not found '" + outputFile + "' : " + e.strerror
        
#         toc= timeit.default_timer()
#         print 'Simulation time ', toc- tic