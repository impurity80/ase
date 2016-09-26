from step0 import *

id = 'encut'

curr_dir = os.getcwd()
work_dir = 'work-{0}'.format(id)
result_file = '{0}/result/result_{1}.txt'.format(curr_dir,id)

os.system('mkdir {0}'.format(work_dir))
os.system('rm -f {0}'.format(result_file))
save(result_file, atoms.get_positions())

os.chdir(work_dir)

OPTIONS = range(540, 810, 40)
energies = []

for opt in OPTIONS:
    save(result_file, '-------------------------\n Option : {0}'.format(opt))

#    a = 3.5086
#    atoms.set_cell([a,a,a], scale_atoms=True)

    opt_dir = 'opt-{0}'.format(opt)
    os.system('mkdir {0}'.format(opt_dir))
    os.chdir(opt_dir)

    calc = Vasp(istart = 0,
                icharg = 2,
                xc = 'PBE',
                kpts = (1,1,1),
                encut = opt,
                ispin = 1,
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

    print 'total energy : {0} eV, {1} eV/atom'.format(p, p/len(atoms))

    save(result_file, '1st calculation \n total energy : {0} eV, {1} eV/atom'.format(p, p/len(atoms)))

    calc.set(istart = 1,
             icharg = 0,
             kpts=(12,12,12)
             )

    p = atoms.get_potential_energy()
    m = 0
#    m = atoms.get_magnetic_moment()

    energies.append(p/len(atoms))

    save(result_file, '2nd calculation \n total energy : {0} eV, {1} eV/atom'.format(p, p/len(atoms)))
    save(result_file, 'magnetic moment : {0} mB, {1} mB/atom'.format(m, m/len(atoms)))
    save(result_file, 'forces \n {0}'.format(atoms.get_forces()))

    save(result_file, '-------------------------------')

    print 'total energy : {0} eV, {1} eV/atom'.format(p, p/len(atoms))

    os.chdir('..')

save(result_file, 'options \n {0}'.format(OPTIONS))
save(result_file, 'energyes eV/atom \n {0}'.format(energies))
save(result_file, '-----------------------------------')

plt.plot(OPTIONS, energies)
plt.xlabel('OPTIONS')
plt.ylabel('Energy (eV/atom)')

plt.savefig('{0}/result/step{1}.png'.format(curr_dir, id))
plt.show('{0}/result/step{1}.png'.format(curr_dir, id))
