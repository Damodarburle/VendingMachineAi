from data_generator import generate_historical_data
from analytics import forecast_demand, calculate_dynamic_price

def run_simulation():
    print("=== Vending Machine Predictive Analytics Simulation ===\n")
    
    # 1. Generate 30 days of historical data
    print("Generating 30 days of historical transaction data...")
    history = generate_historical_data(days=30)
    
    # Products and their base configuration
    inventory = {
        'Cola': {'base_price': 1.50, 'current_stock': 25},
        'Chips': {'base_price': 1.00, 'current_stock': 15},
        'Water': {'base_price': 1.25, 'current_stock': 40},
        'Candy': {'base_price': 0.75, 'current_stock': 5}
    }
    
    print("\n--- Scenario 1: Normal Traffic ---")
    for product, details in inventory.items():
        expected_demand = forecast_demand(history, product)
        current_price = calculate_dynamic_price(
            details['base_price'], 
            details['current_stock'], 
            expected_demand
        )
        print(f"Product: {product:6} | Stock: {details['current_stock']:2} | Forecasted Demand: {expected_demand:5.2f} | Base Price: ${details['base_price']:.2f} -> Dynamic Price: ${current_price:.2f}")


    print("\n--- Scenario 2: +20% Dummy Traffic Spike ---")
    traffic_multiplier = 1.20
    
    for product, details in inventory.items():
        base_forecast = forecast_demand(history, product)
        spiked_demand = base_forecast * traffic_multiplier
        current_price = calculate_dynamic_price(
            details['base_price'], 
            details['current_stock'], 
            spiked_demand
        )
        print(f"Product: {product:6} | Stock: {details['current_stock']:2} | Spiked Demand:   {spiked_demand:5.2f} | Base Price: ${details['base_price']:.2f} -> Dynamic Price: ${current_price:.2f}")

if __name__ == "__main__":
    run_simulation()


