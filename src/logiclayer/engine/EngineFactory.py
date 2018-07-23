'''
Created on 12 Jul 2018

@author: fran_jo
'''
from logiclayer.engine.EngineDYM import EngineDYM
from logiclayer.engine.EngineJMO import EngineJMO
from logiclayer.engine.EngineOMC import EngineOMC

'''TODO engine checks which compilers are installed '''
class EngineFactory(object):
    '''
    classdocs
    '''
    
    def create_EngineDymola(self, sources= None, settings= None, results= None):
        return EngineDYM(sources, settings, results)
     
    def create_EngineOMC(self, sources= None, settings= None, results= None):
        return EngineOMC(sources, settings, results)  
    
    def create_EngineJModelica(self, sources= None, settings= None, results= None):
        return EngineJMO(sources, settings, results)