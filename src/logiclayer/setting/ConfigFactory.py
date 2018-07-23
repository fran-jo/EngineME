'''
Created on 12 Jul 2018

@author: fran_jo
'''
from setting import ConfigDymola
from setting import ConfigOMC
from setting import ConfigJModelica

class ConfigFactory(object):
    '''
    classdocs
    '''
    
    def make_configDymola(self, compiler_name, setting_path):
        return ConfigDymola(compiler_name+ ".properties", setting_path)
     
    def make_configOMC(self, compiler_name, setting_path):
        return ConfigOMC(compiler_name+ ".properties", setting_path)  
    
    def make_configJModelica(self, compiler_name, setting_path):
        return ConfigJModelica(compiler_name+ ".properties", setting_path)