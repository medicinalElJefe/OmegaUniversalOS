"""
Student Ripple Tracker for monitoring learning coherence and progress.
"""

import logging
from typing import Dict, List, Any, Optional
from datetime import datetime


class StudentRippleTracker:
    """
    Track student learning ripple effects and coherence.
    """
    
    def __init__(self, ripple_engine=None):
        """
        Initialize student ripple tracker.
        
        Args:
            ripple_engine: Optional RippleEngine instance for validation
        """
        self.logger = logging.getLogger(__name__)
        self.ripple_engine = ripple_engine
        self.student_ripples = {}
        
    def track_student_ripple(self, student_id: str, 
                            learning_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Track ripple effects of student learning activities.
        
        Args:
            student_id: Student identifier
            learning_data: Learning activity and performance data
            
        Returns:
            Ripple tracking report
        """
        self.logger.info(f"Tracking ripple for student: {student_id}")
        
        # Calculate ripple parameters
        engagement = learning_data.get('engagement_score', 0.7)
        comprehension = learning_data.get('comprehension_score', 0.75)
        collaboration = learning_data.get('collaboration_score', 0.6)
        
        ripple_data = {
            'impact_score': (engagement * 0.4 + comprehension * 0.4 + collaboration * 0.2),
            'alignment': learning_data.get('curriculum_alignment', 0.8),
            'domain': 'education',
            'student_id': student_id
        }
        
        # Validate with ripple engine if available
        coherence_result = None
        if self.ripple_engine:
            coherence_result = self.ripple_engine.validate_coherence(ripple_data)
        
        tracking_report = {
            'student_id': student_id,
            'ripple_data': ripple_data,
            'coherence_result': coherence_result,
            'recommendations': self._generate_student_recommendations(ripple_data),
            'timestamp': datetime.now().isoformat()
        }
        
        # Store tracking data
        if student_id not in self.student_ripples:
            self.student_ripples[student_id] = []
        self.student_ripples[student_id].append(tracking_report)
        
        return tracking_report
    
    def analyze_learning_trajectory(self, student_id: str) -> Dict[str, Any]:
        """
        Analyze student learning trajectory over time.
        
        Args:
            student_id: Student identifier
            
        Returns:
            Trajectory analysis report
        """
        self.logger.info(f"Analyzing learning trajectory for student: {student_id}")
        
        if student_id not in self.student_ripples:
            return {'error': 'No tracking data available for student'}
        
        ripple_history = self.student_ripples[student_id]
        
        # Analyze trends
        impact_scores = [r['ripple_data']['impact_score'] for r in ripple_history]
        
        trajectory_analysis = {
            'student_id': student_id,
            'data_points': len(ripple_history),
            'average_impact': sum(impact_scores) / len(impact_scores) if impact_scores else 0,
            'trend': self._calculate_trend(impact_scores),
            'coherence_stability': self._assess_stability(ripple_history),
            'intervention_needed': self._check_intervention_needed(impact_scores),
            'timestamp': datetime.now().isoformat()
        }
        
        return trajectory_analysis
    
    def generate_coherence_feedback(self, student_id: str) -> Dict[str, Any]:
        """
        Generate coherence-based feedback for student.
        
        Args:
            student_id: Student identifier
            
        Returns:
            Coherence feedback report
        """
        self.logger.info(f"Generating coherence feedback for student: {student_id}")
        
        trajectory = self.analyze_learning_trajectory(student_id)
        
        if 'error' in trajectory:
            return trajectory
        
        feedback = {
            'student_id': student_id,
            'overall_coherence': 'high' if trajectory['average_impact'] > 0.7 else 'medium',
            'strengths': self._identify_strengths(trajectory),
            'improvement_areas': self._identify_improvements(trajectory),
            'action_items': self._generate_action_items(trajectory),
            'timestamp': datetime.now().isoformat()
        }
        
        return feedback
    
    def _generate_student_recommendations(self, ripple_data: Dict[str, Any]) -> List[str]:
        """Generate recommendations based on ripple data."""
        recommendations = []
        
        impact = ripple_data.get('impact_score', 0)
        
        if impact < 0.5:
            recommendations.append('Increase active learning engagement')
            recommendations.append('Review foundational concepts')
        elif impact < 0.7:
            recommendations.append('Continue current learning approach')
            recommendations.append('Consider peer collaboration activities')
        else:
            recommendations.append('Excellent progress - consider advanced materials')
            recommendations.append('Serve as peer mentor')
        
        return recommendations
    
    def _calculate_trend(self, scores: List[float]) -> str:
        """Calculate trend from score history."""
        if len(scores) < 2:
            return 'insufficient_data'
        
        recent_avg = sum(scores[-3:]) / min(3, len(scores[-3:]))
        earlier_avg = sum(scores[:3]) / min(3, len(scores[:3]))
        
        if recent_avg > earlier_avg + 0.1:
            return 'improving'
        elif recent_avg < earlier_avg - 0.1:
            return 'declining'
        else:
            return 'stable'
    
    def _assess_stability(self, ripple_history: List[Dict[str, Any]]) -> str:
        """Assess coherence stability."""
        if len(ripple_history) < 3:
            return 'insufficient_data'
        
        # Calculate variance in impact scores
        scores = [r['ripple_data']['impact_score'] for r in ripple_history]
        mean = sum(scores) / len(scores)
        variance = sum((x - mean) ** 2 for x in scores) / len(scores)
        
        if variance < 0.05:
            return 'high_stability'
        elif variance < 0.15:
            return 'moderate_stability'
        else:
            return 'low_stability'
    
    def _check_intervention_needed(self, scores: List[float]) -> bool:
        """Check if intervention is needed."""
        if len(scores) < 2:
            return False
        
        recent_scores = scores[-3:]
        return sum(recent_scores) / len(recent_scores) < 0.5
    
    def _identify_strengths(self, trajectory: Dict[str, Any]) -> List[str]:
        """Identify student strengths."""
        strengths = []
        
        if trajectory['average_impact'] > 0.7:
            strengths.append('Strong overall performance')
        
        if trajectory['trend'] == 'improving':
            strengths.append('Positive learning trajectory')
        
        if trajectory['coherence_stability'] == 'high_stability':
            strengths.append('Consistent engagement')
        
        return strengths if strengths else ['Developing competency']
    
    def _identify_improvements(self, trajectory: Dict[str, Any]) -> List[str]:
        """Identify areas for improvement."""
        improvements = []
        
        if trajectory['average_impact'] < 0.6:
            improvements.append('Increase learning engagement')
        
        if trajectory['trend'] == 'declining':
            improvements.append('Address recent performance decline')
        
        if trajectory['coherence_stability'] == 'low_stability':
            improvements.append('Improve consistency in learning activities')
        
        return improvements if improvements else ['Maintain current approach']
    
    def _generate_action_items(self, trajectory: Dict[str, Any]) -> List[str]:
        """Generate actionable items."""
        actions = []
        
        if trajectory.get('intervention_needed'):
            actions.append('Schedule one-on-one tutoring session')
            actions.append('Review learning materials with instructor')
        else:
            actions.append('Continue regular progress monitoring')
            actions.append('Explore enrichment opportunities')
        
        return actions
