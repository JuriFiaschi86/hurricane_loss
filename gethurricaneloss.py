#! /usr/bin/python3

import argparse
import numpy as np
from time import time

#############
### INPUT ###
#############

### Input from parsing
### -h for help and description
parser = argparse.ArgumentParser(description="Python code to calculate the average annual hurricane loss in Florida and in Gulf states.")
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

### Vectorise hurricane events in Florida in simulated years
events_florida = np.random.poisson(args.florida_landfall_rate, args.num_monte_carlo_samples)
### Vectorise and sum random loss for each hurricane events in Florida in simulated years
florida_losses = np.random.lognormal(args.florida_mean, args.florida_stddev, events_florida.sum()).sum()

### Vectorise hurricane events in Gulf state in simulated years
events_gulf = np.random.poisson(args.gulf_landfall_rate, args.num_monte_carlo_samples)
### Vectorise and sum random loss for each hurricane events in Gulf states in simulated years
gulf_losses = np.random.lognormal(args.gulf_mean, args.gulf_stddev, events_gulf.sum()).sum()

### Mean loss over simulated years
mean_loss = (florida_losses + gulf_losses) / args.num_monte_carlo_samples

end = time()


##############
### OUTPUT ###
##############

### Print the result
print(f"Mean annual loss: $ {mean_loss:.5f} Billions")
print(f"Computed in {(end - start)} seconds.")

#################
### SAVE DATA ###
#################

import json
import os

current_dir = os.getcwd() + "/"

log_data = {
    "florida_landfall_rate": args.florida_landfall_rate,
    "florida_mean": args.florida_mean,
    "florida_stddev": args.florida_stddev,
    "gulf_landfall_rate": args.gulf_landfall_rate,
    "gulf_mean": args.gulf_mean,
    "gulf_stddev": args.gulf_stddev,
    "num_monte_carlo_samples": args.num_monte_carlo_samples,
    "mean_loss": mean_loss,
    "runtime": (end - start)
}

### Save always to a new file
n = 0
log_file = current_dir + "run_numpy_" + str(n) + ".json"
while (os.path.exists(log_file)):
    n+=1
    log_file = current_dir + "run_numpy_" + str(n) + ".json"
### Saving in JSON format
with open(log_file, "w") as file_object:
    json.dump(log_data, file_object)
