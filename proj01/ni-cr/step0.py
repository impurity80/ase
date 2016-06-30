from ase.lattice.surface import surface
from ase import Atoms
from ase.visualize import view, write
from ase.calculators.vasp import *
import matplotlib.pyplot as plt
from ase.constraints import FixAtoms
from matplotlib import mlab
from numpy import *
from ase.utils.eos import EquationOfState

a = 3.5086

bulk = Atoms('Ni4',
              scaled_positions=[
                                (0.5, 0.5, 0),
                                (0.5, 0, 0.5),
                                (0, 0.5, 0.5),
                                (0, 0, 0)],
              magmoms = [5,5,5,5],
              cell=[a, a, a],
              pbc=(1,1,1))

bulk = bulk*(2,2,2)

np.random.seed(0)
index = range(len(bulk))
np.random.shuffle(index)

for i in index[0:int(round(len(bulk)*0.343))]:
    bulk[index[i]].symbol = 'Cr'


cr = 0
for atom in bulk:
    if atom.symbol =='Cr' :
        cr = cr+1
print cr

view(bulk)

atoms = bulk

print len(atoms)

def save( filename, arg ):
    f = open(filename, 'a+t')
    f.write('{0} \n'.format(arg))
    f.close()

os.system('mkdir result')
