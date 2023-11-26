import pandas as pd
import matplotlib.pyplot as plt

# Assuming the data is already in a CSV file
df = pd.read_excel('traffic_data.xlsx')

# Group by 'linkId' and calculate the mean 'travelTime'
average_travel_times = df.groupby('linkId')['travelTime'].mean().reset_index()

# Sort the results in descending order of average travel time
sorted_linkids = average_travel_times.sort_values('travelTime', ascending=False)

# Prepare table data
table_data = sorted_linkids.values.tolist()

# Plot table
plt.figure(figsize=(12, 8))
plt.axis('off')  # Hide axis
table = plt.table(cellText=table_data, colLabels=sorted_linkids.columns, loc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)  # You can adjust the scaling as per your needs
plt.title('Ranked Link IDs by Average Travel Time')
plt.show()
