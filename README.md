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

    $ gethurricaneloss.py [options] florida_landfall_rate florida_mean florida_stddev gulf_landfall_rate gulf_mean gulf_stddev
    $ gethurricaneloss_multicores.py [options] florida_landfall_rate florida_mean florida_stddev gulf_landfall_rate gulf_mean gulf_stddev
    $ gethurricaneloss_numba.py [options] florida_landfall_rate florida_mean florida_stddev gulf_landfall_rate gulf_mean gulf_stddev
    
Example

    $ gethurricaneloss.py 3 5 2 2 3 1 -n 100000
    $ gethurricaneloss_multicores.py 3 5 2 2 3 1 -n 100000
    $ gethurricaneloss_numba.py 3 5 2 2 3 1 -n 100000

For help, see also

    $ gethurricaneloss.py -h
    $ gethurricaneloss_multicores.py -h
    $ gethurricaneloss_numba.py -h
    
### Test
A pytest script is provided, checking the behaviour of the code for valid and invalid input parameters (9 test on each of the the 3 scripts: 27 tests total)

    $ pytest pytest_gethurricaneloss.py


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
* gethurricaneloss: Runtime 0.008306026458740234 seconds.
* gethurricaneloss_multicores: Runtime 0.04959893226623535 seconds.
* gethurricaneloss_numba: Runtime 1.0626742839813232 seconds.

with 10^5 Monte Carlo simulations:
* gethurricaneloss: Runtime 0.02667689323425293 seconds.
* gethurricaneloss_multicores: Runtime 0.2878227233886719 seconds.
* gethurricaneloss_numba: Runtime 1.0819246768951416 seconds.

with 10^6 Monte Carlo simulations:
* gethurricaneloss: Runtime 0.24503302574157715 seconds.
* gethurricaneloss_multicores: Runtime 2.8667149543762207 seconds.
* gethurricaneloss_numba: Runtime 1.3535361289978027 seconds.

with 10^7 Monte Carlo simulations:
* gethurricaneloss: Runtime 2.4415886402130127 seconds.
* gethurricaneloss_multicores: Runtime 58.561392307281494 seconds.
* gethurricaneloss_numba: Runtime 4.1608922481536865 seconds.

with 10^8 Monte Carlo simulations:
* gethurricaneloss: Runtime 41.176252365112305 seconds.
* gethurricaneloss_multicores: Runtime --- seconds.
* gethurricaneloss_numba: Runtime 37.619906187057495 seconds.

