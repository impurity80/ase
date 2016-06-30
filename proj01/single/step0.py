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


a = 3.6

#bulk = crystal(spacegroup=225,
#        symbols='Ni',
#        basis=[0, 0, 0],
#        cellpar=[a,a,a, 60,60,60])


bulk = Atoms('Fe4',
             scaled_positions=[
                 (0.5, 0.5, 0),
                 (0.5, 0, 0.5),
                 (0, 0.5, 0.5),
                 (0, 0, 0)],
             magmoms=[5, 5, 5, 5],
             cell=[a, a, a],
             pbc=(1, 1, 1))

#bulk = FaceCenteredCubic('Fe', directions=[[0,1,1],[1,0,1],[1,1,0]], latticeconstant=a)
#bulk = BodyCenteredCubic('Fe', directions=[[-1,1,1],[1,-1,1],[1,1,-1]], latticeconstant=2.87)
#bulk.set_initial_magnetic_moments([5])

bulk.append(Atom('C', [0, 0, 0.5*a], magmom=0.6))

calc = Vasp(xc='PBE',
            kpts=(1, 1, 1),
            encut=720,
            ispin=2,
            setups={'Ni': '_pv', 'Cr': '_pv', 'Fe':'_sv'},
            ismear=1,
            sigma=0.1,
            ediff=0.00025,
            algo='Fast',
            potim=0.05,
            lorbit=11,
            lreal='False',
            lwave=False,
            nelm=100,
         #   nupdown=0
            )



view(bulk)
atoms = bulk

os.system('mkdir result')
