
import os
import matplotlib.pyplot as plt
from lattice_check import lattice_check
from lattice_angles_check import lattice_angles_check

def visualization_lattice(model,li_concentration,structure,functional_list,U_value,conf): 
    
    if (model == 'Li2MnO3'):
        dir = os.path.join('/scratch/antwerpen/204/vsc20412',model,model[0:2]+li_concentration+model[3:],structure)
    elif (model == 'Li2IrO3'):
        dir = os.path.join('/scratch/antwerpen/204/vsc20412',model,model[0:2]+li_concentration+model[3:])
    elif (model == 'Li2MnSnO3'):
        dir = os.path.join('/scratch/antwerpen/204/vsc20412',model,'Li'+li_concentration)
    #try:
    if (len(U_value)>1):
        values = U_value 
        
    fig=plt.figure()

    if functional_list == 'pbeU':
        a_angle_a=[0] * (len(values))
        a_angle_b=[0] * (len(values))
        a_angle_c=[0] * (len(values))
        a_lattice_b=[0] * (len(values))
        a_lattice_a=[0] * (len(values))
        a_lattice_c=[0] * (len(values))
        j = 0 
        
        if (model == 'Li2MnO3'):
            for i in values:
                a_lattice_c[j] = lattice_check(model,structure,li_concentration,functional_list,U_value,conf)[1][j][3]

                a_angle_a[j] = lattice_angles_check(model,structure,li_concentration,functional_list,U_value,conf)[1][j][1]

                a_lattice_b[j] = lattice_check(model,structure,li_concentration,functional_list,U_value,conf)[1][j][2]

                a_angle_c[j] = lattice_angles_check(model,structure,li_concentration,functional_list,U_value,conf)[1][j][3]
                j=j+1
            
        elif (model == 'Li2IrO3'):
            for i in values:
                a_lattice_c[j] = lattice_check(model,structure,li_concentration,functional_list,U_value,conf)[1][j][3]

                a_angle_a[j] = lattice_angles_check(model,structure,li_concentration,functional_list,U_value,conf)[1][j][1]

                a_lattice_a[j] = lattice_check(model,structure,li_concentration,functional_list,U_value,conf)[1][j][1]

                a_angle_c[j] = lattice_angles_check(model,structure,li_concentration,functional_list,U_value,conf)[1][j][3]
                j=j+1

        i = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        
        if (model == 'Li2MnO3'):
            plt.subplot(2, 1, 1)
            plt.plot(i, a_lattice_c, 'b-',label='lattice c-parameters',linestyle='--',marker='o', color='b')
            plt.plot(i, a_lattice_b, 'g-',label='lattice a/b-parameters',linestyle='--',marker='o', color='r')
            plt.ylabel('Lattice parameters (A)')
            my_xticks = (0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 3.9, 4, 4.5, 5, 5.5, 6)
            i = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
            plt.xticks(i, my_xticks)
            plt.title('Lattice parameters and angles for different U-values')
            plt.legend(loc='upper center', bbox_to_anchor=(1.4, 1), shadow=True, ncol=1)

            plt.subplot(2, 1, 2)
            plt.plot(i, a_angle_a, 'r-',label='lattice alfa/beta-angles',linestyle='--',marker='o', color='r')
            plt.plot(i, a_angle_c, 'y-',label='lattice gamma-angles',linestyle='--',marker='o', color='b')
            plt.xlabel('U-value (eV)')
            my_xticks = (0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 3.9, 4, 4.5, 5, 5.5, 6)
            i = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
            plt.xticks(i, my_xticks)
            plt.ylabel('Angles (°)')
            plt.legend(loc='upper center', bbox_to_anchor=(1.4, 0.8), shadow=True, ncol=1)
            
        elif (model == 'Li2IrO3'):
            plt.subplot(2, 1, 1)
            plt.plot(i, a_lattice_a, 'b-',label='lattice a-parameters',linestyle='--',marker='o', color='b')
            plt.plot(i, a_lattice_c, 'g-',label='lattice b/c-parameters',linestyle='--',marker='o', color='r')
            plt.ylabel('Lattice parameters (A)')
            my_xticks = (0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 3.9, 4, 4.5, 5, 5.5, 6)
            i = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
            plt.xticks(i, my_xticks)
            plt.title('Lattice parameters and angles for different U-values')
            plt.legend(loc='upper center', bbox_to_anchor=(1.4, 1), shadow=True, ncol=1)

            plt.subplot(2, 1, 2)
            plt.plot(i, a_angle_a, 'r-',label='lattice alpha-angles',linestyle='--',marker='o', color='r')
            plt.plot(i, a_angle_c, 'y-',label='lattice beta/gamma-angles',linestyle='--',marker='o', color='b')
            plt.xlabel('U-value (eV)')
            my_xticks = (0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 3.9, 4, 4.5, 5, 5.5, 6)
            i = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
            plt.xticks(i, my_xticks)
            plt.ylabel('Angles (°)')
            plt.legend(loc='upper center', bbox_to_anchor=(1.4, 0.8), shadow=True, ncol=1)
        
        plt.show()
    
    elif functional_list == ("pbeU", "scan" , "hse"):

        a_angle_a=[0] * (len(values)+2)
        a_angle_b=[0] * (len(values)+2)
        a_angle_c=[0] * (len(values)+2)
        a_lattice_b=[0] * (len(values)+2)
        a_lattice_a=[0] * (len(values)+2)
        a_lattice_c=[0] * (len(values)+2)
        j = 0 

        for i in range(len(values)+2):
            a_lattice_c[j] = lattice_check(model,structure,li_concentration,functional_list,U_value,conf)[1][j][3]

            a_angle_a[j] = lattice_angles_check(model,structure,li_concentration,functional_list,U_value,conf)[1][j][1]

            a_lattice_b[j] = lattice_check(model,structure,li_concentration,functional_list,U_value,conf)[1][j][2]

            a_angle_c[j] = lattice_angles_check(model,structure,li_concentration,functional_list,U_value,conf)[1][j][3]
            j=j+1

        i = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,14,15]
      
        plt.subplot(2, 1, 1)
        plt.plot(i, a_lattice_c, 'b-',label='lattice c-parameters',linestyle='--',marker='o', color='b')
        plt.plot(i, a_lattice_b, 'g-',label='lattice a/b-parameters',linestyle='--',marker='o', color='r')
        plt.ylabel('Lattice parameters (A)')
        my_xticks = (0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 3.9, 4, 4.5, 5, 5.5, 6,'scan','hse')
        i = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,14,15]
        plt.xticks(i, my_xticks)
        plt.title('Lattice parameters and angles for different U-values')
        plt.legend(loc='upper center', bbox_to_anchor=(1.4, 1), shadow=True, ncol=1)

        plt.subplot(2, 1, 2)
        plt.plot(i, a_angle_a, 'r-',label='lattice alfa/beta-angles',linestyle='--',marker='o', color='r')
        plt.plot(i, a_angle_c, 'y-',label='lattice gamma-angles',linestyle='--',marker='o', color='b')
        plt.xlabel('U-value (eV)')
        my_xticks = (0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 3.9, 4, 4.5, 5, 5.5, 6,'scan','hse')
        i = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,14,15]
        plt.xticks(i, my_xticks)
        plt.ylabel('Angles (°)')
        plt.legend(loc='upper center', bbox_to_anchor=(1.4, 0.8), shadow=True, ncol=1)

        plt.show()
        
    elif functional_list == ("pbeU", "scan"):

        a_angle_a=[0] * (len(values)+1)
        a_angle_b=[0] * (len(values)+1)
        a_angle_c=[0] * (len(values)+1)
        a_lattice_b=[0] * (len(values)+1)
        a_lattice_a=[0] * (len(values)+1)
        a_lattice_c=[0] * (len(values)+1)
        j = 0 
        
        if (model == 'Li2MnO3'):
            for i in range(len(values)+1):
                a_lattice_c[j] = lattice_check(model,structure,li_concentration,functional_list,U_value,conf)[1][j][3]

                a_angle_a[j] = lattice_angles_check(model,structure,li_concentration,functional_list,U_value,conf)[1][j][1]

                a_lattice_b[j] = lattice_check(model,structure,li_concentration,functional_list,U_value,conf)[1][j][2]

                a_angle_c[j] = lattice_angles_check(model,structure,li_concentration,functional_list,U_value,conf)[1][j][3]
                j=j+1
            
        elif (model == 'Li2IrO3'):
            for i in range(len(values)+1):
                a_lattice_c[j] = lattice_check(model,structure,li_concentration,functional_list,U_value,conf)[1][j][3]

                a_angle_a[j] = lattice_angles_check(model,structure,li_concentration,functional_list,U_value,conf)[1][j][1]

                a_lattice_a[j] = lattice_check(model,structure,li_concentration,functional_list,U_value,conf)[1][j][1]

                a_angle_c[j] = lattice_angles_check(model,structure,li_concentration,functional_list,U_value,conf)[1][j][3]
                j=j+1
                
        elif (model == 'Li2MnSnO3'):
            for i in range(len(values)+1):
                a_lattice_a[j] = lattice_check(model,structure,li_concentration,functional_list,U_value,conf)[1][j][1]
                a_lattice_b[j] = lattice_check(model,structure,li_concentration,functional_list,U_value,conf)[1][j][2]
                a_lattice_c[j] = lattice_check(model,structure,li_concentration,functional_list,U_value,conf)[1][j][3]
                
                a_angle_a[j] = lattice_angles_check(model,structure,li_concentration,functional_list,U_value,conf)[1][j][1]
                a_angle_b[j] = lattice_angles_check(model,structure,li_concentration,functional_list,U_value,conf)[1][j][2]
                a_angle_c[j] = lattice_angles_check(model,structure,li_concentration,functional_list,U_value,conf)[1][j][3]
                j=j+1

        i = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,14]
        
        if (model == 'Li2MnO3'):
            plt.subplot(2, 1, 1)
            plt.plot(i, a_lattice_c, 'b-',label='lattice a-parameters',linestyle='--',marker='o', color='b')
            plt.plot(i, a_lattice_b, 'g-',label='lattice b/c-parameters',linestyle='--',marker='o', color='r')
            plt.ylabel('Lattice parameters (A)')
            my_xticks = (0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 3.9, 4, 4.5, 5, 5.5, 6,'scan')
            i = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,14]
            plt.xticks(i, my_xticks)
            plt.title('Lattice parameters and angles for different U-values')
            plt.legend(loc='upper center', bbox_to_anchor=(1.4, 1), shadow=True, ncol=1)

            plt.subplot(2, 1, 2)
            plt.plot(i, a_angle_a, 'r-',label='lattice alfa/beta-angles',linestyle='--',marker='o', color='r')
            plt.plot(i, a_angle_c, 'y-',label='lattice gamma-angles',linestyle='--',marker='o', color='b')
            plt.xlabel('U-value (eV)')
            my_xticks = (0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 3.9, 4, 4.5, 5, 5.5, 6,'scan')
            i = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,14]
            plt.xticks(i, my_xticks)
            plt.ylabel('Angles (°)')
            plt.legend(loc='upper center', bbox_to_anchor=(1.4, 0.8), shadow=True, ncol=1)

        elif (model == 'Li2IrO3'):
            plt.subplot(2, 1, 1)
            plt.plot(i, a_lattice_c, 'b-',label='lattice a-parameters',linestyle='--',marker='o', color='b')
            plt.plot(i, a_lattice_a, 'g-',label='lattice b/c-parameters',linestyle='--',marker='o', color='r')
            plt.ylabel('Lattice parameters (A)')
            my_xticks = (0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 3.9, 4, 4.5, 5, 5.5, 6,'scan')
            i = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,14]
            plt.xticks(i, my_xticks)
            plt.title('Lattice parameters and angles for different U-values')
            plt.legend(loc='upper center', bbox_to_anchor=(1.4, 1), shadow=True, ncol=1)

            plt.subplot(2, 1, 2)
            plt.plot(i, a_angle_a, 'r-',label='lattice alfa-angles',linestyle='--',marker='o', color='r')
            plt.plot(i, a_angle_c, 'y-',label='lattice beta/gamma-angles',linestyle='--',marker='o', color='b')
            plt.xlabel('U-value (eV)')
            my_xticks = (0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 3.9, 4, 4.5, 5, 5.5, 6,'scan')
            i = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,14]
            plt.xticks(i, my_xticks)
            plt.ylabel('Angles (°)')
            plt.legend(loc='upper center', bbox_to_anchor=(1.4, 0.8), shadow=True, ncol=1)
            
        elif (model == 'Li2MnSnO3'):
            plt.subplot(2, 1, 1)
            plt.plot(i, a_lattice_a,label='lattice a/b-parameters',linestyle='--',marker='o', color='b')
            #plt.plot(i, a_lattice_b,label='lattice b-parameters',linestyle='--',marker='o', color='r')
            plt.plot(i, a_lattice_c,label='lattice c-parameters',linestyle='--',marker='o', color='r')
            plt.ylabel('Lattice parameters (A)')
            my_xticks = (0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 3.9, 4, 4.5, 5, 5.5, 6,'scan')
            i = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,14]
            plt.xticks(i, my_xticks)
            plt.title('Lattice parameters and angles for different U-values')
            plt.legend(loc='upper center', bbox_to_anchor=(1.4, 1), shadow=True, ncol=1)

            plt.subplot(2, 1, 2)
            plt.plot(i, a_angle_a,label='lattice alfa/beta-angles',linestyle='--',marker='o', color='b')
            #plt.plot(i, a_angle_b,label='lattice beta-angles',linestyle='--',marker='o', color='b')
            plt.plot(i, a_angle_c,label='lattice gamma-angles',linestyle='--',marker='o', color='r')
            plt.xlabel('U-value (eV)')
            my_xticks = (0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 3.9, 4, 4.5, 5, 5.5, 6,'scan')
            i = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,14]
            plt.xticks(i, my_xticks)
            plt.ylabel('Angles (°)')
            plt.legend(loc='upper center', bbox_to_anchor=(1.4, 0.8), shadow=True, ncol=1)
            
        plt.show()

    else:
        print('Not yet implemented. (visualization_lattice.py)')
        
    os.chdir('/scratch/antwerpen/204/vsc20412/temp_files')
    fig.savefig("Test.pdf",bbox_inches='tight',pad_inches=1)
