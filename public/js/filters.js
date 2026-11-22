// filters.js - Data Filtering and Interactivity with jQuery
// Author: Rohan Yaski (SE24UARI042)

// Current active dataset
var activeDataset = 'sales';

$(document).ready(function () {

    // Tab switching using jQuery click event
    $('.tab-btn').click(function () {
        // Remove active class from all tabs
        $('.tab-btn').removeClass('active');
        // Add active class to clicked tab
        $(this).addClass('active');

        // Get selected dataset
        activeDataset = $(this).data('dataset');

        // Show/hide the correct filter group with slide effect
        $('.filter-group').slideUp(200);
        if (activeDataset === 'sales') {
            $('#sales-filters').slideDown(200);
        } else if (activeDataset === 'students') {
            $('#student-filters').slideDown(200);
        } else if (activeDataset === 'weather') {
            $('#weather-filters').slideDown(200);
        }

        // Load data for the selected dataset
        loadData();
    });

    // Apply filter button click
    $('#apply-filter').click(function () {
        loadData();
    });

    // Also apply filters when any dropdown changes
    $('select').on('change', function () {
        loadData();
    });

});

// Function to load data from server using Fetch API
function loadData() {
    if (activeDataset === 'sales') {
        loadSalesData();
    } else if (activeDataset === 'students') {
        loadStudentData();
    } else if (activeDataset === 'weather') {
        loadWeatherData();
    }
}

// Load and visualize sales data
function loadSalesData() {
    var category = $('#category-filter').val();
    var year = $('#year-filter').val();
    var chartType = $('#chart-type-sales').val();

    // Build query string
    var url = '/api/sales?';
    if (category) url += 'category=' + category + '&';
    if (year) url += 'year=' + year;

    fetch(url)
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            renderSalesChart(data, chartType, category);
            renderSalesSummary(data);
            renderSalesTable(data);
        })
        .catch(function (error) {
            console.log('Error fetching sales data:', error);
        });
}

// Render sales data as charts
function renderSalesChart(data, chartType, category) {
    var months = ['January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'];

    if (chartType === 'pie') {
        // Pie chart: total revenue by category
        var categoryTotals = {};
        data.forEach(function (item) {
            if (!categoryTotals[item.category]) {
                categoryTotals[item.category] = 0;
            }
            categoryTotals[item.category] += item.revenue;
        });
        var labels = Object.keys(categoryTotals);
        var values = Object.values(categoryTotals);
        createPieChart(labels, values, 'Revenue by Category');

    } else if (chartType === 'scatter') {
        // Scatter plot: units vs revenue
        var categories = {};
        data.forEach(function (item) {
            if (!categories[item.category]) {
                categories[item.category] = [];
            }
            categories[item.category].push({ x: item.units, y: item.revenue });
        });
        var datasets = [];
        var colorIndex = 0;
        for (var cat in categories) {
            datasets.push({
                label: cat,
                data: categories[cat],
                backgroundColor: chartColors[colorIndex],
                pointRadius: 6
            });
            colorIndex++;
        }
        createScatterChart(datasets, 'Units Sold vs Revenue', 'Units Sold', 'Revenue (Rs)');

    } else {
        // Bar or Line chart: revenue by month
        var categories = {};
        data.forEach(function (item) {
            if (!categories[item.category]) {
                categories[item.category] = {};
            }
            if (!categories[item.category][item.month]) {
                categories[item.category][item.month] = 0;
            }
            categories[item.category][item.month] += item.revenue;
        });

        var datasets = [];
        var colorIndex = 0;
        for (var cat in categories) {
            var values = months.map(function (m) {
                return categories[cat][m] || 0;
            });
            datasets.push({
                label: cat,
                data: values,
                backgroundColor: chartColors[colorIndex],
                borderColor: chartColors[colorIndex],
                fill: false,
                tension: 0.3
            });
            colorIndex++;
        }

        var title = 'Monthly Revenue' + (category ? ' - ' + category : '');
        if (chartType === 'bar') {
            createBarChart(months, datasets, title);
        } else {
            createLineChart(months, datasets, title);
        }
    }
}

