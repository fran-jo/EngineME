'''
Created on 12 Jul 2018

@author: fran_jo
'''

class CompilerSetting(object):
    '''
    classdocs
    '''

    def __init__(self, name="setting.properties", path=""):
        '''
        Constructor
        name= ""
        path= ""
        settings= {}
        '''
        self.settingfile= path.replace('\\','/')+ name
        print self.settingfile
        self.settings= {}

    def save_settings(self):
        fle= open(self.settingfile,'w')
        for key in self.settings:
            fle.writelines(key+"="+str(self.settings[key])+"\n")
    
    def load_settings(self):
        fle= open(self.settingfile,"r")
        self.settings= {}
        for line in fle:
            options=line.split('=')
            self.settings[options[0]]= options[1]

    @property
    def settings(self):
        return self.settings

        