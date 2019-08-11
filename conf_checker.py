# Checks which conf_* dir are present
import os

def conf_checker(model,li_concentration,structure):
    if (model == 'Li2MnO3'):
        dir = os.path.join('/scratch/antwerpen/204/vsc20412',model,model[0:2]+li_concentration+model[3:],structure)
    elif (model == 'Li2IrO3'):
        dir = os.path.join('/scratch/antwerpen/204/vsc20412',model,model[0:2]+li_concentration+model[3:])
    elif (model == 'Li2MnSnO3'):
        dir = os.path.join('/scratch/antwerpen/204/vsc20412',model,'Li'+li_concentration)
        
    check = []
    for x in range(0,15):
        directory=os.path.join(dir,"conf_"+str(x))
        if (os.path.exists(directory) == True):
            check.append(x)
    if check == []:
        check = [0]
    else:
        check = check
        
    return check