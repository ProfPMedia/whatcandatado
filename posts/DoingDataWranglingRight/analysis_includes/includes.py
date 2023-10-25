def get_url_input():
    while True:
        try:
            # Using input() to get user input and strip any leading/trailing whitespaces
            url = input("Please enter the data URL from video: ").strip()

            # Checking if the input is not empty
            if url:
                return url
            else:
                print("Error: URL cannot be empty. Please try again.")
        except KeyboardInterrupt:
            # Handling Ctrl+C to exit gracefully
            print("\nOperation aborted by the user.")
            return None

import numpy as np
import plotly.graph_objects as go
        
def generate_dist_examples():
    # Set a random seed for reproducibility
    np.random.seed(42)

    # Generate a normally distributed dataset with 1000 data points
    mean = 50
    std_dev = 10
    data_points = 1000
    normal_data = np.random.normal(mean, std_dev, data_points)

    # Generate more outliers with a uniform distribution between 0 and 200
    num_outliers = 350
    outliers = np.random.normal(mean+mean, std_dev, num_outliers)

    # Combine the normal data and outliers
    dataset_with_outliers = np.concatenate((normal_data, outliers))

    # Create a histogram with outliers and normal distribution
    histogram_data = [dataset_with_outliers, normal_data]
    histogram_labels = ['With Outliers', 'Normal Distribution']

    fig_histogram = go.Figure()

    for data, label in zip(histogram_data, histogram_labels):
        fig_histogram.add_trace(go.Histogram(x=data, nbinsx=30, opacity=0.75, name=label))

    fig_histogram.update_layout(title='Histogram of Normal Distribution with Outliers and Normal Distribution',
                                xaxis_title='Data Value', yaxis_title='Frequency')
    fig_histogram.show()

    # Calculate the cumulative probabilities for both datasets
    cdf_x_with_outliers = np.sort(dataset_with_outliers)
    cdf_y_with_outliers = np.arange(1, len(cdf_x_with_outliers) + 1) / len(cdf_x_with_outliers)

    dataset_without_outliers = np.setdiff1d(dataset_with_outliers, outliers)
    cdf_x_without_outliers = np.sort(dataset_without_outliers)
    cdf_y_without_outliers = np.arange(1, len(cdf_x_without_outliers) + 1) / len(cdf_x_without_outliers)

    # Create the CDF plot
    fig_cdf = go.Figure()

    fig_cdf.add_trace(go.Scatter(x=cdf_x_with_outliers, y=cdf_y_with_outliers, mode='lines', name='With Outliers'))
    fig_cdf.add_trace(go.Scatter(x=cdf_x_without_outliers, y=cdf_y_without_outliers, mode='lines', name='Without Outliers'))

    fig_cdf.update_layout(title='Cumulative Distribution Function (CDF) with and without Outliers',
                          xaxis_title='Data Value', yaxis_title='Cumulative Probability')

    fig_cdf.show()

    # Generate theoretical quantiles for Q-Q plot with outliers
    normal_quantiles_with_outliers = np.sort(np.random.normal(mean, std_dev, data_points + num_outliers))

    # Create the Q-Q plot with outliers
    fig_qq = go.Figure()

    fig_qq.add_trace(go.Scatter(x=normal_quantiles_with_outliers, y=np.sort(dataset_with_outliers),
                                mode='markers', name='With Outliers'))

    # Generate theoretical quantiles for Q-Q plot of normal distribution
    normal_quantiles = np.sort(np.random.normal(mean, std_dev, data_points))

    # Create the Q-Q plot for normal distribution
    fig_qq.add_trace(go.Scatter(x=normal_quantiles, y=np.sort(normal_data),
                                mode='markers', name='Normal Distribution'))

    # Update layout for Q-Q plot
    fig_qq.update_layout(title='Q-Q Plot of Normal Distribution with and without Outliers',
                         xaxis_title='Theoretical Quantiles', yaxis_title='Sample Quantiles')

    fig_qq.show()
    
    return None