// Render sales data summary
function renderSalesSummary(data) {
    var totalRevenue = 0;
    var totalUnits = 0;
    data.forEach(function (item) {
        totalRevenue += item.revenue;
        totalUnits += item.units;
    });
    var avgRevenue = data.length > 0 ? Math.round(totalRevenue / data.length) : 0;

    var html = '';
    html += '<div class="summary-card"><h3>Total Revenue</h3><p>Rs ' + totalRevenue.toLocaleString() + '</p></div>';
    html += '<div class="summary-card"><h3>Total Units</h3><p>' + totalUnits.toLocaleString() + '</p></div>';
    html += '<div class="summary-card"><h3>Avg Revenue/Month</h3><p>Rs ' + avgRevenue.toLocaleString() + '</p></div>';
    html += '<div class="summary-card"><h3>Records</h3><p>' + data.length + '</p></div>';

    $('#summary-content').html(html);
}

// Render sales data table
function renderSalesTable(data) {
    var headHtml = '<tr><th>Month</th><th>Category</th><th>Revenue</th><th>Units</th><th>Year</th></tr>';
    $('#table-head').html(headHtml);

    var bodyHtml = '';
    data.forEach(function (item) {
        bodyHtml += '<tr>';
        bodyHtml += '<td>' + item.month + '</td>';
        bodyHtml += '<td>' + item.category + '</td>';
        bodyHtml += '<td>Rs ' + item.revenue.toLocaleString() + '</td>';
        bodyHtml += '<td>' + item.units + '</td>';
        bodyHtml += '<td>' + item.year + '</td>';
        bodyHtml += '</tr>';
    });
    $('#table-body').html(bodyHtml);
}

// Load and visualize student data
function loadStudentData() {
    var department = $('#department-filter').val();
    var chartType = $('#chart-type-students').val();

    var url = '/api/students?';
    if (department) url += 'department=' + department;

    fetch(url)
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            renderStudentChart(data, chartType);
            renderStudentSummary(data);
            renderStudentTable(data);
        })
        .catch(function (error) {
            console.log('Error fetching student data:', error);
        });
}

// Render student chart
function renderStudentChart(data, chartType) {
    var labels = data.map(function (s) { return s.name; });

    if (chartType === 'scatter') {
        var datasets = [{
            label: 'Math vs Programming',
            data: data.map(function (s) { return { x: s.math, y: s.programming }; }),
            backgroundColor: '#3498db',
            pointRadius: 8
        }];
        createScatterChart(datasets, 'Math vs Programming Scores', 'Math', 'Programming');
    } else {
        var subjects = ['math', 'science', 'english', 'programming'];
        var subjectColors = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12'];
        var datasets = subjects.map(function (subject, i) {
            return {
                label: subject.charAt(0).toUpperCase() + subject.slice(1),
                data: data.map(function (s) { return s[subject]; }),
                backgroundColor: subjectColors[i],
                borderColor: subjectColors[i],
                fill: false,
                tension: 0.3
            };
        });

        if (chartType === 'bar') {
            createBarChart(labels, datasets, 'Student Subject Scores');
        } else {
            createLineChart(labels, datasets, 'Student Subject Scores');
        }
    }
}

// Render student summary
function renderStudentSummary(data) {
    var totalGpa = 0;
    var highestGpa = 0;
    var topStudent = '';
    data.forEach(function (s) {
        totalGpa += s.gpa;
        if (s.gpa > highestGpa) {
            highestGpa = s.gpa;
            topStudent = s.name;
        }
    });
    var avgGpa = data.length > 0 ? (totalGpa / data.length).toFixed(1) : 0;

    var html = '';
    html += '<div class="summary-card"><h3>Students</h3><p>' + data.length + '</p></div>';
    html += '<div class="summary-card"><h3>Avg GPA</h3><p>' + avgGpa + '</p></div>';
    html += '<div class="summary-card"><h3>Highest GPA</h3><p>' + highestGpa + '</p></div>';
    html += '<div class="summary-card"><h3>Top Student</h3><p>' + topStudent + '</p></div>';

    $('#summary-content').html(html);
}

