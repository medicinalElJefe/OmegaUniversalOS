"""
Resource Allocation framework for governance optimization.
"""

import logging
from typing import Dict, List, Any, Optional
from datetime import datetime


class ResourceAllocator:
    """
    Optimize resource allocation using ripple analysis.
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Initialize resource allocator.
        
        Args:
            config: Optional configuration dictionary
        """
        self.config = config or {}
        self.logger = logging.getLogger(__name__)
        self.allocation_plans = {}
        
    def optimize_allocation(self, budget: float, 
                          priorities: Dict[str, float],
                          constraints: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Optimize resource allocation across priorities.
        
        Args:
            budget: Total budget available
            priorities: Dictionary of priority areas and their weights
            constraints: Optional constraints (min/max allocations, etc.)
            
        Returns:
            Optimized allocation plan
        """
        self.logger.info(f"Optimizing allocation for budget: {budget}")
        
        constraints = constraints or {}
        
        # Normalize priority weights
        total_weight = sum(priorities.values())
        normalized_priorities = {k: v/total_weight for k, v in priorities.items()}
        
        # Calculate base allocation
        base_allocation = {
            area: budget * weight
            for area, weight in normalized_priorities.items()
        }
        
        # Apply constraints
        adjusted_allocation = self._apply_constraints(base_allocation, constraints, budget)
        
        # Calculate impact
        impact_analysis = self._analyze_allocation_impact(adjusted_allocation)
        
        allocation_plan = {
            'total_budget': budget,
            'allocations': adjusted_allocation,
            'impact_analysis': impact_analysis,
            'efficiency_score': self._calculate_efficiency(adjusted_allocation, priorities),
            'recommendations': self._generate_allocation_recommendations(adjusted_allocation, impact_analysis),
            'timestamp': datetime.now().isoformat()
        }
        
        return allocation_plan
    
    def simulate_reallocation(self, current_allocation: Dict[str, float],
                            proposed_changes: Dict[str, float]) -> Dict[str, Any]:
        """
        Simulate impact of reallocating resources.
        
        Args:
            current_allocation: Current resource allocation
            proposed_changes: Proposed changes (positive = increase, negative = decrease)
            
        Returns:
            Reallocation impact analysis
        """
        self.logger.info("Simulating resource reallocation")
        
        # Calculate new allocation
        new_allocation = current_allocation.copy()
        for area, change in proposed_changes.items():
            new_allocation[area] = new_allocation.get(area, 0) + change
        
        # Analyze impacts
        current_impact = self._analyze_allocation_impact(current_allocation)
        new_impact = self._analyze_allocation_impact(new_allocation)
        
        reallocation_result = {
            'current_allocation': current_allocation,
            'new_allocation': new_allocation,
            'current_impact': current_impact,
            'projected_impact': new_impact,
            'impact_delta': new_impact['overall_impact'] - current_impact['overall_impact'],
            'affected_areas': list(proposed_changes.keys()),
            'recommendations': self._assess_reallocation(current_impact, new_impact),
            'timestamp': datetime.now().isoformat()
        }
        
        return reallocation_result
    
    def analyze_resource_gaps(self, allocation: Dict[str, float],
                             target_outcomes: Dict[str, float]) -> Dict[str, Any]:
        """
        Analyze gaps between current allocation and target outcomes.
        
        Args:
            allocation: Current resource allocation
            target_outcomes: Desired outcome levels per area
            
        Returns:
            Gap analysis report
        """
        self.logger.info("Analyzing resource gaps")
        
        gaps = {}
        for area, target in target_outcomes.items():
            current = allocation.get(area, 0)
            estimated_need = self._estimate_resource_need(target)
            gap = estimated_need - current
            
            gaps[area] = {
                'current_allocation': current,
                'estimated_need': estimated_need,
                'gap': gap,
                'gap_percentage': (gap / estimated_need * 100) if estimated_need > 0 else 0
            }
        
        gap_analysis = {
            'area_gaps': gaps,
            'total_gap': sum(g['gap'] for g in gaps.values()),
            'critical_gaps': [area for area, data in gaps.items() if data['gap_percentage'] > 30],
            'recommendations': self._generate_gap_recommendations(gaps),
            'timestamp': datetime.now().isoformat()
        }
        
        return gap_analysis
    
    def _apply_constraints(self, allocation: Dict[str, float],
                          constraints: Dict[str, Any],
                          total_budget: float) -> Dict[str, float]:
        """Apply allocation constraints."""
        adjusted = allocation.copy()
        
        # Apply minimum allocations
        min_allocations = constraints.get('minimums', {})
        for area, min_val in min_allocations.items():
            if area in adjusted:
                adjusted[area] = max(adjusted[area], min_val)
        
        # Apply maximum allocations
        max_allocations = constraints.get('maximums', {})
        for area, max_val in max_allocations.items():
            if area in adjusted:
                adjusted[area] = min(adjusted[area], max_val)
        
        # Normalize to budget
        total_allocated = sum(adjusted.values())
        if total_allocated != total_budget and total_allocated > 0:
            scale_factor = total_budget / total_allocated
            adjusted = {k: v * scale_factor for k, v in adjusted.items()}
        
        return adjusted
    
    def _analyze_allocation_impact(self, allocation: Dict[str, float]) -> Dict[str, Any]:
        """Analyze impact of allocation."""
        # Calculate impact scores per area
        area_impacts = {}
        for area, amount in allocation.items():
            # Simplified impact calculation
            area_impacts[area] = min(1.0, amount / 100000) * 0.8
        
        overall_impact = sum(area_impacts.values()) / len(area_impacts) if area_impacts else 0
        
        return {
            'overall_impact': overall_impact,
            'area_impacts': area_impacts,
            'high_impact_areas': [area for area, impact in area_impacts.items() if impact > 0.7],
            'low_impact_areas': [area for area, impact in area_impacts.items() if impact < 0.4]
        }
    
    def _calculate_efficiency(self, allocation: Dict[str, float],
                            priorities: Dict[str, float]) -> float:
        """Calculate allocation efficiency."""
        # Efficiency = alignment between allocation and priorities
        total = sum(allocation.values())
        if total == 0:
            return 0
        
        allocation_ratios = {k: v/total for k, v in allocation.items()}
        priority_total = sum(priorities.values())
        priority_ratios = {k: v/priority_total for k, v in priorities.items()}
        
        # Calculate alignment
        alignment_scores = []
        for area in allocation_ratios:
            if area in priority_ratios:
                diff = abs(allocation_ratios[area] - priority_ratios[area])
                alignment_scores.append(1.0 - diff)
        
        return sum(alignment_scores) / len(alignment_scores) if alignment_scores else 0
    
    def _generate_allocation_recommendations(self, allocation: Dict[str, float],
                                           impact_analysis: Dict[str, Any]) -> List[str]:
        """Generate allocation recommendations."""
        recommendations = []
        
        low_impact = impact_analysis.get('low_impact_areas', [])
        if low_impact:
            recommendations.append(f"Consider reallocating from low-impact areas: {', '.join(low_impact)}")
        
        high_impact = impact_analysis.get('high_impact_areas', [])
        if high_impact:
            recommendations.append(f"Maintain or increase allocation to high-impact areas: {', '.join(high_impact)}")
        
        if impact_analysis['overall_impact'] < 0.6:
            recommendations.append("Overall impact is suboptimal - review allocation strategy")
        
        return recommendations if recommendations else ["Current allocation is well-optimized"]
    
    def _assess_reallocation(self, current_impact: Dict[str, Any],
                           new_impact: Dict[str, Any]) -> List[str]:
        """Assess reallocation recommendations."""
        recommendations = []
        
        delta = new_impact['overall_impact'] - current_impact['overall_impact']
        
        if delta > 0.1:
            recommendations.append("Reallocation shows significant positive impact - recommend proceeding")
        elif delta > 0:
            recommendations.append("Reallocation shows modest improvement")
        elif delta < -0.1:
            recommendations.append("Reallocation may reduce overall impact - reconsider")
        else:
            recommendations.append("Reallocation has minimal impact")
        
        return recommendations
    
    def _estimate_resource_need(self, target_outcome: float) -> float:
        """Estimate resource need for target outcome."""
        # Simplified estimation: linear relationship
        return target_outcome * 150000
    
    def _generate_gap_recommendations(self, gaps: Dict[str, Dict[str, Any]]) -> List[str]:
        """Generate recommendations for closing gaps."""
        recommendations = []
        
        critical_gaps = [area for area, data in gaps.items() if data['gap_percentage'] > 30]
        
        if critical_gaps:
            recommendations.append(f"Priority: Address critical gaps in {', '.join(critical_gaps)}")
        
        total_gap = sum(g['gap'] for g in gaps.values())
        if total_gap > 0:
            recommendations.append(f"Total additional resources needed: ${total_gap:,.2f}")
        
        recommendations.append("Consider phased approach to gap closure")
        
        return recommendations
