import numpy as np
from Bio.PDB import PDBParser
import trimesh
import os  # Added: for handling file paths

# -----------------------------
# 1. Read PDB File
# -----------------------------
pdb_file = "demo.pdb"  # Change to your PDB file path
parser = PDBParser(QUIET=True)
structure = parser.get_structure("protein", pdb_file)
base_name = os.path.splitext(os.path.basename(pdb_file))[0]
atom_coords = []

for atom in structure.get_atoms():
    # Get atomic coordinates
    pos = atom.get_coord()  # Returns [x, y, z] as a numpy array
    atom_coords.append(pos)

atom_coords = np.array(atom_coords)
print(f"Read {len(atom_coords)} atom coordinates")

# -----------------------------
# 2. Generate Sphere STL
# -----------------------------
sphere_radius = 2  # Radius 2 Å 
sphere_mesh = trimesh.creation.icosphere(subdivisions=2, radius=sphere_radius)

all_meshes = []

for coord in atom_coords:
    # Translate sphere to atom coordinates
    mesh_copy = sphere_mesh.copy()
    mesh_copy.apply_translation(coord)
    all_meshes.append(mesh_copy)

# Merge all spheres
combined = trimesh.util.concatenate(all_meshes)

# # -----------------------------
# # 3. Export STL File
# # -----------------------------
# output_file = "protein_atoms.stl"
# combined.export(output_file)
# print(f"STL file generated: {output_file}")

# -----------------------------
# 3. Export STL File (Dynamic Naming)
# -----------------------------
# Prepend base_name to the default filename
output_file = f"{base_name}_protein_atoms.stl"

combined.export(output_file)
print(f"STL file generated: {output_file}")