// Render student table
function renderStudentTable(data) {
    var headHtml = '<tr><th>Name</th><th>Department</th><th>Math</th><th>Science</th><th>English</th><th>Programming</th><th>GPA</th></tr>';
    $('#table-head').html(headHtml);

    var bodyHtml = '';
    data.forEach(function (s) {
        bodyHtml += '<tr>';
        bodyHtml += '<td>' + s.name + '</td>';
        bodyHtml += '<td>' + s.department + '</td>';
        bodyHtml += '<td>' + s.math + '</td>';
        bodyHtml += '<td>' + s.science + '</td>';
        bodyHtml += '<td>' + s.english + '</td>';
        bodyHtml += '<td>' + s.programming + '</td>';
        bodyHtml += '<td>' + s.gpa + '</td>';
        bodyHtml += '</tr>';
    });
    $('#table-body').html(bodyHtml);
}

// Load and visualize weather data
function loadWeatherData() {
    var city = $('#city-filter').val();
    var chartType = $('#chart-type-weather').val();

    var url = '/api/weather?';
    if (city) url += 'city=' + city;

    fetch(url)
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            renderWeatherChart(data, chartType, city);
            renderWeatherSummary(data);
            renderWeatherTable(data);
        })
        .catch(function (error) {
            console.log('Error fetching weather data:', error);
        });
}

// Render weather chart
function renderWeatherChart(data, chartType, city) {
    var months = ['January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'];

    if (chartType === 'scatter') {
        var cities = {};
        data.forEach(function (item) {
            if (!cities[item.city]) cities[item.city] = [];
            cities[item.city].push({ x: item.temperature, y: item.rainfall });
        });
        var datasets = [];
        var colorIndex = 0;
        for (var c in cities) {
            datasets.push({
                label: c,
                data: cities[c],
                backgroundColor: chartColors[colorIndex],
                pointRadius: 8
            });
            colorIndex++;
        }
        createScatterChart(datasets, 'Temperature vs Rainfall', 'Temperature (C)', 'Rainfall (mm)');
    } else {
        // Group by city
        var cities = {};
        data.forEach(function (item) {
            if (!cities[item.city]) cities[item.city] = {};
            cities[item.city][item.month] = item.temperature;
        });

        var datasets = [];
        var colorIndex = 0;
        for (var c in cities) {
            var values = months.map(function (m) { return cities[c][m] || 0; });
            datasets.push({
                label: c,
                data: values,
                backgroundColor: chartColors[colorIndex],
                borderColor: chartColors[colorIndex],
                fill: false,
                tension: 0.3
            });
            colorIndex++;
        }

        var title = 'Monthly Temperature' + (city ? ' - ' + city : '');
        if (chartType === 'bar') {
            createBarChart(months, datasets, title);
        } else {
            createLineChart(months, datasets, title);
        }
    }
}

// Render weather summary
function renderWeatherSummary(data) {
    var totalTemp = 0;
    var maxTemp = -100;
    var maxRainfall = 0;
    var hottestCity = '';
    data.forEach(function (item) {
        totalTemp += item.temperature;
        if (item.temperature > maxTemp) {
            maxTemp = item.temperature;
            hottestCity = item.city + ' (' + item.month + ')';
        }
        if (item.rainfall > maxRainfall) {
            maxRainfall = item.rainfall;
        }
    });
    var avgTemp = data.length > 0 ? (totalTemp / data.length).toFixed(1) : 0;

    var html = '';
    html += '<div class="summary-card"><h3>Records</h3><p>' + data.length + '</p></div>';
    html += '<div class="summary-card"><h3>Avg Temp</h3><p>' + avgTemp + ' C</p></div>';
    html += '<div class="summary-card"><h3>Max Temp</h3><p>' + maxTemp + ' C</p></div>';
    html += '<div class="summary-card"><h3>Max Rainfall</h3><p>' + maxRainfall + ' mm</p></div>';

    $('#summary-content').html(html);
}

// Render weather table
function renderWeatherTable(data) {
    var headHtml = '<tr><th>City</th><th>Month</th><th>Temperature (C)</th><th>Humidity (%)</th><th>Rainfall (mm)</th></tr>';
    $('#table-head').html(headHtml);

    var bodyHtml = '';
    data.forEach(function (item) {
        bodyHtml += '<tr>';
        bodyHtml += '<td>' + item.city + '</td>';
        bodyHtml += '<td>' + item.month + '</td>';
        bodyHtml += '<td>' + item.temperature + '</td>';
        bodyHtml += '<td>' + item.humidity + '</td>';
        bodyHtml += '<td>' + item.rainfall + '</td>';
        bodyHtml += '</tr>';
    });
    $('#table-body').html(bodyHtml);
}
