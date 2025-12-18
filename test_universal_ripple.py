#!/usr/bin/env python3
"""
Test script for Universal Ripple Coherence Analysis.
Demonstrates cross-domain ripple propagation and universal coherence validation.
"""

from ai_engine import RippleEngine, UniversalRippleCoordinator
from utils import load_config, setup_logging

def test_cross_domain_ripple():
    """Test cross-domain ripple propagation."""
    print("="*70)
    print("Testing Universal Cross-Domain Ripple Propagation")
    print("="*70)
    
    # Initialize components
    config = load_config()
    ripple_engine = RippleEngine(config.get_module_config('ai_engine'))
    coordinator = UniversalRippleCoordinator(ripple_engine, config.get_module_config('ai_engine'))
    
    # Test 1: Education domain action
    print("\n1. Education Domain Action: Technology Integration")
    print("-" * 70)
    education_action = {
        'domain': 'education',
        'action_type': 'technology_integration',
        'impact_score': 0.85,
        'alignment': 0.88,
        'magnitude': 1.0
    }
    
    result = coordinator.analyze_universal_ripple(education_action)
    print(f"   Primary Domain: {result['primary_domain']}")
    print(f"   Universal Coherence: {result['universal_coherence_score']:.3f}")
    print(f"   Harmonic Resonance: {result['harmonic_resonance']['resonance_score']:.3f}")
    print(f"   Resonance Type: {result['harmonic_resonance']['resonance_type']}")
    print(f"\n   Cross-Domain Impacts:")
    for domain, impact in result['cross_domain_impacts'].items():
        print(f"     • {domain:12} → {impact['impact_score']:.3f} ({impact['propagation_strength']})")
    
    # Test 2: Healthcare domain action
    print("\n2. Healthcare Domain Action: Public Health Campaign")
    print("-" * 70)
    healthcare_action = {
        'domain': 'healthcare',
        'action_type': 'public_health_campaign',
        'impact_score': 0.75,
        'alignment': 0.80,
        'magnitude': 0.9
    }
    
    result = coordinator.analyze_universal_ripple(healthcare_action)
    print(f"   Primary Domain: {result['primary_domain']}")
    print(f"   Universal Coherence: {result['universal_coherence_score']:.3f}")
    print(f"   Ethical Alignment: {result['ethical_alignment']['ethically_aligned']}")
    print(f"   Ethics Level: {result['ethical_alignment']['ethics_level']}")
    print(f"\n   Cross-Domain Impacts:")
    for domain, impact in result['cross_domain_impacts'].items():
        print(f"     • {domain:12} → {impact['impact_score']:.3f}")
    
    # Test 3: Governance domain action
    print("\n3. Governance Domain Action: Economic Policy Reform")
    print("-" * 70)
    governance_action = {
        'domain': 'governance',
        'action_type': 'economic_policy',
        'impact_score': 0.82,
        'alignment': 0.78,
        'magnitude': 1.0
    }
    
    result = coordinator.analyze_universal_ripple(governance_action)
    print(f"   Primary Domain: {result['primary_domain']}")
    print(f"   Universal Coherence: {result['universal_coherence_score']:.3f}")
    print(f"   Status: {'COHERENT ✓' if result['is_universally_coherent'] else 'NEEDS REVIEW ⚠'}")
    print(f"\n   Recommendations:")
    for rec in result['recommendations']:
        print(f"     • {rec}")
    
    # Test 4: Economics domain action
    print("\n4. Economics Domain Action: Infrastructure Investment")
    print("-" * 70)
    economics_action = {
        'domain': 'economics',
        'action_type': 'infrastructure_investment',
        'impact_score': 0.90,
        'alignment': 0.85,
        'magnitude': 1.2
    }
    
    result = coordinator.analyze_universal_ripple(economics_action)
    print(f"   Primary Domain: {result['primary_domain']}")
    print(f"   Universal Coherence: {result['universal_coherence_score']:.3f}")
    print(f"   Direct Impact: {result['direct_impact']['adjusted_impact']:.3f}")
    print(f"\n   Cross-Domain Impacts:")
    for domain, impact in result['cross_domain_impacts'].items():
        strength_icon = "🔥" if impact['propagation_strength'] == 'strong' else "⚡"
        print(f"     {strength_icon} {domain:12} → {impact['impact_score']:.3f}")


