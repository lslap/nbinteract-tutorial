# This function will determine which direcotry('s) will be looked at.
import os


import sys 
import os
sys.path.append(os.path.abspath("notebooks/functional_comparison_analyse/out_checker.py"))
from out_checker import *
out_checker(model,li_concentration,structure,functional_list,U_value,conf,checkbox_conf)



def directory(model,li_concentration,structure,conf,functional_list,U_value):
    start = '/scratch/antwerpen/204/vsc20412' # Here you specify your scratch directory
    if (model == 'Li2MnO3'):
        directory = os.path.join(start,model,model[0:2]+li_concentration+model[3:],structure,'conf_'+str(conf),functional_list,U_value)   
    elif (model == 'Li2IrO3'):
        directory = os.path.join(start,model,model[0:2]+li_concentration+model[3:],structure,'conf_'+str(conf),functional_list,U_value)
    elif (model == 'Li2MnSnO3'):
        directory = os.path.join(start,model,'Li'+li_concentration,structure,'conf_'+str(conf),functional_list,U_value)
        
    return directory
