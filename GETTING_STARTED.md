# Omega Universal OS - Getting Started Guide

## Quick Start

### 1. Installation

```bash
# Clone the repository
git clone https://github.com/medicinalElJefe/OmegaUniversalOS.git
cd OmegaUniversalOS

# Install dependencies
pip install -r requirements.txt

# Or install the package
pip install -e .
```

### 2. Run GUI Application (Recommended)

```bash
python gui_app.py
```

The modern graphical interface will launch with:
- **Overview Dashboard**: Cross-domain ripple coherence analysis
- **Education Dashboard**: Student learning ripple tracking
- **Healthcare Dashboard**: Personal health simulations
- **Governance Dashboard**: Policy impact testing
- **Economics Dashboard**: Trade-off analysis

### 3. Run Command-Line Interface (Legacy)

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

### 4. Build Standalone Executable

```bash
# Install PyInstaller if needed
pip install pyinstaller

# Build executable
./build_executable.sh
```

The standalone application will be in the `dist/` directory and can be distributed without Python!

## Module Overview

### AI Engine
- **RippleEngine**: Validates ripple coherence with cross-domain analysis
- **Advanced Mathematics**: Harmonic mean, sigmoid, Metcalfe's Law, Shannon entropy
- **Domain Interaction Matrix**: Scientific coefficients for cross-domain effects
- **PredictionModel**: AI predictions with self-correction
- **CalibrationEngine**: Model optimization and alignment

### Education
- **AdaptiveLearningSystem**: Personalized learning paths
- **StudentRippleTracker**: Monitor student progress and coherence with cross-domain impacts

### Healthcare
- **HealthRippleSimulator**: Personal health trajectory modeling
- **PublicHealthAnalyzer**: Population-level health analysis

### Governance
- **PolicyTester**: Simulate policy impacts with cross-domain ripple analysis
- **ResourceAllocator**: Optimize resource distribution

### Economics
- **TradeOffAnalyzer**: Analyze economic decisions with domain interactions
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

### Cross-Domain Ripple Analysis (NEW!)

```python
from ai_engine import RippleEngine

engine = RippleEngine()

# Analyze ripple effects across all domains
domain_data = {
    'education': {'impact_score': 0.78, 'alignment': 0.82},
    'healthcare': {'impact_score': 0.75, 'alignment': 0.79},
    'governance': {'impact_score': 0.70, 'alignment': 0.73},
    'economics': {'impact_score': 0.72, 'alignment': 0.76}
}

result = engine.analyze_cross_domain_ripple(domain_data)
print(f"System Coherence: {result['system_coherence']:.3f}")
print(f"Overall System Health: {result['overall_system_health']:.3f}")
```

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

✅ Modern GUI with interactive visualizations
✅ Cross-domain ripple coherence analysis
✅ Advanced mathematical models (harmonic mean, sigmoid, Metcalfe's Law, etc.)
✅ Modular architecture across 5 domains
✅ Self-correcting AI predictions
✅ Role-based workflows
✅ Fail-safe mechanisms
✅ Comprehensive logging
✅ Standalone executable packaging

## System Requirements

- Python 3.8+
- PyQt5 (for GUI)
- matplotlib (for visualizations)
- numpy (for calculations)

## Support

For issues or questions, please open an issue on GitHub.
