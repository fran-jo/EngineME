'''
Created on 4 apr 2014

@author: fragom
'''
from domainlayer.CompilerSetting import CompilerSetting
    
class ConfigDYM(CompilerSetting):
    '''
    Supported options
    startTime=0 
    stopTime=0
    timeOut= 60
    numberOfIntervals=0
    fixedStepSize=false
    tolerance=0 
    method=''  
    outputFormat=''
    '''    
    #_solver_config= {}
    
    def __init__(self, name="", path=""):
        ''' 
        Constructor
        '''
        CompilerSetting.__init__(self, name, path)
        self.settings= {'startTime':'','stopTime':'','numberOfIntervals':'',\
                          'fixedStepSize':'','tolerance':'','method':'','outputFormat':''}
        
    def load_Settings(self):
        CompilerSetting.load_settings(self)

    @property
    def startTime(self):
        return self.settings['startTime'].rstrip('\n')
    @startTime.setter
    def startTime(self, valor):
        self.settings['startTime']= valor.rstrip('\n') if '\n' in valor else valor
        
    @property
    def stopTime(self):
        return self.settings['stopTime'].rstrip('\n')
    @stopTime.setter
    def stopTime(self, valor):
        self.settings['stopTime']= valor.rstrip('\n') if '\n' in valor else valor
    
    @property
    def timeOut(self):
        return self.settings['timeOut'].rstrip('\n')
    @timeOut.setter
    def timeOut(self, valor):
        self.settings['timeOut']= valor.rstrip('\n') if '\n' in valor else valor
        
    @property
    def numberOfIntervals(self):
        return self.settings['numberOfIntervals'].rstrip('\n')
    @numberOfIntervals.setter
    def numberOfIntervals(self, valor):
        self.settings['numberOfIntervals']= valor.rstrip('\n') if '\n' in valor else valor
    
    @property
    def tolerance(self):
        return self.settings['tolerance'].rstrip('\n')
    @tolerance.setter
    def tolerance(self, valor):
        self.settings['tolerance']= valor.rstrip('\n') if '\n' in valor else valor
    
    @property
    def method(self):
        return self.settings['method'].rstrip('\n') #without char \n
    @method.setter
    def method(self, valor):
        self.settings['method']= valor.rstrip('\n') if '\n' in valor else valor
    
    @property
    def outputFormat(self):
        return self.settings['outputFormat'].rstrip('\n') #without char \n
    @outputFormat.setter
    def outputFormat(self, valor):
        self.settings['outputFormat']= valor
        
    @property
    def modelName(self):
        return self.settings['modelName']
    @modelName.setter
    def modelName(self, name):
        self.settings['modelName']= name
        
    def isFixedStepSize(self):
        return int(self.settings['fixedStepSize'])
    
    def setSimulationOptions(self):
        ''' creates a command string with simulation configuration values '''
        simulate_options = ""
        for k, v in self.settings.iteritems():
            simulate_options = simulate_options + "," + str(k) + "=" + str(v)
        return simulate_options
