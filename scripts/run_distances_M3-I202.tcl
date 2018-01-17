#run_distances_M3-I202.tcl

#Run with VMD: $VMD -dispdev text -e run_distances_M3-I202.tcl -args path/to/trajectory

#Loads the molecule
mol new [lindex $argv 0] waitfor all

#Sources the script for calculating distances
source distance.tcl

#Calculating the distances

#I202-V242

distance "chain A and resid 202 and name CA" "chain A and resid 242 and name CA" 10 I202-V242_distance_chainA.dat I202-V242_distribution_chainA.dat

distance "chain C and resid 202 and name CA" "chain C and resid 242 and name CA" 10 I202-V242_distance_chainC.dat I202-V242_distribution_chainC.dat

distance "chain E and resid 202 and name CA" "chain E and resid 242 and name CA" 10 I202-V242_distance_chainE.dat I202-V242_distribution_chainE.dat

distance "chain G and resid 202 and name CA" "chain G and resid 242 and name CA" 10 I202-V242_distance_chainG.dat I202-V242_distribution_chainG.dat

distance "chain I and resid 202 and name CA" "chain I and resid 242 and name CA" 10 I202-V242_distance_chainI.dat I202-V242_distribution_chainI.dat

#M205-I258

distance "chain A and resid 205 and name CA" "chain A and resid 258 and name CA" 10 M205-I258_distance_chainA.dat M205-I258_distribution_chainA.dat

distance "chain G and resid 205 and name CA" "chain G and resid 258 and name CA" 10 M205-I258_distance_chainG.dat M205-I258_distribution_chainG.dat

distance "chain C and resid 205 and name CA" "chain C and resid 258 and name CA" 10 M205-I258_distance_chainC.dat M205-I258_distribution_chainC.dat

distance "chain I and resid 205 and name CA" "chain I and resid 258 and name CA" 10 M205-I258_distance_chainI.dat M205-I258_distribution_chainI.dat

distance "chain E and resid 205 and name CA" "chain E and resid 258 and name CA" 10 M205-I258_distance_chainE.dat M205-I258_distribution_chainE.dat


#Exit VMD
exit