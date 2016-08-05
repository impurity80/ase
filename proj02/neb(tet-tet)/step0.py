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

a = 2.8920

cell = [[1,0,0],[0,1,0],[0,0,1]]
atoms = BodyCenteredCubic('Fe', directions=cell)
atoms.set_initial_magnetic_moments([5,5])

carbon = Atom('C', position=(0,0.75*a,0.5*a), charge=0.4)

atoms = atoms*(2,2,2) + carbon
init = atoms.copy()

final = atoms.copy()
final[-1].position = [0, 0.5*a, 0.75*a]

for i in range(0,13):
    os.system('mkdir {:02d}'.format(i))
    os.chdir('{:02d}'.format(i))
    atoms[-1].position = [0,(0.75-0.25/12.*i)*a,(0.5+0.25/12.*i)*a]
 #   view(atoms)
    write('POSCAR', atoms)
    os.chdir('..')

view(init)
view(final)

def save( filename, arg ):
    f = open(filename, 'a+t')
    f.write('{0} \n'.format(arg))
    f.close()

os.system('mkdir result')
