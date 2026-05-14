import random
from typing import List
from app.models.profile import UserProfile, SevenDimensions
from app.models.results import PathProbability, CelestialBody
from .optionality_index import calculate_oi

def classify_bodies(profile: UserProfile, dimensions: SevenDimensions, paths: List[PathProbability]) -> List[CelestialBody]:
    oi = calculate_oi(profile)
    bodies = []
    body_id = 0
    
    # Count per path type
    path_counts = {}
    total_prob = sum(p.probability for p in paths)
    
    for p in paths:
        count = max(3, int(50 * p.probability / total_prob))
        path_counts[p.path_type] = count
    
    for path_type, count in path_counts.items():
        for _ in range(count):
            x = random.uniform(0, 6000)
            y = random.uniform(0, 4000)
            radius = random.uniform(3, 15)
            
            # Determine body kind based on profile
            if profile.ace10_score >= 6 and profile.trauma_profile > 0.7:
                kind = "blackhole"
                color = [255, 107, 53]
            elif oi >= 0.8 and profile.career_mobility >= 0.8:
                kind = "supernova"
                color = [255, 215, 0]
            elif dimensions.career >= 75 and profile.value_stability >= 0.6:
                kind = "star"
                color = [93, 173, 226]
            elif dimensions.wealth >= 65 and profile.financial_buffer >= 0.6:
                kind = "planet"
                color = [123, 109, 141]
            elif dimensions.health >= 70 and profile.work_rhythm >= 0.5:
                kind = "pulsar"
                color = [0, 206, 209]
            elif profile.transition_readiness >= 0.7 and profile.risk_appetite >= 0.6:
                kind = "meteor"
                color = [212, 165, 116]
            else:
                kind = "nebula"
                color = [155, 89, 182]
            
            bodies.append(CelestialBody(
                id=body_id,
                x=x, y=y, radius=radius,
                kind=kind, color=color,
                path_type=path_type,
                probability=random.random(),
                title=f"{kind.capitalize()} {body_id}",
                philosophy=f"Body of {path_type}"
            ))
            body_id += 1
    
    return bodies
