import numpy as np

def year_loss(args):
    year_loss = 0
    
    ### Number of hurricare in the year drawn from Poisson distribution with mean "florida_landfall_rate"
    events_per_year_florida = np.random.poisson(args.florida_landfall_rate)
    ### Vectorise and sum random loss for each hurricane events in Florida in simulated year
    year_loss += np.random.lognormal(args.florida_mean, args.florida_stddev, events_per_year_florida).sum()

    ### Number of hurricare in the year drawn from Poisson distribution with mean "gulf_landfall_rate"
    events_per_year_gulf = np.random.poisson(args.gulf_landfall_rate)
    ### Vectorise and sum random loss for each hurricane events in Gulf states in simulated year
    year_loss += np.random.lognormal(args.gulf_mean, args.gulf_stddev, events_per_year_gulf).sum()

    return year_loss