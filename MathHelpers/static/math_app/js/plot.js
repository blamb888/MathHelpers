function plotHistogram(data) {
    var canvas = document.getElementById('histogram');
    var ctx = canvas.getContext('2d');
    var [hist, bins] = numpy.histogram(data, bins=30, density=true);
    var chartData = {
      labels: bins.slice(0, -1),
      datasets: [{
        label: 'Histogram',
        data: hist,
        backgroundColor: 'rgba(255, 99, 132, 0.5)',
        borderWidth: 1,
      }]
    };
    var chartOptions = {
      scales: {
        xAxes: [{
          ticks: {
            beginAtZero: true
          }
        }]
      }
    };
    var chart = new Chart(ctx, {
      type: 'bar',
      data: chartData,
      options: chartOptions,
    });
  }
  
  function plotNormalDistribution(data) {
    var canvas = document.getElementById('normal-distribution');
    var ctx = canvas.getContext('2d');
    var mean = numpy.mean(data);
    var std_dev = numpy.std(data, ddof=1);
    var curveX = numpy.linspace(numpy.min(data), numpy.max(data), 100);
    let curveY = 1 / (this.stdDev * Math.sqrt(2 * Math.PI)) * Math.exp(-Math.pow((curveX - this.mean), 2) / (2 * Math.pow(this.stdDev, 2)));
    var chartData = {
      labels: curveX,
      datasets: [{
        label: 'Normal distribution',
        data: curveY,
        type: 'line',
        borderColor: 'rgba(54, 162, 235, 1)',
        borderWidth: 1,
        fill: false,
      }]
    };
    var chartOptions = {
      scales: {
        xAxes: [{
          ticks: {
            beginAtZero: true
          }
        }]
      }
    };
    var chart = new Chart(ctx, {
      type: 'line',
      data: chartData,
      options: chartOptions,
    });
  }
  