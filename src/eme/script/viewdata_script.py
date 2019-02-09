'''
Created on 24 Jul 2018

@author: fran_jo
'''
import sys
from eme.logiclayer.command.viewdata import ViewData
from modelicares import SimRes

if __name__ == '__main__':
    resData= SimRes(sys.argv[1])
    selectedSignals= ViewData.selectData(sorted(resData.names()),
                                         "Select the signal you want to plot? ")
    ViewData.plotOutputs(selectedSignals)
    