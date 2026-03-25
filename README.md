# Polarizability Computation Suite

This suite provides an efficient numerical framework for calculating the **electric ($\alpha_{ee}$)** and **electro-magnetic ($\alpha_{em}$)** polarizability of chiral biomolecules (such as GFP) or nanoparticles. The methodology is based on the research paper: *"Electro-magnetic polarizability of chiral biomolecules."*

The tool leverages **Tidy3D**'s high-performance FDTD engine to extract induced dipole moments and derive the polarizability tensors.

---

## 1. Workflow

### Step 1: Geometry Generation (`create_stl.py`)
Convert Protein Data Bank (.pdb) files into a simulation-ready format.
* **Input**: `.pdb` file.
* **Output**: `.stl` mesh file representing the molecular surface.

### Step 2: Tidy3D Simulation Setup
Configure your project in the [Tidy3D Workbench](https://tidy3d.simulation.cloud/workbench?taskId=pa-4cf8fe6f-b353-4e3d-8834-bc98afedc175):

* **Import STL**: Load the generated protein mesh into the simulation domain.
* **Monitor Configuration**: Ensure `fieldmonitor_1` is set to capture the full **3D frequency-domain field distribution** ($E$ and $H$) around the structure.
* **Excitation Strategy**: 
    * Use two **symmetric plane waves** to isolate specific polarizability components.
    * Adjust source settings to maintain required components (e.g., $E_x$ for electric response, $H_y$ for magnetic/chiral response).

### Step 3: Extraction & Analysis (`cal_polarizability.py`)
Download the result (`data.zip` or `.hdf5`) and run the script to compute the final values.

* **Dipole Calculation**: The script computes induced dipole moments ($p_x, p_y, p_z$) by integrating the electric field divergence/polarization across the volume.
* **Polarizability Derivation**:
    * **$\alpha_{ee}$**: Calculated as the ratio $p_x / E_{ext}$.
    * **$\alpha_{em}$**: Calculated as the ratio $p_y / H_{ext}$.
* **Field Verification**: External field values ($E_{ext}, H_{ext}$) can be extracted from the field mornitor.

---

## 2. Mathematical Background

The tool solves for the relationship:

$$p = \alpha_{ee} E_{ext} + \alpha_{em} H_{ext}$$

The dipole moment $p$ is obtained via volume integration of the induced polarization:
$$\mathbf{p} =  \int_{V} (\varepsilon_{0} \nabla \cdot \mathbf{E}(\mathbf{r}) ) \mathbf{r} dV$$

---

## 3. Project Structure

* `create_stl.py`: Utility to process PDB biological data into STL meshes.
* `cal_polarizability.py`: Main post-processing script to parse Tidy3D data and output $\alpha$.
* `data/`: Directory for storing downloaded `data.zip` or simulation results.

---

## 4. Citation
If you utilize this code in your research, please cite:
> *“Electro-magnetic polarizability of chiral biomolecules”*

---

