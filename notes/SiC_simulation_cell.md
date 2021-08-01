# Calculation for the Simulation cell in Al-SiC nano-composite
## particle_radius, specific_surface, volume_fraction, mass_fraction
## Range of particle radius(r) ------> 5 nm - 75 nm
## Range of volume fraction(v_frac) ------> 0.5% - 4.5%
## calculate cell size

volume_SiC= 4/3*pi*r**3
volume_AlSiC= (100/v_frac)*volume_SiC
Cell_size = cubic_root(volume_AlSiC)
