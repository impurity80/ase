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
from ase.io import read

os.system('phonopy -d --dim="2 2 3" ')

curr_dir = os.getcwd()
result_file = '{0}/result/result_{1}.txt'.format(curr_dir,id)

OPTIONS = ['001','002','003']

for opt in OPTIONS:
    save(result_file, '-------------------------\n Option : {0}'.format(opt))

    atoms = read('POSCAR-{0}'.format(opt))

    opt_dir = 'opt-{0}'.format(opt)
    os.system('mkdir {0}'.format(opt_dir))
    os.chdir(opt_dir)

    calc = Vasp(istart=0,
                icharg=2,
                xc='PBE',
                ibrion=-1,
                encut=500,
                ediff=1.0e-8,
                ismear=0,
                sigma=0.01,
                ialgo=38,
                lreal='False',
                lwave=False,
                lcharg=False,
                nelm=100,
                kpts=[5, 5, 5]
                )

    atoms.set_calculator(calc)
    p = atoms.get_potential_energy()

    print 'total energy : {0} eV, {1} eV/atom'.format(p, p/len(atoms))

    os.chdir('..')