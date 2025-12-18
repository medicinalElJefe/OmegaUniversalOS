"""
AI Engine Module for Omega Universal OS
Provides core prediction, calibration, and ripple alignment capabilities.
"""

from .ripple_engine import RippleEngine
from .prediction_models import PredictionModel
from .calibration import CalibrationEngine
from .universal_coordinator import UniversalRippleCoordinator

__all__ = ['RippleEngine', 'PredictionModel', 'CalibrationEngine', 'UniversalRippleCoordinator']
