import numpy as np

def year_loss(args):
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
    
    return year_loss