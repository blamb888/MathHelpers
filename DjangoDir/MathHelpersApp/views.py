from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import numpy as np
import io
import re
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def home(request):
    if request.method == 'POST':
        data_str = request.POST.get('data')
        data = [float(x.strip()) for x in re.split(r'[,\s]+', data_str)]
        
        # Calculate mean
        mean = np.mean(data)

        # Calculate variance
        variance = np.var(data, ddof=1)

        # Calculate standard deviation
        std_dev = np.std(data, ddof=1)

        # Generate histogram
        fig = Figure()
        ax = fig.add_subplot(1, 1, 1)
        n, bins, patches = ax.hist(data, bins=30, density=True, alpha=0.5)
        ax.set_xlabel('Data')
        ax.set_ylabel('Frequency')
        ax.set_title('Histogram of Data')
        canvas = FigureCanvas(fig)
        buffer = io.BytesIO()
        canvas.print_png(buffer)
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()
        histogram_image = base64.b64encode(image_png).decode('utf-8')

        # Generate normal distribution plot
        x = np.linspace(np.min(data) - std_dev * 5, np.max(data) + std_dev * 5, 1000)
        y = 1 / (std_dev * np.sqrt(2 * np.pi)) * np.exp(-(x - mean) ** 2 / (2 * std_dev ** 2))
        fig = Figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.plot(x, y)
        ax.axvline(mean, color='r', linestyle='--')
        ax.axvline(mean - std_dev, color='g', linestyle='--')
        ax.axvline(mean + std_dev, color='g', linestyle='--')
        ax.axvline(mean - 2 * std_dev, color='y', linestyle='--')
        ax.axvline(mean + 2 * std_dev, color='y', linestyle='--')
        ax.set_xlabel('Data')
        ax.set_ylabel('Probability density')
        ax.set_title('Normal Distribution of Data')
        canvas = FigureCanvas(fig)
        buffer = io.BytesIO()
        canvas.print_png(buffer)
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()
        normal_distribution_image = base64.b64encode(image_png).decode('utf-8')

        context = {
            'mean': mean,
            'variance': variance,
            'std_dev': std_dev,
            'histogram_image': 'data:image/png;base64,' + histogram_image,
            'normal_distribution_image': 'data:image/png;base64,' + normal_distribution_image,
        }
        return render(request, 'index.html', context)

    return render(request, 'index.html')