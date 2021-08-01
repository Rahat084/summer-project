import numpy as np
from math import pi as PI
""" This script calculates the required simulation cell sizes for given spherical particle size and volume fraction"""
def cell_size(max_cell_size=50,
        radius_range=[5,75],
        radius_inc=1,
        vfrac_range=[0.5,5],
        vfrac_inc=0.5):

    params=np.empty((1,3))
    # calculate and store cell sizes for radius and volume fraction
    # in the range
    for radius in range(radius_range[0],radius_range[1],radius_inc):
        for vfrac in np.arange(vfrac_range[0],vfrac_range[1],vfrac_inc):
            cell_size= ((100/vfrac)*(4/3)*PI*(radius)**3)**(1/3)
            if cell_size< max_cell_size:
                params=np.append(params,[[radius,vfrac,cell_size]],axis=0)

    params=params[1:,:] # Remove the empty row
    return params

if __name__=="__main__":
    params=cell_size(radius_range=[2,75],max_cell_size=50)
    print(params)
    np.savetxt("parameters.txt",params,fmt="%10.2f")

