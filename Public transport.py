import pandas as pd
import matplotlib.pyplot as plt

# Load data (replace 'your_data.csv' with the path to your actual data file)
routes = pd.read_csv('routes.csv')  # Information about routes
trips = pd.read_csv('trips.csv')    # Trips for each route
stop_times = pd.read_csv('stop_times.csv')  # Times at each stop for each trip

# Let's say we want to analyze route utilization
# Merge trips with routes to get complete route info for each trip
trip_details = pd.merge(trips, routes, on='route_id')

# Analyze the frequency of trips on each route
route_frequency = trip_details['route_short_name'].value_counts()

# Plotting the frequency of trips per route
plt.figure(figsize=(10, 6))
route_frequency.plot(kind='bar')
plt.title('Frequency of Trips per Route')
plt.xlabel('Route')
plt.ylabel('Number of Trips')
plt.show()
