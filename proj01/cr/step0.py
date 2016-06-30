from ase.lattice.surface import surface
from ase import Atoms
from ase.visualize import view, write
from ase.calculators.vasp import *
import matplotlib.pyplot as plt
from ase.constraints import FixAtoms
from matplotlib import mlab
from numpy import *
from ase.utils.eos import EquationOfState

a = 3.624

bulk = Atoms('Cr4',
              scaled_positions=[
                                (0.5, 0.5, 0),
                                (0.5, 0, 0.5),
                                (0, 0.5, 0.5),
                                (0, 0, 0)],
              magmoms = [5,5,5,5],
              cell=[a, a, a],
              pbc=(1,1,1))

bulk[0].symbol = 'Ni'
bulk[1].symbol = 'Ni'
bulk[2].symbol = 'Ni'
bulk[3].symbol = 'Ni'

view(bulk)

atoms = bulk

def save( filename, arg ):
    f = open(filename, 'a+t')
    f.write('{0} \n'.format(arg))
    f.close()

os.system('mkdir result')
