from typing import List, Tuple, Optional
from app.models.profile import UserProfile, SevenDimensions
from app.models.results import PathProbability, StoryLine

def generate_story_lines(profile: UserProfile, dimensions: SevenDimensions, paths: List[PathProbability]) -> Tuple[List[StoryLine], Optional[StoryLine]]:
    story_lines = []
    
    for path in paths[:3]:  # Top 3 paths
        # Core logic based on profile
        core = f"基于您的画像分析，「{path.title}」是最匹配的路径（概率{path.probability*100:.1f}%）。"
        
        if path.path_type == "tech":
            core += f"您拥有{dimensions.career:.0f}分的事业基础和{profile.job_tenure*10:.0f}年的经验积累，适合在现有领域持续深耕。"
        elif path.path_type == "explorer":
            core += f"您的职业流动性({profile.career_mobility*100:.0f}%)和冒险意愿({profile.sacrifice_tolerance*100:.0f}%)支持高风险跃迁。"
        elif path.path_type == "business":
            core += f"您的财务缓冲({profile.financial_buffer*100:.0f}%)和资产状况为商业探索提供了基础。"
        elif path.path_type == "family":
            core += f"您对健康({dimensions.health:.0f}分)和生活品质的重视，使生活方式优化成为优先选择。"
        elif path.path_type == "academia":
            core += f"您的认知开放性({profile.cognitive_openness*100:.0f}%)和跨域曝光支持探索新方向。"
        elif path.path_type == "freelance":
            core += f"您的收入渠道多样性({profile.income_channel*100:.0f}%)和跨域能力适合多元发展。"
        elif path.path_type == "public":
            core += f"您的影响力({dimensions.impact:.0f}分)和协作倾向适合社群共创。"
        elif path.path_type == "art":
            core += f"您的疗愈需求优先级较高，建议先关注内在恢复再规划未来。"
        
        # Key assets
        assets = []
        if profile.financial_buffer > 0.6:
            assets.append("财务缓冲充足")
        if profile.career_mobility > 0.6:
            assets.append("职业流动性高")
        if dimensions.career > 70:
            assets.append("事业基础稳固")
        if profile.cognitive_openness > 0.6:
            assets.append("认知开放度高")
        if profile.positive_mirroring > 0.6:
            assets.append
cat > app/engines/optionality_index.py << 'EOF'
from app.models.profile import UserProfile

def calculate_oi(profile: UserProfile) -> float:
    """
    Optionality Index: measures the value of user's future choices.
    Weighted sum of 10 dimensions.
    """
    oi = (
        profile.income_channel * 0.20 +
        profile.option_generation * 0.15 +
        profile.career_mobility * 0.15 +
        profile.cognitive_openness * 0.10 +
        profile.info_curating * 0.10 +
        profile.identity_independence * 0.10 +
        profile.education * 0.05 +
        profile.cognitive_update_speed * 0.05 +
        profile.liquid_assets * 0.05 +
        profile.unconditional_support * 0.05
    )
    return min(1.0, max(0.0, oi))
