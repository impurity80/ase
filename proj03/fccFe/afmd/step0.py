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

a = 3.6

bulk = FaceCenteredCubic('Fe', directions=[[1,0,0],[0,1,0],[0,0,1]], latticeconstant=a)

#bulk = Atoms('Fe4', scaled_positions=[ (0.5,0.5,0), (0.5, 0, 0.5), (0, 0.5, 0.5), (0,0,0)],
#            magmoms=[5,5,-5,-5], cell=[a,a,a], pbc=(1,1,1))

bulk = bulk*(1,2,1)
bulk.set_initial_magnetic_moments([5,5,5,5,-5,-5,-5,-5])

atoms = bulk

os.system('mkdir result')

pts = get_special_points('cubic')
print pts

def dos_info(filename):
    f = open(filename, 'r')
    for i in range(5):
        line = f.readline()
    emax, emin, ngrid, efermi, unknown = [float(x) for x in f.readline().split()]
    return emax, emin, ngrid, efermi

def band_info(cell):
    pts = get_special_points('cubic')
    G = pts['Gamma']
    X = pts['X']
    R = pts['R']
    M = pts['M']

    kpt, x, X = get_bandpath([G,X,M,G,R,X,M,R], cell, 200)
    names = ['G','X','M','G','R','X','M','R']
    return kpt, x, X, names