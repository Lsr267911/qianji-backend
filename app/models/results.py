from pydantic import BaseModel
from typing import List, Optional
from .profile import UserProfile, SevenDimensions

class PathProbability(BaseModel):
    path_type: str
    probability: float
    title: str
    description: str

class StoryLine(BaseModel):
    core_logic: str
    key_assets: List[str] = []
    timeline: List[dict] = []
    risk_warnings: List[str] = []
    recovery_protocol: Optional[str] = None

class CelestialBody(BaseModel):
    id: int
    x: float
    y: float
    radius: float
    kind: str
    color: List[int]
    path_type: str
    probability: float
    title: str
    philosophy: str

class HistoricalAnalogue(BaseModel):
    figure: str
    era: str
    domain: str
    similarity: float
    common_points: List[str]

class HedgePortfolio(BaseModel):
    primary_allocation: dict
    secondary_allocation: dict
    risk_level: float
    expected_return: float

class DivinationResult(BaseModel):
    user_profile: UserProfile
    seven_dimensions: SevenDimensions
    paths: List[PathProbability]
    primary_path: PathProbability
    secondary_path: PathProbability
    bodies: List[CelestialBody] = []
    story_lines: List[StoryLine]
    healing_b_line: Optional[StoryLine] = None
    ace10_severity: float
    optionality_index: float
    monte_carlo: Optional[dict] = None
    historical_analogues: List[HistoricalAnalogue] = []
    hedge_portfolio: Optional[HedgePortfolio] = None
