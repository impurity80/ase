from step0 import *

id = 1
os.system('mkdir work-{0}'.format(id))
os.chdir('work-{0}'.format(id))
CWD = os.getcwd()
os.system('rm -f {0}/result.txt'.format(CWD))
save('{0}/result.txt'.format(CWD), atoms.get_positions())

OPTIONS = range(3,15,1)
volumes, energies = [], []

for opt in OPTIONS:

    save('{0}/result.txt'.format(CWD), 'Option : {0}'.format(opt))

    a = 3.57
    atoms.set_cell([a,a,a], scale_atoms=True)

    dir = 'opt-{0}'.format(opt)
    os.system('mkdir {0}'.format(dir))
    os.chdir('{0}'.format(dir))

    calc = Vasp(istart = 0,
                icharg = 2,
                xc='PBE',
                kpts=(1,1,1),
                encut=700,
            #  ispin=2,
                setups={'C':'_h'},
                ismear = 1,
                sigma  = 0.1,
                )

    atoms.set_calculator(calc)
    p = atoms.get_potential_energy()

    print p, p/len(atoms)

    save('{0}/result.txt'.format(CWD), '{0} {1}'.format(p, p/len(atoms)))

    # k-point increase
    calc.set(istart = 1,
             icharg = 0,
             kpts=(opt,opt,opt)
             )
    p = atoms.get_potential_energy()

    energies.append(p/len(atoms))

    save('{0}/result.txt'.format(CWD), '{0} {1}'.format(p, p/len(atoms)))
    save('{0}/result.txt'.format(CWD), '{0}'.format(atoms.get_forces()))
    save('{0}/result.txt'.format(CWD), '----------------------')

    print p, p/len(atoms)
    print atoms.get_forces()

    os.chdir('..')

os.chdir('..')

save('{0}/result.txt'.format(CWD), '{0}'.format(OPTIONS))
save('{0}/result.txt'.format(CWD), '{0}'.format(energies))
save('{0}/result.txt'.format(CWD), '----------------------')

plt.plot(OPTIONS, energies)
plt.xlabel('OPTIONS')
plt.ylabel('Energy (eV)')

plt.savefig('{0}/step{1}.png'.format(CWD, id))
plt.show('{0}/step{1}.png'.format(CWD, id))


