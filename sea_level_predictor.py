import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    line_f = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_f = pd.Series([i for i in range(df['Year'].min(), 2051)]).values
    y_f = x_f*line_f.slope + line_f.intercept
    plt.plot(x_f,y_f)
    
    # Create second line of best fit
    df_2000 = df[df['Year']>=2000]
    line_s = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    x_s = pd.Series([i for i in range(2000, 2051)]).values
    y_s = x_s*line_s.slope + line_s.intercept
    plt.plot(x_s,y_s)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()