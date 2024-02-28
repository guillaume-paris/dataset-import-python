import pandas as pd
import matplotlib.pyplot as plt

file_path = 'datasets/Occupancy.csv'

df = pd.read_csv(file_path)

# Convert the 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])


def console_print(df):
    # Obtain global information about the dataset
    print("*****************\n Informations about the dataset\n*****************")
    df.info()
    # Obtain descriptive statistics for each column
    print("\n\n*****************\n Descriptive statistics\n*****************\n", df.describe())
    # Example of selection of specific columns
    df_selected = df[['Temperature', 'Humidity']]
    print("\n\n*****************\n Example of Temperature and Humidity column selection\n*****************\n",
          df_selected)
    # Example of selection of specific rows
    df_filtered = df[df['Temperature'] > 20]
    print("\n\n*****************\n Example of Temperature filter (>20)\n*****************\n", df_filtered)


def plot_generation(df):
    # Plots of C02 levels over time
    plt.figure(figsize=(14, 6))
    plt.plot(df['date'], df['CO2'], label='CO2 Levels')
    plt.title('CO2 Levels Over Time')
    plt.xlabel('Time')
    plt.ylabel('CO2 (ppm)')
    plt.legend()
    plt.show()

    # Extract hour of the day
    df['hour'] = df['date'].dt.hour

    # Group by hour and calculate mean CO2 levels
    hourly_co2 = df.groupby('hour')['CO2'].mean()

    # Plot average CO2 levels by hour of the day
    plt.figure(figsize=(10, 6))
    hourly_co2.plot(kind='bar')
    plt.title('Average CO2 Levels by Hour of the Day')
    plt.xlabel('Hour of the Day')
    plt.ylabel('Average CO2 (ppm)')
    plt.xticks(rotation=45)
    plt.show()

console_print(df)
plot_generation(df)