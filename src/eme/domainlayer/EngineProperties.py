'''
Created on 24 Jul 2018

@author: fran_jo
'''

class EngineProperties():
    '''
    classdocs
    '''
    
    def __init__(self, propertyfilename=".properties"):
        '''
        Constructor
        propertyfilename=".properties"
        accessmode='r'
        '''
        self.__fichero= propertyfilename
        self._properties= {}
        
    def __save_Properties__(self):
        fle= open(self.__fichero,'w')
        for key in self._properties:
            print key+"="+str(self._properties[key])+'\n'
            fle.write(key+"="+str(self._properties[key])+'\n')
    
    def __load_Properties__(self):
        fle= open(self.__fichero, 'r')
        for line in fle:
            options=line.split('=')
            self._properties[options[0]]= options[1]
#         print self._properties
    
    @property
    def properties_names(self):
        '''
        This function works after storing or loading _properties into the dictionary object
        '''
        return self._properties.keys()
    
    @property
    def properties_values(self):
        '''
        This function works after storing or loading _properties into the dictionary object
        '''
        return self._properties.values()
