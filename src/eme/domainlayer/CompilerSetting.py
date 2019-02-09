'''
Created on 12 Jul 2018

@author: fran_jo
'''

import EngineProperties

class CompilerSetting(EngineProperties):
    '''
    classdocs
    '''

    def __init__(self, settingfile="setting.properties", settingpath=""):
        '''
        Constructor
        name= ""
        path= ""
        _properties= {}
        '''
        self.path= settingpath.replace('\\','/')
        self.name= settingfile
        super(CompilerSetting,self).__init__(self.path+ self.name)
    
    @property
    def startTime(self):
        return self._properties["startTime"].rstrip('\n')
    @startTime.setter
    def startTime(self, value):
        self._properties["startTime"]= value.rstrip('\n') if '\n' in value else value
        
    @property
    def stopTime(self):
        return self._properties["stopTime"].rstrip('\n')
    @stopTime.setter
    def stopTime(self, value):
        self._properties["stopTime"]= value.rstrip('\n') if '\n' in value else value
        
    @property
    def solver(self):
        return self._properties["solver"].rstrip('\n')
    @solver.setter
    def solver(self, value):
        self._properties["solver"]= value.rstrip('\n') if '\n' in value else value
        
    @property
    def tolerance(self):
        return self._properties["tolerance"].rstrip('\n')
    @tolerance.setter
    def tolerance(self, value):
        self._properties["tolerance"]= value.rstrip('\n') if '\n' in value else value
        
    @property
    def numberOfIntervals(self):
        return self._properties["numberOfIntervals"].rstrip('\n')
    @numberOfIntervals.setter
    def numberOfIntervals(self, value):
        self._properties["numberOfIntervals"]= value.rstrip('\n') if '\n' in value else value
