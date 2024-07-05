import numpy as np
import matplotlib.pyplot as plt

import random
from datetime import datetime, timedelta
import pandas as pd
def collective_anomaly():
    # Generate synthetic heartbeat data
    time = np.linspace(0, 30, 30)  # 10 seconds, sampled 1000 times
    heartbeat = np.sin(2 * np.pi * 1 * time) + 0.5 * np.sin(2 * np.pi * 2 * time)

    # Introduce irregularity in the heartbeat
    irregularity_start = 15
    irregularity_end = 20
    heartbeat[irregularity_start:irregularity_end] = 0.1 * np.random.randn(irregularity_end - irregularity_start)

    # Plot the heartbeat
    plt.figure(figsize=(10, 6))
    plt.plot(time, heartbeat, label='Heartbeat')

    # Highlight the section with irregular heartbeat in red
    plt.fill_between(time[irregularity_start:irregularity_end], -1, 1, color='red', alpha=0.3, label='Irregular heartbeat')

    # Add labels and title
    plt.xlabel('Time (seconds)')
    plt.ylabel('Amplitude')
    plt.title('Heartbeat with Irregularity')
    plt.legend()

    # Show the plot
    plt.show()


def point_anomaly():
    # Generate synthetic data with a clear correlation and outliers
    np.random.seed(42)
    x = np.linspace(0, 30, 30)
    #y = 2 * x + 1 + np.random.normal(0, 1, size=len(x))
    y = 1 + np.random.normal(0, 1, size=len(x))
    # Introduce outliers
    outliers_indices = [5, 15, 25]
    y[outliers_indices] += 2  # Increase the y-values for outliers

    # Plot the scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, label='Data points')

    # Identify and circle the outliers
    outliers_x = x[outliers_indices]
    outliers_y = y[outliers_indices]
    plt.scatter(outliers_x, outliers_y, color='red', label='Outliers')
    for i in range(len(outliers_x)):
        circle = plt.Circle((outliers_x[i], outliers_y[i]), 0.5, color='red', fill=False)
        plt.gca().add_patch(circle)

    # Add labels and title
    plt.xlabel('Time (Days)')
    plt.ylabel('Price (£)')
    plt.title('Point Anomalies Credit card ')
    plt.legend()

    # Show the plot
    plt.savefig('point_anomalies.png')
    #plt.show()


def point_anomaly_v2():
    # Generate synthetic data with a clear correlation and outliers
    np.random.seed(42)
    x = np.linspace(0, 26, 26)
    #y = 2 * x + 1 + np.random.normal(0, 1, size=len(x))
    y = 1000 + np.abs(np.random.normal(0, 1000, size=len(x)))
    # Introduce outliers
    outliers_indices = [5, 15, 25]
    y[outliers_indices] += 1500  # Increase the y-values for outliers

    # Plot the scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, label='Data points')

    # Identify and circle the outliers
    outliers_x = x[outliers_indices]
    outliers_y = y[outliers_indices]
    plt.scatter(outliers_x, outliers_y, color='red', label='Outliers')
    for i in range(len(outliers_x)):
        circle = plt.Circle((outliers_x[i], outliers_y[i]), 0.5, color='red', fill=False)
        plt.gca().add_patch(circle)

    # Add labels and title
    plt.xlabel('Time (Weeks)')
    plt.ylabel('Cost (£)')
    plt.title('Point OOD Example - Weekly Credit Card Cost')
    plt.legend()

    # Show the plot
    plt.savefig('point_anomalies_v2.png')
    #plt.show()

