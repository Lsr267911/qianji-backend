import numpy as np
from typing import List
from app.models.profile import UserProfile
from app.models.results import HistoricalAnalogue

HISTORICAL_FIGURES = [
    {"name": "爱因斯坦", "era": "20世纪", "domain": "物理学", "vector": [0.9, 0.3, 0.4, 0.5, 0.95, 1.0, 0.8]},
    {"name": "居里夫人", "era": "20世纪", "domain": "化学/物理", "vector": [0.95, 0.4, 0.5, 0.4, 0.9, 0.9, 0.85]},
    {"name": "乔布斯", "era": "20-21世纪", "domain": "科技/商业", "vector": [0.8, 0.3, 0.9, 0.4, 0.85, 0.95, 0.9]},
    {"name": "马云", "era": "21世纪", "domain": "商业", "vector": [0.7, 0.8, 0.95, 0.5, 0.8, 0.9, 0.85]},
    {"name": "任正非", "era": "21世纪", "domain": "科技/商业", "vector": [0.95, 0.5, 0.8, 0.6, 0.75, 0.7, 0.8]},
    {"name": "马斯克", "era": "21世纪", "domain": "科技/商业", "vector": [0.85, 0.3, 0.95, 0.4, 0.9, 1.0, 0.95]},
    {"name": "梵高", "era": "19世纪", "domain": "艺术", "vector": [0.3, 0.2, 0.2, 0.3, 0.95, 1.0, 0.7]},
    {"name": "贝多芬", "era": "18-19世纪", "domain": "音乐", "vector": [0.4, 0.3, 0.3, 0.2, 0.9, 1.0, 0.75]},
    {"name": "苏格拉底", "era": "古希腊", "domain": "哲学", "vector": [0.5, 0.8, 0.2, 0.5, 1.0, 0.9, 0.95]},
    {"name": "孔子", "era": "春秋", "domain": "哲学/教育", "vector": [0.6, 0.9, 0.3, 0.6, 0.85, 0.6, 1.0]},
    {"name": "甘地", "era": "20世纪", "domain": "社会运动", "vector": [0.5, 0.9, 0.2, 0.5, 1.0, 0.7, 1.0]},
    {"name": "曼德拉", "era": "20世纪", "domain": "政治", "vector": [0.7, 0.8, 0.3, 0.5, 0.95, 0.6, 1.0]},
    {"name": "达芬奇", "era": "文艺复兴", "domain": "艺术/科学", "vector": [0.8, 0.4, 0.6, 0.5, 0.95, 1.0, 0.85]},
    {"name": "牛顿", "era": "17世纪", "domain": "物理学/数学", "vector": [0.95, 0.2, 0.5, 0.5, 1.0, 0.95, 0.9]},
    {"name": "图灵", "era": "20世纪", "domain": "计算机科学", "vector": [0.95, 0.2, 0.4, 0.4, 1.0, 1.0, 0.85]},
]

def historical_phase_calibration(profile: UserProfile) -> List[HistoricalAnalogue]:
    # Create user feature vector (7 dimensions)
    user_vector = np.array([
        profile.education,
        profile.family_structure,
        profile.financial_buffer,
        profile.health_asset,
        profile.self_realization / 100,
        profile.creativity / 100,
        profile.impact / 100
    ])
    
    similarities = []
    for fig in HISTORICAL_FIGURES:
        fig_vector = np.array(fig["vector"])
        similarity = np.dot(user_vector, fig_vector) / (np.linalg.norm(user_vector) * np.linalg.norm(fig_vector))
        similarities.append((fig, float(similarity)))
cat > app/engines/hedge_engine.py << 'EOF'
import numpy as np
from typing import List
from app.models.profile import UserProfile
from app.models.results import PathProbability, HedgePortfolio

def hedge_engine(paths: List[PathProbability], profile: UserProfile) -> HedgePortfolio:
    """
    Modern Portfolio Theory applied to life paths.
    """
    n = len(paths)
    if n == 0:
        return HedgePortfolio(
            primary_allocation={},
            secondary_allocation={},
            risk_level=0.5,
            expected_return=50.0
        )
    
    # Returns = path probabilities
    returns = np.array([p.probability for p in paths])
    
    # Covariance matrix (simplified: assume some correlation between similar paths)
    cov = np.eye(n) * 0.1
    for i in range(n):
        for j in range(i+1, n):
            if paths[i].path_type == paths[j].path_type:
                cov[i, j] = cov[j, i] = 0.05
    
    # Risk aversion based on profile
    risk_aversion = 2.0 + (1.0 - profile.risk_appetite) * 3.0
    
    # Optimize weights
    try:
        inv_cov = np.linalg.inv(cov + np.eye(n) * 0.001)
        ones = np.ones(n)
        weights = inv_cov @ (returns / risk_aversion + ones * 0.1)
        weights = np.maximum(weights, 0)
        weights /= np.sum(weights)
    except:
        weights = returns / np.sum(returns)
    
    primary = {paths[i].path_type: round(float(weights[i]), 3) for i in range(min(3, n))}
    secondary = {paths[i].path_type: round(float(weights[i]), 3) for i in range(3, n) if weights[i] > 0.05}
    
    return HedgePortfolio(
        primary_allocation=primary,
        secondary_allocation=secondary,
        risk_level=float(profile.risk_appetite),
        expected_return=float(np.dot(weights, returns) * 100)
    )
