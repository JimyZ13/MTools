# MTools
Computational Tools for Materials Calculation with DFT and QE

## Folder Structure:
### - Plots: python scripts for plotting single functions, multiple functions, and band structures from string output
  - /one.py: given a string input, plot the data on a graph
  - /multiple.py: given a string output with each set separated by \n, plot data independently
  - /bands.py: given a string input, plot the band structure, can also plot verticle lines of high symmetry
### - PyMatGen: utilities associated with Materials Libary, Slab Generation, etc
  - /Materials_Api.py: getting, forming, saving, and altering structures using pymatgen and materials library; search by, download, and change structures by id.
### - Transform: utilities associated with transforming structures by hand
  - /add.py: add a constant vector to all atomic positions in a given lattice cell, works with both direct(fractional) and cartesian coordinates.
  - /cut.py: Given a string of atomic positions and three ranges in cartesian format (x, y, z), select atoms within the given constraint
  - /fract_to_cart.py: given a fraction coordinate set as a string, and three lattice vectors, convert to cartesian coordinates
  - /min_max.py: find the min and max of a structure in direct coordinate space
  - /transform.py: rotate an structure along any defined vector by any degrees, atomic coordinates must be in fractional, the result is the transformed lattice vectors
### - Bash: bash scripts for convergence in k-point, ecutoff in QE
  - /run_submit.sh: run the submit.pw script iteratively and on each iteration increase the ecutoff by 1
  - /run.sh: reset the submit.pw script by copying the original and replacing the current copy
  - /submit.pw: standard submit script for CARC clusters 
