"""
Configuration management for Omega Universal OS.
"""

import json
import os
from typing import Dict, Any, Optional


class Config:
    """
    Configuration manager for Omega Universal OS.
    """
    
    def __init__(self, config_dict: Optional[Dict[str, Any]] = None):
        """
        Initialize configuration.
        
        Args:
            config_dict: Optional configuration dictionary
        """
        self._config = config_dict or self._default_config()
    
    def _default_config(self) -> Dict[str, Any]:
        """Return default configuration."""
        return {
            'ai_engine': {
                'coherence_threshold': 0.7,
                'max_propagation_depth': 5,
                'accuracy_threshold': 0.75,
                'target_accuracy': 0.85
            },
            'education': {
                'default_proficiency': 'intermediate',
                'feedback_frequency': 'weekly'
            },
            'healthcare': {
                'health_score_threshold': 0.6,
                'intervention_success_base': 0.75
            },
            'governance': {
                'policy_impact_threshold': 0.6,
                'resource_optimization_enabled': True
            },
            'economics': {
                'trade_off_threshold': 0.6,
                'market_volatility_default': 0.15
            },
            'logging': {
                'level': 'INFO',
                'file': None
            }
        }
    
    def get(self, key: str, default: Any = None) -> Any:
        """
        Get configuration value by key.
        
        Args:
            key: Configuration key (supports dot notation, e.g., 'ai_engine.coherence_threshold')
            default: Default value if key not found
            
        Returns:
            Configuration value
        """
        keys = key.split('.')
        value = self._config
        
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
                if value is None:
                    return default
            else:
                return default
        
        return value
    
    def set(self, key: str, value: Any):
        """
        Set configuration value.
        
        Args:
            key: Configuration key (supports dot notation)
            value: Value to set
        """
        keys = key.split('.')
        config = self._config
        
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        
        config[keys[-1]] = value
    
    def get_module_config(self, module_name: str) -> Dict[str, Any]:
        """
        Get configuration for a specific module.
        
        Args:
            module_name: Module name (ai_engine, education, etc.)
            
        Returns:
            Module configuration dictionary
        """
        return self._config.get(module_name, {})
    
    def to_dict(self) -> Dict[str, Any]:
        """Return configuration as dictionary."""
        return self._config.copy()
    
    def save(self, filepath: str):
        """
        Save configuration to JSON file.
        
        Args:
            filepath: Path to save configuration
        """
        with open(filepath, 'w') as f:
            json.dump(self._config, f, indent=2)
    
    @classmethod
    def from_file(cls, filepath: str) -> 'Config':
        """
        Load configuration from JSON file.
        
        Args:
            filepath: Path to configuration file
            
        Returns:
            Config instance
        """
        with open(filepath, 'r') as f:
            config_dict = json.load(f)
        return cls(config_dict)


def load_config(filepath: Optional[str] = None) -> Config:
    """
    Load configuration from file or return default.
    
    Args:
        filepath: Optional path to configuration file
        
    Returns:
        Config instance
    """
    if filepath and os.path.exists(filepath):
        return Config.from_file(filepath)
    return Config()
