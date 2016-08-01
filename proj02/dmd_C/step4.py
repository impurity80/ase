from step0 import *

id = 4

curr_dir = os.getcwd()
work_dir = 'work-{0}'.format(id)
result_file = '{0}/result/result_{1}.txt'.format(curr_dir,id)

os.system('mkdir {0}'.format(work_dir))
os.system('rm -f {0}'.format(result_file))
save(result_file, atoms.get_positions())

os.chdir(work_dir)

a = 3.5724
atoms.set_cell([a,a,a], scale_atoms=True)

calc = Vasp(istart=0,
            icharg=2,
            xc='PBE',
            kpts=(1, 1, 1),
            encut=700,
            #    setups={'C':'_h'},
            #     ispin=2,
            #     setups={'Ni':'_pv'},
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
v = atoms.get_volume()

save(result_file, '{0} {1}'.format(p, p/len(atoms)))
save(result_file, '{0}'.format(atoms.get_forces()))

print p, p/len(atoms)
print atoms.get_forces()

calc.set(isif=2,ibrion=2, nsw=99)
p = atoms.get_potential_energy()
v = atoms.get_volume()

save(result_file, 'isif=2 \n t energy : {0}, a energy : {1}, volume : {2}'.format(p, p / len(atoms), v))
save(result_file, 'pos \n {0}'.format(atoms.get_positions()))
save(result_file, 'force \n {0}'.format(atoms.get_forces()))

calc.set(isif=4)
p = atoms.get_potential_energy()
v = atoms.get_volume()

save(result_file, 'isif=4 \n t energy : {0}, a energy : {1}, volume : {2}'.format(p, p / len(atoms), v))
save(result_file, 'pos \n {0}'.format(atoms.get_positions()))
save(result_file, 'force \n {0}'.format(atoms.get_forces()))

calc.set(isif=3)
p = atoms.get_potential_energy()
v = atoms.get_volume()

save(result_file, 'isif=3 \n t energy : {0}, a energy : {1}, volume : {2}'.format(p, p / len(atoms), v))
save(result_file, 'pos \n {0}'.format(atoms.get_positions()))
save(result_file, 'force \n {0}'.format(atoms.get_forces()))

print p, p / len(atoms)

save(result_file, '----------------------')

os.chdir('..')

