
from ase.io import read
from ase.visualize import view, write
from ase.constraints import FixAtoms
from ase.neb import NEB
from numpy import *
from ase.calculators.vasp import *

#init = read('work-1/init/CONTCAR')
#final = read('work-1/final/CONTCAR')
init = read('work-1/init/POSCAR')
final = read('work-1/init/POSCAR')

a = final.get_cell()[0][0]
final[-1].position = [0, 1./4.*a, 3./8.*a]

init[1].position = [1.636, 1.445, 1.447]
init[9].position = [4.153, 1.445, 1.447]
final[1].position = [1.636, 1.445, 1.447]
final[9].position = [4.153, 1.445, 1.447]

# constraint = FixAtoms(mask=[atom.symbol=='Fe' for atom in init])
#constraint = FixAtoms(mask=[atom.tag < 1 for atom in init])

constraint = FixAtoms(mask=[])
init.set_constraint(constraint)

images = [init]
for i in range(8):
    image = init.copy()
    images.append(image)
images.append(final)

neb = NEB(images)
neb.interpolate()

for i in range(neb.nimages):
    image = neb.images[i]
    constraint = FixAtoms(indices=[1,3,5,7,8,9,10,11,12,13,14,15])
    image.set_constraint(constraint)
    os.system('mkdir {:02d}'.format(i))
    os.chdir('{:02d}'.format(i))
    write('POSCAR', image)
    os.chdir('..')

