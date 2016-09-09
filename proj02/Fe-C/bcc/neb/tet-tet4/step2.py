
from ase.io import read
from ase.visualize import view, write
from ase.constraints import FixAtoms
from ase.neb import NEB
from numpy import *
from ase.calculators.vasp import *

init = read('work-1/init/CONTCAR')
final = read('work-1/init/CONTCAR')

a = final.get_cell()[0][0]
final[-1].position = [0, 3./8.*a, 1./4.*a]

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
    constraint = FixAtoms(mask=[atom.tag <1 for atom in image])
    image.set_constraint(constraint)
    os.system('mkdir {:02d}'.format(i))
    os.chdir('{:02d}'.format(i))
    write('POSCAR', image)
    os.chdir('..')

