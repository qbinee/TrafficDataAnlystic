import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('traffic_data.xlsx')

# Plotting
plt.figure(figsize=(12, 6))
for linkid in df['linkId'].unique():
    subset = df[df['linkId'] == linkid]
    plt.plot(subset['createdDate'], subset['travelTime'], label=f'Link ID: {linkid}')

plt.xlabel('Created Date')
plt.ylabel('Travel Time')
plt.title('Travel Time / Created Date for each Link ID')
plt.legend()
plt.show()
