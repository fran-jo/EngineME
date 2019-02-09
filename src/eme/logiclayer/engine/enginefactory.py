'''
Created on 12 Jul 2018

@author: fran_jo
'''
from eme.logiclayer.engine.enginedym import EngineDYM
from eme.logiclayer.engine.enginejmo import EngineJMO
from eme.logiclayer.engine.engineomc import EngineOMC

'''TODO engine checks which compilers are installed '''
class EngineFactory(object):
    '''
    classdocs
    '''
    def check_InstalledCompiler(self):
        pass
    
    def create_EngineDymola(self, sources= None, settings= None):
        return EngineDYM(sources, settings)
     
    def create_EngineOMC(self, sources= None, settings= None):
        return EngineOMC(sources, settings)  
    
    def create_EngineJModelica(self, sources= None, settings= None):
        return EngineJMO(sources, settings)