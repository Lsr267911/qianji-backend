import numpy as np
from typing import Dict
from app.models.profile import UserProfile, SevenDimensions

def run_monte_carlo(profile: UserProfile, dimensions: SevenDimensions, n_samples: int = 1000) -> Dict:
    """
    Metropolis-Hastings MCMC sampling for future path probability distribution.
    """
    current = np.array([
        dimensions.career, dimensions.relationship, dimensions.wealth,
        dimensions.health, dimensions.self_realization, dimensions.creativity, dimensions.impact
    ])
    
    # Prior: based on current dimensions with some uncertainty
    prior_mean = current
    prior_std = np.array([10, 10, 10, 10, 10, 10, 10])
    
    # Proposal distribution: random walk
    proposal_std = 8
    
    samples = []
    n_burnin = 200
    
    for i in range(n_samples + n_burnin):
        # Proposal
        proposal = current + np.random.normal(0, proposal_std, 7)
        proposal = np.clip(proposal, 0, 100)
        
        # Acceptance probability (Gaussian prior)
        log_p_current = -0.5 * np.sum(((current - prior_mean) / prior_std) ** 2)
        log_p_proposal = -0.5 * np.sum(((proposal - prior_mean) / prior_std) ** 2)
        
        log_alpha = log_p_proposal - log_p_current
        alpha = np.exp(min(0, log_alpha))
        
        if np.random.random() < alpha:
            current = proposal
        
        if i >= n_burnin:
            samples.append(current.copy())
    
    samples = np.array(samples)
    
    # Calculate statistics
    optimistic = np.percentile(samples, 75, axis=0).tolist()
    baseline = np.percentile(samples, 50, axis=0).tolist()
    conservative = np.percentile(samples, 25, axis=0).tolist()
    
    return {
        "optimistic": {
            "career": optimistic[0], "relationship": optimistic[1],
            "wealth": optimistic[2], "health": optimistic[3],
            "self_realization": optimistic[4], "creativity": optimistic[5],
            "impact": optimistic[6]
        },
        "baseline": {
            "career": baseline[0], "relationship": baseline[1],
            "wealth": baseline[2], "health": baseline[3],
            "self_realization": baseline[4], "creativity": baseline[5],
            "impact": baseline[6]
        },
        "conservative": {
            "career": conservative[0], "relationship": conservative[1],
            "wealth": conservative[2], "health": conservative[3],
            "self_realization": conservative[4], "creativity": conservative[5],
            "impact": conservative[6]
        }
    }
