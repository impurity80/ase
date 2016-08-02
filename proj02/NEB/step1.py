from neb import *

id = 1

curr_dir = os.getcwd()
work_dir = 'work-{0}'.format(id)
result_file = '{0}/result/result_{1}.txt'.format(curr_dir,id)

os.system('mkdir {0}'.format(work_dir))
os.system('rm -f {0}'.format(result_file))
save(result_file, atoms.get_positions())

os.chdir(work_dir)

OPTIONS = ['init','final']
energies = []

for opt in OPTIONS:

    save(result_file, 'Option : {0}'.format(opt))

    if opt=='init':
        atoms = init
    elif opt=='final':
        atoms = final

    dir = 'opt-{0}'.format(opt)
    os.system('mkdir {0}'.format(dir))
    os.chdir('{0}'.format(dir))

    calc = Vasp(istart = 0,
                icharg = 2,
                xc = 'PBE',
                kpts = (1,1,1),
                encut = 720,
                ispin = 2,
                setups = {'Fe':'_pv'},
                ismear = 1,
                sigma = 0.1,
          #      prec='Accurate',
          #      ediff=0.00025,
                algo='Fast',
          #      potim=0.05,
          #      lorbit=11,
          #      lreal='False',
          #      lwave=False,
                nelm=100
                )

    atoms.set_calculator(calc)
    p = atoms.get_potential_energy()
    print p, p/len(atoms)

    save(result_file, '{0} {1}'.format(p, p/len(atoms)))

    # k-point increase
    calc.set(istart = 1,
             icharg = 0,
             kpts=(8,8,8)
             )
    p = atoms.get_potential_energy()

    save(result_file, '{0} {1}'.format(p, p/len(atoms)))
    save(result_file, '{0}'.format(atoms.get_forces()))

    calc.set(isif=2,ibrion=2, nsw=99)
    p = atoms.get_potential_energy()
    m = atoms.get_magnetic_moment()
    v = atoms.get_volume()

    energies.append(p)

    save(result_file, '3rd calculation \n total energy : {0} eV, {1} eV/atom'.format(p, p/len(atoms)))
    save(result_file, 'magnetic moment : {0} mB, {1} mB/atom'.format(m, m/len(atoms)))
    save(result_file, 'forces \n {0}'.format(atoms.get_forces()))

    save(result_file, '----------------------')

    print p, p/len(atoms)
    print atoms.get_forces()

    os.chdir('..')

os.chdir('..')

save(result_file, '{0}'.format(OPTIONS))
save(result_file, '{0}'.format(energies))
save(result_file, '----------------------')

plt.plot(OPTIONS, energies)
plt.xlabel('OPTIONS')
plt.ylabel('Energy (eV)')

plt.savefig('{0}/result/step{1}.png'.format(curr_dir, id))
plt.show('{0}/result/step{1}.png'.format(curr_dir, id))
