
from step0 import *

os.system('cp work-2/INCAR .')

# os.system('cp work-2/KPOINTS .')
save('KPOINTS','KPOINTS created')
save('KPOINTS','0 \nMonkhorst-Pack\n6 6 6\n0 0 0')

os.system('cp work-2/POTCAR .')
os.system('cp work-2/POSCAR .')

os.system('phonopy-qha --cu POSCAR')
os.system('./script-qha.sh -m')
# os.system('./script-qha.sh -r')

#os.system('./script-qha.sh -c')
#os.system('phonopy-qha e-v.dat QHA-*/thermal_properties.yaml -p --sparse=50')