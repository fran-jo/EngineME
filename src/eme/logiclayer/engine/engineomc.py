'''
Created on 5 apr 2014

@author: fragom
'''
import sys
from eme.logiclayer.engine.modelicaengine import ModelicaEngine
from eme.logiclayer.command.commandOMC import CommandOMC
from OMPython import OMCSession

# from domainlayer import OutVariableStream as outvar

if sys.platform == 'darwin':
    # On Mac let's assume omc is installed here and there might be a broken omniORB installed in a bad place
    sys.path.append('/opt/openmodelica/bin/omc')
    sys.path.append('/opt/local/bin/omc')

class EngineOMC(ModelicaEngine):
    
    def __init__(self, resources= None, settings= None):
        super(EngineOMC, self).__init__(resources, settings)
        self._omcSession= OMCSession()
        self._simulationResult= None
        
    @property
    def omcSession(self):
        return self._omcSession
        
    @property
    def simulationResult(self):
        return self._simulationResult
        
    def simulate(self):
        objCOMC= CommandOMC()
        '''Load Modelica library'''
        self._omcSession.execute("loadModel(Modelica)")
        command= objCOMC.loadFile(self._resources.libraryFile)
        print '1) Command', command
        self._omcSession.execute(command)
        '''loading the model we want to simulate'''
        command= objCOMC.loadFile(self._resources.modelFile)
        print '2) Command', command
        # here, show the list of parameters we can modify, (variability= parameter)
        print self._resources.modelName 
        success= self._omcSession.execute(command)
        if (success):
            #command= objCOMC.simulate(self.moModel, self.simOptions, 'vf1=0.1,pm1=0.001')
            command= objCOMC.simulate(self._configuration.modelName, self._configuration, False)
            print '3) Command', command
            omc_result= self._omcSession.execute(command)
            print '4) Result', omc_result
        # TODO: Handle when simulation fails, no result file
#         inMemoryResultFile= OMPython.get(result, 'SimulationResults.resultFile')
#         print '5) Result file ', inMemoryResultFile
#         resultfile= objCOMC.saveResult(inMemoryResultFile, self.outPath)
            print '5) Simulation Results', omc_result['SimulationResults']
            self._simulationResult= omc_result['SimulationResults']
            print '6) Result file', self._simulationResult['resultFile']
        else:
            print ("Failed to load resources!")

    def linearize(self):
        pass