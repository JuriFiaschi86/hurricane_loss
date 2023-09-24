#! /usr/bin/python3

import argparse
import random
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



##################
### SIMULATION ###
##################

start = time()

### Initialise losses
total_loss = 0
year_loss = 0
florida_losses = 0
gulf_losses = 0

### Loop over number of simulated years
for n in range(args.num_monte_carlo_samples):

    year_loss = 0
    
    ### Number of hurricare in the year drawn from Poisson distribution with mean "florida_landfall_rate"
    events_per_year_florida = np.random.poisson(args.florida_landfall_rate)
    ### Loop over each hurricane event in the year in Florida
    for i in range(events_per_year_florida):
        ### Random loss following LogNormal distribution with mean "florida_mean" and standard deviation "florida_stddev"
        florida_losses = np.random.lognormal(args.florida_mean, args.florida_stddev)
        ### Add the loss from the hurricane tot the year loss
        year_loss += florida_losses

    ### Number of hurricare in the year drawn from Poisson distribution with mean "gulf_landfall_rate"
    events_per_year_gulf = np.random.poisson(args.gulf_landfall_rate)
    ### Loop over each hurricane event in the year in Gulf states
    for i in range(events_per_year_gulf):
        ### Random loss following LogNormal distribution with mean "gulf_mean" and standard deviation "gulf_stddev"
        gulf_losses = np.random.lognormal(args.gulf_mean, args.gulf_stddev)
        ### Add the loss from the hurricane tot the year loss
        year_loss += gulf_losses
    

    ### Add year loss to total loss
    total_loss += year_loss


### Calculate the average loss over the simulated years
mean_loss = total_loss / args.num_monte_carlo_samples


##############
### OUTPUT ###
##############

### Print the result
print(f"Mean annual loss: ${mean_loss:.2f} Billion")

end = time()
print(f"Computed in {(end - start)} seconds.")