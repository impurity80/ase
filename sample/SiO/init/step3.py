
from step0 import *

os.system('phonopy -f opt-001/vasprun.xml opt-002/vasprun.xml opt-003/vasprun.xml')

save('mesh.conf', 'ATOM_NAME = Si O')
save('mesh.conf', 'DIM = 2 2 3')
save('mesh.conf', 'MP = 8 8 8')

#os.system('phonopy -p mesh.conf')
#os.system('phonopy -t mesh.conf')
os.system('phonopy -t -p mesh.conf')