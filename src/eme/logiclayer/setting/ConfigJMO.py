'''
Created on 1 apr 2014
Read / Write values for the options of the different simulators we will implement in the MEE
@author: fragom
'''
from eme.domainlayer.CompilerSetting import CompilerSetting

class ConfigJMO(CompilerSetting):
    '''
    JModelica Configuration
    start_time=0
    final_time=0
    algorithm=''
    ncp=0
    solver=''
    initialize=false
    algorithm_options=0,'',...
    '''

    def __init__(self, name="", path=""):
        ''' 
        Constructor
        '''
        CompilerSetting.__init__(self, name, path)
        self.settings= {'start_time':'','final_time':'','algorithm':'',\
                          'ncp':'','solver':'','initialize':'','outputFormat':''}
    
    def load_Settings(self):
        CompilerSetting.load_settings(self)
    
    @property
    def startTime(self):
        return float(self.settings['start_time'])
    
    @property
    def stopTime(self):
        return float(self.settings['final_time'])
    
    @property
    def algorithm(self):
        return self.settings['algorithm']
    
    @property
    def ncp(self):
        return int(self.settings['ncp'])
    
    @property
    def solver(self):
        return self.settings['solver']
    
    @property
    def initialize(self):
        if (self.settings['initialize'].equals('0')):
            return False
        else:
            return True
    
    @property
    def outputFormat(self):
        return self.settings['outputFormat']