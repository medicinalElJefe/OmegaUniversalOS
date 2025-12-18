"""
Healthcare Module for Omega Universal OS
Provides personal and public health ripple simulations.
"""

from .health_ripple import HealthRippleSimulator
from .public_health import PublicHealthAnalyzer

__all__ = ['HealthRippleSimulator', 'PublicHealthAnalyzer']
