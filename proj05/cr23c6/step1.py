from step0 import *

id = 1

curr_dir = os.getcwd()
work_dir = 'work-{0}'.format(id)
result_file = '{0}/result/result_{1}.txt'.format(curr_dir, id)

os.system('mkdir {0}'.format(work_dir))
os.system('rm -f {0}'.format(result_file))
save(result_file, atoms.get_positions())

os.chdir(work_dir)

OPTIONS = np.linspace(a*0.95, a*1.05, 11)

print OPTIONS
volumes = []
energies = []
magmoms = []

for opt in OPTIONS:
    save(result_file, '-------------------------\n Option : {0}'.format(opt))

    atoms.set_cell([opt, opt, opt], scale_atoms=True)

    opt_dir = 'opt-{0}'.format(opt)
    os.system('mkdir {0}'.format(opt_dir))
    os.chdir(opt_dir)

    calc = Vasp(istart = 0,
                icharg = 2,
                xc = 'PBE',
                kpts = (1,1,1),
                encut = 540,
                ispin = 2,
          #      setups = {'Ni':'_pv', 'Cr':'_pv'},
                ismear = 1,
                sigma = 0.1,
                algo='Fast',
                potim=0.05,
                lorbit=11,
                lreal='False',
                lwave=False,
                nelm=100
                )

    atoms.set_calculator(calc)
    p = atoms.get_potential_energy()

    print 'total energy : {0} eV, {1} eV/atom'.format(p, p / len(atoms))

    save(result_file, '1st calculation \n total energy : {0} eV, {1} eV/atom'.format(p, p / len(atoms)))

    calc.set(istart=1,
             icharg=0,
             kpts=(4,4,4)
             )

    p = atoms.get_potential_energy()
    m = atoms.get_magnetic_moment()
    v = atoms.get_volume()

    save(result_file, '2nd calculation \n total energy : {0} eV, {1} eV/atom'.format(p, p / len(atoms)))
    save(result_file, 'magnetic moment : {0} mB, {1} mB/atom'.format(m, m / len(atoms)))
    save(result_file, 'forces \n {0}'.format(atoms.get_forces()))

    calc.set(isif=2, ibrion=2, nsw=99)
    p = atoms.get_potential_energy()
    m = atoms.get_magnetic_moment()
    v = atoms.get_volume()

    energies.append(p)
    volumes.append(v)
    magmoms.append(m)

    save(result_file, '3rd calculation \n total energy : {0} eV, {1} eV/atom'.format(p, p / len(atoms)))
    save(result_file, 'magnetic moment : {0} mB, {1} mB/atom'.format(m, m / len(atoms)))
    save(result_file, 'forces \n {0}'.format(atoms.get_forces()))

    save(result_file, '-------------------------------')

    print 'total energy : {0} eV, {1} eV/atom'.format(p, p / len(atoms))

    os.chdir('..')

eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()
eos.plot('eos.png')
os.system('cp eos.png ../result/')

save(result_file, 'volume, energy(eV), energy(eV/atom), bulk modulus, lattice parameter \n')
save(result_file, '{0} {1} {2} {3} {4}\n'.format(v0, e0, e0 / len(atoms), B, v0 ** (1. / 3.)))

save(result_file, 'options \n {0}'.format(OPTIONS))
save(result_file, 'volumes \n {0}'.format(volumes))
save(result_file, 'energyes eV \n {0}'.format(energies))
save(result_file, 'magnetic moment \n {0}'.format(magmoms))

save(result_file, 'v, e, m per atoms')
for o, v, e, m in zip(OPTIONS, volumes, energies, magmoms):
    save(result_file, '{0}, {1}, {2}, {3} '.format(o, v / len(atoms), e / len(atoms), m / len(atoms)))

save(result_file, '-----------------------------------')

plt.plot(OPTIONS, energies)
plt.xlabel('OPTIONS')
plt.ylabel('Energy (eV/atom)')

plt.savefig('{0}/result/step{1}.png'.format(curr_dir, id))
plt.show('{0}/result/step{1}.png'.format(curr_dir, id))