def test_universal_synthesis():
    """Test holistic synthesis across all domains."""
    print("\n" + "="*70)
    print("Testing Universal Holistic Synthesis")
    print("="*70)
    
    config = load_config()
    ripple_engine = RippleEngine(config.get_module_config('ai_engine'))
    coordinator = UniversalRippleCoordinator(ripple_engine, config.get_module_config('ai_engine'))
    
    # Mock domain results
    domain_results = {
        'education': {
            'coherence_result': {'coherence_score': 0.82},
            'impact_score': 0.79
        },
        'healthcare': {
            'coherence_result': {'coherence_score': 0.75},
            'impact_score': 0.71
        },
        'governance': {
            'ripple_coherence': {'coherence_score': 0.88},
            'impact_analysis': {'overall_impact': 0.85}
        },
        'economics': {
            'coherence_result': {'coherence_score': 0.78},
            'impact_score': 0.76
        }
    }
    
    summary = coordinator.synthesize_universal_summary(domain_results)
    
    print(f"\n   Universal Coherence Score: {summary['universal_coherence_score']:.3f}")
    print(f"   Cross-Domain Synergy: {summary['cross_domain_synergy']:.3f}")
    print(f"   System State: {summary['system_state'].upper()}")
    print(f"   Universally Aligned: {'✓ YES' if summary['universally_aligned'] else '⚠ NO'}")
    print(f"   Dominant Domain: {summary['dominant_domain']}")
    
    print(f"\n   Domain Coherences:")
    for domain, coherence in summary['domain_coherences'].items():
        bar = "█" * int(coherence * 20) + "░" * (20 - int(coherence * 20))
        print(f"     {domain:12} [{bar}] {coherence:.3f}")
    
    print(f"\n   Holistic Insights:")
    for insight in summary['holistic_insights']:
        print(f"     • {insight}")


def test_multi_domain_coherence():
    """Test multi-domain coherence validation."""
    print("\n" + "="*70)
    print("Testing Multi-Domain Coherence Validation")
    print("="*70)
    
    config = load_config()
    ripple_engine = RippleEngine(config.get_module_config('ai_engine'))
    
    # Test multi-domain validation
    domain_ripples = {
        'education': {
            'impact_score': 0.80,
            'alignment': 0.82
        },
        'healthcare': {
            'impact_score': 0.75,
            'alignment': 0.78
        },
        'governance': {
            'impact_score': 0.85,
            'alignment': 0.80
        },
        'economics': {
            'impact_score': 0.78,
            'alignment': 0.76
        }
    }
    
    result = ripple_engine.validate_multi_domain_coherence(domain_ripples)
    
    print(f"\n   Multi-Domain Coherent: {'✓ YES' if result['multi_domain_coherent'] else '⚠ NO'}")
    print(f"   Average Coherence: {result['average_coherence']:.3f}")
    print(f"   Min Coherence: {result['min_coherence']:.3f}")
    print(f"   Max Coherence: {result['max_coherence']:.3f}")
    print(f"   Coherence Range: {result['coherence_range']:.3f}")
    print(f"   Balanced: {'✓ YES' if result['balanced'] else '⚠ NO'}")
    
    print(f"\n   Individual Domain Coherences:")
    for domain, coherence_data in result['domain_coherences'].items():
        score = coherence_data['coherence_score']
        status = '✓' if coherence_data['coherent'] else '⚠'
        print(f"     {status} {domain:12} → {score:.3f}")


if __name__ == '__main__':
    # Setup logging
    setup_logging(level='INFO')
    
    print("\n" + "="*70)
    print("OMEGA UNIVERSAL OS - UNIVERSAL RIPPLE COHERENCE TEST SUITE")
    print("="*70)
    
    # Run tests
    test_cross_domain_ripple()
    test_universal_synthesis()
    test_multi_domain_coherence()
    
    print("\n" + "="*70)
    print("All Tests Completed Successfully!")
    print("="*70 + "\n")
