#! /usr/bin/python3

import argparse
import random
import numpy as np
from time import time
import multiprocessing
from simulation import year_loss  


#############
### INPUT ###
#############

### Input from parsing
### -h for help and description
parser = argparse.ArgumentParser(description="Python code to calculate the average annual hurricane loss in Florida and in Gulf states. The script is optimised for multi-core processing.")
parser.add_argument("florida_landfall_rate", type=float, help="Annual hurricane rate in Florida (Poisson)")
parser.add_argument("florida_mean", type=float, help="Mean of Florida economic loss (LogNormal)")
parser.add_argument("florida_stddev", type=float, help="Standard deviation of Florida economic loss (LogNormal)")
parser.add_argument("gulf_landfall_rate", type=float, help="Annual hurricane rate in Gulf states (Poisson)")
parser.add_argument("gulf_mean", type=float, help="Mean of Gulf states economic loss (LogNormal)")
parser.add_argument("gulf_stddev", type=float, help="Standard deviation of Gulf states economic loss (LogNormal)")
parser.add_argument("-n", "--num_monte_carlo_samples", type=int, default=10000, help="Years of simulations (number of MonteCarlo samples)")

args = parser.parse_args()


### Check input consistency ###
if (args.florida_landfall_rate < 0):
    print("florida_landfall_rate must be >= 0. Exit.")
    exit()
if (args.florida_mean < 0):
    print("florida_mean must be >= 0. Exit.")
    exit()
if (args.florida_stddev < 0):
    print("florida_stddev must be >= 0. Exit.")
    exit()
if (args.gulf_landfall_rate < 0):
    print("gulf_landfall_rate must be >= 0. Exit.")
    exit()
if (args.gulf_mean < 0):
    print("gulf_mean must be >= 0. Exit.")
    exit()
if (args.gulf_stddev < 0):
    print("gulf_stddev must be >= 0. Exit.")
    exit()
if (args.num_monte_carlo_samples <= 0):
    print("florida_landfall_rate must be an integer > 0. Exit.")
    exit()


##################
### SIMULATION ###
##################

start = time()

### MULTIPROCESSING OPTIONS ###
cores = multiprocessing.cpu_count()
pool = multiprocessing.Pool(cores)

### Distribute pool over processor cores
results = pool.map(year_loss, [args] * args.num_monte_carlo_samples)
### Sum and average the simulated year losses
total_loss = sum(results)
mean_loss = total_loss / args.num_monte_carlo_samples

# Close and join the pool
pool.close()
pool.join()


#############
## OUTPUT ###
#############

### Print the result
print(f"Mean annual loss: ${mean_loss:.2f} Billion")

end = time()
print(f"Computed in {(end - start)} seconds.")