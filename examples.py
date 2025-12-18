#!/usr/bin/env python3
"""
Example usage of Omega Universal OS
Demonstrates key features across different domains.
"""

from utils import setup_logging, load_config
from ai_engine import RippleEngine, PredictionModel
from education import AdaptiveLearningSystem, StudentRippleTracker
from healthcare import HealthRippleSimulator
from governance import PolicyTester
from economics import TradeOffAnalyzer


def main():
    """Run example demonstrations."""
    
    # Setup
    setup_logging(level="INFO")
    config = load_config()
    
    print("="*70)
    print("Omega Universal OS - Example Demonstrations")
    print("="*70 + "\n")
    
    # 1. AI Engine Example
    print("1. AI Engine - Ripple Coherence Validation")
    print("-" * 70)
    ripple_engine = RippleEngine(config.get_module_config('ai_engine'))
    
    ripple_data = {
        'impact_score': 0.75,
        'alignment': 0.80,
        'domain': 'education'
    }
    
    result = ripple_engine.validate_coherence(ripple_data)
    print(f"   Input: impact={ripple_data['impact_score']}, alignment={ripple_data['alignment']}")
    print(f"   Coherence Score: {result['coherence_score']:.2f}")
    print(f"   Status: {'✓ Coherent' if result['coherent'] else '✗ Needs Improvement'}")
    
    # Simulate propagation
    propagation = ripple_engine.simulate_propagation(ripple_data, depth=3)
    print(f"   Propagated {len(propagation)} levels")
    print()
    
    # 2. Education Example
    print("2. Education - Adaptive Learning System")
    print("-" * 70)
    learning_system = AdaptiveLearningSystem()
    student_tracker = StudentRippleTracker(ripple_engine)
    
    student_data = {
        'proficiency_level': 'intermediate',
        'learning_style': 'visual',
        'interests': ['AI', 'machine learning']
    }
    
    learning_path = learning_system.create_learning_path('student_001', student_data)
    print(f"   Created learning path for student_001")
    print(f"   Proficiency: {learning_path['proficiency_level']}")
    print(f"   Modules: {len(learning_path['modules'])}")
    
    # Track student ripple
    learning_data = {
        'engagement_score': 0.85,
        'comprehension_score': 0.78,
        'collaboration_score': 0.72,
        'curriculum_alignment': 0.88
    }
    
    ripple_report = student_tracker.track_student_ripple('student_001', learning_data)
    if ripple_report.get('coherence_result'):
        print(f"   Learning Coherence: {ripple_report['coherence_result']['coherence_score']:.2f}")
    print()
    
    # 3. Healthcare Example
    print("3. Healthcare - Personal Health Simulation")
    print("-" * 70)
    health_simulator = HealthRippleSimulator(ripple_engine)
    
    health_data = {
        'vital_signs': {'normalized_score': 0.80},
        'lifestyle_factors': {
            'exercise_frequency': 0.75,
            'nutrition_quality': 0.78,
            'sleep_quality': 0.70,
            'sustainability_score': 0.75
        },
        'medical_history': [],
        'treatment_compliance': 0.90
    }
    
    health_result = health_simulator.simulate_personal_health('patient_001', health_data)
    print(f"   Current Health Score: {health_result['current_health_score']:.2f}")
    print(f"   Projected 6-month: {health_result['predicted_trajectory']['6_months']:.2f}")
    print(f"   Trend: {health_result['predicted_trajectory']['trend']}")
    print()
    
    # 4. Governance Example
    print("4. Governance - Policy Testing")
    print("-" * 70)
    policy_tester = PolicyTester(ripple_engine)
    
    policy_params = {
        'type': 'education_reform',
        'scope': 'regional',
        'affected_population': 500000,
        'economic_impact': 0.70,
        'social_impact': 0.82,
        'environmental_impact': 0.68,
        'implementation_cost': 2000000,
        'implementation_timeline': 9,
        'alignment_with_objectives': 0.78
    }
    
    policy_result = policy_tester.test_policy('policy_001', policy_params)
    print(f"   Policy: {policy_params['type']}")
    print(f"   Overall Impact: {policy_result['impact_analysis']['overall_impact']:.2f}")
    print(f"   Implementation Readiness: {policy_result['implementation_readiness']}")
    print()
    
    # 5. Economics Example
    print("5. Economics - Trade-Off Analysis")
    print("-" * 70)
    trade_off_analyzer = TradeOffAnalyzer(ripple_engine)
    
    options = [
        {
            'name': 'Option A',
            'economic_impact': 0.72,
            'cost': 1000000,
            'roi': 1.6,
            'risk_level': 'medium',
            'timeline': 12,
            'strategic_alignment': 0.75,
            'sustainability': 0.68
        },
        {
            'name': 'Option B',
            'economic_impact': 0.78,
            'cost': 1200000,
            'roi': 1.9,
            'risk_level': 'low',
            'timeline': 15,
            'strategic_alignment': 0.82,
            'sustainability': 0.80
        }
    ]
    
    analysis = trade_off_analyzer.analyze_trade_offs('decision_001', options)
    best_idx = analysis['comparison']['best_option_index']
    print(f"   Options analyzed: {analysis['options_analyzed']}")
    print(f"   Best option: Option {chr(65 + best_idx)}")
    print(f"   Best score: {analysis['comparison']['best_option_score']:.2f}")
    print(f"   Trade-off acceptable: {'✓ Yes' if analysis['trade_off_acceptable'] else '✗ No'}")
    print()
    
    print("="*70)
    print("All examples completed successfully!")
    print("="*70)


if __name__ == '__main__':
    main()
