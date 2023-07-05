from gettext import npgettext
import numpy as np
from pymatgen.core import Lattice, Structure, Molecule, PeriodicSite, Site
from pymatgen.core.surface import SlabGenerator, generate_all_slabs
from pymatgen.analysis.local_env import CrystalNN
from pymatgen.ext.matproj import MPRester

lattice = Lattice.from_parameters(a=3.84, b=3.84, c=3.84, alpha=120,
                                  beta=90, gamma=60)

coords = coords = [[0, 0, 0], [0.75,0.5,0.75]]

bulk_structure = Structure(lattice, ["Si", "Si"], coords)


bulk_structure.to(filename="Si2.cif")

slab = SlabGenerator(bulk_structure, (1, 1, 1), 10, 10)
slabs = slab.get_slabs()

slabs[0].to(filename="Si2_slab.cif")

with MPRester("gb9x0HQBvwxb1OZzyaJZ0gQeZUUNguYN") as m:
    
    structure = m.get_structure_by_material_id("mp-20351")
    hydrogen = m.get_structure_by_material_id("mp-24504")

    structure.to(filename="InP_20351.cif")
    print (structure)

structure = Structure.from_file("In1 P1.vasp")

slab = SlabGenerator(structure, (1, 1, 1), 10, 10, center_slab=True, reorient_lattice=True)
slabs = slab.get_slab()
slabs.to(filename="InP_20351_slab111.cif")


surface_sites = slabs.get_surface_sites()
print(surface_sites)

for site in surface_sites["top"]:
    print(site)
    c = site[0].coords + (0.1 * site[0].coords)
    print(structure.get_sites_in_sphere(site[0].coords, 2))
    slabs.append("H", c, coords_are_cartesian=True, validate_proximity=True)


for site in surface_sites["bottom"]:
    c = site[0].coords - (0.1 * site[0].coords)
    slabs.append("H", c, coords_are_cartesian=True, validate_proximity=True)
# Get the minimum and maximum fractional coordinates along each direction
min_frac_coords = slabs.frac_coords.min(axis=0)
max_frac_coords = slabs.frac_coords.max(axis=0)


slabs.to(filename="InP_20351_slab111_H.cif")


slab = SlabGenerator(structure, (0,0,1), 10, 10)
slabs = slab.get_slabs()
slabs[0].to(filename="InP_20351_slab001.cif")

slab = SlabGenerator(structure, (1, 1, 0), 10, 10)
slabs = slab.get_slabs()
slabs[0].to(filename="InP_20351_slab110.cif")



