from typing import Optional
from app.models.profile import UserProfile
from app.models.results import StoryLine

def trauma_terrain(profile: UserProfile) -> dict:
    """
    ACE-10 trauma assessment + healing B-line generation.
    """
    severity = profile.ace10_score
    
    # Probability flattening detection
    is_flattened = profile.trauma_profile > 0.5
    
    result = {
        "severity": severity,
        "is_flattened": is_flattened,
        "healing_b_line": None
    }
    
    if severity >= 4:
        healing = StoryLine(
            core_logic=f"ACE-10评分{severity:.1f}表明童年逆境经历较高。建议在追求目标的同时，优先建立心理安全基地。",
            key_assets=["心理韧性", "恢复空间", "支持网络", "自我关怀"],
            timeline=[
                {"year": 1, "milestone": "建立安全基地：稳定生活节律，建立支持关系"},
                {"year": 2, "milestone": "温和探索：在安全感基础上小步尝试"},
                {"year": 3, "milestone": "整合成长：将逆境经历转化为内在力量"}
            ],
            risk_warnings=["避免高压环境", "保持恢复节奏", "建立退出机制"],
            recovery_protocol="感到overwhelmed时：降低30%强度→启动自我关怀→联系支持网络→必要时寻求专业帮助。"
        )
        result["healing_b_line"] = healing
    
    return result
