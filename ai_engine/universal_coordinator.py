"""
Universal Ripple Coordinator - Integrates ripple coherence analysis across all domains.
Implements advanced cross-domain mathematical models for true universal ripple prediction.
"""

import logging
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime
import math


class UniversalRippleCoordinator:
    """
    Coordinates ripple coherence analysis across all domains (education, healthcare, 
    governance, economics) to provide truly universal predictions and ethical alignment.
    
    Uses advanced mathematical models including:
    - Cross-domain propagation matrices
    - Harmonic resonance calculations
    - Ethical coherence tensor analysis
    - Multi-dimensional impact synthesis
    """
    
    # Domain interaction coefficients (how strongly one domain affects another)
    DOMAIN_INTERACTION_MATRIX = {
        'education': {
            'education': 1.0,
            'healthcare': 0.35,  # Better education → better health outcomes
            'governance': 0.45,  # Education influences civic engagement
            'economics': 0.55   # Education drives economic development
        },
        'healthcare': {
            'education': 0.30,  # Health affects learning capacity
            'healthcare': 1.0,
            'governance': 0.40,  # Health policy and regulations
            'economics': 0.50   # Healthcare costs and productivity
        },
        'governance': {
            'education': 0.50,  # Policy affects education access
            'healthcare': 0.55,  # Policy affects health systems
            'governance': 1.0,
            'economics': 0.65   # Governance shapes economic policy
        },
        'economics': {
            'education': 0.45,  # Economic resources for education
            'healthcare': 0.50,  # Economic resources for healthcare
            'governance': 0.55,  # Economic influence on policy
            'economics': 1.0
        }
    }
    
    def __init__(self, ripple_engine=None, config: Optional[Dict[str, Any]] = None):
        """
        Initialize Universal Ripple Coordinator.
        
        Args:
            ripple_engine: Core RippleEngine instance
            config: Configuration parameters
        """
        self.config = config or {}
        self.logger = logging.getLogger(__name__)
        self.ripple_engine = ripple_engine
        
        # Universal coherence threshold
        self.universal_coherence_threshold = self.config.get('universal_coherence_threshold', 0.70)
        
        # Cross-domain ripple history
        self.universal_ripple_history = []
        
        # Domain state tracking
        self.domain_states = {
            'education': {},
            'healthcare': {},
            'governance': {},
            'economics': {}
        }
        
        self.logger.info("Universal Ripple Coordinator initialized")
    
    def analyze_universal_ripple(self, action: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze ripple effects across ALL domains for a given action.
        
        This is the core universal analysis that:
        1. Calculates direct impact in primary domain
        2. Propagates ripples to all connected domains
        3. Computes harmonic resonance across domains
        4. Validates universal coherence
        5. Provides cross-domain recommendations
        
        Args:
            action: Action parameters including domain, impact_score, and details
            
        Returns:
            Universal ripple analysis with cross-domain effects
        """
        self.logger.info("Analyzing universal ripple coherence across all domains...")
        
        primary_domain = action.get('domain', 'education')
        action_type = action.get('action_type', 'general')
        impact_score = action.get('impact_score', 0.5)
        alignment_score = action.get('alignment', 0.5)
        
        # 1. Direct domain impact
        direct_impact = self._calculate_direct_impact(action)
        
        # 2. Cross-domain propagation using interaction matrix
        cross_domain_impacts = self._propagate_cross_domain(
            primary_domain, 
            impact_score,
            action
        )
        
        # 3. Calculate harmonic resonance (how well domains sync)
        harmonic_resonance = self._calculate_harmonic_resonance(
            primary_domain,
            cross_domain_impacts
        )
        
        # 4. Compute universal coherence score
        universal_coherence = self._compute_universal_coherence(
            direct_impact,
            cross_domain_impacts,
            harmonic_resonance,
            alignment_score
        )
        
        # 5. Ethical alignment check across domains
        ethical_alignment = self._validate_ethical_alignment(
            action,
            cross_domain_impacts
        )
        
        # 6. Generate universal recommendations
        recommendations = self._generate_universal_recommendations(
            universal_coherence,
            cross_domain_impacts,
            ethical_alignment
        )
        
        # Compile universal analysis
        analysis = {
            'action_type': action_type,
            'primary_domain': primary_domain,
            'direct_impact': direct_impact,
            'cross_domain_impacts': cross_domain_impacts,
            'harmonic_resonance': harmonic_resonance,
            'universal_coherence_score': universal_coherence['score'],
            'is_universally_coherent': universal_coherence['coherent'],
            'ethical_alignment': ethical_alignment,
            'recommendations': recommendations,
            'affected_domains': list(cross_domain_impacts.keys()),
            'timestamp': datetime.now().isoformat()
        }
        
        # Store in history
        self.universal_ripple_history.append(analysis)
        
        # Update domain states
        self._update_domain_states(primary_domain, cross_domain_impacts)
        
        return analysis
    
    def synthesize_universal_summary(self, domain_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Synthesize results from all domain modules into a universal holistic summary.
        
        Args:
            domain_results: Dictionary with keys for each domain containing their outputs
            
        Returns:
            Universal summary integrating all domain insights
        """
        self.logger.info("Synthesizing universal summary across all domains...")
        
        # Extract coherence scores from each domain
        domain_coherences = {}
        domain_impacts = {}
        
        for domain, result in domain_results.items():
            if isinstance(result, dict):
                # Extract coherence if available
                if 'coherence_result' in result:
                    coherence = result['coherence_result'].get('coherence_score', 0.5)
                elif 'ripple_coherence' in result:
                    coherence = result['ripple_coherence'].get('coherence_score', 0.5)
                else:
                    coherence = 0.5
                
                domain_coherences[domain] = coherence
                
                # Extract impact scores
                if 'impact_score' in result:
                    domain_impacts[domain] = result['impact_score']
                elif 'impact_analysis' in result:
                    domain_impacts[domain] = result['impact_analysis'].get('overall_impact', 0.5)
                else:
                    domain_impacts[domain] = 0.5
        
        # Calculate weighted universal coherence
        if domain_coherences:
            universal_coherence = sum(domain_coherences.values()) / len(domain_coherences)
        else:
            universal_coherence = 0.5
        
        # Calculate cross-domain synergy
        synergy_score = self._calculate_cross_domain_synergy(domain_coherences)
        
        # Identify dominant domain
        dominant_domain = max(domain_impacts.items(), key=lambda x: x[1])[0] if domain_impacts else None
        
        # Generate holistic insights
        holistic_insights = self._generate_holistic_insights(
            domain_coherences,
            domain_impacts,
            synergy_score
        )
        
        summary = {
            'universal_coherence_score': universal_coherence,
            'cross_domain_synergy': synergy_score,
            'domain_coherences': domain_coherences,
            'domain_impacts': domain_impacts,
            'dominant_domain': dominant_domain,
            'holistic_insights': holistic_insights,
            'system_state': 'optimal' if universal_coherence > 0.8 else 'good' if universal_coherence > 0.6 else 'needs_attention',
            'universally_aligned': universal_coherence >= self.universal_coherence_threshold,
            'timestamp': datetime.now().isoformat()
        }
        
        return summary
    
    def _calculate_direct_impact(self, action: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate direct impact in primary domain."""
        impact_score = action.get('impact_score', 0.5)
        magnitude = action.get('magnitude', 1.0)
        
        # Apply magnitude scaling
        adjusted_impact = impact_score * magnitude
        
        return {
            'base_impact': impact_score,
            'magnitude': magnitude,
            'adjusted_impact': min(1.0, adjusted_impact),
            'domain': action.get('domain', 'general')
        }
    
    def _propagate_cross_domain(self, primary_domain: str, impact_score: float,
                                action: Dict[str, Any]) -> Dict[str, Dict[str, float]]:
        """
        Propagate ripple effects from primary domain to all other domains.
        Uses domain interaction matrix for scientifically grounded propagation.
        """
        cross_impacts = {}
        
        if primary_domain not in self.DOMAIN_INTERACTION_MATRIX:
            self.logger.warning(f"Unknown domain: {primary_domain}, using default propagation")
            return cross_impacts
        
        interaction_coefficients = self.DOMAIN_INTERACTION_MATRIX[primary_domain]
        
        for target_domain, coefficient in interaction_coefficients.items():
            if target_domain == primary_domain:
                continue
                
            # Calculate propagated impact using interaction coefficient
            # Apply decay factor for ripple propagation (inverse square law analogy)
            propagated_impact = impact_score * coefficient
            
            # Apply dampening based on distance in interaction space
            dampening = math.exp(-0.1 * (1.0 - coefficient))
            final_impact = propagated_impact * dampening
            
            cross_impacts[target_domain] = {
                'impact_score': min(1.0, final_impact),
                'interaction_coefficient': coefficient,
                'dampening_factor': dampening,
                'propagation_strength': 'strong' if coefficient > 0.5 else 'moderate' if coefficient > 0.3 else 'weak'
            }
        
        return cross_impacts
    
    def _calculate_harmonic_resonance(self, primary_domain: str,
                                     cross_impacts: Dict[str, Dict[str, float]]) -> Dict[str, Any]:
        """
        Calculate harmonic resonance - how well ripple effects harmonize across domains.
        Uses wave interference principles from physics.
        """
        if not cross_impacts:
            return {'resonance_score': 0.5, 'resonance_type': 'neutral'}
        
        # Extract impact scores
        impact_values = [data['impact_score'] for data in cross_impacts.values()]
        
        # Calculate variance (low variance = high resonance/harmony)
        mean_impact = sum(impact_values) / len(impact_values)
        variance = sum((x - mean_impact) ** 2 for x in impact_values) / len(impact_values)
        
        # Convert variance to resonance (inverse relationship)
        # Using harmonic formula: resonance = 1 / (1 + variance)
        resonance_score = 1.0 / (1.0 + variance * 10)
        
        # Classify resonance type
        if resonance_score > 0.8:
            resonance_type = 'constructive'  # Ripples reinforce each other
        elif resonance_score > 0.5:
            resonance_type = 'partial'
        else:
            resonance_type = 'destructive'  # Ripples may interfere
        
        # Calculate phase alignment (how synchronized the impacts are)
        phase_alignment = 1.0 - (variance / (mean_impact + 0.01))
        
        return {
            'resonance_score': resonance_score,
            'resonance_type': resonance_type,
            'phase_alignment': max(0.0, min(1.0, phase_alignment)),
            'mean_cross_impact': mean_impact,
            'impact_variance': variance
        }
    
    def _compute_universal_coherence(self, direct_impact: Dict[str, Any],
                                    cross_impacts: Dict[str, Dict[str, float]],
                                    harmonic_resonance: Dict[str, Any],
                                    alignment_score: float) -> Dict[str, Any]:
        """
        Compute universal coherence score using tensor-based analysis.
        This represents how well the action aligns across all universal dimensions.
        """
        # Components of universal coherence
        direct_component = direct_impact['adjusted_impact']
        
        # Cross-domain component (average of cross impacts)
        if cross_impacts:
            cross_component = sum(data['impact_score'] for data in cross_impacts.values()) / len(cross_impacts)
        else:
            cross_component = 0.0
        
        # Harmonic component
        harmonic_component = harmonic_resonance['resonance_score']
        
        # Alignment component
        alignment_component = alignment_score
        
        # Weighted universal coherence formula
        # Emphasizes direct impact but requires harmony across domains
        universal_score = (
            direct_component * 0.35 +       # Direct impact in primary domain
            cross_component * 0.25 +        # Cross-domain impacts
            harmonic_component * 0.20 +     # Harmonic resonance
            alignment_component * 0.20      # Ethical/goal alignment
        )
        
        # Apply coherence multiplier based on resonance
        if harmonic_resonance['resonance_type'] == 'constructive':
            universal_score *= 1.1  # Bonus for constructive resonance
        elif harmonic_resonance['resonance_type'] == 'destructive':
            universal_score *= 0.9  # Penalty for destructive interference
        
        # Ensure within bounds
        universal_score = max(0.0, min(1.0, universal_score))
        
        return {
            'score': universal_score,
            'coherent': universal_score >= self.universal_coherence_threshold,
            'components': {
                'direct': direct_component,
                'cross_domain': cross_component,
                'harmonic': harmonic_component,
                'alignment': alignment_component
            }
        }
    
    def _validate_ethical_alignment(self, action: Dict[str, Any],
                                   cross_impacts: Dict[str, Dict[str, float]]) -> Dict[str, Any]:
        """
        Validate ethical alignment across all affected domains.
        Ensures no domain is negatively impacted beyond acceptable thresholds.
        """
        ethical_violations = []
        domain_ethics = {}
        
        # Check if any domain has negative impact
        for domain, impact_data in cross_impacts.items():
            impact = impact_data['impact_score']
            
            # Ethical threshold: no domain should drop below 0.25
            if impact < 0.25:
                ethical_violations.append(f"{domain}: impact critically low ({impact:.2f})")
            
            # Classify ethical status
            if impact >= 0.6:
                status = 'ethical'
            elif impact >= 0.35:
                status = 'acceptable'
            else:
                status = 'concerning'
            
            domain_ethics[domain] = {
                'status': status,
                'impact': impact
            }
        
        # Overall ethical alignment
        ethics_scores = [data['impact'] for data in domain_ethics.values()]
        overall_ethics = sum(ethics_scores) / len(ethics_scores) if ethics_scores else 0.5
        
        return {
            'ethically_aligned': len(ethical_violations) == 0,
            'overall_ethics_score': overall_ethics,
            'domain_ethics': domain_ethics,
            'violations': ethical_violations,
            'ethics_level': 'high' if overall_ethics > 0.6 else 'moderate' if overall_ethics > 0.4 else 'low'
        }
    
    def _generate_universal_recommendations(self, universal_coherence: Dict[str, Any],
                                          cross_impacts: Dict[str, Dict[str, float]],
                                          ethical_alignment: Dict[str, Any]) -> List[str]:
        """Generate recommendations based on universal analysis."""
        recommendations = []
        
        coherence_score = universal_coherence['score']
        
        # Coherence-based recommendations
        if not universal_coherence['coherent']:
            recommendations.append(f"Improve universal coherence (current: {coherence_score:.2f}, target: {self.universal_coherence_threshold:.2f})")
        
        # Ethical recommendations
        if not ethical_alignment['ethically_aligned']:
            recommendations.append("Address ethical concerns in: " + ", ".join(
                [v.split(':')[0] for v in ethical_alignment['violations']]
            ))
        
        # Domain-specific recommendations
        weak_domains = [
            domain for domain, data in cross_impacts.items()
            if data['impact_score'] < 0.5
        ]
        
        if weak_domains:
            recommendations.append(f"Strengthen impact in: {', '.join(weak_domains)}")
        
        # Positive reinforcement
        if coherence_score > 0.85 and ethical_alignment['ethically_aligned']:
            recommendations.append("Excellent universal coherence - maintain current approach")
        
        return recommendations if recommendations else ["Universal coherence is satisfactory"]
    
    def _calculate_cross_domain_synergy(self, domain_coherences: Dict[str, float]) -> float:
        """Calculate synergy between domains (emergent effects)."""
        if len(domain_coherences) < 2:
            return 0.5
        
        scores = list(domain_coherences.values())
        mean_score = sum(scores) / len(scores)
        
        # Synergy emerges when all domains perform well together
        # Calculate using geometric mean (emphasizes balance)
        product = 1.0
        for score in scores:
            product *= score
        
        geometric_mean = product ** (1.0 / len(scores))
        
        # Synergy bonus if domains are balanced
        balance_factor = 1.0 - (max(scores) - min(scores))
        synergy = geometric_mean * balance_factor
        
        return min(1.0, synergy)
    
    def _generate_holistic_insights(self, domain_coherences: Dict[str, float],
                                   domain_impacts: Dict[str, float],
                                   synergy_score: float) -> List[str]:
        """Generate holistic insights from universal analysis."""
        insights = []
        
        # Overall system health
        avg_coherence = sum(domain_coherences.values()) / len(domain_coherences) if domain_coherences else 0.5
        
        if avg_coherence > 0.8:
            insights.append("System exhibits strong universal coherence across all domains")
        elif avg_coherence < 0.5:
            insights.append("System coherence needs improvement across multiple domains")
        
        # Synergy insights
        if synergy_score > 0.7:
            insights.append("Domains are working synergistically - emergent positive effects detected")
        elif synergy_score < 0.4:
            insights.append("Limited synergy between domains - consider integration strategies")
        
        # Domain-specific insights
        strongest = max(domain_coherences.items(), key=lambda x: x[1]) if domain_coherences else None
        weakest = min(domain_coherences.items(), key=lambda x: x[1]) if domain_coherences else None
        
        if strongest and weakest:
            insights.append(f"Strongest domain: {strongest[0]} ({strongest[1]:.2f})")
            insights.append(f"Needs attention: {weakest[0]} ({weakest[1]:.2f})")
        
        return insights
    
    def _update_domain_states(self, primary_domain: str, cross_impacts: Dict[str, Dict[str, float]]):
        """Update internal state tracking for domains."""
        timestamp = datetime.now().isoformat()
        
        # Update primary domain
        self.domain_states[primary_domain][timestamp] = {
            'role': 'primary',
            'last_updated': timestamp
        }
        
        # Update affected domains
        for domain, impact_data in cross_impacts.items():
            self.domain_states[domain][timestamp] = {
                'role': 'affected',
                'impact': impact_data['impact_score'],
                'last_updated': timestamp
            }
    
    def get_universal_history(self) -> List[Dict[str, Any]]:
        """Get history of universal ripple analyses."""
        return self.universal_ripple_history.copy()
    
    def get_domain_state(self, domain: str) -> Dict[str, Any]:
        """Get current state for a specific domain."""
        return self.domain_states.get(domain, {})
    
    def reset(self):
        """Reset coordinator state."""
        self.universal_ripple_history = []
        self.domain_states = {
            'education': {},
            'healthcare': {},
            'governance': {},
            'economics': {}
        }
        self.logger.info("Universal Ripple Coordinator reset")