def contextual_anomaly():
    # https://www.geeksforgeeks.org/contextual-outliers/
    

 
    # Generate random data for the dataset
    random_data = {
        'Date': [datetime(2023, 1, 1) + timedelta(days=i) for i in range(30)],
        'Temperature': np.sort([round(random.uniform(-10.0, 40.0), 1) for _ in range(30)]
                               )
    }
    
    # Create the DataFrame
    data = pd.DataFrame(random_data)
    
    # Mark temperature values greater than 35 as contextual outliers
    contextual_outlier_index = data['Temperature'] > 30
    
    # Format date to show only date and month
    data['Date'] = data['Date'].dt.strftime('%d-%b')
    
    # Visualize the data
    plt.plot(data['Date'], data['Temperature'], marker="o")
    plt.plot(data['Date'][contextual_outlier_index],
             data['Temperature'][contextual_outlier_index],
             'ro-', label="Contextual Outliers\nIn January temperature is always < 30")
    
    plt.xlabel('Date')
    plt.ylabel('Temperature')
    plt.title('Contextual Outliers')
    plt.legend()
    # Rotate x-axis labels for better visibility
    plt.xticks(rotation=90)  
    plt.show()
    # Generate synthetic data with a clear correlation and contextual outliers
    np.random.seed(42)
    x = np.linspace(0, 10, 50)
    y = 2 * x + 1 + np.random.normal(0, 1, size=len(x))

    # Introduce contextual outliers
    contextual_outliers = [(4, 25), (7, 20)]  # Coordinates of contextual outliers

    # Plot the scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, label='Data points')

    # Circle the contextual outliers in red
    for outlier in contextual_outliers:
        plt.scatter(outlier[0], outlier[1], color='red', label='Contextual outliers')
        circle = plt.Circle(outlier, 0.5, color='red', fill=False)
        plt.gca().add_patch(circle)

    # Add labels and title
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Scatter Plot with Contextual Outliers')
    plt.legend()

    # Show the plot
    plt.show()



def collective_anomaly_v2():
    # Generate synthetic data for 30 days with fluctuations
    days = np.arange(1, 31)
    intercept = 3
    values = np.sin(2 * np.pi * days / 30) + 0.5 * np.random.randn(30)+ intercept

    # Introduce a period of high values
    high_values_start = 10
    high_values_end = 20
    values[high_values_start:high_values_end] =intercept+2.2  # Increase values during this period

    # Plot the curve
    plt.figure(figsize=(10, 6))
    #plt.plot(days, values, label='Curve')
    plt.plot(days, values)

    # Highlight the period of high values in red
    plt.fill_between(days[high_values_start:high_values_end], min(values), max(values),
                     color='red', alpha=0.3, label='High values period')

    # Add labels and title
    plt.xlabel('Time (Days)')
    plt.ylabel('Price (£)')
    plt.title('Group Anomalies Credit card')
    plt.legend()
    plt.savefig('group_anomalies.png')
    # Show the plot
    #plt.show()

def collective_anomaly_v3():
    # Generate synthetic data for 30 days with fluctuations
    days = np.arange(1, 31)
    intercept = 20
    values = np.sin(2 * np.pi * days / 30) + 0.5 * np.random.randn(30)+ intercept

    # Introduce a period of high values
    high_values_start = 10
    high_values_end = 20
    values[high_values_start:high_values_end] =intercept+20  # Increase values during this period

    # Plot the curve
    plt.figure(figsize=(10, 6))
    #plt.plot(days, values, label='Curve')
    plt.plot(days, values)

    # Highlight the period of high values in red
    plt.fill_between(days[high_values_start:high_values_end], min(values), max(values),
                     color='red', alpha=0.3, label='High values period')

    # Add labels and title
    plt.xlabel('Time (Days)')
    plt.ylabel('Cost (£)')
    plt.title('Group OOD Example - Daily Living Cost')
    plt.legend()
    plt.savefig('group_anomalies_v3.png')
    # Show the plot
    #plt.show()


