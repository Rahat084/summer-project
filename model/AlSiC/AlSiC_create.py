#!/usr/bin/env python

"""
This is a python script to automate a series of comman line program
Author: Md S Hasan"""

import os
import shutil

ALAT= 4.046 # Lattice distance of matrix
SLAT= 4.3595 # Lattice distance of Silicon carbide
xa,ya,za=25,25,25
# Load the AlSiC_atomsk_template file as a template.
with open("AlSiC_atomsk_template") as f:
    template = f.read()

# Set default values for various parameters
rss = [10.0] # radiuses of SiC particle in Angstrom
#n_particle=[0,25,50,100] #

# Loop through a series of values of grain size and percent H
for rs in rss:
    jobname=f"AlSiC_dia_{rs}"
    scell=int(rs/2)
    xshift=0.5*xa*ALAT-0.5*SLAT*scell
    yshift=0.5*ya*ALAT-0.5*SLAT*scell
    zshift=0.5*ya*ALAT-0.5*SLAT*scell

    inputfile= f"{jobname}_atomsk.sh"
    # by the specified values.
    s= template.format(ALAT=ALAT,xa=xa,ya=ya,za=za,rs=rs,SLAT=SLAT,
            scell=scell,xshift=xshift,yshift=yshift,zshift=zshift,jobname=jobname)

    # Write the actual input file for atomsk
    with open(inputfile, "w") as f:
        f.write(s)

    #Print some status messages.
    print(f"Creating AlSiC with SiC dia = {rs} .....")
    # Run atomsk script accordingly if needed.
    os.system(f"bash < {inputfile}")

    print("{0} is created".format( jobname))

# This just does cleanup. For this lab, we don't need the files that are
# dumped into the tmp directory.
#shutil.rmtree("tmp")
