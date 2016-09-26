from step0 import *

id = 1

curr_dir = os.getcwd()
work_dir = 'work-{0}'.format(id)
result_file = '{0}/result/result_{1}.txt'.format(curr_dir, id)

os.system('mkdir {0}'.format(work_dir))
os.system('rm -f {0}'.format(result_file))
save(result_file, atoms.get_positions())

os.chdir(work_dir)

a = 3.5349

atoms.set_cell([a, a*2, a], scale_atoms=True)

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
            nelm=100,
            nupdown=0
            )

atoms.set_calculator(calc)
p = atoms.get_potential_energy()

print 'total energy : {0} eV, {1} eV/atom'.format(p, p / len(atoms))

save(result_file, '1st calculation \n total energy : {0} eV, {1} eV/atom'.format(p, p / len(atoms)))

calc.set(istart=1,
         icharg=0,
         kpts=(2, 2, 2)
         )

p = atoms.get_potential_energy()
m = atoms.get_magnetic_moment()
v = atoms.get_volume()

save(result_file, '2nd calculation \n total energy : {0} eV, {1} eV/atom'.format(p, p / len(atoms)))
save(result_file, 'magnetic moment : {0} mB, {1} mB/atom'.format(m, m / len(atoms)))
save(result_file, 'forces \n {0}'.format(atoms.get_forces()))

#calc.set(isif=2, ibrion=2, nsw=99)
#p = atoms.get_potential_energy()
#m = atoms.get_magnetic_moment()
#v = atoms.get_volume()


save(result_file, '3rd calculation \n total energy : {0} eV, {1} eV/atom'.format(p, p / len(atoms)))
save(result_file, 'magnetic moment : {0} mB, {1} mB/atom'.format(m, m / len(atoms)))
save(result_file, 'forces \n {0}'.format(atoms.get_forces()))

save(result_file, '-------------------------------')

print 'total energy : {0} eV, {1} eV/atom'.format(p, p / len(atoms))


