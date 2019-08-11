import os
import imolecule

def show_structure(structure, supercell=None):
    if supercell:
        structure = structure.copy()
        structure.make_supercell(supercell)
        
    os.chdir('/scratch/antwerpen/204/vsc20412/temp_files') # Make a directory in your scratch for all the temp files.
    structure.to("cif", "temp.cif")
    imolecule.draw("temp.cif")
