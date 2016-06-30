f = open('band/EIGENVAL', 'r')
Ef = 7.6463

line1 = f.readline()
line2 = f.readline()
line3 = f.readline()
line4 = f.readline()
comment = f.readline()
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


import matplotlib.pyplot as plt

for i in range(nbands):
    plt.plot(range(nkpoints), band_energies_up[i], color = 'r')
    plt.plot(range(nkpoints), band_energies_down[i], color = 'b')

plt.plot([0,200], [0,0], color='g', linewidth=2)

ax = plt.gca()
ax.set_xticks([]) # no tick marks
plt.xlabel('k-vector')
plt.ylabel('Energy (eV)')
plt.ylim(-10, 30)
plt.grid(True)
#plt.axhspan(0.25, 0.75)
ax.set_xticks(range(0,200,10))
ax.set_xticklabels(['G','X','W','K','G','L','U','W','L','K','U','X'])
plt.savefig('result/bandstructure.png')
plt.show('result/bandstructure.png')

