import random
from datetime import datetime, timedelta

def generate_historical_data(days=30):
    """
    Generates dummy historical transaction data.
    Returns a list of dictionaries containing daily sales data.
    """
    data = []
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)

    products = ['Cola', 'Chips', 'Water', 'Candy']

    current_date = start_date
    while current_date <= end_date:
        for product in products:
            # Generate random daily demand (sales volume)
            # Cola and Water sell more than Chips and Candy
            if product in ['Cola', 'Water']:
                base_demand = random.randint(15, 30)
            else:
                base_demand = random.randint(5, 15)
                
            # Add some noise/randomness
            actual_demand = base_demand + random.randint(-5, 5)
            actual_demand = max(0, actual_demand) # Ensure non-negative

            data.append({
                'date': current_date.strftime('%Y-%m-%d'),
                'product': product,
                'units_sold': actual_demand
            })
        current_date += timedelta(days=1)
        
    return data

if __name__ == "__main__":
    # Test generation
    sample_data = generate_historical_data(days=5)
    for row in sample_data[:10]:
        print(row)
