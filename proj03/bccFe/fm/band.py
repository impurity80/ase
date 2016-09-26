
from step0 import *

emax, emin, ngrid, Ef = dos_info('work-band/DOSCAR')
kpt, x_pt, X, names = band_info(atoms.get_cell())

f = open('work-band/EIGENVAL', 'r')

for i in range(5):
    line = f.readline()

unknown, nkpoints, nbands = [int(x) for x in f.readline().split()]

blankline = f.readline()

band_energies_up = [[] for i in range(nbands)]
band_energies_down = [[] for i in range(nbands)]

for i in range(nkpoints):
    x,y,z, weight = [float(x) for x in f.readline().split()]

    for j in range(nbands):
        fields = f.readline().split()
        id, energy_up, energy_down = int(fields[0]), float(fields[1])-Ef, float(fields[2])-Ef
        band_energies_up[id-1].append(energy_up)
        band_energies_down[id - 1].append(energy_down)
    blankline = f.readline()
f.close()

plt.plot((0,X[-1]), [0,0], color='black', linewidth=1)

for i in range(nbands):
    plt.plot(x_pt, band_energies_up[i], color='r')
    plt.plot(x_pt, band_energies_down[i], color='b')

ax = plt.gca()
ax.set_xticks([]) # no tick marks
plt.xlabel('k-vector')
plt.ylabel('Energy (eV)')
#plt.ylim(emin-efermi, 10)
plt.ylim(-10,10)
plt.xlim(0,X[-1])
plt.grid(True)
# plt.axhspan(0.25, 0.75)
ax.set_xticks(X)
ax.set_xticklabels(names)
plt.savefig('result/bandstructure.png')
plt.show('result/bandstructure.png')


