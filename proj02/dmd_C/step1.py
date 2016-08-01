from step0 import *

id = 1

curr_dir = os.getcwd()
work_dir = 'work-{0}'.format(id)
result_file = '{0}/result/result_{1}.txt'.format(curr_dir,id)

os.system('mkdir {0}'.format(work_dir))
os.system('rm -f {0}'.format(result_file))
save(result_file, atoms.get_positions())

os.chdir(work_dir)

OPTIONS = range(3,15,1)
volumes, energies = [], []

for opt in OPTIONS:

    save(result_file, 'Option : {0}'.format(opt))

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

    save(result_file, '{0} {1}'.format(p, p/len(atoms)))

    # k-point increase
    calc.set(istart = 1,
             icharg = 0,
             kpts=(opt,opt,opt)
             )
    p = atoms.get_potential_energy()

    energies.append(p/len(atoms))

    save(result_file, '{0} {1}'.format(p, p/len(atoms)))
    save(result_file, '{0}'.format(atoms.get_forces()))
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


