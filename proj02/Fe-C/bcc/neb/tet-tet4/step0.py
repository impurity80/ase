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

a = 5.7885/2

cell = [[1,0,0],[0,1,0],[0,0,1]]
atoms = BodyCenteredCubic('Fe', directions=cell)
atoms.set_initial_magnetic_moments([5,5])
atoms.set_cell([a, a, a], scale_atoms=True)

carbon = Atom('C', position=(0,0.5*a,0.75*a), charge=0.4)
atoms = atoms*(2,2,2) + carbon

constraint = FixAtoms(indices=[8,10,12,14,16])

atoms.set_constraint(constraint)

atoms[-1].position = [0, 0.5*a, 0.75*a]
init = atoms.copy()
view(init)

atoms[-1].position = [0, 0.75*a, 0.5*a]
final = atoms.copy()
# view(final)

def save( filename, arg ):
    f = open(filename, 'a+t')
    f.write('{0} \n'.format(arg))
    f.close()

os.system('mkdir result')

print atoms.get_cell()

