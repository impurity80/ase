from step0 import *

id = 1

curr_dir = os.getcwd()
work_dir = 'work-dos'.format(id)
result_file = '{0}/result/result_{1}.txt'.format(curr_dir,id)

os.system('mkdir {0}'.format(work_dir))
os.system('rm -f {0}'.format(result_file))
save(result_file, atoms.get_positions())

os.chdir(work_dir)

calc.set(istart = 0,
         icharg = 2)

atoms.set_calculator(calc)
p = atoms.get_potential_energy()

print 'total energy : {0} eV, {1} eV/atom'.format(p, p/len(atoms))

save(result_file, '1st calculation \n total energy : {0} eV, {1} eV/atom'.format(p, p/len(atoms)))

calc.set(istart = 1,
         icharg = 0,
         kpts=(12,12,12)
         )

p = atoms.get_potential_energy()
m = atoms.get_magnetic_moment()

save(result_file, '2nd calculation \n total energy : {0} eV, {1} eV/atom'.format(p, p/len(atoms)))
save(result_file, 'magnetic moment : {0} mB, {1} mB/atom'.format(m, m/len(atoms)))
save(result_file, 'forces \n {0}'.format(atoms.get_forces()))

calc.set(ismear=-5, lorbit=11, nedos=2000, sigma=0.5)
p = atoms.get_potential_energy()
save(result_file, '3rd calculation \n total energy : {0} eV, {1} eV/atom'.format(p, p/len(atoms)))

tm = atoms.get_magnetic_moment()
m = atoms.get_magnetic_moments()
save(result_file, 'total magnetic moment : {0} mB {1} mB/atom '.format(tm, tm/len(atoms)))
save(result_file, 'magnetic moment: {0}'.format(m))

print 'total energy : {0} eV, {1} eV/atom'.format(p, p/len(atoms))



