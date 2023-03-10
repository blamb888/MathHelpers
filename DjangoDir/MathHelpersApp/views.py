# Create your views here.
from django.shortcuts import render
import numpy as np
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def home(request):
    if request.method == 'POST':
        # Get the data from the form
        data = request.POST['data']
        # Convert the comma-separated string input to a NumPy array
        data = np.array(list(map(float, data.split(','))))
        # Calculate the mean, variance, and standard deviation
        mean = np.mean(data)
        variance = np.var(data, ddof=1)
        std_dev = np.std(data, ddof=1)
        # Create the histogram data and plot the histogram
        # Code for creating the histogram chart goes here...
        # Create the normal distribution data and plot the curve
        # Code for creating the normal distribution chart goes here...
        return render(request, 'index.html', {
            'mean': mean,
            'variance': variance,
            'std_dev': std_dev,
            # Pass any other variables needed for rendering the template here
        })
    else:
        return render(request, 'index.html')
