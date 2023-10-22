import pandas as pd
import time
from datetime import datetime, timedelta

# Define the CSV file path (replace with your CSV file)
csv_file = "crowd_store1.csv"

'''# Making up some data
day = ['2023-10-22', '2023-10-22', '2023-10-22', '2023-10-20', '2023-10-20', '2023-10-20', '2023-10-20', '2023-10-20', '2023-10-20', '2023-10-20', '2023-10-20', '2023-10-20', '2023-10-20', '2023-10-22']
timestamp = ['8:00:00', '8:05:00','8:09:00','12:00:00','12:05:00','13:15:00', '13:30:00', '13:40:00', '14:30:00', '14:10:00','14:11:00','15:45:00','16:00:00','19:00:00']
crowd = [1, 1, 1, 1, 1, 3, 4, 1, 1, 2, 3, 4, 2, 2]

data = {
    'Day': day,
    'Time': timestamp,
    'Crowd': crowd,
}

df = pd.DataFrame(data)

df.to_csv("crowd_store1.csv", index=False)
'''

# Function to read and process the CSV file
def read_and_process_csv(csv_file):
    try:
        # Combine columns data and time
        df = pd.read_csv(csv_file)
        df['datetime'] = pd.to_datetime(df['Day'] + ' ' + df['Time'])

        # Calculate the time threshold for the last hour
        current_time = datetime.now()
        print(current_time)
        last_hour_time = current_time - timedelta(hours=1)

        # Find crowd average in the last hour
        last_hour_df = df[df['datetime'] >= last_hour_time]
        average_crowd_level = last_hour_df['Crowd'].mean()

        print(f"Average Crowd Level in the Last Hour: {average_crowd_level:.2f}")
    except FileNotFoundError:
        print(f"File {csv_file} not found.")
    except pd.errors.EmptyDataError:
        print(f"File {csv_file} is empty.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Set the interval (in seconds) for reading the CSV file
refresh_interval = 120  

while True:
    read_and_process_csv(csv_file)
    time.sleep(refresh_interval)