def contextual_anomaly_v2():
    # Generate synthetic data for January and February
    days_january = np.arange(1, 32)
    days_february = np.arange(32, 60)
    values_january = 5 +  0.5*np.sin(2 * np.pi * days_january / 31) + 0.5 * np.random.randn(31)
    values_february = 1 + 0.5 * np.random.randn(28)

    # Introduce an occurrence in February close to January values
    occurrence_day = 45
    values_february[occurrence_day - 32] += 3  # Increase the value on the occurrence day

    # Concatenate January and February data
    days = np.concatenate((days_january, days_february))
    values = np.concatenate((values_january, values_february))

    # Plot the curve
    plt.figure(figsize=(10, 6))
    plt.plot(days, values)

    # Highlight the occurrence in February in red
    plt.scatter(occurrence_day, values[occurrence_day - 1], color='red', label='Contextual Anomaly in Second Month', zorder=5)
    plt.annotate(f'Occurrence', xy=(occurrence_day, values[occurrence_day - 1]), xytext=(occurrence_day + 2, values[occurrence_day - 1] + 1),
                 arrowprops=dict(facecolor='black', arrowstyle='->'))

    # Add labels and title
    plt.xlabel('Time (Days)')
    plt.ylabel('Price (£)')
    plt.title('Contextual Anomalies Credit card')
    plt.legend()
    plt.savefig('contextual_anomalies.png')


def contextual_anomaly_v3():
    # Generate synthetic data for January and February
    days_january = np.arange(1, 32)
    days_february = np.arange(32, 60)
    values_january = 5 +  0.5*np.sin(2 * np.pi * days_january / 31) + 0.5 * np.random.randn(31)
    values_february = 2+ 0.5 * np.random.randn(28)

    # Introduce an occurrence in February close to January values
    occurrence_day = 45
    values_february[occurrence_day - 32] += 3  # Increase the value on the occurrence day

    # Concatenate January and February data
    days = np.concatenate((days_january, days_february))
    values = np.concatenate((values_january, values_february))

    # Plot the curve
    plt.figure(figsize=(10, 6))
    plt.plot(days, values)

    # Highlight the occurrence in February in red
    plt.scatter(occurrence_day, values[occurrence_day - 1], color='red', label='Contextual Anomaly in Second Month', zorder=5)
    plt.annotate(f'Occurrence', xy=(occurrence_day, values[occurrence_day - 1]), xytext=(occurrence_day + 2, values[occurrence_day - 1] + 1),
                 arrowprops=dict(facecolor='black', arrowstyle='->'))

    # Add labels and title
    plt.xlabel('Time (Days)')
    plt.ylabel('Cost (£)')
    plt.title('Contextual OOD Example - Daily Heating Cost')
    plt.legend()
    plt.savefig('contextual_anomalies_v2.png')


def contextual_anomaly_v4():
    # Generate synthetic data for January and February
    days_january = np.arange(1, 32)
    days_february = np.arange(32, 60)
    days_march = np.arange(60, 91)
    
    values_january = 7 +  0.5*np.sin(2 * np.pi * days_january / 31) + 0.5 * np.random.randn(31)
    values_february = 5 + 0.5 * np.random.randn(28)
    values_march = 2 + 0.5 * np.random.randn(28)

    # Introduce an occurrence in February close to January values
    occurrence_day = 66
    values_march[occurrence_day - 60] += 1  # Increase the value on the occurrence day

    # Concatenate January and February data
    days = np.concatenate((days_january, days_february,days_march))
    values = np.concatenate((values_january, values_february,days_march))

    # Plot the curve
    plt.figure(figsize=(10, 6))
    plt.plot(days, values)

    # Highlight the occurrence in February in red
    plt.scatter(occurrence_day, values[occurrence_day - 1], color='red', label='Contextual Anomaly in Third Month', zorder=5)
    plt.annotate(f'Occurrence', xy=(occurrence_day, values[occurrence_day - 1]), xytext=(occurrence_day + 2, values[occurrence_day - 1] + 1),
                 arrowprops=dict(facecolor='black', arrowstyle='->'))

    # Add labels and title
    plt.xlabel('Time (Days)')
    plt.ylabel('Cost (£)')
    plt.title('Contextual OOD Example - Daily Heating Cost')
    plt.legend()
    plt.savefig('contextual_anomalies_v2.png')


if __name__ == "__main__":
    #point_anomaly_v2()
    #contextual_anomaly_v3()
    collective_anomaly_v3()
    #contextual_anomaly()
    #collective_anomaly()
    #collective_anomaly_v2()
    #contextual_anomaly_v2()
