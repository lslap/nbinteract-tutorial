
import os
import pymatgen as pmg
from show_structure import show_structure

def visualization(model,li_concentration,structure,functional_list,U_value,conf):
    if (model == 'Li2MnO3'):
        dir = os.path.join('/scratch/antwerpen/204/vsc20412',model,model[0:2]+li_concentration+model[3:],structure)
    elif (model == 'Li2IrO3'):
        dir = os.path.join('/scratch/antwerpen/204/vsc20412',model,model[0:2]+li_concentration+model[3:])
    elif (model == 'Li2MnSnO3'):
        dir = os.path.join('/scratch/antwerpen/204/vsc20412',model,'Li'+li_concentration)

    if functional_list == 'pbeU':
        directory=os.path.join(dir,"conf_"+str(conf), 'pbeU',str(U_value)) # <--- Specify U-vaule (last number) or dir for SCAN and HSE06   
    elif functional_list == 'scan':
        directory=os.path.join(dir,"conf_"+str(conf), 'scan') # <--- Specify U-vaule (last number) or dir for SCAN and HSE06   
    elif functional_list == 'hse':
        directory=os.path.join(dir,"conf_"+str(conf), 'hse') # <--- Specify U-vaule (last number) or dir for SCAN and HSE06   


    file=os.path.join(directory, "CONTCAR") # Which file do you want to visualize?
    s = pmg.Structure.from_file(file)
    if (model == 'Li2MnSnO3'):
        show_structure(s,)
    else: 
        show_structure(s,[2,2,2])