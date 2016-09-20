from step0 import *

atoms = read('work-init/CONTCAR')

id = 2

curr_dir = os.getcwd()
work_dir = 'work-{0}'.format(id)
result_file = '{0}/result/result_{1}.txt'.format(curr_dir, id)

os.system('mkdir {0}'.format(work_dir))
os.system('rm -f {0}'.format(result_file))
save(result_file, atoms.get_positions())

os.chdir(work_dir)

calc = Vasp(istart=0,
            icharg=2,
            xc='PBE',
            ibrion=-1,
            encut=540,
            ispin = 2,
            ediff = 1.0e-8,
            ismear = 1,
            sigma = 0.1,
            ialgo = 38,
            lreal = 'False',
            lwave=False,
            lcharg=False,
            nelm=100,
            kpts=[8,8,8]
            )

atoms.set_calculator(calc)
p = atoms.get_potential_energy()

save(result_file, '-----------------------------------')