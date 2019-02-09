'''
Created on 17 Jul 2018

@author: fran_jo
'''

class ModelicaEngine():
    '''
    classdocs
    _resources of type domain.ModelResources
    _configuration of type domain.CompilerSettings
    '''
    _resources= None 
    _configuration= None

    def __init__(self, resources= None, settings= None):
        '''
        Constructor
        '''
        ''' Loading simulations resources. Parameters related to models to be simulated and libraries'''
        self._resources= resources
        ''' Loading configuration values for the simulator solver '''
        self._configuration= settings
        
    @property
    def resources(self):
        return self._resources
    @resources.setter
    def resources(self, resources):
        self._resources= resources
        
    @property
    def settings(self):
        return self._configuration
    @settings.setter
    def settings(self, configuration):
        self._configuration= configuration

        