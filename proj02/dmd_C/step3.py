from step0 import *

id = 3

curr_dir = os.getcwd()
work_dir = 'work-{0}'.format(id)
result_file = '{0}/result/result_{1}.txt'.format(curr_dir,id)

os.system('mkdir {0}'.format(work_dir))
os.system('rm -f {0}'.format(result_file))
save(result_file, atoms.get_positions())

os.chdir(work_dir)

OPTIONS = np.linspace(3.5, 3.65, 15)

magmoms, volumes, energies = [], [], []

for opt in OPTIONS:

    save(result_file, 'Option : {0}'.format(opt))

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
                lorbit=11,
                #    setups={'C':'_h'},
                 #    ispin=2,
                ismear=1,
                sigma=0.1,
                )

    atoms.set_calculator(calc)
    p = atoms.get_potential_energy()

    print p, p/len(atoms)

    save(result_file, '{0} {1}'.format(p, p/len(atoms)))

    # k-point increase
    calc.set(istart = 1,
             icharg = 0,
             kpts=(6,6,6)
             )
    p = atoms.get_potential_energy()
 #   m = atoms.get_magnetic_moment()

    save(result_file, '2nd calculation \n total energy : {0} eV, {1} eV/atom'.format(p, p / len(atoms)))
  #  save(result_file, 'magnetic moment : {0} mB, {1} mB/atom'.format(m, m / len(atoms)))
    save(result_file, 'forces \n {0}'.format(atoms.get_forces()))

    calc.set(isif=2, ibrion=2, nsw=99)
    p = atoms.get_potential_energy()
  #  m = atoms.get_magnetic_moment()
    v = atoms.get_volume()

    energies.append(p)
    volumes.append(v)
    magmoms.append(0)
  #  magmoms.append(m)

    save(result_file, '3rd calculation \n total energy : {0} eV, {1} eV/atom'.format(p, p / len(atoms)))
  #  save(result_file, 'magnetic moment : {0} mB, {1} mB/atom'.format(m, m / len(atoms)))
    save(result_file, 'forces \n {0}'.format(atoms.get_forces()))

    save(result_file, '-------------------------------')

    print 'total energy : {0} eV, {1} eV/atom'.format(p, p / len(atoms))

    os.chdir('..')

os.chdir('..')

eos = EquationOfState(volumes,energies)
v0, e0, B = eos.fit()
eos.plot('eos.png')

save(result_file, 'volume, energy(eV), energy(eV/atom), bulk modulus, lattice parameter \n')
save(result_file, '{0} {1} {2} {3} {4}\n'.format(v0,e0,e0/len(atoms), B,v0**(1./3.)))

save(result_file, 'options \n {0}'.format(OPTIONS))
save(result_file, 'volumes \n {0}'.format(volumes))
save(result_file, 'energyes eV \n {0}'.format(energies))
save(result_file, 'magnetic moment \n {0}'.format(magmoms))

save(result_file, 'v, e, m per atoms')
for o, v, e, m in zip(OPTIONS, volumes, energies, magmoms):
    save(result_file, '{0}, {1}, {2}, {3} '.format(o, v/len(atoms), e/len(atoms), m/len(atoms)))
save(result_file, '-----------------------------------')

plt.plot(OPTIONS, energies)
plt.xlabel('OPTIONS')
plt.ylabel('Energy (eV/atom)')

plt.savefig('{0}/result/step{1}.png'.format(curr_dir, id))
plt.show('{0}/result/step{1}.png'.format(curr_dir, id))
