// server.js - Express.js Backend
// Handles: serving static files, API routes for JSON data
// Author: Varun Ventrapagada (SE24UARI006)

const express = require('express');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = 3000;

// Middleware: Request logger
app.use(function (req, res, next) {
    console.log('[' + new Date().toLocaleTimeString() + '] ' + req.method + ' ' + req.url);
    next();
});

// Middleware: Serve static files from 'public' folder
app.use(express.static(path.join(__dirname, 'public')));

// API Route: GET /api/sales - returns sales data
app.get('/api/sales', function (req, res) {
    var filePath = path.join(__dirname, 'public', 'data', 'sales.json');
    fs.readFile(filePath, 'utf8', function (err, data) {
        if (err) {
            res.status(500).json({ error: 'Failed to read sales data' });
            return;
        }
        var salesData = JSON.parse(data);

        // Filter by category if query parameter provided
        if (req.query.category) {
            salesData = salesData.filter(function (item) {
                return item.category === req.query.category;
            });
        }

        // Filter by year if query parameter provided
        if (req.query.year) {
            salesData = salesData.filter(function (item) {
                return item.year === parseInt(req.query.year);
            });
        }

        res.json(salesData);
    });
});

// API Route: GET /api/students - returns student performance data
app.get('/api/students', function (req, res) {
    var filePath = path.join(__dirname, 'public', 'data', 'students.json');
    fs.readFile(filePath, 'utf8', function (err, data) {
        if (err) {
            res.status(500).json({ error: 'Failed to read student data' });
            return;
        }
        var studentData = JSON.parse(data);

        // Filter by department if query parameter provided
        if (req.query.department) {
            studentData = studentData.filter(function (item) {
                return item.department === req.query.department;
            });
        }

        res.json(studentData);
    });
});

// API Route: GET /api/weather - returns weather data
app.get('/api/weather', function (req, res) {
    var filePath = path.join(__dirname, 'public', 'data', 'weather.json');
    fs.readFile(filePath, 'utf8', function (err, data) {
        if (err) {
            res.status(500).json({ error: 'Failed to read weather data' });
            return;
        }
        var weatherData = JSON.parse(data);

        // Filter by city if query parameter provided
        if (req.query.city) {
            weatherData = weatherData.filter(function (item) {
                return item.city === req.query.city;
            });
        }

        res.json(weatherData);
    });
});

// API Route: GET /api/categories - returns unique categories for filters
app.get('/api/categories', function (req, res) {
    var filePath = path.join(__dirname, 'public', 'data', 'sales.json');
    fs.readFile(filePath, 'utf8', function (err, data) {
        if (err) {
            res.status(500).json({ error: 'Failed to read data' });
            return;
        }
        var salesData = JSON.parse(data);
        var categories = [];
        salesData.forEach(function (item) {
            if (categories.indexOf(item.category) === -1) {
                categories.push(item.category);
            }
        });
        res.json(categories);
    });
});

// 404 handler for undefined routes
app.use(function (req, res) {
    res.status(404).json({ error: 'Route not found' });
});

// Error handling middleware
app.use(function (err, req, res, next) {
    console.error('Server error:', err.message);
    res.status(500).json({ error: 'Internal server error' });
});

// Start server
app.listen(PORT, function () {
    console.log('Data Visualizer server running at http://localhost:' + PORT);
});
