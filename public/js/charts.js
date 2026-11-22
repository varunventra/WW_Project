// charts.js - Chart Rendering with Chart.js
// Author: Vishnu Vardhan Rao (SE24UARI010)

// Global variable to store the current chart instance
var currentChart = null;

// Color palette for charts
var chartColors = [
    '#3498db', '#e74c3c', '#2ecc71', '#f39c12',
    '#9b59b6', '#1abc9c', '#e67e22', '#34495e',
    '#16a085', '#c0392b', '#27ae60', '#2980b9'
];

// Function to destroy existing chart before creating new one
function destroyChart() {
    if (currentChart !== null) {
        currentChart.destroy();
        currentChart = null;
    }
}

// Function to create a Bar Chart
function createBarChart(labels, datasets, title) {
    destroyChart();
    var ctx = document.getElementById('mainChart').getContext('2d');
    currentChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: datasets
        },
        options: {
            responsive: true,
            plugins: {
                title: {
                    display: true,
                    text: title,
                    font: { size: 18 }
                },
                legend: {
                    display: true,
                    position: 'top'
                }
            },
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

// Function to create a Line Graph
function createLineChart(labels, datasets, title) {
    destroyChart();
    var ctx = document.getElementById('mainChart').getContext('2d');
    currentChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: datasets
        },
        options: {
            responsive: true,
            plugins: {
                title: {
                    display: true,
                    text: title,
                    font: { size: 18 }
                },
                legend: {
                    display: true,
                    position: 'top'
                }
            },
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

// Function to create a Pie Chart
function createPieChart(labels, data, title) {
    destroyChart();
    var ctx = document.getElementById('mainChart').getContext('2d');
    currentChart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: labels,
            datasets: [{
                data: data,
                backgroundColor: chartColors.slice(0, labels.length),
                borderColor: '#fff',
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            plugins: {
                title: {
                    display: true,
                    text: title,
                    font: { size: 18 }
                },
                legend: {
                    display: true,
                    position: 'right'
                }
            }
        }
    });
}

// Function to create a Scatter Plot
function createScatterChart(datasets, title, xLabel, yLabel) {
    destroyChart();
    var ctx = document.getElementById('mainChart').getContext('2d');
    currentChart = new Chart(ctx, {
        type: 'scatter',
        data: {
            datasets: datasets
        },
        options: {
            responsive: true,
            plugins: {
                title: {
                    display: true,
                    text: title,
                    font: { size: 18 }
                },
                legend: {
                    display: true,
                    position: 'top'
                }
            },
            scales: {
                x: {
                    title: { display: true, text: xLabel }
                },
                y: {
                    title: { display: true, text: yLabel },
                    beginAtZero: true
                }
            }
        }
    });
}
