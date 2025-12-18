"""
Policy Testing framework for governance ripple analysis.
"""

import logging
from typing import Dict, List, Any, Optional
from datetime import datetime


class PolicyTester:
    """
    Test policy impacts using ripple simulation before implementation.
    """
    
    def __init__(self, ripple_engine=None, config: Optional[Dict[str, Any]] = None):
        """
        Initialize policy tester.
        
        Args:
            ripple_engine: Optional RippleEngine instance
            config: Optional configuration dictionary
        """
        self.config = config or {}
        self.logger = logging.getLogger(__name__)
        self.ripple_engine = ripple_engine
        self.policy_tests = {}
        
    def test_policy(self, policy_id: str, policy_params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Test a policy before implementation.
        
        Args:
            policy_id: Unique policy identifier
            policy_params: Policy parameters and configuration
            
        Returns:
            Policy test results with impact analysis
        """
        self.logger.info(f"Testing policy: {policy_id}")
        
        # Extract policy details
        policy_type = policy_params.get('type', 'regulatory')
        scope = policy_params.get('scope', 'local')
        affected_population = policy_params.get('affected_population', 10000)
        
        # Simulate policy impact
        impact_analysis = self._simulate_policy_impact(policy_params)
        
        # Calculate ripple effects
        ripple_data = {
            'impact_score': impact_analysis['overall_impact'],
            'alignment': policy_params.get('alignment_with_objectives', 0.75),
            'domain': 'governance'
        }
        
        coherence_result = None
        if self.ripple_engine:
            coherence_result = self.ripple_engine.validate_coherence(ripple_data)
            
            # Simulate propagation
            propagation = self.ripple_engine.simulate_propagation(ripple_data, depth=3)
        else:
            propagation = []
        
        test_result = {
            'policy_id': policy_id,
            'policy_type': policy_type,
            'scope': scope,
            'affected_population': affected_population,
            'impact_analysis': impact_analysis,
            'ripple_coherence': coherence_result,
            'ripple_propagation': propagation,
            'recommendations': self._generate_policy_recommendations(impact_analysis, coherence_result),
            'implementation_readiness': self._assess_readiness(impact_analysis),
            'timestamp': datetime.now().isoformat()
        }
        
        self.policy_tests[policy_id] = test_result
        return test_result
    
    def compare_policies(self, policy_ids: List[str]) -> Dict[str, Any]:
        """
        Compare multiple policy alternatives.
        
        Args:
            policy_ids: List of policy identifiers to compare
            
        Returns:
            Comparative analysis
        """
        self.logger.info(f"Comparing {len(policy_ids)} policies")
        
        policies = []
        for pid in policy_ids:
            if pid in self.policy_tests:
                policies.append(self.policy_tests[pid])
        
        if not policies:
            return {'error': 'No policies found for comparison'}
        
        comparison = {
            'policies_compared': len(policies),
            'ranking': self._rank_policies(policies),
            'trade_offs': self._analyze_trade_offs(policies),
            'recommended_policy': self._select_best_policy(policies),
            'timestamp': datetime.now().isoformat()
        }
        
        return comparison
    
    def simulate_policy_rollback(self, policy_id: str) -> Dict[str, Any]:
        """
        Simulate effects of rolling back a policy.
        
        Args:
            policy_id: Policy identifier
            
        Returns:
            Rollback impact analysis
        """
        self.logger.info(f"Simulating rollback for policy: {policy_id}")
        
        if policy_id not in self.policy_tests:
            return {'error': 'Policy not found'}
        
        original_test = self.policy_tests[policy_id]
        original_impact = original_test['impact_analysis']['overall_impact']
        
        # Estimate rollback effects (inverse of implementation)
        rollback_impact = {
            'policy_id': policy_id,
            'original_impact': original_impact,
            'rollback_effect': -original_impact * 0.7,  # Partial reversal
            'transition_cost': self._calculate_transition_cost(original_test),
            'stakeholder_impact': self._assess_stakeholder_impact(original_test, rollback=True),
            'recommendations': ['Plan phased rollback', 'Communicate clearly with stakeholders'],
            'timestamp': datetime.now().isoformat()
        }
        
        return rollback_impact
    
    def _simulate_policy_impact(self, policy_params: Dict[str, Any]) -> Dict[str, Any]:
        """Simulate overall policy impact."""
        economic_impact = policy_params.get('economic_impact', 0.6)
        social_impact = policy_params.get('social_impact', 0.7)
        environmental_impact = policy_params.get('environmental_impact', 0.65)
        
        # Weighted impact score
        overall_impact = (
            economic_impact * 0.4 +
            social_impact * 0.35 +
            environmental_impact * 0.25
        )
        
        return {
            'overall_impact': overall_impact,
            'economic_impact': economic_impact,
            'social_impact': social_impact,
            'environmental_impact': environmental_impact,
            'estimated_cost': policy_params.get('implementation_cost', 100000),
            'timeline_months': policy_params.get('implementation_timeline', 6)
        }
    
    def _generate_policy_recommendations(self, impact_analysis: Dict[str, Any], 
                                        coherence_result: Optional[Dict[str, Any]]) -> List[str]:
        """Generate policy recommendations."""
        recommendations = []
        
        if impact_analysis['overall_impact'] < 0.5:
            recommendations.append('Reconsider policy design - low overall impact')
            recommendations.append('Engage stakeholders for feedback')
        
        if coherence_result and not coherence_result.get('coherent'):
            recommendations.append('Improve alignment with governance objectives')
        
        if impact_analysis['economic_impact'] < 0.5:
            recommendations.append('Assess economic viability')
        
        if not recommendations:
            recommendations.append('Policy shows positive indicators')
            recommendations.append('Proceed with pilot implementation')
        
        return recommendations
    
    def _assess_readiness(self, impact_analysis: Dict[str, Any]) -> str:
        """Assess implementation readiness."""
        impact = impact_analysis['overall_impact']
        
        if impact >= 0.75:
            return 'ready'
        elif impact >= 0.6:
            return 'needs_refinement'
        else:
            return 'not_ready'
    
    def _rank_policies(self, policies: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Rank policies by overall impact."""
        ranked = sorted(
            policies,
            key=lambda p: p['impact_analysis']['overall_impact'],
            reverse=True
        )
        
        return [
            {
                'rank': idx + 1,
                'policy_id': p['policy_id'],
                'impact_score': p['impact_analysis']['overall_impact']
            }
            for idx, p in enumerate(ranked)
        ]
    
    def _analyze_trade_offs(self, policies: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyze trade-offs between policies."""
        economic_scores = [p['impact_analysis']['economic_impact'] for p in policies]
        social_scores = [p['impact_analysis']['social_impact'] for p in policies]
        
        return {
            'economic_range': [min(economic_scores), max(economic_scores)],
            'social_range': [min(social_scores), max(social_scores)],
            'trade_off_exists': max(economic_scores) - min(economic_scores) > 0.2
        }
    
    def _select_best_policy(self, policies: List[Dict[str, Any]]) -> str:
        """Select best policy based on criteria."""
        best = max(policies, key=lambda p: p['impact_analysis']['overall_impact'])
        return best['policy_id']
    
    def _calculate_transition_cost(self, policy_test: Dict[str, Any]) -> float:
        """Calculate cost of policy transition."""
        implementation_cost = policy_test['impact_analysis']['estimated_cost']
        return implementation_cost * 0.3  # Transition typically 30% of implementation
    
    def _assess_stakeholder_impact(self, policy_test: Dict[str, Any], 
                                  rollback: bool = False) -> Dict[str, Any]:
        """Assess impact on stakeholders."""
        affected = policy_test['affected_population']
        impact_score = policy_test['impact_analysis']['overall_impact']
        
        if rollback:
            impact_score = -impact_score * 0.7
        
        return {
            'affected_population': affected,
            'positive_impact_percent': max(0, impact_score * 100),
            'negative_impact_percent': max(0, -impact_score * 100),
            'neutral_percent': 100 - abs(impact_score * 100)
        }
