
from ase import Atoms
from ase.visualize import view, write
from ase.io import read
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

atoms = read('sample/POSCAR')

a = atoms.get_cell()[1][1]

magmon = [1]
magmon = magmon*116

atoms.set_initial_magnetic_moments(magmon)

for atom in atoms:
    if atom.symbol=='Cr':
       atom.magmom = 5.0
    elif atom.symbol=='C':
       atom.magmom = 0.6

print atoms

view(atoms)

os.system('mkdir result')