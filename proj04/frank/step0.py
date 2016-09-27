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

a = 3.5349

bulk = FaceCenteredCubic('Fe', directions=[[1,0,0],[0,1,0],[0,0,1]], latticeconstant=a)

#bulk = Atoms('Fe4', scaled_positions=[ (0.5,0.5,0), (0.5, 0, 0.5), (0, 0.5, 0.5), (0,0,0)],
#            magmoms=[5,5,-5,-5], cell=[a,a,a], pbc=(1,1,1))

bulk = bulk*(1,2,1)
bulk.set_initial_magnetic_moments([5,5,5,5,-5,-5,-5,-5])

s1 = surface(bulk, (1,2,1), 3)
s1 = s1*(1,2,1)

# view(s1)

s2 = s1.copy()
s2.translate(s2.get_cell()[2])

cell = s1.get_cell()
# cell[1] = cell[1]*8./7.
cell[1] = cell[1]*24./23.
s2.set_cell(cell, scale_atoms=True)

s1 = s1+s2

#s2.set_cell([0,1,0], scale_atoms=True)

# print s2.get_cell()


mask = [ [0,2,9,11,20,22,32,34,41,43,48,50,57,59,77,79,80,82,68,70,29,31].count(atom.index)==1 for atom in s1]
# mask = [atom.position[2] < 4.2 or ([41,43,32,34,29,31,20,22,9,11].count(atom.index)==1 )for atom in s1]
constraint = FixAtoms(mask=mask)
s1.set_constraint(constraint)
s1.center(vacuum=10, axis=2)
s1.center(vacuum=10, axis=1)

del s1[95]
del s1[93]
del s1[91]
del s1[90]
del s1[89]
del s1[88]
del s1[74]
del s1[72]
del s1[55]
del s1[54]
del s1[53]
del s1[52]
# del s1[86]
# del s1[84]
# del s1[75]
# del s1[73]
# del s1[66]
# del s1[64]


view(s1)

atoms = s1

os.system('mkdir result')

pts = get_special_points('cubic')
print pts

def dos_info(filename):
    f = open(filename, 'r')
    for i in range(5):
        line = f.readline()
    emax, emin, ngrid, efermi, unknown = [float(x) for x in f.readline().split()]
    return emax, emin, ngrid, efermi
