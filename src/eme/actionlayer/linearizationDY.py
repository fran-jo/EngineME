'''
Created on 4 apr 2014

@author: fragom
'''
import os, sys

from setting import CompilerResources
from setting import ConfigDymola
from modelicares import SimRes
from engine.engineDymola import EngineDYM
from utilsmee import ViewData

    
def load_Sources(filesource):
    __sources= CompilerResources([filesource,'r'])
    __sources.load_Properties()
    print "Model Folder: "+ __sources.modelFolder
    print "Model File: "+ __sources.modelFile
    print "Model Name: "+ __sources.modelName
    print "Library Folder: "+ __sources.libraryFolder
    print "Library File: "+ __sources.libraryFile
    print "Output Folder: "+ __sources.outputFolder
    valuechange= raw_input("Do you want to change any value (y/n) ?: ")
    if valuechange== 'y' or valuechange=='Y':
        valueconfig= raw_input("Model Folder: ")
        __sources.modelFolder= valueconfig if valueconfig!= '' else __sources.modelFolder
        valueconfig= raw_input("Model File: ")
        __sources.modelFile= valueconfig if valueconfig!= '' else __sources.modelFile
        valueconfig= raw_input("Model Name: ")
        __sources.modelName= valueconfig if valueconfig!= '' else __sources.modelName
        valueconfig= raw_input("Library Folder: ")
        __sources.libraryFolder= valueconfig if valueconfig!= '' else __sources.libraryFolder
        valueconfig= raw_input("Library File: ")
        __sources.libraryFile= valueconfig if valueconfig!= '' else __sources.libraryFile
        valueconfig= raw_input("Output Folder: ")
        __sources.outputFolder= valueconfig if valueconfig!= '' else __sources.outputFolder
        __sources.save_Properties()
    return __sources
    
def load_configuration(fileconfig):
    __solverconfig= ConfigDymola([fileconfig,'r'])
    __solverconfig.load_Properties()
    print "Start Time: "+ __solverconfig.startTime
    print "Stop Time: "+ __solverconfig.stopTime
    print "Number of Intervals: "+ __solverconfig.numberOfIntervals
    print "Solver: "+ __solverconfig.method
    print "Tolerance: "+ __solverconfig.tolerance
    print "Output Format: "+ __solverconfig.outputFormat 
    valuechange= raw_input("Do you want to change any value (y/n) ?: ")
    if valuechange== 'y' or valuechange=='Y':
        valueconfig= raw_input("Start Time: ")
        __solverconfig.startTime= valueconfig if valueconfig!= '' else __solverconfig.startTime
        valueconfig= raw_input("Stop Time: ")
        __solverconfig.stopTime= valueconfig if valueconfig!= '' else __solverconfig.stopTime
        valueconfig= raw_input("Number of Intervals: ")
        __solverconfig.numberOfIntervals= valueconfig if valueconfig!= '' else __solverconfig.numberOfIntervals
        valueconfig= raw_input("Solver: ")
        __solverconfig.method= valueconfig if valueconfig!= '' else __solverconfig.method
        valueconfig= raw_input("Tolerance: ")
        __solverconfig.tolerance= valueconfig if valueconfig!= '' else __solverconfig.tolerance
        __solverconfig.save_Properties()
    return __solverconfig

def startEngine(sources):
    __simCity= EngineDYM(sources)
    pathModelicaLinearize= "C:\Program Files (x86)\Dymola 2017 FD01\Modelica\Library\Modelica_LinearSystems2 2.3.4"
    __simCity.updateModelicaPath(sources, pathModelicaLinearize)
    os.chdir(sources.modelFolder)
    return __simCity
    
def runLinearization(simCity, solverconfig):
    ''' Change path to model folder '''
    simCity.updateSolverConfiguration(solverconfig)
    simCity.numberOfIntervals= solverconfig.numberOfIntervals
    simCity.solver= solverconfig.method
    simCity.startTime= solverconfig.startTime
    simCity.stopTime= solverconfig.stopTime
    simCity.tolerance= solverconfig.tolerance
    simCity.resultFile= sources.modelName
    #TODO test the call to the function
    simCity.linearize('linearize')
    print 'simCity.resultFile ', simCity.resultFile
    #TODO get the proper result file with ModelicaRes
    __simulationFile= sources.outputFolder+ os.sep+ simCity.resultFile
    # resultFile = dslin.mat -> we have to extract nx= order, xuyName= list of variables, ABCD
    __simulationData= SimRes(__simulationFile)
    return [__simulationFile, __simulationData]

def runPoles(simCity, solverconfig):
    # resultFile = funcin.mat / funcout.mat -> we have to extract from funcout.mat alphaReal alphaImag = the eigenvalues
    pass

if __name__ == '__main__':
    sources= load_Sources(sys.argv[1])
    solverconfig= load_configuration(sys.argv[2])
    "simulate and return a ModelicaRes.SimRes object"
    simCity= startEngine(sources)
    [resFile, resData]= runLinearization(simCity, solverconfig)
    sources.outputFile= resFile
    sources.save_Properties()
    while (True):
        ViewData.plotOutputs(resData)
        value= raw_input("Plot another signal (y/n) ?: ")
        if (value[0]== 'n'):
            break
