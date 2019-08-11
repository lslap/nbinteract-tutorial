
import os
from magnetic_check import magnetic_check
import matplotlib.pyplot as plt

def magnetic_plot(model,li_concentration,structure,functional_list,U_value,conf):
    
    if functional_list == 'pbeU':
        if (len(U_value)>1):
            values = U_value  

            [header,results] = magnetic_check(model,structure,li_concentration,functional_list,U_value,conf) 

            testing_Mn = [0]*len(values)
            testing_O = [0]*len(values)
            q=0
            for i in values:
                testing_Mn[q] = results[q][1]
                testing_O[q] = results[q][2]
                q = q + 1

            i = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
            fig=plt.figure()
            plt.subplot(2, 1, 1)
            plt.plot(i, testing_Mn, 'b-',label='Magnetic moment '+str(model[3:5]),linestyle='--',marker='o', color='b')
            plt.plot(i, testing_O, 'g-',label='Magnetic moment O',linestyle='--',marker='o', color='r')
            plt.ylabel('Magnetic moment (\mu_B)')
            plt.xlabel('U-values (eV)')
            my_xticks = (0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 3.9, 4, 4.5, 5, 5.5, 6)
            i = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
            plt.xticks(i, my_xticks)
            plt.title('Magnetic moments for different U-values')
            plt.legend(loc='upper center', bbox_to_anchor=(1.4, 1), shadow=True, ncol=1)
            plt.show()

            os.chdir('/scratch/antwerpen/204/vsc20412/temp_files')
            fig.savefig("Test5.pdf",bbox_inches='tight',pad_inches=1)
        else:
            print('oeps')
            
    elif functional_list == ("pbeU", "scan" , "hse"):
        if (len(U_value)>1):
            values = U_value  

            [header,results] = magnetic_check(model,structure,li_concentration,functional_list,U_value,conf) 

            testing_Mn = [0]*(len(values)+2)
            testing_O = [0]*(len(values)+2)
            q=0
            for i in range(0,len(values)+2):
                testing_Mn[q] = results[q][1]
                testing_O[q] = results[q][2]
                q = q + 1

            i = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,14,15]
            fig=plt.figure()
            plt.subplot(2, 1, 1)
            plt.plot(i, testing_Mn, 'b-',label='Magnetic moment '+str(model[3:5]),linestyle='--',marker='o', color='b')
            plt.plot(i, testing_O, 'g-',label='Magnetic moment O',linestyle='--',marker='o', color='r')
            plt.ylabel('Magnetic moment (\mu_B)')
            plt.xlabel('U-values (eV)')
            my_xticks = (0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 3.9, 4, 4.5, 5, 5.5, 6,'scan',"hse")
            i = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,14,15]
            plt.xticks(i, my_xticks)
            plt.title('Magnetic moments for different U-values')
            plt.legend(loc='upper center', bbox_to_anchor=(1.4, 1), shadow=True, ncol=1)
            plt.show()

            os.chdir('/scratch/antwerpen/204/vsc20412/temp_files')
            fig.savefig("Test5.pdf",bbox_inches='tight',pad_inches=1)
        else:
            print('oeps')
    
    elif functional_list == ("pbeU", "scan"):
        if (len(U_value)>1):
            values = U_value  

            [header,results] = magnetic_check(model,structure,li_concentration,functional_list,U_value,conf) 

            testing_Mn = [0]*(len(values)+1)
            testing_O = [0]*(len(values)+1)
            q=0
            for i in range(0,len(values)+1):
                testing_Mn[q] = results[q][1]
                testing_O[q] = results[q][2]
                q = q + 1

            i = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,14]
            fig=plt.figure()
            plt.subplot(2, 1, 1)
            plt.plot(i, testing_Mn, 'b-',label='Magnetic moment '+str(model[3:5]),linestyle='--',marker='o', color='b')
            plt.plot(i, testing_O, 'g-',label='Magnetic moment O',linestyle='--',marker='o', color='r')
            plt.ylabel('Magnetic moment (\mu_B)')
            plt.xlabel('U-values (eV)')
            my_xticks = (0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 3.9, 4, 4.5, 5, 5.5, 6,'scan')
            i = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,14]
            plt.xticks(i, my_xticks)
            plt.title('Magnetic moments for different U-values')
            plt.legend(loc='upper center', bbox_to_anchor=(1.4, 1), shadow=True, ncol=1)
            plt.show()

            os.chdir('/scratch/antwerpen/204/vsc20412/temp_files')
            fig.savefig("Test5.pdf",bbox_inches='tight',pad_inches=1)
        else:
            print('oeps')
    else:
        print('Not yet implemented. (magnetic_plot.py)')
    
    os.chdir('/scratch/antwerpen/204/vsc20412/temp_files')
    fig.savefig("Test.pdf",bbox_inches='tight',pad_inches=1)