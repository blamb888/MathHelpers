import numpy as np
import matplotlib.pyplot as plt

def calculateStats(inputData):
    # Convert the input string to a NumPy array
    data = np.array(inputData.split(',').astype(float))

    # Calculate the mean, variance, and standard deviation
    mean = np.mean(data)
    variance = np.var(data, ddof=1)  # set ddof=1 to use the unbiased estimator of variance
    std_dev = np.std(data, ddof=1)

    # Create the histogram data and plot the histogram
    hist, bins = np.histogram(data, bins=30, density=True)
    fig, ax = plt.subplots()
    ax.hist(data, bins=30, density=True, alpha=0.5)
    ax.set_xlabel('Data')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram of Data')
    fig.savefig('histogram.png')
    plt.close()

    # Create the normal distribution data and plot the curve
    curve_x = np.linspace(np.min(data), np.max(data), 100)
    curve_y = 1 / (std_dev * np.sqrt(2 * np.pi)) * np.exp(-(curve_x - mean) ** 2 / (2 * std_dev ** 2))
    fig, ax = plt.subplots()
    ax.plot(curve_x, curve_y, color='r')
    ax.set_xlabel('Data')
    ax.set_ylabel('Probability Density')
    ax.set_title('Normal Distribution Curve')
    fig.savefig('normal_distribution.png')
    plt.close()

    return {'mean': mean, 'variance': variance, 'std_dev': std_dev}
