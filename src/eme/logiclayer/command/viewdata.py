'''
Created on 4 okt. 2017

@author: fragom
'''

# from modelicares import SimRes
from matplotlib import pyplot as mplt

class ViewData():
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
    
    @staticmethod
    def selectData(arrayQualquiera, message):
        count= 0
        indexMapping={}
        for i, meas in enumerate(arrayQualquiera):
            print '[%d] %s' % (i, meas)
            indexMapping[count]= i
            count+= 1
        try:
            value= raw_input(message)
            lindex = value.split()
        except ValueError:
            print "Wrong choice..." 
        values= []
        for idx in lindex:  
            idx= int(idx)
            values.append(arrayQualquiera[indexMapping[idx]])
        return values  
        
    @staticmethod
    def plotOutputs(selectedSignals= None):
        mplt.figure(1)
        for senyal in selectedSignals: 
            signal_magnitude= selectedSignals[senyal]
            signal_sampletime= selectedSignals["Time"]
            mplt.plot(signal_sampletime, signal_magnitude)
        mplt.legend(selectedSignals)
        mplt.ylabel("Units (p.u.)")
        mplt.xlabel('Time (s)')
        mplt.grid(b=True, which='both')
        mplt.show()
