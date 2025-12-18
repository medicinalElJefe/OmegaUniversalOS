# Omega Universal OS - Getting Started Guide

## Quick Start

### 1. Installation

```bash
# Clone the repository
git clone https://github.com/medicinalElJefe/OmegaUniversalOS.git
cd OmegaUniversalOS

# Install the package
pip install -e .
```

### 2. Run Interactive Mode

```bash
python main.py --mode interactive
```

Select your role when prompted:
- 1 = Student
- 2 = Educator  
- 3 = Patient/Individual
- 4 = Health Official
- 5 = Policymaker
- 6 = Economist
- 7 = Demo Mode

### 3. Run Demo Mode

```bash
python main.py --mode demo
```

### 4. Run Examples

```bash
python examples.py
```

## Module Overview

### AI Engine
- **RippleEngine**: Validates ripple coherence with fail-safe mechanisms
- **PredictionModel**: AI predictions with self-correction
- **CalibrationEngine**: Model optimization and alignment

### Education
- **AdaptiveLearningSystem**: Personalized learning paths
- **StudentRippleTracker**: Monitor student progress and coherence

### Healthcare
- **HealthRippleSimulator**: Personal health trajectory modeling
- **PublicHealthAnalyzer**: Population-level health analysis

### Governance
- **PolicyTester**: Simulate policy impacts before implementation
- **ResourceAllocator**: Optimize resource distribution

### Economics
- **TradeOffAnalyzer**: Analyze economic decisions
- **MarketSimulator**: Model market dynamics

## Configuration

Create a `config.json` file:

```json
{
  "ai_engine": {
    "coherence_threshold": 0.7,
    "max_propagation_depth": 5
  },
  "logging": {
    "level": "INFO",
    "file": "omega.log"
  }
}
```

Run with custom config:

```bash
python main.py --config config.json
```

## Quick Examples

### Student Learning Path

```python
from education import AdaptiveLearningSystem
from ai_engine import RippleEngine

engine = RippleEngine()
learning = AdaptiveLearningSystem()

path = learning.create_learning_path('student_123', {
    'proficiency_level': 'intermediate',
    'learning_style': 'visual'
})
```

### Health Simulation

```python
from healthcare import HealthRippleSimulator

simulator = HealthRippleSimulator()
result = simulator.simulate_personal_health('patient_123', {
    'vital_signs': {'normalized_score': 0.8},
    'lifestyle_factors': {
        'exercise_frequency': 0.7,
        'nutrition_quality': 0.75
    }
})
```

### Policy Testing

```python
from governance import PolicyTester

tester = PolicyTester()
result = tester.test_policy('policy_123', {
    'type': 'education_reform',
    'economic_impact': 0.72,
    'social_impact': 0.80
})
```

## Features

✅ Modular architecture across 5 domains
✅ Ripple coherence validation
✅ Self-correcting AI predictions
✅ Role-based workflows
✅ Fail-safe mechanisms
✅ Comprehensive logging
✅ Zero external dependencies

## System Requirements

- Python 3.8+
- No external dependencies (stdlib only)

## Support

For issues or questions, please open an issue on GitHub.
