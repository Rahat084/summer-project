#! /bin/bash .
# create metal supercell
atomsk --create fcc 4.046 Al orient [100] [010] [001] -duplicate 66 66 25 fccAl_matrix.cfg
# create hollow of radius (CNT radius+ Catom radius)
atomsk fccAl_matrix.cfg  -select in cylinder Z 0.5*box 0.5*box 5.768 -cut above -1 Z hollow.cfg
# Create CNT of calulated number of chain(n)
atomsk --create nanotube 2.46 6 6 C -shift 133.518 133.518 0 -duplicate 1 1 41 CNT.cfg
# merge the hollow matrix and CNT
atomsk --merge 2 hollow.cfg CNT.cfg 0.5%cnt.cfg
# create the lammps data file
atomsk 0.5%cnt.cfg lammps

