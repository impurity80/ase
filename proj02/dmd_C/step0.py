from ase.lattice.surface import surface
from ase import Atoms
from ase.visualize import view, write
from ase.calculators.vasp import *
import matplotlib.pyplot as plt
from ase.constraints import FixAtoms
from matplotlib import mlab
from numpy import *
from ase.utils.eos import EquationOfState
from ase.dft.kpoints import *
from ase.lattice.spacegroup import crystal

def dos_info(filename):
    f = open(filename, 'r')
    for i in range(5):
        line = f.readline()
    emax, emin, ngrid, efermi, unknown = [float(x) for x in f.readline().split()]
    return emax, emin, ngrid, efermi

def band_info(cell):
    pts = get_special_points('fcc')
    G = pts['Gamma']
    X = pts['X']
    W = pts['W']
    K = pts['K']
    L = pts['L']
    U = pts['U']
    kpt, x, X = get_bandpath([G,X,W,K,G,L,U,W,L,K,U,X], cell, 200)
    names = ['G','X','W','K','G','L','U','W','L','K','U','X']
    return kpt, x, X, names

def save( filename, arg ):
    f = open(filename, 'a+t')
    f.write('{0} \n'.format(arg))
    f.close()

atoms = crystal(spacegroup=227,
                symbols='C',
                basis=[0,0,0],
                cellpar=[3.57,3.57,3.57,90.0,90.0,90.0])

# atoms.set_initial_magnetic_moments([1,1,1,1,1,1,1,1])

view(atoms)

os.system('mkdir result')


