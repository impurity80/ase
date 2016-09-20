from ase.lattice.surface import surface
from ase import Atoms
from ase.visualize import view, write
from ase.calculators.vasp import *
import matplotlib.pyplot as plt
from ase.constraints import FixAtoms
from matplotlib import mlab
from numpy import *
from ase.utils.eos import EquationOfState
from ase.lattice.cubic import BodyCenteredCubic
from ase import Atom
from ase.io import read

atoms = read('POSCAR')

view(atoms)

def save( filename, arg ):
    f = open(filename, 'a+t')
    f.write('{0} \n'.format(arg))
    f.close()

os.system('mkdir result')