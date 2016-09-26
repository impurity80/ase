from step0 import *

id = 'dos'

curr_dir = os.getcwd()
work_dir = 'work-{0}'.format(id)
result_file = '{0}/result/result_{1}.txt'.format(curr_dir,id)

os.system('mkdir {0}'.format(work_dir))
os.system('rm -f {0}'.format(result_file))
save(result_file, atoms.get_positions())

os.chdir(work_dir)

a = 2.7558

atoms.set_cell([a, a, a], scale_atoms=True)

calc = Vasp(istart =0,
            icharg =2,
            xc='PBE',
            kpts=(1, 1, 1),
            encut=540,
            ispin=1,
          #  setups={'Ni': '_pv', 'Cr': '_pv'},
            ismear=1,
            sigma=0.1,
            ediff=0.00025,
            algo='Fast',
            potim=0.05,
            lorbit=11,
            lreal='False',
            lwave=False,
            nelm=100,
         #   nupdown=0
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
# m = atoms.get_magnetic_moment()

save(result_file, '2nd calculation \n total energy : {0} eV, {1} eV/atom'.format(p, p/len(atoms)))
save(result_file, 'magnetic moment : {0} mB, {1} mB/atom'.format(m, m/len(atoms)))
save(result_file, 'forces \n {0}'.format(atoms.get_forces()))

calc.set(ismear=-5, lorbit=11, nedos=2000, sigma=0.5)
p = atoms.get_potential_energy()
save(result_file, '3rd calculation \n total energy : {0} eV, {1} eV/atom'.format(p, p/len(atoms)))

# tm = atoms.get_magnetic_moment()
# m = atoms.get_magnetic_moments()
# save(result_file, 'total magnetic moment : {0} mB {1} mB/atom '.format(tm, tm/len(atoms)))
# save(result_file, 'magnetic moment: {0}'.format(m))

print 'total energy : {0} eV, {1} eV/atom'.format(p, p/len(atoms))



