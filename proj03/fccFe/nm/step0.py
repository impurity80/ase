from ase.lattice.surface import surface
from ase import Atoms
from ase.visualize import view, write
from ase.calculators.vasp import *
import matplotlib.pyplot as plt
from ase.constraints import FixAtoms
from matplotlib import mlab
from numpy import *
from ase.utils.eos import EquationOfState
from ase.lattice.cubic import *
from ase.lattice.spacegroup import *
from ase.dft.kpoints import *
from ase import Atom

def save( filename, arg ):
    f = open(filename, 'a+t')
    f.write('{0} \n'.format(arg))
    f.close()

a = 3.6

bulk = FaceCenteredCubic('Fe', directions=[[1,0,0],[0,1,0],[0,0,1]], latticeconstant=a)
bulk.set_initial_magnetic_moments([5,5,5,5])

view(bulk)
atoms = bulk

os.system('mkdir result')
