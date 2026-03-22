def forecast_demand(historical_data, product_name, days_to_analyze=14):
    """
    Simulates demand forecasting by calculating the simple moving average 
    of daily sales for the specified product over the given period.
    """
    product_data = [row for row in historical_data if row['product'] == product_name]
    
    if not product_data:
        return 0
        
    # In a real scenario, date order matters. For this simple average, we just take the last 'days' entries.
    recent_data = product_data[-days_to_analyze:]
    
    if not recent_data:
        return 0
        
    total_sales = sum(row['units_sold'] for row in recent_data)
    average_daily_demand = total_sales / len(recent_data)
    
    return round(average_daily_demand, 2)


def calculate_dynamic_price(base_price, current_stock, forecasted_demand, price_surge_factor=0.20):
    """
    Calculates dynamic price based on stock and forecasted demand.
    If demand is consistently high (forecast > stock) or stock is critically low (<20% of demand),
    price increases.
    """
    # Defensive programming against div by zero
    if forecasted_demand <= 0:
        return base_price
        
    stock_to_demand_ratio = current_stock / forecasted_demand
    
    # Logic:
    # If stock is highly abundant compared to expected demand, price is normal.
    # If stock is less than 1.5x expected demand, slight surge.
    # If stock is less than expected demand (predicted to run out today), higher surge.
    
    if stock_to_demand_ratio < 1.0:
        # High likelihood of selling out, maximum surge
        adjusted_price = base_price * (1 + price_surge_factor)
        return round(adjusted_price, 2)
    elif stock_to_demand_ratio < 1.5:
        # Stock is getting low relative to demand, slight surge
        adjusted_price = base_price * (1 + (price_surge_factor / 2))
        return round(adjusted_price, 2)
    else:
        # Normal stock levels
        return base_price

