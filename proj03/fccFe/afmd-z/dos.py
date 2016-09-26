
from step0 import *

from numpy import *
from ase.dft import DOS
from ase.dft import get_distribution_moment
from ase.calculators.vasp import VaspDos

os.chdir('work-dos')

emax, emin, ngrid, efermi = dos_info('DOSCAR')

vdos = VaspDos()
vdos.read_doscar('DOSCAR')

vdos._set_efermi(efermi)

e = vdos.energy
dos_up = vdos.dos[0]
dos_down = vdos.dos[1]
dos_total = dos_up + dos_down

dos_s_up = np.zeros(len(e))
dos_p_up = np.zeros(len(e))
dos_d_up = np.zeros(len(e))
dos_s_down = np.zeros(len(e))
dos_p_down = np.zeros(len(e))
dos_d_down = np.zeros(len(e))

for i in range(len(atoms)):
    dos_s_up += vdos.site_dos(i,'s-up')
    dos_p_up += vdos.site_dos(i,'px-up') + vdos.site_dos(i,'py-up') + vdos.site_dos(i,'pz-up')
    dos_d_up += vdos.site_dos(i,'dxy-up') + vdos.site_dos(i,'dyz-up') + vdos.site_dos(i,'dz2-up') + vdos.site_dos(i,'dxz-up') + vdos.site_dos(i,'dx2-up')
    dos_s_down += vdos.site_dos(i, 's-down')
    dos_p_down += vdos.site_dos(i, 'px-down') + vdos.site_dos(i, 'py-down') + vdos.site_dos(i, 'pz-down')
    dos_d_down += vdos.site_dos(i, 'dxy-down') + vdos.site_dos(i, 'dyz-down') + vdos.site_dos(i, 'dz2-down') + vdos.site_dos(i,'dxz-down') + vdos.site_dos(i,'dx2-down')

#dos_s_up = vdos.site_dos(4,'s-up')
#dos_p_up = vdos.site_dos(4,'px-up') + vdos.site_dos(4,'py-up') + vdos.site_dos(4, 'pz-up')

#dos_s_down = vdos.site_dos(0,'s-down')
#dos_p_down = vdos.site_dos(0,'px-down') + vdos.site_dos(0,'py-down') + vdos.site_dos(0,'pz-down')
#dos_d_down = vdos.site_dos(0,'dxy-down') + vdos.site_dos(0,'dyz-down') + vdos.site_dos(0,'dz2-down') + vdos.site_dos(0,'dxz-down') + vdos.site_dos(0,'dx2-down')

plt.plot([-10,10],[0,0],color='black')
plt.plot(e, dos_up/2, label='up', color='b')
plt.plot(e, -1*dos_down/2, label='down', color='#0000ff')
#plt.plot(e, dos_up, label='up', color='r')
# plt.plot(e, -1*dos_down, label='down', color='r')

plt.plot(e, 1*dos_s_up/2, label='s', color='y')
#plt.plot(e, -1*dos_s_down, color='y')

plt.plot(e, 1*dos_p_up/2, label='p', color='g')
# plt.plot(e, 4*dos_p_up, label='p')
plt.plot(e, 1*dos_d_up/2, label='d', color='r')
#plt.plot(e, -1*dos_d_down, color='g')
#plt.plot(e, 1*vdos.site_dos(0,'dxy-up') - 0.5, label='dxy')
#plt.plot(e, 1*vdos.site_dos(0,'dyz-up') - 0.5, label='dyz')
#plt.plot(e, 1*vdos.site_dos(0,'dz2-up') - 0.5, label='dz2')
#plt.plot(e, 1*vdos.site_dos(0,'dxz-up') - 0.5, label='dxz')
#plt.plot(e, 1*vdos.site_dos(0,'dx2-up') - 0.5, label='dx2')
#plt.plot(e, -4*dos_s_down, label='s')
# plt.plot(e, -4*dos_p_down, label='p')
#plt.plot(e, -4*dos_d_down, label='d')

#plt.plot(e, -1*vdos.site_dos(0,'pz-down'))
#for i in range(0,18):
#    plt.plot(e, vdos.site_dos(0,i), label='dos{0}'.format(i))

plt.grid(True)
#plt.xlim(emin-efermi, 10)
plt.xlim(-15,10)
plt.ylim(-16.0, 16.0)
plt.legend()
plt.xlabel('E-Ef')
plt.ylabel('DOS')
plt.savefig('../result/dos.png')
plt.show('{../result/dos.png')

