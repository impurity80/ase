from step0 import *

id = 1

curr_dir = os.getcwd()
work_dir = 'work-{0}'.format(id)
result_file = '{0}/result/result_{1}.txt'.format(curr_dir,id)

os.system('mkdir {0}'.format(work_dir))
os.system('rm -f {0}'.format(result_file))
save(result_file, atoms.get_positions())

os.chdir(work_dir)

OPTIONS = ['init', 'final']
print OPTIONS
volumes = []
energies = []
magmoms = []

for opt in OPTIONS:
    save(result_file, '-------------------------\n Option : {0}'.format(opt))

#    atoms.set_cell([opt,opt,opt], scale_atoms=True)

    if opt=='init':
        atoms = init
    elif opt=='final':
        atoms = final

    opt_dir = '{0}'.format(opt)
    os.system('mkdir {0}'.format(opt_dir))
    os.chdir(opt_dir)

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
             kpts=(8,8,8)
             )

    p = atoms.get_potential_energy()
    m = atoms.get_magnetic_moment()

    save(result_file, '2nd calculation \n total energy : {0} eV, {1} eV/atom'.format(p, p/len(atoms)))
    save(result_file, 'magnetic moment : {0} mB, {1} mB/atom'.format(m, m/len(atoms)))
    save(result_file, 'forces \n {0}'.format(atoms.get_forces()))

    calc.set(isif=2,ibrion=2, nsw=99)
    p = atoms.get_potential_energy()
    m = atoms.get_magnetic_moment()
    v = atoms.get_volume()

    energies.append(p)
    volumes.append(v)
    magmoms.append(m)

    save(result_file, '3rd calculation \n total energy : {0} eV, {1} eV/atom'.format(p, p/len(atoms)))
    save(result_file, 'magnetic moment : {0} mB, {1} mB/atom'.format(m, m/len(atoms)))
    save(result_file, 'forces \n {0}'.format(atoms.get_forces()))

    save(result_file, '-------------------------------')

    print 'total energy : {0} eV, {1} eV/atom'.format(p, p/len(atoms))

    os.chdir('..')

save(result_file, 'options \n {0}'.format(OPTIONS))
save(result_file, 'volumes \n {0}'.format(volumes))
save(result_file, 'energyes eV \n {0}'.format(energies))
save(result_file, 'magnetic moment \n {0}'.format(magmoms))

save(result_file, 'v, e, m per atoms')
for o, v, e, m in zip(OPTIONS, volumes, energies, magmoms):
    save(result_file, '{0}, {1}, {2}, {3} '.format(o, v/len(atoms), e/len(atoms), m/len(atoms)))
   
save(result_file, '-----------------------------------')
                                                      
    
