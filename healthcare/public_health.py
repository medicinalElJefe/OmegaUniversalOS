"""
Public Health Analyzer for population-level health ripple simulations.
"""

import logging
from typing import Dict, List, Any, Optional
from datetime import datetime


class PublicHealthAnalyzer:
    """
    Analyze public health trends and population ripple effects.
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Initialize public health analyzer.
        
        Args:
            config: Optional configuration dictionary
        """
        self.config = config or {}
        self.logger = logging.getLogger(__name__)
        self.population_data = {}
        
    def analyze_population_health(self, population_id: str, 
                                  health_metrics: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze population health metrics and ripple effects.
        
        Args:
            population_id: Population identifier (e.g., region, community)
            health_metrics: Aggregate health data for population
            
        Returns:
            Population health analysis
        """
        self.logger.info(f"Analyzing population health for: {population_id}")
        
        # Extract population metrics
        disease_prevalence = health_metrics.get('disease_prevalence', {})
        vaccination_rate = health_metrics.get('vaccination_rate', 0.7)
        healthcare_access = health_metrics.get('healthcare_access', 0.75)
        population_size = health_metrics.get('population_size', 10000)
        
        # Calculate population health score
        health_score = self._calculate_population_score(
            disease_prevalence, vaccination_rate, healthcare_access
        )
        
        # Identify vulnerable groups
        vulnerable_groups = self._identify_vulnerable_groups(health_metrics)
        
        analysis_result = {
            'population_id': population_id,
            'population_size': population_size,
            'overall_health_score': health_score,
            'vaccination_rate': vaccination_rate,
            'healthcare_access': healthcare_access,
            'vulnerable_groups': vulnerable_groups,
            'risk_level': self._assess_risk_level(health_score),
            'recommendations': self._generate_population_recommendations(health_score, vulnerable_groups),
            'timestamp': datetime.now().isoformat()
        }
        
        self.population_data[population_id] = analysis_result
        return analysis_result
    
    def simulate_public_health_intervention(self, population_id: str, 
                                           intervention: Dict[str, Any]) -> Dict[str, Any]:
        """
        Simulate impact of public health intervention.
        
        Args:
            population_id: Population identifier
            intervention: Public health intervention details
            
        Returns:
            Intervention impact simulation
        """
        self.logger.info(f"Simulating public health intervention for: {population_id}")
        
        if population_id not in self.population_data:
            return {'error': 'No baseline population data available'}
        
        baseline = self.population_data[population_id]
        
        intervention_type = intervention.get('type', 'vaccination_campaign')
        coverage = intervention.get('coverage', 0.7)
        duration_months = intervention.get('duration_months', 3)
        
        # Calculate expected impact
        current_score = baseline['overall_health_score']
        projected_improvement = self._calculate_intervention_impact(
            intervention_type, coverage, current_score
        )
        
        projected_score = min(1.0, current_score + projected_improvement)
        
        simulation_result = {
            'population_id': population_id,
            'intervention_type': intervention_type,
            'coverage': coverage,
            'duration_months': duration_months,
            'baseline_score': current_score,
            'projected_score': projected_score,
            'estimated_lives_saved': int(baseline['population_size'] * projected_improvement * 0.01),
            'cost_effectiveness': self._calculate_cost_effectiveness(intervention),
            'timestamp': datetime.now().isoformat()
        }
        
        return simulation_result
    
    def model_disease_spread(self, disease_params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Model disease spread dynamics using ripple propagation.
        
        Args:
            disease_params: Disease transmission parameters
            
        Returns:
            Disease spread model results
        """
        self.logger.info("Modeling disease spread dynamics")
        
        transmission_rate = disease_params.get('transmission_rate', 0.3)
        incubation_days = disease_params.get('incubation_days', 7)
        initial_cases = disease_params.get('initial_cases', 10)
        population_size = disease_params.get('population_size', 10000)
        
        # Simple SIR model simulation
        spread_model = {
            'day_0': {'susceptible': population_size - initial_cases, 'infected': initial_cases, 'recovered': 0},
            'day_7': self._calculate_sir_state(population_size, initial_cases, transmission_rate, 7),
            'day_14': self._calculate_sir_state(population_size, initial_cases, transmission_rate, 14),
            'day_30': self._calculate_sir_state(population_size, initial_cases, transmission_rate, 30),
            'peak_infection_day': self._estimate_peak_day(transmission_rate, incubation_days),
            'total_affected_estimate': int(population_size * min(0.7, transmission_rate * 2))
        }
        
        return spread_model
    
    def _calculate_population_score(self, disease_prevalence: Dict[str, float], 
                                   vaccination_rate: float, 
                                   healthcare_access: float) -> float:
        """Calculate overall population health score."""
        # Invert disease prevalence (lower is better)
        avg_prevalence = sum(disease_prevalence.values()) / len(disease_prevalence) if disease_prevalence else 0.1
        disease_score = 1.0 - min(1.0, avg_prevalence)
        
        # Combine factors
        population_score = (
            disease_score * 0.4 +
            vaccination_rate * 0.3 +
            healthcare_access * 0.3
        )
        
        return min(1.0, max(0.0, population_score))
    
    def _identify_vulnerable_groups(self, health_metrics: Dict[str, Any]) -> List[str]:
        """Identify vulnerable population groups."""
        vulnerable = []
        
        age_distribution = health_metrics.get('age_distribution', {})
        if age_distribution.get('elderly_percent', 0) > 0.15:
            vulnerable.append('Elderly population')
        
        if age_distribution.get('children_percent', 0) > 0.2:
            vulnerable.append('Pediatric population')
        
        if health_metrics.get('chronic_disease_rate', 0) > 0.25:
            vulnerable.append('Chronic disease patients')
        
        if health_metrics.get('low_income_percent', 0) > 0.3:
            vulnerable.append('Low-income communities')
        
        return vulnerable if vulnerable else ['No specific vulnerable groups identified']
    
    def _assess_risk_level(self, health_score: float) -> str:
        """Assess population health risk level."""
        if health_score >= 0.8:
            return 'low'
        elif health_score >= 0.6:
            return 'moderate'
        else:
            return 'high'
    
    def _generate_population_recommendations(self, health_score: float, 
                                            vulnerable_groups: List[str]) -> List[str]:
        """Generate public health recommendations."""
        recommendations = []
        
        if health_score < 0.6:
            recommendations.append('Implement urgent public health interventions')
            recommendations.append('Increase healthcare infrastructure capacity')
        
        if len(vulnerable_groups) > 2:
            recommendations.append('Prioritize targeted interventions for vulnerable groups')
            recommendations.append('Enhance community outreach programs')
        
        recommendations.append('Continue regular health monitoring and surveillance')
        recommendations.append('Promote preventive health education')
        
        return recommendations
    
    def _calculate_intervention_impact(self, intervention_type: str, 
                                      coverage: float, 
                                      current_score: float) -> float:
        """Calculate expected impact of intervention."""
        base_impact = {
            'vaccination_campaign': 0.15,
            'health_education': 0.08,
            'infrastructure_improvement': 0.12,
            'screening_program': 0.10
        }.get(intervention_type, 0.08)
        
        # Scale by coverage and current score gap
        score_gap = 1.0 - current_score
        adjusted_impact = base_impact * coverage * min(1.0, score_gap * 1.5)
        
        return adjusted_impact
    
    def _calculate_cost_effectiveness(self, intervention: Dict[str, Any]) -> str:
        """Calculate cost-effectiveness rating."""
        budget = intervention.get('budget', 100000)
        coverage = intervention.get('coverage', 0.7)
        
        cost_per_person = budget / (coverage * 1000) if coverage > 0 else float('inf')
        
        if cost_per_person < 50:
            return 'highly_cost_effective'
        elif cost_per_person < 200:
            return 'cost_effective'
        else:
            return 'expensive'
    
    def _calculate_sir_state(self, population: int, initial_infected: int, 
                            transmission_rate: float, days: int) -> Dict[str, int]:
        """Calculate SIR model state at given day (simplified)."""
        # Simplified exponential growth with saturation
        infected = min(
            int(initial_infected * (1 + transmission_rate) ** (days / 7)),
            int(population * 0.4)
        )
        recovered = int(infected * 0.2 * (days / 14))
        susceptible = population - infected - recovered
        
        return {
            'susceptible': max(0, susceptible),
            'infected': infected,
            'recovered': recovered
        }
    
    def _estimate_peak_day(self, transmission_rate: float, incubation_days: int) -> int:
        """Estimate peak infection day."""
        # Simplified estimation
        return int(30 + (1.0 - transmission_rate) * 20)
