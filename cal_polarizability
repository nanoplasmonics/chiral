# computing alpha_ee or alpha_em
# set the external field
# use the same direction for the dipole moment

import tidy3d as td
import numpy as np

eps0 = 8.8541878128e-12  # Vacuum permittivity
E_ext=74 # external electric field, 74 in GFP

# Load the downloaded simulation file
sim_data = td.SimulationData.from_file('data/gfp_demo.hdf5')

# Get all E-field components
Ex = sim_data["fieldmonitor_1"].Ex[:,:,:,0]
Ey = sim_data["fieldmonitor_1"].Ey[:,:,:,0]
Ez = sim_data["fieldmonitor_1"].Ez[:,:,:,0]

divE = Ex.differentiate("x") + Ey.differentiate("y") + Ez.differentiate("z")

# Get the coordinates of divE
x_coords = divE.x
y_coords = divE.y
z_coords = divE.z

# Calculate the three components of the dipole moment (px, py, pz)
px_density = x_coords * divE
py_density = y_coords * divE
pz_density = z_coords * divE

px = eps0 * px_density.integrate(coord=['x', 'y', 'z'])
py = eps0 * py_density.integrate(coord=['x', 'y', 'z'])
pz = eps0 * pz_density.integrate(coord=['x', 'y', 'z'])

print(f"Dipole Moment: p_x={px.values}, p_y={py.values}, p_z={pz.values}")

# print(np.abs(px.values) )
alpha = np.abs(px.values) * 1e-18 / E_ext #um to SI

print('numerical result of alpha_ee:', alpha)
