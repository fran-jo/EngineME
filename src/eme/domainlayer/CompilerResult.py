'''
Created on 12 Jul 2018

@author: fran_jo
'''

class CompilerResult(object):
    '''
    classdocs
    outputPath= '' a CompilerResult
    outputFile= '' a CompilerResult
    '''


    def __init__(self, res_name="", res_path= ""):
        '''
        Constructor
        '''
        self.outputFile= res_path.replace('\\','/')+ res_name
        self.outputPath= res_path
        self.signals= {}
        
    def save_signals(self):
        pass
   
    def load_signals(self):
        with open(self.resultFile,'r') as fvarList:
            for line in fvarList:
                namevar= line.split('=')
                self.signals[namevar[0]]= namevar[1][:-1]
                 
    @property
    def varibles(self):
        ''' returns the variable name from the component.
        This name corresponds to a readable name for the user, it is not the variable name '''
        return self.signals.keys()
    
    @property
    def signal(self, variable_name):
        ''' returns the variable name from the component. 
        This name is the same name implemented in the model '''
        return self.signals[variable_name]
    
    @property
    def allSignals(self):
        ''' returns the variable name from the component. 
        This name is the same name implemented in the model '''
        return self.signals.items()
