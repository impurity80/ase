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


a = 2.87

cell = [[1,0,0],[0,1,0],[0,0,1]]
bcc = BodyCenteredCubic('Fe', directions=cell)
bcc.set_initial_magnetic_moments([5,5])

carbon = Atom('C', position=(0,0.5*a,0.75*a), charge=0.4)

bcc = bcc*(2,2,2) + carbon
#atoms = atoms*(2,2,2)
constraint = FixAtoms(indices=[5,7,8,10,12,13,14,15,16])

bcc.set_constraint(constraint)

view(bcc)

def save( filename, arg ):
    f = open(filename, 'a+t')
    f.write('{0} \n'.format(arg))
    f.close()

os.system('mkdir result')

print bcc.get_cell()

