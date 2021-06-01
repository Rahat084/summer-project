#! /bin/bash
# create metal supercell
atomsk --create fcc 4.046 Al orient [100] [010] [001] -duplicate 25 25 25 fccAl_matrix.cfg
# create hollow of radius (CNT radius+ Catom radius)
atomsk fccAl_matrix.cfg  -select in sphere 0.5*box 0.5*box 0.5*box 10.1 -rmatom select hollow.cfg
# Create SiC nanoparticle
atomsk --create zb 4.3595 Si C \
-duplicate 5 5 5 \
-select out sphere 0.5*box 0.5*box 0.5*box 10 \
-remove-atoms select \
-shift 39.67625 39.67625 39.67625 SiC_sphere.cfg
# merge the hollow matrix and CNT
atomsk --merge 2 hollow.cfg SiC_sphere.cfg AlSiC.cfg
# create the lammps data file
#atomsk 0.5%cnt.cfg lammps

