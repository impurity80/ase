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


a = 2.8920

cell = [[1,0,0],[0,1,0],[0,0,1]]
atoms = BodyCenteredCubic('Fe', directions=cell)
atoms.set_initial_magnetic_moments([5,5])

carbon = Atom('C', position=(0,0.5*a,0.5*a), charge=0.4)

atoms = atoms*(2,2,2) + carbon
init = atoms.copy()

final = atoms.copy()
final[-1].position = [0, 0.5*a, (0.5+1.0)*a]

images = [init]

for i in range(9):
    os.system('mkdir 0{0}'.format(i+1))
    os.chdir('0{0}'.format(i+1))
    atoms = read('POSCAR')
 #   atoms[-1].position = [0,0.5*a,(0.5+(1./10.*i))*a]
 #   view(atoms)
    images.append(atoms.copy())
 #   write('POSCAR', atoms)
    os.chdir('..')

images.append(final)

#view(init)
#view(final)
view(images)

def save( filename, arg ):
    f = open(filename, 'a+t')
    f.write('{0} \n'.format(arg))
    f.close()

os.system('mkdir result')
