"""
Trade-Off Analyzer for economic decision analysis.
"""

import logging
from typing import Dict, List, Any, Optional
from datetime import datetime


class TradeOffAnalyzer:
    """
    Analyze economic trade-offs and ripple effects.
    """
    
    def __init__(self, ripple_engine=None, config: Optional[Dict[str, Any]] = None):
        """
        Initialize trade-off analyzer.
        
        Args:
            ripple_engine: Optional RippleEngine instance
            config: Optional configuration dictionary
        """
        self.config = config or {}
        self.logger = logging.getLogger(__name__)
        self.ripple_engine = ripple_engine
        self.analyses = {}
        
    def analyze_trade_offs(self, decision_id: str, 
                          options: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Analyze trade-offs between economic options.
        
        Args:
            decision_id: Unique decision identifier
            options: List of option configurations
            
        Returns:
            Trade-off analysis with recommendations
        """
        self.logger.info(f"Analyzing trade-offs for decision: {decision_id}")
        
        if len(options) < 2:
            return {'error': 'Need at least 2 options to analyze trade-offs'}
        
        # Analyze each option
        option_analyses = []
        for idx, option in enumerate(options):
            analysis = self._analyze_option(f"{decision_id}_option_{idx}", option)
            option_analyses.append(analysis)
        
        # Compare options
        comparison = self._compare_options(option_analyses)
        
        # Calculate ripple effects
        ripple_effects = []
        if self.ripple_engine:
            for analysis in option_analyses:
                ripple_data = {
                    'impact_score': analysis['economic_impact'],
                    'alignment': analysis['alignment_score'],
                    'domain': 'economics'
                }
                ripple_effect = self.ripple_engine.validate_coherence(ripple_data)
                ripple_effects.append(ripple_effect)
        
        trade_off_analysis = {
            'decision_id': decision_id,
            'options_analyzed': len(options),
            'option_analyses': option_analyses,
            'comparison': comparison,
            'ripple_effects': ripple_effects,
            'recommended_option': comparison['best_option_index'],
            'trade_off_acceptable': self._assess_trade_off_acceptability(comparison),
            'timestamp': datetime.now().isoformat()
        }
        
        self.analyses[decision_id] = trade_off_analysis
        return trade_off_analysis
    
    def validate_alignment(self, decision_id: str, 
                          economic_objectives: Dict[str, float]) -> Dict[str, Any]:
        """
        Validate alignment of decision with economic objectives.
        
        Args:
            decision_id: Decision identifier
            economic_objectives: Target economic objectives with weights
            
        Returns:
            Alignment validation report
        """
        self.logger.info(f"Validating alignment for decision: {decision_id}")
        
        if decision_id not in self.analyses:
            return {'error': 'Decision not found'}
        
        analysis = self.analyses[decision_id]
        recommended_idx = analysis['recommended_option']
        recommended_option = analysis['option_analyses'][recommended_idx]
        
        # Calculate alignment with objectives
        alignment_scores = {}
        for objective, target_weight in economic_objectives.items():
            option_value = recommended_option.get(objective, 0.5)
            alignment_scores[objective] = min(1.0, option_value / target_weight) if target_weight > 0 else 0.5
        
        overall_alignment = sum(alignment_scores.values()) / len(alignment_scores) if alignment_scores else 0
        
        validation_result = {
            'decision_id': decision_id,
            'overall_alignment': overall_alignment,
            'objective_alignments': alignment_scores,
            'well_aligned': overall_alignment >= 0.7,
            'misaligned_objectives': [obj for obj, score in alignment_scores.items() if score < 0.6],
            'recommendations': self._generate_alignment_recommendations(overall_alignment, alignment_scores),
            'timestamp': datetime.now().isoformat()
        }
        
        return validation_result
    
    def simulate_ripple_effects(self, economic_change: Dict[str, Any]) -> Dict[str, Any]:
        """
        Simulate ripple effects of an economic change.
        
        Args:
            economic_change: Economic change parameters
            
        Returns:
            Ripple effect simulation
        """
        self.logger.info("Simulating economic ripple effects")
        
        change_magnitude = economic_change.get('magnitude', 0.1)
        affected_sectors = economic_change.get('affected_sectors', [])
        
        # Simulate direct and indirect effects
        direct_impact = self._calculate_direct_impact(economic_change)
        indirect_impact = self._calculate_indirect_impact(economic_change, affected_sectors)
        
        # Propagate ripples
        propagation_chain = []
        if self.ripple_engine:
            ripple_data = {
                'impact_score': direct_impact,
                'alignment': economic_change.get('policy_alignment', 0.75),
                'domain': 'economics'
            }
            propagation_chain = self.ripple_engine.simulate_propagation(ripple_data, depth=4)
        
        simulation_result = {
            'change_type': economic_change.get('type', 'market_adjustment'),
            'magnitude': change_magnitude,
            'direct_impact': direct_impact,
            'indirect_impact': indirect_impact,
            'total_impact': direct_impact + indirect_impact * 0.5,
            'affected_sectors': affected_sectors,
            'propagation_chain': propagation_chain,
            'stabilization_time': self._estimate_stabilization_time(change_magnitude),
            'timestamp': datetime.now().isoformat()
        }
        
        return simulation_result
    
    def _analyze_option(self, option_id: str, option: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze a single option."""
        return {
            'option_id': option_id,
            'economic_impact': option.get('economic_impact', 0.6),
            'implementation_cost': option.get('cost', 100000),
            'roi': option.get('roi', 1.5),
            'risk_level': option.get('risk_level', 'medium'),
            'timeline_months': option.get('timeline', 12),
            'alignment_score': option.get('strategic_alignment', 0.7),
            'sustainability': option.get('sustainability', 0.65)
        }
    
    def _compare_options(self, option_analyses: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Compare analyzed options."""
        # Score each option
        scores = []
        for option in option_analyses:
            score = (
                option['economic_impact'] * 0.3 +
                min(option['roi'] / 2.0, 1.0) * 0.3 +
                option['alignment_score'] * 0.2 +
                option['sustainability'] * 0.2
            )
            scores.append(score)
        
        best_idx = scores.index(max(scores))
        
        return {
            'option_scores': scores,
            'best_option_index': best_idx,
            'best_option_score': scores[best_idx],
            'score_range': [min(scores), max(scores)],
            'clear_winner': max(scores) - min(scores) > 0.2
        }
    
    def _assess_trade_off_acceptability(self, comparison: Dict[str, Any]) -> bool:
        """Assess if trade-offs are acceptable."""
        best_score = comparison['best_option_score']
        score_range = comparison['score_range']
        
        # Trade-off is acceptable if best option is significantly better
        # and overall score is above threshold
        return best_score > 0.6 and (score_range[1] - score_range[0]) > 0.15
    
    def _generate_alignment_recommendations(self, overall_alignment: float,
                                          alignment_scores: Dict[str, float]) -> List[str]:
        """Generate alignment recommendations."""
        recommendations = []
        
        if overall_alignment < 0.6:
            recommendations.append("Realign decision with economic objectives")
        
        misaligned = [obj for obj, score in alignment_scores.items() if score < 0.6]
        if misaligned:
            recommendations.append(f"Address misalignment in: {', '.join(misaligned)}")
        
        if overall_alignment >= 0.8:
            recommendations.append("Excellent alignment - proceed with confidence")
        
        return recommendations if recommendations else ["Alignment is satisfactory"]
    
    def _calculate_direct_impact(self, economic_change: Dict[str, Any]) -> float:
        """Calculate direct economic impact."""
        magnitude = economic_change.get('magnitude', 0.1)
        change_type = economic_change.get('type', 'neutral')
        
        type_multipliers = {
            'stimulus': 1.3,
            'regulation': 0.8,
            'tax_change': 1.1,
            'market_adjustment': 1.0
        }
        
        multiplier = type_multipliers.get(change_type, 1.0)
        return min(1.0, abs(magnitude) * multiplier)
    
    def _calculate_indirect_impact(self, economic_change: Dict[str, Any],
                                   affected_sectors: List[str]) -> float:
        """Calculate indirect economic impact."""
        direct_impact = self._calculate_direct_impact(economic_change)
        
        # Indirect impact scales with number of affected sectors
        sector_multiplier = min(len(affected_sectors) * 0.1, 0.5)
        
        return direct_impact * sector_multiplier
    
    def _estimate_stabilization_time(self, magnitude: float) -> str:
        """Estimate time for economic stabilization."""
        if magnitude < 0.1:
            return "1-3 months"
        elif magnitude < 0.3:
            return "3-6 months"
        elif magnitude < 0.5:
            return "6-12 months"
        else:
            return "12+ months"
