# hurricane_loss

### Description

Python code to calculate the average annual hurricane loss in Florida and in Gulf states.
The script requires the entry of the following parameters in the specific order:

* Annual hurricane rate in Florida (mean of Poisson distribution) = florida_landfall_rate
* Mean of Florida economic loss (mean of LogNormal distribution) = florida_mean
* Standard deviation of Florida economic loss (standard deviation of LogNormal distribution) = florida_stddev
* Annual hurricane rate in Gulf states (mean of Poisson distribution) = gulf_landfall_rate
* Mean of Gulf states economic loss (mean of LogNormal distribution) = gulf_mean
* Standard deviation of Gulf states economic loss (standard deviation of LogNormal distribution) = gulf_stddev
* Years of simulations (number of MonteCarlo samples) = num_monte_carlo_samples, n [optional, default = 10000]

The code first performs a consistency check, requiring all input parameters to be positive, and the number of simulated years a positive integer.


### Usage

    $ gethurricaneloss [options] florida_landfall_rate florida_mean florida_stddev gulf_landfall_rate gulf_mean gulf_stddev
    $ gethurricaneloss_multicores [options] florida_landfall_rate florida_mean florida_stddev gulf_landfall_rate gulf_mean gulf_stddev
    $ gethurricaneloss_numba [options] florida_landfall_rate florida_mean florida_stddev gulf_landfall_rate gulf_mean gulf_stddev
    
Example

    $ gethurricaneloss 0.5 0.1 0.3 0.4 0.2 0.7 -n 10000000
    $ gethurricaneloss_multicores 0.5 0.1 0.3 0.4 0.2 0.7 -n 10000000
    $ gethurricaneloss_numba 0.5 0.1 0.3 0.4 0.2 0.7 -n 10000000

For help, see also

    $ gethurricaneloss -h
    $ gethurricaneloss_multicores -h
    $ gethurricaneloss_numba -h
    
    
### Performances

The scripts gethurricaneloss_multicores and gethurricaneloss_numba are optimised using the multiprocessing and numba python packages.

Speed test on local machine (8 cores):

with 10^7 Monte Carlo simulations:
* gethurricaneloss: Runtime 22.660911083221436 seconds.
* gethurricaneloss_multicores: Runtime 7.916680812835693 seconds.
* gethurricaneloss_numba: Runtime 1.642557144165039 seconds.

with 10^8 Monte Carlo simulations:
* gethurricaneloss: Runtime 309.77609276771545 seconds.
* gethurricaneloss_multicores: Runtime 171.1051468849182 seconds.
* gethurricaneloss_numba: Runtime 10.642749547958374 seconds.

