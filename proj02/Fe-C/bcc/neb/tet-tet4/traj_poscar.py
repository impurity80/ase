from ase.lattice.surface import surface
from ase import Atoms
from ase.visualize import view, write
from ase.io import read
from ase.calculators.vasp import *
import matplotlib.pyplot as plt
from ase.constraints import FixAtoms
from matplotlib import mlab
from numpy import *
from ase.utils.eos import EquationOfState
from ase.lattice.cubic import BodyCenteredCubic
from ase import Atom

images = []

for i in range(0,10):
    os.chdir('{:02d}'.format(i))
    atoms = read('POSCAR')
    images.append(atoms.copy())
    os.chdir('..')

view(images)
