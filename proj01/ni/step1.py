from step0 import *

from ase.dft import DOS
from ase.dft import get_distribution_moment
from ase.calculators.vasp import VaspDos

id = 4

curr_dir = os.getcwd()
work_dir = 'work-{0}'.format(id)
result_file = '{0}/result/result_{1}.txt'.format(curr_dir,id)

os.system('mkdir {0}'.format(work_dir))
os.system('rm -f {0}'.format(result_file))
save(result_file, atoms.get_positions())

os.chdir(work_dir)


a = 3.5209

atoms.set_cell([a,a,a], scale_atoms=True)

calc = Vasp(istart = 0,
            icharg = 2,
            xc = 'PBE',
            kpts = (1,1,1),
            encut = 720,
            ispin = 2,
            setups = {'Ni':'_pv', 'Cr':'_pv'},
            ismear = 1,
            sigma = 0.1,
            prec='Accurate',
            ediff=0.00025,
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
m = atoms.get_magnetic_moment()

save(result_file, '2nd calculation \n total energy : {0} eV, {1} eV/atom'.format(p, p/len(atoms)))
save(result_file, 'magnetic moment : {0} mB, {1} mB/atom'.format(m, m/len(atoms)))
save(result_file, 'forces \n {0}'.format(atoms.get_forces()))

calc.set(isif=2,ibrion=2, nsw=99)
p = atoms.get_potential_energy()
m = atoms.get_magnetic_moment()
v = atoms.get_volume()

save(result_file, '3rd calculation \n total energy : {0} eV, {1} eV/atom'.format(p, p/len(atoms)))
save(result_file, 'magnetic moment : {0} mB, {1} mB/atom'.format(m, m/len(atoms)))
save(result_file, 'forces \n {0}'.format(atoms.get_forces()))

calc.set(ismear=-5, lorbit=11, nedos=3001)
p = atoms.get_potential_energy()
save(result_file, '4th calculation \n total energy : {0} eV, {1} eV/atom'.format(p, p/len(atoms)))

tm = atoms.get_magnetic_moment()
m = atoms.get_magnetic_moments()
save(result_file, 'total magnetic moment : {0} mB {1} mB/atom '.format(tm, tm/len(atoms)))
save(result_file, 'magnetic moment: {0}'.format(m))


vdos = VaspDos()
vdos.read_doscar('DOSCAR')
print vdos.efermi
print vdos.site_dos(0,0)


dos = DOS(calc, width=0.05)

d = dos.get_dos()
up = dos.get_dos(0)
down = dos.get_dos(1)

e = dos.get_energies()

plt.plot(e,d, label='total')
plt.plot(e,up, label='spin-up')
plt.plot(e,-1.0*down, label='spin-down')

plt.grid(True)
plt.xlim(-20, 20)
plt.ylim(-10, 10)
plt.legend()
plt.xlabel('E-Ef')
plt.ylabel('DOS')
plt.savefig('{0}/result/dos_{1}.png'.format(curr_dir, id))
plt.show('{0}/result/dos_{1}.png'.format(curr_dir, id))

save(result_file, '-------------------------------')

print 'total energy : {0} eV, {1} eV/atom'.format(p, p/len(atoms))



