
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
dos_total = vdos.dos

dos_s = np.zeros(len(e))
dos_p = np.zeros(len(e))
dos_d = np.zeros(len(e))

for i in range(len(atoms)): # atomic type number
    dos_s += vdos.site_dos(i,'s')
    dos_p += vdos.site_dos(i,'px') + vdos.site_dos(i,'py') + vdos.site_dos(i,'pz')
    dos_d += vdos.site_dos(i,'dxy') + vdos.site_dos(i,'dyz') + vdos.site_dos(i,'dz2') + vdos.site_dos(i,'dxz') + vdos.site_dos(i,'dx2')

# dos_s_up = vdos.site_dos(4,'s-up')
# dos_p_up = vdos.site_dos(4,'px-up') + vdos.site_dos(4,'py-up') + vdos.site_dos(4, 'pz-up')

# dos_s_down = vdos.site_dos(0,'s-down')
#dos_p_down = vdos.site_dos(0,'px-down') + vdos.site_dos(0,'py-down') + vdos.site_dos(0,'pz-down')
#dos_d_down = vdos.site_dos(0,'dxy-down') + vdos.site_dos(0,'dyz-down') + vdos.site_dos(0,'dz2-down') + vdos.site_dos(0,'dxz-down') + vdos.site_dos(0,'dx2-down')

plt.plot([-10,10],[0,0],color='black')
plt.plot(e, dos_total, label='total', color='b')
#plt.plot(e, dos_up, label='up', color='r')
#plt.plot(e, -1*dos_down, label='down', color='r')

plt.plot(e, 1*dos_s, label='s', color='y')
# plt.plot(e, -1*dos_s_down, color='y')

plt.plot(e, dos_p, label='p', color='g')
# plt.plot(e, 4*dos_p_up, label='p')
plt.plot(e, 1*dos_d, label='d', color='r')
# plt.plot(e, -1*dos_d_down, color='g')


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
plt.ylim(0.0, 16.0)
plt.legend()
plt.xlabel('E-Ef')
plt.ylabel('DOS')
plt.savefig('../result/dos.png')
plt.show('{../result/dos.png')

