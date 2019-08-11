# This functions calculates the baseline energy. This is the energy of the fully discharged material.

import os

def baseline_energy(model,li_concentration,structure,functional_list,U_value,conf):
    if (model == 'Li2MnO3'):
        dir = os.path.join('/scratch/antwerpen/204/vsc20412',model,model[0:2]+str(2)+model[3:],structure)
    elif (model == 'Li2IrO3'):
        dir = os.path.join('/scratch/antwerpen/204/vsc20412',model,model[0:2]+str(2)+model[3:])
    elif (model == 'Li2MnSnO3'):
        dir = os.path.join('/scratch/antwerpen/204/vsc20412',model,'Li'+str(2))
        
    h=len(U_value)
    baseline = [0] * h
    j=0
    for i in U_value:
        directory=os.path.join(dir,'conf_'+str(0),functional_list,str(i))
        os.chdir(directory)
        with open('OUTCAR', 'r') as searchfile:
            for line in searchfile:
                if 'free  en' in line:
                    baseline[j]=float(line[-14-3:-10])
        j = j + 1
    return baseline