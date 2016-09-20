
from step0 import *

os.system('./script-qha.sh -c')
os.system('phonopy-qha e-v.dat QHA-*/thermal_properties.yaml -p --sparse=50')