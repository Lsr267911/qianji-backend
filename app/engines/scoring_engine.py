from app.models.profile import UserProfile, SevenDimensions

def calculate_seven_dimensions(profile: UserProfile) -> SevenDimensions:
    d = SevenDimensions()
    
    # Career
    d.career = min(100, (
        profile.job_level * 0.15 + profile.job_tenure * 0.10 +
        profile.career_mobility * 0.15 + profile.job_satisfaction * 0.10 +
        profile.next_career_move * 0.10 + profile.education * 0.10 +
        profile.school_tier * 0.10 + profile.work_culture * 0.10 +
        profile.possibility_vision * 0.10
    ) * 100)
    
    # Relationship
    d.relationship = min(100, (
        profile.family_structure * 0.10 + profile.family_economic * 0.10 +
        profile.cultural_capital * 0.15 + profile.authentic_belonging * 0.15 +
        profile.positive_mirroring * 0.10 + profile.unconditional_support * 0.10 +
        profile.social_security * 0.10 + profile.work_culture * 0.10 +
        profile.generative_giving * 0.10
    ) * 100)
    
    # Wealth
    d.wealth = min(100, (
        profile.financial_buffer * 0.20 + profile.monthly_income * 0.15 +
        profile.savings_rate * 0.15 + profile.income_channel * 0.10 +
        profile.liquid_assets * 0.10 + profile.debt_ratio * 0.10 +
        profile.no_income_survival * 0.10 + profile.housing_fund * 0.10
    ) * 100)
    
    # Health
    d.health = min(100, (
        profile.sleep_duration * 0.15 + profile.sleep_quality_wake * 0.15 +
        profile.sleep_quality_night * 0.15 + profile.health_behavior * 0.20 +
        profile.health_asset * 0.15 + profile.job_drain * 0.10 +
        profile.work_hours * 0.10
    ) * 100)
    
    # Self-realization
    d.self_realization = min(100, (
        profile.identity_independence * 0.15 + profile.flow_experience * 0.15 +
        profile.creation_pride * 0.10 + profile.agency_experience * 0.10 +
        profile.meaning_source * 0.15 + profile.value_stability * 0.10 +
        profile.life_texture * 0.10 + profile.decision_trust * 0.15
    ) * 100)
    
    # Creativity
    d.creativity = min(100, (
        profile.cognitive_openness * 0.15 + profile.cross_domain_exposure * 0.15 +
        profile.option_generation * 0.15 + profile.life_paradigm_rupture * 0.10 +
        profile.life_sample_research * 0.10 + profile.cognitive_update_speed * 0.10 +
        profile.creation_pride * 0.15 + profile.boundary_break * 0.10
    ) * 100)
    
    # Impact
    d.impact = min(100, (
        profile.cultural_capital * 0.15 + profile.generative_giving * 0.15 +
        profile.agency_experience * 0.15 + profile.creation_pride * 0.10 +
        profile.immune_source * 0.15 + profile.role_model_portfolio * 0.15 +
        profile.info_curating * 0.15
    ) * 100)
    
    return d
