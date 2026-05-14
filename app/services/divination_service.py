from typing import List
from app.models.questionnaire import Answer, Question
from app.models.profile import UserProfile, SevenDimensions
from app.models.results import DivinationResult, PathProbability, StoryLine, CelestialBody
from app.engines.feature_extractor import extract_features
from app.engines.scoring_engine import calculate_seven_dimensions
from app.engines.path_matcher import match_paths
from app.engines.monte_carlo import run_monte_carlo
from app.engines.body_classifier import classify_bodies
from app.engines.story_generator import generate_story_lines
from app.engines.optionality_index import calculate_oi
from app.engines.historical_phase import historical_phase_calibration
from app.engines.hedge_engine import hedge_engine
from app.engines.trauma_terrain import trauma_terrain

def run_full_divination(answers: List[Answer]) -> DivinationResult:
    """
    Run the complete divination pipeline.
    """
    # For now, use built-in questions (simplified)
    questions = []  # Will be loaded from data file
    
    # E1: Feature extraction
    profile = extract_features(answers, questions)
    
    # E2: Seven dimensions scoring
    dimensions = calculate_seven_dimensions(profile)
    
    # E3: Path matching
    paths = match_paths(profile, dimensions)
    
    # E4: Monte Carlo
    mc = run_monte_carlo(profile, dimensions)
    
    # E7: Optionality index
    oi = calculate_oi(profile)
    
    # E6: Story lines
    story_lines, healing = generate_story_lines(profile, dimensions, paths)
    
    # E8: Historical phase
    historical = historical_phase_calibration(profile)
    
    # E9: Hedge engine
    hedge = hedge_engine(paths, profile)
    
    # E10: Trauma terrain
    trauma = trauma_terrain(profile)
    if trauma["healing_b_line"]:
        healing = trauma["healing_b_line"]
    
    # E5: Body classification
    bodies = classify_bodies(profile, dimensions, paths)
    
    return DivinationResult(
        user_profile=profile,
        seven_dimensions=dimensions,
        paths=paths,
        primary_path=paths[0] if paths else PathProbability(path_type="unknown", probability=0, title="未知", description=""),
        secondary_path=paths[1] if len(paths) > 1 else PathProbability(path_type="unknown", probability=0, title="未知", description=""),
        bodies=bodies,
        story_lines=story_lines,
        healing_b_line=healing,
        ace10_severity=profile.ace10_score,
        optionality_index=oi,
        monte_carlo=mc,
        historical_analogues=historical,
        hedge_portfolio=hedge
    )
