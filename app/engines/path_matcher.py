import numpy as np
from typing import List
from app.models.profile import UserProfile, SevenDimensions
from app.models.results import PathProbability

PATH_DEFS = [
    ("tech", "深耕专家型", "在已有领域持续深耕，成为技术权威"),
    ("freelance", "副业探索型", "在保持主业的同时探索多元可能性"),
    ("business", "资源变现型", "将积累的资源转化为商业价值"),
    ("family", "生活方式型", "以生活品质和家庭为优先"),
    ("explorer", "激进跃迁型", "高风险高回报的人生跃迁"),
    ("art", "修复蓄力型", "先疗愈再出发，积蓄能量"),
    ("academia", "蓝海捕手型", "探索新领域，寻找蓝海机会"),
    ("public", "社群共创型", "通过协作和共创实现价值"),
]

def match_paths(profile: UserProfile, dimensions: SevenDimensions) -> List[PathProbability]:
    scores = []
    
    # Tech: high career + stable
    scores.append(("tech", dimensions.career * 0.7 + profile.job_tenure * 30))
    
    # Freelance: income diversity + cross-domain
    scores.append(("freelance", profile.income_channel * 50 + profile.cross_domain_exposure * 50))
    
    # Business: financial buffer + mobility
    scores.append(("business", profile.financial_buffer * 50 + profile.career_mobility * 50))
    
    # Family: health + low work hours
    scores.append(("family", dimensions.health * 0.7 + (1 - profile.work_hours) * 30))
    
    # Explorer: high mobility + risk tolerance
    scores.append(("explorer", profile.career_mobility * 50 + profile.sacrifice_tolerance * 50))
    
    # Art: high ACE10 + trauma
    scores.append(("art", max(0, 100 - profile.ace10_score * 10) * 0.3 + profile.trauma_profile * 70))
    
    # Academia: vision + openness
    scores.append(("academia", profile.possibility_vision * 50 + profile.cross_domain_exposure * 50))
    
    # Public: impact + giving
    scores.append(("public", dimensions.impact * 0.7 + profile.generative_giving * 30))
    
    # Softmax
    exp_scores = [np.exp(s[1] / 20) for s in scores]
    total = sum(exp_scores)
    probs = [e / total for e in exp_scores]
    
    results = []
    for i, (pt, title, desc) in enumerate(PATH_DEFS):
        results.append(PathProbability(
            path_type=pt,
            probability=probs[i],
            title=title,
            description=desc
        ))
    
    return sorted(results, key=lambda x: x.probability, reverse=True)
