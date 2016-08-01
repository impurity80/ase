from ase.lattice.surface import surface
from ase import Atoms
from ase.visualize import view, write
from ase.calculators.vasp import *
import matplotlib.pyplot as plt
from ase.constraints import FixAtoms
from matplotlib import mlab
from numpy import *
from ase.utils.eos import EquationOfState
from ase.lattice.spacegroup import crystal

atoms = crystal(spacegroup=227,
                symbols='C',
                basis=[0,0,0],
                cellpar=[3.57,3.57,3.57,90.0,90.0,90.0])

view(atoms)

def save( filename, arg ):
    f = open(filename, 'a+t')
    f.write('{0} \n'.format(arg))
    f.close()
