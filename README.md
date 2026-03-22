# Vending Machine Predictive Analytics

A Python-based predictive analytics module designed for smart vending machine systems. This project simulates historical transaction data to forecast daily product demand and applies dynamic pricing logic to maximize revenue and manage inventory when stock becomes critically low relative to demand.

## Features

- **Historical Data Generation**: Simulates 30 days of past transaction data with realistic sales volumes and slight random variations for different product categories (Cola, Chips, Water, Candy).
- **Demand Forecasting**: Calculates a simple moving average to predict the expected demand for each product.
- **Dynamic Pricing Engine**: Analyzes the ratio of current physical stock to the forecasted demand.
  - Applies a **10% Price Surge** if stock is running low (< 1.5x expected demand).
  - Applies a **20% Price Surge** if stock is critically low and likely to sell out (< 1.0x expected demand).
- **Traffic Spikes**: Includes simulation logic to demonstrate how the pricing engine instantly reacts to artificial demand bursts (e.g., a sudden 20% increase in foot traffic due to an event).

## Project Structure

- `data_generator.py`: Generates the mock daily transaction data.
- `analytics.py`: Contains the `forecast_demand` and `calculate_dynamic_price` algorithms.
- `simulation.py`: The main execution script that runs the predictive model against a normal traffic scenario and a +20% demand spike scenario.
- `simulation_results.txt`: The expected terminal output from running the simulation.

## How to Run

1. Ensure you have Python 3 installed.
2. Clone this repository.
3. Run the simulation script from your terminal:

```bash
python simulation.py
```

The script will automatically generate new historical data, calculate the base forecasts, and print the dynamic pricing adjustments directly to your console for both scenarios!
