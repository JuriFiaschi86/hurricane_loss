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
Speed test on local machine (Intel® Core™ i7-8565U CPU @ 1.80GHz × 8):

Benchmark point parameters:
"florida_landfall_rate": 3,
"florida_mean": 5,
"florida_stddev": 2,
"gulf_landfall_rate": 2,
"gulf_mean": 3,
"gulf_stddev": 1

with 10^4 Monte Carlo simulations:
* gethurricaneloss: Runtime 0.050960540771484375 seconds.
* gethurricaneloss_multicores: Runtime 0.03963303565979004 seconds.
* gethurricaneloss_numba: Runtime 0.9022736549377441 seconds.

with 10^5 Monte Carlo simulations:
* gethurricaneloss: Runtime 0.490692138671875 seconds.
* gethurricaneloss_multicores: Runtime 0.18401741981506348 seconds.
* gethurricaneloss_numba: Runtime 0.6957817077636719 seconds.

with 10^6 Monte Carlo simulations:
* gethurricaneloss: Runtime 5.221672058105469 seconds.
* gethurricaneloss_multicores: Runtime 1.699613332748413 seconds.
* gethurricaneloss_numba: Runtime 0.9563498497009277 seconds.

with 10^7 Monte Carlo simulations:
* gethurricaneloss: Runtime 50.14009714126587 seconds.
* gethurricaneloss_multicores: Runtime 30.176668882369995 seconds.
* gethurricaneloss_numba: Runtime 3.4051709175109863 seconds.

with 10^8 Monte Carlo simulations:
* gethurricaneloss: Runtime 726.0821187496185 seconds.
* gethurricaneloss_multicores: Runtime 355.67957615852356 seconds.
* gethurricaneloss_numba: Runtime 34.81420302391052 seconds.
