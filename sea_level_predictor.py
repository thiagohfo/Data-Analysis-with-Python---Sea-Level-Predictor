import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    ax = df.plot.scatter(x='Year', y='CSIRO Adjusted Sea Level')
    fig = ax.get_figure()
    fig.set_size_inches(16, 10)

    # Create first line of best fit
    slope, intercept, _, _, _ = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    new_x = list(range(1880, 2051, 1))
    new_y = [(intercept + slope * x) for x in new_x]
    plt.plot(new_x, new_y, 'r')

    # Create second line of best fit
    df_copy = df[df['Year'] >= 2000]
    slope, intercept, _, _, _ = linregress(x=df_copy['Year'], y=df_copy['CSIRO Adjusted Sea Level'])
    new_x = list(range(2000, 2051, 1))
    new_y = [(intercept + slope * x) for x in new_x]
    plt.plot(new_x, new_y, 'g')

    # Add labels and title
    ax.set_xticks(list(range(1850, 2076, 25)))
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()