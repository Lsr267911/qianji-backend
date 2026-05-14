from pydantic import BaseModel
from typing import List

class UserProfile(BaseModel):
    # 基础资源
    age: float = 0.5
    gender: float = 0.5
    education: float = 0.5
    job_level: float = 0.5
    job_tenure: float = 0.5
    career_mobility: float = 0.5
    job_satisfaction: float = 0.5
    work_hours: float = 0.5
    work_culture: float = 0.5
    family_structure: float = 0.5
    family_economic: float = 0.5
    cultural_capital: float = 0.5
    primary_caregiver: float = 0.5
    school_tier: float = 0.5
    major_type: float = 0.5
    growth_place: float = 0.5
    hukou: float = 0.5
    
    # 财务
    financial_buffer: float = 0.5
    monthly_income: float = 0.5
    savings_rate: float = 0.5
    debt_ratio: float = 0.5
    income_channel: float = 0.5
    liquid_assets: float = 0.5
    no_income_survival: float = 0.5
    housing_fund: float = 0.5
    
    # 身心
    sleep_duration: float = 0.5
    sleep_quality_wake: float = 0.5
    sleep_quality_night: float = 0.5
    health_behavior: float = 0.5
    health_asset: float = 0.5
    
    # 心理负面
    ace10_score: float = 0.0
    trauma_profile: float = 0.0
    
    # 心理积极
    positive_mirroring: float = 0.5
    flow_experience: float = 0.5
    creation_pride: float = 0.5
    agency_experience: float = 0.5
    unconditional_support: float = 0.5
    boundary_break: float = 0.5
    generative_giving: float = 0.5
    somatic_healing: float = 0.5
    decision_trust: float = 0.5
    authentic_belonging: float = 0.5
    immune_source: float = 0.5
    
    # 认知
    possibility_vision: float = 0.5
    cross_domain_exposure: float = 0.5
    identity_independence: float = 0.5
    life_paradigm_rupture: float = 0.5
    life_sample_research: float = 0.5
    cognitive_openness: float = 0.5
    cocoon_awareness: float = 0.5
    cross_life_experience: float = 0.5
    option_generation: float = 0.5
    adjacent_possibility_map: float = 0.5
    
    # 独特性
    family_origin: float = 0.5
    stress_response: float = 0.5
    unique_edge: float = 0.5
    
    # 价值观
    primary_drive: float = 0.5
    success_judge: float = 0.5
    core_lack: float = 0.5
    work_rhythm: float = 0.5
    life_texture: float = 0.5
    time_discount_rate: float = 0.5
    meaning_source: float = 0.5
    value_stability: float = 0.5
    life_dimension_rank: List[int] = [1, 2, 3, 4, 5, 6, 7]
    
    # 信息
    value_source_diet: float = 0.5
    value_source_gap: float = 0.5
    info_curating: float = 0.5
    role_model_portfolio: float = 0.5
    info_depth_ratio: float = 0.5
    cognitive_update_speed: float = 0.5
    
    # 目标
    compounding_package: float = 0.5
    target_concretion: float = 0.5
    desire_archaeology: float = 0.5
    career_path_type: float = 0.5
    transition_readiness: float = 0.5
    
    # 代价
    sacrifice_tolerance: float = 0.5
    risk_appetite: float = 0.5
    risk_diversification: float = 0.5
    choice_management: float = 0.5
    # 职业扩展
    job_nature: float = 0.5
    work_location: float = 0.5
    social_security: float = 0.5
    next_career_move: float = 0.5
    job_drain: float = 0.5
    # 能力
    skill_depth: float = 0.5
    transferable_skills: float = 0.5
    learning_speed: float = 0.5
    # 社交
    social_network_size: float = 0.5
    environmental_support: float = 0.5
    geographic_mobility: float = 0.5
    # 心理扩展
    emotional_state: float = 0.5
    stress_level: float = 0.5
    anxiety_level: float = 0.5
    depression_indicator: float = 0.5
    negative_coping: float = 0.5
    emotional_regulation: float = 0.5
    self_worth: float = 0.5
    life_satisfaction: float = 0.5
    mental_fatigue: float = 0.5
    social_anxiety: float = 0.5
    perfectionism: float = 0.5
    rumination: float = 0.5
    hopelessness: float = 0.5
    loneliness: float = 0.5
    alienation: float = 0.5
    distrust: float = 0.5
    helplessness: float = 0.5
    despair: float = 0.5
    emotional_numbness: float = 0.5
    dissociation: float = 0.5
    somatic_symptoms: float = 0.5
    sleep_disorder: float = 0.5
    appetite_change: float = 0.5

class SevenDimensions(BaseModel):
    career: float = 50.0
    relationship: float = 50.0
    wealth: float = 50.0
    health: float = 50.0
    self_realization: float = 50.0
    creativity: float = 50.0
    impact: float = 50.0
