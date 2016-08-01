from step0 import *

id = 3
os.system('mkdir work-{0}'.format(id))
os.chdir('work-{0}'.format(id))
CWD = os.getcwd()
os.system('rm -f {0}/result.txt'.format(CWD))

result = '{0}/result.txt'.format(CWD)

save('{0}/result.txt'.format(CWD), atoms.get_positions())

OPTIONS = np.linspace(3.5, 3.65, 15)

volumes, energies = [], []

for opt in OPTIONS:

    save('{0}/result.txt'.format(CWD), 'Option : {0}'.format(opt))

    a = opt
    atoms.set_cell([a,a,a], scale_atoms=True)

    dir = 'opt-{0}'.format(opt)
    os.system('mkdir {0}'.format(dir))
    os.chdir('{0}'.format(dir))

    calc = Vasp(istart=0,
                icharg=2,
                xc='PBE',
                kpts=(1, 1, 1),
                encut=700,
                #    setups={'C':'_h'},
                #     ispin=2,
                #     setups={'Ni':'_pv'},
                ismear=1,
                sigma=0.1,
                )

    atoms.set_calculator(calc)
    p = atoms.get_potential_energy()

    print p, p/len(atoms)

    save('{0}/result.txt'.format(CWD), '{0} {1}'.format(p, p/len(atoms)))

    # k-point increase
    calc.set(istart = 1,
             icharg = 0,
             kpts=(6,6,6)
             )
    p = atoms.get_potential_energy()
    v = atoms.get_volume()

    energies.append(p)
    volumes.append(v)

    save(result, '{0} {1}'.format(p, p/len(atoms)))
    save(result, '{0}'.format(atoms.get_forces()))

    print p, p/len(atoms)
    print atoms.get_forces()

    calc.set(isif=2,ibrion=2, nsw=99)
    p = atoms.get_potential_energy()
    v = atoms.get_volume()

    save(result, 't energy : {0}, a energy : {1}, volume : {2}'.format(p, p / len(atoms), v))
    save(result, 'pos \n {0}'.format(atoms.get_positions()))
    save(result, 'force \n {0}'.format(atoms.get_forces()))

    print p, p / len(atoms)

    save(result, '----------------------')

    os.chdir('..')

os.chdir('..')

eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()
eos.plot('eos.png')

save('{0}/result.txt'.format(CWD), '{0} {1} {2} {3}\n'.format(v0, e0, B, v0 ** (1. / 3.)))

save('{0}/result.txt'.format(CWD), '{0}'.format(OPTIONS))
save('{0}/result.txt'.format(CWD), '{0}'.format(energies))
save('{0}/result.txt'.format(CWD), '----------------------')

plt.plot(OPTIONS, energies)
plt.xlabel('OPTIONS')
plt.ylabel('Energy (eV)')

plt.savefig('{0}/step{1}.png'.format(CWD, id))
plt.show('{0}/step{1}.png'.format(CWD, id))

