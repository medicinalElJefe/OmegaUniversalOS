"""
Market Simulator for economic modeling and prediction.
"""

import logging
from typing import Dict, List, Any, Optional
from datetime import datetime
import random


class MarketSimulator:
    """
    Simulate market dynamics and economic scenarios.
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Initialize market simulator.
        
        Args:
            config: Optional configuration dictionary
        """
        self.config = config or {}
        self.logger = logging.getLogger(__name__)
        self.simulations = {}
        
    def simulate_market_scenario(self, scenario_id: str,
                                 market_params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Simulate a market scenario.
        
        Args:
            scenario_id: Unique scenario identifier
            market_params: Market parameters and initial conditions
            
        Returns:
            Market simulation results
        """
        self.logger.info(f"Simulating market scenario: {scenario_id}")
        
        # Extract market parameters
        initial_price = market_params.get('initial_price', 100.0)
        volatility = market_params.get('volatility', 0.15)
        trend = market_params.get('trend', 0.02)
        time_periods = market_params.get('time_periods', 12)
        
        # Run simulation
        price_trajectory = self._simulate_price_trajectory(
            initial_price, volatility, trend, time_periods
        )
        
        # Calculate market metrics
        metrics = self._calculate_market_metrics(price_trajectory)
        
        simulation_result = {
            'scenario_id': scenario_id,
            'initial_price': initial_price,
            'final_price': price_trajectory[-1],
            'price_trajectory': price_trajectory,
            'metrics': metrics,
            'market_regime': self._identify_market_regime(metrics),
            'risk_assessment': self._assess_market_risk(volatility, metrics),
            'timestamp': datetime.now().isoformat()
        }
        
        self.simulations[scenario_id] = simulation_result
        return simulation_result
    
    def simulate_supply_demand(self, market_id: str,
                              supply_demand_params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Simulate supply and demand dynamics.
        
        Args:
            market_id: Market identifier
            supply_demand_params: Supply and demand parameters
            
        Returns:
            Supply-demand simulation results
        """
        self.logger.info(f"Simulating supply-demand for market: {market_id}")
        
        # Extract parameters
        initial_supply = supply_demand_params.get('initial_supply', 1000)
        initial_demand = supply_demand_params.get('initial_demand', 1000)
        price_elasticity_supply = supply_demand_params.get('price_elasticity_supply', 0.5)
        price_elasticity_demand = supply_demand_params.get('price_elasticity_demand', -0.4)
        
        # Find equilibrium
        equilibrium = self._find_equilibrium(
            initial_supply, initial_demand,
            price_elasticity_supply, price_elasticity_demand
        )
        
        # Simulate market clearing
        market_clearing = self._simulate_market_clearing(equilibrium)
        
        simulation_result = {
            'market_id': market_id,
            'initial_supply': initial_supply,
            'initial_demand': initial_demand,
            'equilibrium': equilibrium,
            'market_clearing': market_clearing,
            'efficiency': self._calculate_market_efficiency(equilibrium),
            'timestamp': datetime.now().isoformat()
        }
        
        return simulation_result
    
    def predict_market_trend(self, historical_data: List[float],
                           forecast_periods: int = 6) -> Dict[str, Any]:
        """
        Predict market trend based on historical data.
        
        Args:
            historical_data: List of historical price/value data
            forecast_periods: Number of periods to forecast
            
        Returns:
            Market trend prediction
        """
        self.logger.info(f"Predicting market trend for {forecast_periods} periods")
        
        if len(historical_data) < 3:
            return {'error': 'Insufficient historical data'}
        
        # Calculate trend
        trend = self._calculate_trend(historical_data)
        volatility = self._calculate_volatility(historical_data)
        
        # Generate forecast
        forecast = self._generate_forecast(
            historical_data[-1], trend, volatility, forecast_periods
        )
        
        prediction_result = {
            'historical_periods': len(historical_data),
            'forecast_periods': forecast_periods,
            'detected_trend': trend,
            'volatility': volatility,
            'forecast': forecast,
            'confidence_level': self._calculate_forecast_confidence(volatility),
            'trend_direction': 'upward' if trend > 0.01 else 'downward' if trend < -0.01 else 'stable',
            'timestamp': datetime.now().isoformat()
        }
        
        return prediction_result
    
    def _simulate_price_trajectory(self, initial_price: float, volatility: float,
                                   trend: float, periods: int) -> List[float]:
        """Simulate price trajectory over time."""
        prices = [initial_price]
        
        for _ in range(periods - 1):
            # Random walk with drift
            random_shock = random.gauss(0, volatility)
            new_price = prices[-1] * (1 + trend + random_shock)
            prices.append(max(0.01, new_price))  # Prevent negative prices
        
        return prices
    
    def _calculate_market_metrics(self, price_trajectory: List[float]) -> Dict[str, Any]:
        """Calculate market performance metrics."""
        if len(price_trajectory) < 2:
            return {}
        
        returns = [
            (price_trajectory[i] - price_trajectory[i-1]) / price_trajectory[i-1]
            for i in range(1, len(price_trajectory))
        ]
        
        avg_return = sum(returns) / len(returns) if returns else 0
        volatility = (sum((r - avg_return) ** 2 for r in returns) / len(returns)) ** 0.5 if returns else 0
        
        return {
            'average_return': avg_return,
            'volatility': volatility,
            'total_return': (price_trajectory[-1] - price_trajectory[0]) / price_trajectory[0],
            'max_price': max(price_trajectory),
            'min_price': min(price_trajectory)
        }
    
    def _identify_market_regime(self, metrics: Dict[str, Any]) -> str:
        """Identify current market regime."""
        total_return = metrics.get('total_return', 0)
        volatility = metrics.get('volatility', 0)
        
        if total_return > 0.15 and volatility < 0.2:
            return 'bull_market'
        elif total_return < -0.15 and volatility > 0.2:
            return 'bear_market'
        elif volatility > 0.25:
            return 'volatile'
        else:
            return 'stable'
    
    def _assess_market_risk(self, volatility: float, metrics: Dict[str, Any]) -> str:
        """Assess market risk level."""
        if volatility > 0.3 or metrics.get('volatility', 0) > 0.25:
            return 'high'
        elif volatility > 0.15 or metrics.get('volatility', 0) > 0.15:
            return 'medium'
        else:
            return 'low'
    
    def _find_equilibrium(self, supply: float, demand: float,
                         elasticity_supply: float, elasticity_demand: float) -> Dict[str, Any]:
        """Find market equilibrium."""
        # Simplified equilibrium calculation
        # Assume base price of 100
        base_price = 100.0
        
        # Equilibrium where supply = demand
        if supply > demand:
            # Excess supply -> lower price
            price_adjustment = -0.1 * (supply - demand) / demand
        else:
            # Excess demand -> higher price
            price_adjustment = 0.1 * (demand - supply) / supply
        
        equilibrium_price = base_price * (1 + price_adjustment)
        equilibrium_quantity = (supply + demand) / 2
        
        return {
            'price': equilibrium_price,
            'quantity': equilibrium_quantity,
            'surplus': 0  # At equilibrium, no surplus
        }
    
    def _simulate_market_clearing(self, equilibrium: Dict[str, Any]) -> Dict[str, Any]:
        """Simulate market clearing process."""
        return {
            'clearing_price': equilibrium['price'],
            'clearing_quantity': equilibrium['quantity'],
            'time_to_clear': 'immediate',  # Simplified
            'unmet_demand': 0,
            'excess_supply': 0
        }
    
    def _calculate_market_efficiency(self, equilibrium: Dict[str, Any]) -> float:
        """Calculate market efficiency score."""
        # Simplified efficiency measure
        # Higher efficiency when equilibrium is achieved quickly
        return 0.85  # Placeholder for demonstration
    
    def _calculate_trend(self, data: List[float]) -> float:
        """Calculate trend from historical data."""
        if len(data) < 2:
            return 0
        
        # Simple linear trend
        returns = [(data[i] - data[i-1]) / data[i-1] for i in range(1, len(data))]
        return sum(returns) / len(returns) if returns else 0
    
    def _calculate_volatility(self, data: List[float]) -> float:
        """Calculate volatility from historical data."""
        if len(data) < 2:
            return 0
        
        returns = [(data[i] - data[i-1]) / data[i-1] for i in range(1, len(data))]
        avg_return = sum(returns) / len(returns) if returns else 0
        variance = sum((r - avg_return) ** 2 for r in returns) / len(returns) if returns else 0
        
        return variance ** 0.5
    
    def _generate_forecast(self, last_value: float, trend: float,
                          volatility: float, periods: int) -> List[float]:
        """Generate forecast values."""
        forecast = [last_value]
        
        for _ in range(periods):
            # Add trend and some uncertainty
            uncertainty = random.gauss(0, volatility * 0.5)
            next_value = forecast[-1] * (1 + trend + uncertainty)
            forecast.append(max(0.01, next_value))
        
        return forecast[1:]  # Exclude the starting point
    
    def _calculate_forecast_confidence(self, volatility: float) -> str:
        """Calculate confidence level for forecast."""
        if volatility < 0.1:
            return 'high'
        elif volatility < 0.2:
            return 'medium'
        else:
            return 'low'
