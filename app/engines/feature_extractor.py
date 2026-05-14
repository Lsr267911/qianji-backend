import numpy as np
from typing import List, Dict
from app.models.questionnaire import Question, Answer
from app.models.profile import UserProfile

# dimension -> profile fields mapping
DIMENSION_MAP = {
    "切面可见性": ["possibility_vision", "cross_domain_exposure", "identity_independence",
                  "life_paradigm_rupture", "life_sample_research", "cognitive_openness",
                  "cocoon_awareness", "cross_life_experience", "option_generation",
                  "adjacent_possibility_map"],
    "客观资源-背景出身": ["age", "gender", "hukou", "growth_place", "family_structure",
                       "primary_caregiver", "family_economic", "education",
                       "school_tier", "major_type", "cultural_capital"],
    "客观资源-职业角色": ["job_level", "job_tenure", "job_nature", "work_hours",
                       "work_location", "social_security", "housing_fund",
                       "work_culture", "job_satisfaction", "career_mobility",
                       "next_career_move", "job_drain"],
    "客观资源-时间资源": ["sleep_duration", "sleep_quality_wake", "sleep_quality_night"],
    "客观资源-财务资源": ["financial_buffer", "no_income_survival", "monthly_income",
                       "debt_ratio", "savings_rate", "income_channel", "liquid_assets"],
    "客观资源-能力资产": ["skill_depth", "transferable_skills", "learning_speed"],
    "客观资源-社交与环境": ["social_network_size", "environmental_support", "geographic_mobility"],
    "客观资源-健康资产": ["health_asset"],
    "心理切面-负面": ["emotional_state", "stress_level", "anxiety_level", "depression_indicator",
                    "negative_coping", "emotional_regulation", "self_worth", "life_satisfaction",
                    "mental_fatigue", "social_anxiety", "perfectionism", "rumination",
                    "hopelessness", "loneliness", "alienation", "distrust", "helplessness",
                    "despair", "emotional_numbness", "dissociation", "somatic_symptoms",
                    "sleep_disorder", "appetite_change"],
    "心理切面-积极": ["positive_mirroring", "flow_experience", "creation_pride",
                    "agency_experience", "unconditional_support", "boundary_break",
                    "generative_giving", "somatic_healing", "decision_trust",
                    "authentic_belonging", "immune_source"],
    "健康行为习惯": ["health_behavior"],
    "独特性坐标": ["family_origin", "stress_response", "unique_edge"],
    "价值观牵引": ["primary_drive", "success_judge", "core_lack", "work_rhythm",
                  "life_texture", "time_discount_rate", "meaning_source", "value_stability"],
    "信息源土壤": ["value_source_diet", "value_source_gap", "info_curating",
                  "role_model_portfolio", "info_depth_ratio", "cognitive_update_speed"],
    "复利套餐": ["compounding_package"],
    "目标具象化": ["target_concretion"],
    "欲望考古": ["desire_archaeology"],
    "职业与转折": ["career_path_type", "transition_readiness"],
    "代价承受": ["sacrifice_tolerance"],
    "风险管理": ["risk_appetite"],
    "风险分散": ["risk_diversification"],
    "选择管理": ["choice_management"],
}

def extract_features(answers: List[Answer], questions: List[Question]) -> UserProfile:
    profile = UserProfile()
    field_values: Dict[str, List[float]] = {}
    ace_scores = []
    
    for answer in answers:
        q = next((q for q in questions if q.id == answer.question_id), None)
        if not q or not q.options:
            continue
        
        option = next((o for o in q.options if o.value == answer.value), None)
        if not option:
            continue
        
        score = option.score
        
        # ACE-10 special handling
        if q.id.startswith("A60"):
            ace_scores.append(score)
            continue
        
        # B1w ranking special handling
        if q.id == "B1w":
            continue
        
        fields = DIMENSION_MAP.get(q.dimension, [])
        if not fields:
            fields = [q.data_purpose] if q.data_purpose else []
        
        for field in fields:
            if field not in field_values:
                field_values[field] = []
            field_values[field].append(score)
    
    # Average and assign
    for field, values in field_values.items():
        if values and hasattr(profile, field):
            setattr(profile, field, sum(values) / len(values))
    
    # ACE-10 score
    if ace_scores:
        profile.ace10_score = sum(ace_scores) / len(ace_scores) * 10
    
    return profile
