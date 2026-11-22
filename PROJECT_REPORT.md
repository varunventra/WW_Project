# Project 15: Interactive Data Visualizer

## Web Workshop - Final Group Project Report

---

## Team Members

| Roll Number   | Name                  | Role                                      |
|---------------|-----------------------|-------------------------------------------|
| SE24UARI021   | Vineela Reddy         | HTML Structure & Page Layout              |
| SE24UARI009   | Annyunaa Gandra       | CSS Styling & Responsive Design           |
| SE24UARI010   | Vishnu Vardhan Rao    | Chart Rendering (Chart.js)                |
| SE24UARI042   | Rohan Yaski           | Data Filtering & Interactivity (jQuery)   |
| SE24UARI006   | Varun Ventrapagada    | Backend Server (Node.js / Express.js)     |
| SE24UARI032   | Akshat Reddy          | JSON Data Preparation & Export Feature    |

---

## 1. Project Abstract

This project is an interactive data visualization application that reads data from JSON files and displays charts and graphs using JavaScript. The visualizer supports multiple chart types including bar charts, line graphs, pie charts, and scatter plots. Users can filter data, drill down into specific segments, and export visualizations as PNG images.

The application follows a client-server architecture. The backend is built with Node.js and Express.js — it reads JSON data files from the filesystem using the `fs` module, applies server-side filtering based on query parameters from the URL, and returns the filtered data as JSON responses. The frontend is built with HTML5, CSS3, jQuery, and Chart.js — it fetches data from the backend API using the Fetch API, transforms the raw data into the format required by Chart.js, renders interactive charts on an HTML5 Canvas element, and displays summary statistics and data tables using jQuery DOM manipulation.

The project demonstrates working with JSON data, implementing data transformation algorithms, creating dynamic Canvas-based visualizations, handling user events with jQuery, and building RESTful API endpoints with Express.js.

---

## 2. Tools and Technologies Used

| Technology        | Version  | Purpose                                                      |
|-------------------|----------|--------------------------------------------------------------|
| HTML5             | -        | Page structure using semantic tags (header, nav, main, etc.) |
| CSS3              | -        | External stylesheet for layout, colors, hover effects        |
| JavaScript (ES6)  | -        | DOM manipulation, data transformation, callbacks             |
| jQuery            | 3.7.1    | Event handling, DOM updates, slide animations                |
| Chart.js          | 4.4.0    | Rendering bar, line, pie, and scatter charts on Canvas       |
| Node.js           | -        | Server-side JavaScript runtime environment                   |
| Express.js        | 4.18.2   | Web framework for routing, middleware, static file serving   |
| Fetch API         | -        | Browser API for making HTTP requests to our Express server   |
| Canvas API        | -        | HTML5 graphics surface used by Chart.js and for PNG export   |
| npm               | -        | Node package manager for installing Express dependency       |

**CDN Links Used:**
- Chart.js: `https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js`
- jQuery: `https://code.jquery.com/jquery-3.7.1.min.js`

---

## 3. Project Structure

```
interactive-data-visualizer/
├── server.js                    # Express.js backend server (Varun)
├── package.json                 # Node.js project configuration
├── node_modules/                # Installed npm packages (auto-generated)
├── public/                      # Static files served by Express
│   ├── index.html               # Main HTML dashboard page (Vineela)
│   ├── css/
│   │   └── styles.css           # All CSS styling (Annyunaa)
│   ├── js/
│   │   ├── app.js               # App initialization on page load (Vineela)
│   │   ├── charts.js            # Chart.js rendering functions (Vishnu Vardhan)
│   │   ├── filters.js           # jQuery filtering, Fetch API, data logic (Rohan)
│   │   └── export.js            # PNG export functionality (Akshat)
│   └── data/
│       ├── sales.json           # Sales dataset - 72 records (Akshat)
│       ├── students.json        # Student performance dataset - 20 records (Akshat)
│       └── weather.json         # Weather dataset - 36 records (Akshat)
└── PROJECT_REPORT.md            # This report
```

---

## 4. How to Run the Project

**Prerequisites:** Node.js must be installed on the computer.

**Steps:**

1. Open a terminal/command prompt and navigate to the project folder:
   ```
   cd interactive-data-visualizer
   ```

2. Install the Express.js dependency using npm:
   ```
   npm install
   ```
   This reads `package.json` and installs Express.js (version 4.18.2) into the `node_modules/` folder.

3. Start the server:
   ```
   npm start
   ```
   OR directly:
   ```
   node server.js
   ```
   The terminal will display: `Data Visualizer server running at http://localhost:3000`

4. Open any web browser and go to: **http://localhost:3000**

5. The dashboard loads with the Sales dataset displayed as a bar chart by default. Use the tabs to switch datasets, dropdowns to filter, and the Export button to download charts.

**Testing the API with a browser or Postman:**
- `http://localhost:3000/api/sales` — returns all sales data as JSON
- `http://localhost:3000/api/sales?category=Electronics` — returns only Electronics sales
- `http://localhost:3000/api/sales?category=Electronics&year=2024` — returns Electronics sales for 2024
- `http://localhost:3000/api/students?department=AI` — returns only AI department students
- `http://localhost:3000/api/weather?city=Hyderabad` — returns only Hyderabad weather data

---

## 5. Features

| Feature                | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| Three Datasets         | Sales (revenue/units by category), Student Performance (scores by dept), Weather (temp/rainfall by city) |
| Four Chart Types       | Bar chart, line graph, pie chart, scatter plot — user selects from dropdown  |
| Server-Side Filtering  | Express API filters data using query parameters before sending to frontend  |
| Data Summary Cards     | Computed statistics (totals, averages, max values) displayed in styled cards |
| Data Table             | Full filtered dataset displayed as an HTML table with alternating row colors |
| PNG Export             | Download the current chart as a PNG image using Canvas toDataURL()          |
| Tab Navigation         | Switch between Sales, Students, and Weather datasets using navigation tabs  |
| Real-Time Updates      | Charts, summaries, and tables update immediately when any dropdown changes  |
| jQuery Animations      | Filter panels slide up/down with 200ms animation when switching datasets    |
| Request Logging        | Server logs every HTTP request with timestamp, method, and URL              |
| Error Handling         | Server returns proper HTTP status codes (200, 404, 500) with JSON messages  |

---

## 6. Application Architecture & Data Flow

```
User clicks filter/tab in browser
        |
        v
jQuery event handler reads dropdown values
        |
        v
Fetch API sends GET request to Express server
   e.g., GET /api/sales?category=Electronics&year=2024
        |
        v
Express route handler in server.js:
   1. fs.readFile() reads the JSON file from disk
   2. JSON.parse() converts string to JavaScript array
   3. Array .filter() applies query parameter conditions
   4. res.json() sends filtered array back as JSON response
        |
        v
Fetch .then() receives JSON response in browser
        |
        v
Data transformation functions in filters.js:
   - Group data by category/city using forEach loops
   - Calculate totals, averages using forEach loops
   - Build Chart.js dataset objects with labels and colors
        |
        v
Chart creation functions in charts.js:
   1. destroyChart() removes old chart from Canvas
   2. new Chart(ctx, config) renders new chart on Canvas
        |
        v
jQuery .html() updates summary cards and data table
```

---

## 7. API Endpoints — Detailed Documentation

The Express.js server exposes four REST API endpoints. All endpoints use the **GET** HTTP method and return **JSON** responses with `Content-Type: application/json`.

### 7.1 GET /api/sales

**Purpose:** Returns monthly sales data, optionally filtered by product category and/or year.

**Query Parameters:**

| Parameter  | Type   | Required | Values                                | Description               |
|------------|--------|----------|---------------------------------------|---------------------------|
| `category` | string | No       | Electronics, Clothing, Food, Books    | Filter by product category |
| `year`     | number | No       | 2023, 2024                            | Filter by year            |

**Example Request:** `GET /api/sales?category=Electronics&year=2024`

**Example Response:**
```json
[
  { "month": "January", "category": "Electronics", "revenue": 45000, "units": 120, "year": 2024 },
  { "month": "February", "category": "Electronics", "revenue": 52000, "units": 140, "year": 2024 }
]
```

**Server-Side Code Logic:**
```javascript
app.get('/api/sales', function (req, res) {
    var filePath = path.join(__dirname, 'public', 'data', 'sales.json');
    fs.readFile(filePath, 'utf8', function (err, data) {
        if (err) {
            res.status(500).json({ error: 'Failed to read sales data' });
            return;
        }
        var salesData = JSON.parse(data);
        if (req.query.category) {
            salesData = salesData.filter(function (item) {
                return item.category === req.query.category;
            });
        }
        if (req.query.year) {
            salesData = salesData.filter(function (item) {
                return item.year === parseInt(req.query.year);
            });
        }
        res.json(salesData);
    });
});
```

### 7.2 GET /api/students

**Query Parameters:** `department` (optional) — values: CSE, ECE, AI, ME

**Example:** `GET /api/students?department=CSE` returns only CSE students.

### 7.3 GET /api/weather

**Query Parameters:** `city` (optional) — values: Hyderabad, Mumbai, Delhi

**Example:** `GET /api/weather?city=Mumbai` returns only Mumbai weather data.

### 7.4 GET /api/categories

**Purpose:** Returns an array of unique product category names extracted from the sales data. No query parameters.

**Response:** `["Electronics", "Clothing", "Food", "Books"]`

---

## 8. Individual Contributions — Detailed Explanations

Each team member's work is explained below in first person, with the complete source code they wrote and line-by-line technical explanations of how their code works.

---

### 8.1 Vineela Reddy (SE24UARI021) — HTML Structure & Page Layout

**Files I Worked On:** `public/index.html`, `public/js/app.js`

**My Role:** I designed and built the complete HTML structure for the dashboard — the page layout, navigation tabs, filter controls, chart area, summary section, data table, and footer. I also wrote the app initialization script.

#### 8.1.1 Complete Source Code — index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interactive Data Visualizer</title>
    <link rel="stylesheet" href="css/styles.css">
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
    <script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
</head>
<body>
    <header>
        <h1>Interactive Data Visualizer</h1>
        <p>Explore data through charts and graphs</p>
    </header>
    <nav id="dataset-tabs">
        <button class="tab-btn active" data-dataset="sales">Sales Data</button>
        <button class="tab-btn" data-dataset="students">Student Performance</button>
        <button class="tab-btn" data-dataset="weather">Weather Data</button>
    </nav>
    <main>
        <section id="filters">
            <h2>Filters</h2>
            <div id="sales-filters" class="filter-group">
                <label for="category-filter">Category:</label>
                <select id="category-filter">
                    <option value="">All Categories</option>
                    <option value="Electronics">Electronics</option>
                    <option value="Clothing">Clothing</option>
                    <option value="Food">Food</option>
                    <option value="Books">Books</option>
                </select>
                <label for="year-filter">Year:</label>
                <select id="year-filter">
                    <option value="">All Years</option>
                    <option value="2024">2024</option>
                    <option value="2023">2023</option>
                </select>
                <label for="chart-type-sales">Chart Type:</label>
                <select id="chart-type-sales">
                    <option value="bar">Bar Chart</option>
                    <option value="line">Line Graph</option>
                    <option value="pie">Pie Chart</option>
                    <option value="scatter">Scatter Plot</option>
                </select>
            </div>
            <div id="student-filters" class="filter-group" style="display: none;">
                <label for="department-filter">Department:</label>
                <select id="department-filter">
                    <option value="">All Departments</option>
                    <option value="CSE">CSE</option>
                    <option value="ECE">ECE</option>
                    <option value="AI">AI</option>
                    <option value="ME">ME</option>
                </select>
                <label for="chart-type-students">Chart Type:</label>
                <select id="chart-type-students">
                    <option value="bar">Bar Chart</option>
                    <option value="line">Line Graph</option>
                    <option value="scatter">Scatter Plot</option>
                </select>
            </div>
            <div id="weather-filters" class="filter-group" style="display: none;">
                <label for="city-filter">City:</label>
                <select id="city-filter">
                    <option value="">All Cities</option>
                    <option value="Hyderabad">Hyderabad</option>
                    <option value="Mumbai">Mumbai</option>
                    <option value="Delhi">Delhi</option>
                </select>
                <label for="chart-type-weather">Chart Type:</label>
                <select id="chart-type-weather">
                    <option value="bar">Bar Chart</option>
                    <option value="line">Line Graph</option>
                    <option value="scatter">Scatter Plot</option>
                </select>
            </div>
            <button id="apply-filter">Apply Filters</button>
            <button id="export-btn">Export as PNG</button>
        </section>
        <section id="chart-container">
            <canvas id="mainChart"></canvas>
        </section>
        <section id="data-summary">
            <h2>Data Summary</h2>
            <div id="summary-content">
                <p>Select a dataset and apply filters to see the summary.</p>
            </div>
        </section>
        <section id="data-table-section">
            <h2>Data Table</h2>
            <div id="table-container">
                <table id="data-table">
                    <thead id="table-head"></thead>
                    <tbody id="table-body"></tbody>
                </table>
            </div>
        </section>
    </main>
    <footer>
        <p>Web Workshop Project 15 - Interactive Data Visualizer</p>
        <p>Team: Vineela | Annyunaa | Vishnu Vardhan | Rohan | Varun | Akshat</p>
    </footer>
    <script src="js/charts.js"></script>
    <script src="js/filters.js"></script>
    <script src="js/export.js"></script>
    <script src="js/app.js"></script>
</body>
</html>
```

#### 8.1.2 Detailed Technical Explanation

**Document Structure and Meta Tags:**
- `<!DOCTYPE html>` declares this as an HTML5 document, which is the latest HTML standard.
- `<meta charset="UTF-8">` sets the character encoding to UTF-8 so the browser correctly displays all characters.
- `<meta name="viewport" content="width=device-width, initial-scale=1.0">` makes the page responsive on mobile devices by setting the viewport width to match the device's screen width.
- `<link rel="stylesheet" href="css/styles.css">` connects the external CSS file created by Annyunaa. We used an external stylesheet (not inline CSS) as taught in the course.

**External Library Loading:**
- I included Chart.js (version 4.4.0) and jQuery (version 3.7.1) from CDN links in the `<head>` section. CDN (Content Delivery Network) means the browser downloads these libraries from a fast external server. This is the same approach we used in our jQuery lab exercises.
- Our custom JavaScript files (`charts.js`, `filters.js`, `export.js`, `app.js`) are loaded at the bottom of `<body>`, just before `</body>`. This is important because JavaScript needs the HTML elements to exist in the DOM before it can manipulate them. By placing scripts at the bottom, the browser parses all the HTML first.
- The loading order matters: `charts.js` loads first (defines chart functions), then `filters.js` (uses those chart functions), then `export.js` (uses the `currentChart` variable), and finally `app.js` (calls `loadData()` which is defined in `filters.js`).

**Semantic HTML Tags:**
I used HTML5 semantic tags throughout the page instead of generic `<div>` elements. Semantic tags tell the browser and developers what type of content each section contains:
- `<header>` — The page header with the application title "Interactive Data Visualizer" in an `<h1>` tag and a subtitle in a `<p>` tag.
- `<nav id="dataset-tabs">` — The navigation bar containing three `<button>` elements for switching between datasets. Each button has a custom HTML5 `data-dataset` attribute that stores which dataset it represents ("sales", "students", or "weather"). The first button has the CSS class `active` by default because Sales is the default dataset.
- `<main>` — Wraps all the primary content of the page.
- `<section>` — I used four `<section>` elements inside `<main>`, each with a unique `id`:
  - `<section id="filters">` — Contains all the filter dropdown controls.
  - `<section id="chart-container">` — Contains the `<canvas>` element where Chart.js renders charts.
  - `<section id="data-summary">` — Contains computed statistics displayed in summary cards.
  - `<section id="data-table-section">` — Contains the HTML data table.
- `<footer>` — The page footer showing project info and all team member names.

**Form Controls — Filter Dropdowns:**
I created three groups of filter controls, one for each dataset. Each group is wrapped in a `<div>` with the class `filter-group` (for CSS styling) and a unique `id` (for jQuery show/hide):

- **Sales Filters** (`id="sales-filters"`): Three `<select>` dropdowns:
  - Category filter: Options are "All Categories" (empty value), "Electronics", "Clothing", "Food", "Books".
  - Year filter: Options are "All Years" (empty value), "2024", "2023".
  - Chart type: Options are "Bar Chart", "Line Graph", "Pie Chart", "Scatter Plot".

- **Student Filters** (`id="student-filters"`): Two `<select>` dropdowns for department and chart type. Initially hidden using `style="display: none;"`.

- **Weather Filters** (`id="weather-filters"`): Two `<select>` dropdowns for city and chart type. Also initially hidden.

Each `<select>` has a unique `id` attribute (like `category-filter`, `year-filter`) so that JavaScript can read its current value using `$('#category-filter').val()`. Each `<label>` element uses the `for` attribute to associate it with its corresponding `<select>` by `id` — this is proper HTML form accessibility practice.

The first `<option>` in each dropdown has `value=""` (empty string), which represents "show all" — when the JavaScript sees an empty value, it doesn't add that filter to the API request.

**Canvas Element:**
`<canvas id="mainChart"></canvas>` is the HTML5 Canvas element. The Canvas API provides a 2D drawing surface that JavaScript can draw on. Chart.js uses this canvas to render all the charts. The canvas is inside its own `<section>` so it gets its own CSS styling (white background, shadow, padding).

**Table Structure:**
I created an HTML table with separate `<thead>` and `<tbody>` elements, each with their own `id`:
- `<thead id="table-head">` — The table header row (column names). This gets filled dynamically by JavaScript depending on which dataset is active.
- `<tbody id="table-body">` — The table data rows. JavaScript generates `<tr>` and `<td>` elements for each record and injects them here.

The table is wrapped in a `<div id="table-container">` with `overflow-x: auto` CSS so that if the table is wider than the screen, it becomes horizontally scrollable instead of breaking the layout.

**Action Buttons:**
Two `<button>` elements:
- `<button id="apply-filter">Apply Filters</button>` — Triggers data reload when clicked.
- `<button id="export-btn">Export as PNG</button>` — Downloads the current chart as a PNG image.

#### 8.1.3 Complete Source Code — app.js

```javascript
// app.js - Application Entry Point
// Initializes the dashboard on page load

$(document).ready(function () {
    // Load default dataset (sales) on page load
    loadData();
});
```

**Explanation:** This file uses jQuery's `$(document).ready()` function, which waits until the entire HTML DOM has been fully loaded and parsed before executing the code inside it. This ensures that all HTML elements (canvas, dropdowns, table) exist before we try to manipulate them. The `loadData()` function (defined in Rohan's `filters.js`) is called once to load the default Sales dataset and render the initial bar chart when the user first opens the page.

---

### 8.2 Annyunaa Gandra (SE24UARI009) — CSS Styling & Responsive Design

**File I Worked On:** `public/css/styles.css`

**My Role:** I designed and implemented all the visual styling for the dashboard using an external CSS stylesheet. I styled every section of the page including the header, navigation tabs, filter controls, chart container, summary cards, data table, and footer.

#### 8.2.1 Complete Source Code — styles.css

```css
/* styles.css - Dashboard Styling */

/* Reset and base styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background-color: #f0f2f5;
    color: #333;
    line-height: 1.6;
}

/* Header */
header {
    background-color: #2c3e50;
    color: #fff;
    text-align: center;
    padding: 20px;
}

header h1 {
    font-size: 28px;
    margin-bottom: 5px;
}

header p {
    font-size: 14px;
    color: #bdc3c7;
}

/* Navigation Tabs */
nav#dataset-tabs {
    display: flex;
    justify-content: center;
    background-color: #34495e;
    padding: 10px 0;
    gap: 10px;
}

.tab-btn {
    background-color: transparent;
    color: #bdc3c7;
    border: 2px solid transparent;
    padding: 10px 25px;
    font-size: 15px;
    cursor: pointer;
    border-radius: 5px;
    transition: all 0.3s;
}

.tab-btn:hover {
    color: #fff;
    border-color: #3498db;
}

.tab-btn.active {
    background-color: #3498db;
    color: #fff;
    border-color: #3498db;
}

/* Main Content */
main {
    max-width: 1100px;
    margin: 20px auto;
    padding: 0 20px;
}

/* Filter Section */
#filters {
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
    margin-bottom: 20px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

#filters h2 {
    font-size: 18px;
    margin-bottom: 15px;
    color: #2c3e50;
}

.filter-group {
    display: flex;
    align-items: center;
    gap: 12px;
    flex-wrap: wrap;
}

.filter-group label {
    font-weight: bold;
    font-size: 14px;
    color: #555;
}

.filter-group select {
    padding: 8px 12px;
    border: 1px solid #ccc;
    border-radius: 5px;
    font-size: 14px;
    background-color: #fff;
    cursor: pointer;
}

.filter-group select:focus {
    border-color: #3498db;
    outline: none;
}

#apply-filter, #export-btn {
    margin-top: 15px;
    padding: 10px 25px;
    border: none;
    border-radius: 5px;
    font-size: 14px;
    cursor: pointer;
    transition: background-color 0.3s;
}

#apply-filter {
    background-color: #3498db;
    color: #fff;
    margin-right: 10px;
}

#apply-filter:hover {
    background-color: #2980b9;
}

#export-btn {
    background-color: #27ae60;
    color: #fff;
}

#export-btn:hover {
    background-color: #219a52;
}

/* Chart Container */
#chart-container {
    background-color: #fff;
    padding: 25px;
    border-radius: 8px;
    margin-bottom: 20px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    min-height: 400px;
}

#mainChart {
    width: 100% !important;
    max-height: 450px;
}

/* Data Summary */
#data-summary {
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
    margin-bottom: 20px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

#data-summary h2 {
    font-size: 18px;
    margin-bottom: 10px;
    color: #2c3e50;
}

#summary-content {
    display: flex;
    gap: 20px;
    flex-wrap: wrap;
}

.summary-card {
    background-color: #ecf0f1;
    padding: 15px 20px;
    border-radius: 8px;
    text-align: center;
    min-width: 150px;
    flex: 1;
}

.summary-card h3 {
    font-size: 13px;
    color: #7f8c8d;
    margin-bottom: 5px;
    text-transform: uppercase;
}

.summary-card p {
    font-size: 22px;
    font-weight: bold;
    color: #2c3e50;
}

/* Data Table */
#data-table-section {
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
    margin-bottom: 20px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

#data-table-section h2 {
    font-size: 18px;
    margin-bottom: 10px;
    color: #2c3e50;
}

#table-container {
    overflow-x: auto;
}

#data-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 14px;
}

#data-table th {
    background-color: #2c3e50;
    color: #fff;
    padding: 10px 12px;
    text-align: left;
}

#data-table td {
    padding: 8px 12px;
    border-bottom: 1px solid #ddd;
}

#data-table tr:nth-child(even) {
    background-color: #f9f9f9;
}

#data-table tr:hover {
    background-color: #eaf2f8;
}

/* Footer */
footer {
    background-color: #2c3e50;
    color: #bdc3c7;
    text-align: center;
    padding: 15px;
    font-size: 13px;
}

footer p {
    margin: 3px 0;
}

/* Loading State */
.loading {
    text-align: center;
    padding: 40px;
    color: #7f8c8d;
    font-size: 16px;
}
```

#### 8.2.2 Detailed Technical Explanation

**CSS Reset (Universal Selector `*`):**
The first rule `* { margin: 0; padding: 0; box-sizing: border-box; }` is a CSS reset. The universal selector `*` matches every single HTML element on the page. By default, browsers add their own margins and padding to elements like `<h1>`, `<p>`, `<ul>`, etc. The reset removes all default spacing so we have full control. `box-sizing: border-box` changes how element width/height is calculated — with `border-box`, padding and border are included inside the specified width, so a `width: 100%` element doesn't overflow its container even with padding.

**Body Styling (Element Selector):**
I set the body font to `'Segoe UI', Tahoma, Geneva, Verdana, sans-serif` — this is a font stack. The browser tries the first font; if it's not available, it moves to the next. `Segoe UI` is the Windows system font and looks clean. The background color `#f0f2f5` is a light gray that creates contrast with the white content cards. `line-height: 1.6` adds spacing between lines of text for readability.

**Header Styling (Element Selector + Descendant Selector):**
`header` uses `background-color: #2c3e50` (dark blue-gray) with white text and centered alignment. The descendant selector `header h1` targets only `<h1>` elements inside `<header>`, setting font-size to 28px. `header p` targets the subtitle paragraph with a lighter gray color `#bdc3c7`.

**Navigation Tabs (ID Selector + Class Selector + Pseudo-class):**
- `nav#dataset-tabs` uses both an element selector and ID selector together — this is a compound selector that targets the `<nav>` element with `id="dataset-tabs"`. I used `display: flex` with `justify-content: center` to horizontally center the tab buttons, and `gap: 10px` to add spacing between them.
- `.tab-btn` is a class selector for all tab buttons. The key property is `transition: all 0.3s` — this creates a smooth 300-millisecond animation when any CSS property changes (like color or border-color on hover). `cursor: pointer` changes the mouse cursor to a hand icon when hovering, indicating the element is clickable.
- `.tab-btn:hover` is a **pseudo-class selector**. The `:hover` pseudo-class applies styles only when the user's mouse pointer is over the element. I change the text color to white and add a blue border.
- `.tab-btn.active` is a **compound class selector** — it matches elements that have BOTH the `tab-btn` class AND the `active` class. This styles the currently selected tab with a blue background (`#3498db`).

**Main Content Layout:**
`main { max-width: 1100px; margin: 20px auto; }` — `max-width` limits the content width on large screens so lines of text don't stretch too wide. `margin: 20px auto` creates 20px top/bottom spacing and `auto` left/right margins, which centers the `<main>` element horizontally on the page.

**Card-Style Sections:**
All content sections (`#filters`, `#chart-container`, `#data-summary`, `#data-table-section`) share a common card style:
- `background-color: #fff` — white background contrasting against the gray page background
- `padding: 20px` — inner spacing so content doesn't touch the card edges
- `border-radius: 8px` — rounded corners
- `margin-bottom: 20px` — spacing between cards
- `box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1)` — a subtle shadow. The `rgba()` function creates a black color with 10% opacity (0.1 alpha). The shadow is offset 0px horizontally, 2px downward, with a 5px blur radius. This creates a "floating card" depth effect.

**Filter Controls (Class Selector + Descendant Selector):**
`.filter-group` uses `display: flex` with `align-items: center` to vertically align labels and dropdowns on the same line. `flex-wrap: wrap` allows items to wrap to the next line if the screen is too narrow. `.filter-group select:focus` uses the `:focus` pseudo-class to change the border color to blue when the user clicks on a dropdown — this provides visual feedback showing which input is active.

**Button Styling (ID Selector + Pseudo-class):**
I used ID selectors for the two action buttons. Both share common styles via `#apply-filter, #export-btn` (a grouped selector — applying the same rules to multiple selectors at once). The Apply button is blue (`#3498db`) and the Export button is green (`#27ae60`). Each has a `:hover` pseudo-class that darkens the color — `#2980b9` (darker blue) and `#219a52` (darker green). The `transition: background-color 0.3s` makes the color change smooth.

**Summary Cards (Class Selector):**
`.summary-card` uses `flex: 1` which makes all cards grow equally to fill available space. `min-width: 150px` ensures cards don't get too narrow. `.summary-card h3` uses `text-transform: uppercase` to convert the heading text to all capital letters, and a small font-size of 13px for the label. `.summary-card p` uses a large 22px bold font for the statistic value.

**Table Styling (ID Selector + Pseudo-class + Descendant):**
- `#data-table { border-collapse: collapse; }` removes the default spacing between table cells, making cell borders touch each other.
- `#data-table th` styles table headers with the same dark background as the page header, white text, and left-aligned text.
- `#data-table td` adds padding and a light bottom border between rows.
- `#data-table tr:nth-child(even)` uses the `:nth-child(even)` pseudo-class to select every even-numbered table row and give it a light gray background (`#f9f9f9`). This creates the "zebra stripe" effect that makes tables easier to read.
- `#data-table tr:hover` changes the row background to light blue on hover, so users can track which row they're looking at.
- `#table-container { overflow-x: auto; }` adds a horizontal scrollbar if the table is wider than its container. This prevents the table from breaking the page layout on small screens.

**Five Types of CSS Selectors Used:**
1. **Simple (Element) Selectors:** `body`, `header`, `main`, `footer`, `table`
2. **Class Selectors:** `.tab-btn`, `.filter-group`, `.summary-card`, `.loading`
3. **ID Selectors:** `#filters`, `#chart-container`, `#data-table`, `#apply-filter`, `#export-btn`
4. **Pseudo-class Selectors:** `:hover`, `:focus`, `:nth-child(even)`
5. **Descendant/Compound Selectors:** `header h1`, `header p`, `#filters h2`, `.filter-group label`, `nav#dataset-tabs`, `.tab-btn.active`, `.summary-card h3`

---

### 8.3 Vishnu Vardhan Rao (SE24UARI010) — Chart Rendering with Chart.js

**File I Worked On:** `public/js/charts.js`

**My Role:** I wrote all the chart creation and rendering functions that use the Chart.js library to draw four different types of visualizations on the HTML5 Canvas element.

#### 8.3.1 Complete Source Code — charts.js

```javascript
// charts.js - Chart Rendering with Chart.js

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
```

#### 8.3.2 Detailed Technical Explanation

**How Chart.js Works:**
Chart.js is a JavaScript library that renders charts using the HTML5 Canvas API. The Canvas API provides a 2D drawing context on a `<canvas>` HTML element — it can draw shapes, lines, text, and images pixel by pixel. Chart.js abstracts this complexity: instead of manually drawing bars and axes, we pass a configuration object describing what we want, and Chart.js handles all the drawing, scaling, labeling, and animation.

**Global Variables:**
- `var currentChart = null;` — Stores a reference to the currently active Chart.js instance. This is essential because Chart.js does not automatically clean up old charts. If we create a new chart on the same canvas without destroying the old one, both charts will exist in memory and cause visual glitches (old chart data flickering behind the new chart). The `currentChart` variable lets us track and destroy the previous chart.
- `var chartColors = [...]` — An array of 12 hex color codes. These colors are used to distinguish different datasets in the chart (e.g., different product categories get different bar colors). The colors are chosen from a balanced palette that is visually distinct.

**destroyChart() Function:**
```javascript
function destroyChart() {
    if (currentChart !== null) {
        currentChart.destroy();
        currentChart = null;
    }
}
```
This function checks if a chart currently exists. If it does, `currentChart.destroy()` calls Chart.js's built-in `destroy()` method which removes the chart from the canvas, removes all event listeners, and frees memory. Then we set `currentChart = null` so subsequent checks know there's no active chart. This function is called at the beginning of every chart creation function.

**Canvas 2D Context:**
Every chart creation function starts with:
```javascript
var ctx = document.getElementById('mainChart').getContext('2d');
```
`document.getElementById('mainChart')` uses the DOM API to find the `<canvas>` element with `id="mainChart"` (created by Vineela in `index.html`). `.getContext('2d')` returns a `CanvasRenderingContext2D` object — this is the 2D drawing context that Chart.js uses to draw pixels on the canvas. The `ctx` variable is passed to `new Chart(ctx, config)`.

**createBarChart(labels, datasets, title) — Bar Chart:**

Parameters:
- `labels` — An array of strings for the x-axis (e.g., `['January', 'February', ..., 'December']`).
- `datasets` — An array of dataset objects. Each object has: `label` (string displayed in legend), `data` (array of numbers — one per label), `backgroundColor` (hex color for the bars).
- `title` — String displayed at the top of the chart.

The Chart.js configuration object has three main sections:
- `type: 'bar'` — Tells Chart.js to render vertical bars.
- `data` — Contains `labels` (x-axis categories) and `datasets` (the actual data values and their appearance).
- `options` — Configuration for chart behavior:
  - `responsive: true` — The chart automatically resizes when the browser window is resized, maintaining its aspect ratio.
  - `plugins.title` — Displays a title above the chart with font size 18px.
  - `plugins.legend` — Shows a legend at the top that maps colors to dataset labels.
  - `scales.y.beginAtZero: true` — Forces the y-axis to start from 0. Without this, Chart.js might start the axis at the minimum data value, which can be misleading.

**createLineChart(labels, datasets, title) — Line Graph:**

This function is structurally similar to the bar chart but uses `type: 'line'`. Line charts in Chart.js connect data points with lines. The dataset objects passed to this function include additional properties set by Rohan in `filters.js`:
- `fill: false` — By default, Chart.js fills the area under a line with a semi-transparent color. Setting this to `false` shows only the line.
- `tension: 0.3` — Controls the curve of the line. A value of 0 creates straight lines between points. 0.3 creates a gentle Bezier curve that makes the line smoother and easier to read.
- `borderColor` — The color of the line itself (not just the fill area).

**createPieChart(labels, data, title) — Pie Chart:**

Pie charts work differently from bar/line charts. Instead of multiple datasets with shared labels, a pie chart has one dataset with multiple values:
- `labels` — Names for each slice (e.g., `['Electronics', 'Clothing', 'Food', 'Books']`).
- `data` — Numeric values for each slice (e.g., `[753000, 459000, 310000, 162000]`). Chart.js automatically calculates percentages.
- `backgroundColor: chartColors.slice(0, labels.length)` — Uses the JavaScript array `slice()` method to take the first N colors from our palette, where N equals the number of pie slices. This ensures each slice gets a different color.
- `borderColor: '#fff'` and `borderWidth: 2` — Adds a white 2px border between pie slices for visual separation.
- `legend.position: 'right'` — Places the legend to the right of the pie chart instead of on top. This is better for pie charts because the legend doesn't cover the circle.

Pie charts do not have `scales` in their options because they don't use x/y axes.

**createScatterChart(datasets, title, xLabel, yLabel) — Scatter Plot:**

Scatter plots display individual data points as dots on an x-y coordinate system. They're useful for showing relationships between two variables (e.g., "do products with more units sold also have higher revenue?").

Key differences from bar/line charts:
- The `data` property in each dataset is an array of `{x, y}` objects instead of just numbers. For example: `[{x: 120, y: 45000}, {x: 140, y: 52000}]`.
- There is no `labels` array in the chart data — the x-axis is a numeric scale, not categories.
- Both `scales.x` and `scales.y` have `title` objects with `display: true` and `text` set to the axis label (e.g., "Units Sold" and "Revenue (Rs)").
- `pointRadius: 6` or `pointRadius: 8` (set in `filters.js`) controls how large the dots appear.

---

### 8.4 Rohan Yaski (SE24UARI042) — Data Filtering & Interactivity with jQuery

**File I Worked On:** `public/js/filters.js`

**My Role:** I wrote the core application logic that ties everything together — jQuery event handlers for user interactions, Fetch API calls to the Express server, data transformation algorithms that convert raw JSON into Chart.js format, and dynamic HTML generation for summary cards and data tables.

#### 8.4.1 Complete Source Code — filters.js

```javascript
// filters.js - Data Filtering and Interactivity with jQuery

// Current active dataset
var activeDataset = 'sales';

$(document).ready(function () {

    // Tab switching using jQuery click event
    $('.tab-btn').click(function () {
        $('.tab-btn').removeClass('active');
        $(this).addClass('active');
        activeDataset = $(this).data('dataset');
        $('.filter-group').slideUp(200);
        if (activeDataset === 'sales') {
            $('#sales-filters').slideDown(200);
        } else if (activeDataset === 'students') {
            $('#student-filters').slideDown(200);
        } else if (activeDataset === 'weather') {
            $('#weather-filters').slideDown(200);
        }
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
    var url = '/api/sales?';
    if (category) url += 'category=' + category + '&';
    if (year) url += 'year=' + year;
    fetch(url)
        .then(function (response) { return response.json(); })
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
        createScatterChart(datasets, 'Units Sold vs Revenue', 'Units Sold',
            'Revenue (Rs)');
    } else {
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
    html += '<div class="summary-card"><h3>Total Revenue</h3><p>Rs ' +
        totalRevenue.toLocaleString() + '</p></div>';
    html += '<div class="summary-card"><h3>Total Units</h3><p>' +
        totalUnits.toLocaleString() + '</p></div>';
    html += '<div class="summary-card"><h3>Avg Revenue/Month</h3><p>Rs ' +
        avgRevenue.toLocaleString() + '</p></div>';
    html += '<div class="summary-card"><h3>Records</h3><p>' + data.length +
        '</p></div>';
    $('#summary-content').html(html);
}

// Render sales data table
function renderSalesTable(data) {
    var headHtml = '<tr><th>Month</th><th>Category</th><th>Revenue</th>' +
        '<th>Units</th><th>Year</th></tr>';
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

// (Similar functions exist for loadStudentData, renderStudentChart,
//  renderStudentSummary, renderStudentTable, loadWeatherData,
//  renderWeatherChart, renderWeatherSummary, renderWeatherTable)
```

*Note: The student and weather rendering functions follow the same pattern as the sales functions shown above. The full source code is in the `filters.js` file.*

#### 8.4.2 Detailed Technical Explanation

**Global Variable — activeDataset:**
`var activeDataset = 'sales';` tracks which dataset tab is currently selected. This is a global variable (declared outside any function) so it's accessible by all functions in every JS file. The `export.js` file also reads this variable to name the exported PNG file.

**jQuery Event Handling — $(document).ready():**
All my event handlers are wrapped inside `$(document).ready(function() { ... })`. This is a jQuery function that waits until the browser has fully loaded and parsed the HTML document before running the code inside. Without this, our jQuery selectors might try to find elements that don't exist yet. This is the same pattern we learned in the jQuery module of the course.

**Tab Click Event Handler:**
```javascript
$('.tab-btn').click(function () {
    $('.tab-btn').removeClass('active');
    $(this).addClass('active');
    activeDataset = $(this).data('dataset');
    // ...
});
```
- `$('.tab-btn')` — jQuery class selector that selects all elements with class `tab-btn` (the three navigation buttons).
- `.click(function() {...})` — Attaches a click event handler. When any tab button is clicked, this function runs. This is a **callback function** — a function passed as an argument to another function, which runs when an event occurs.
- `$('.tab-btn').removeClass('active')` — Removes the `active` CSS class from ALL tab buttons. The `.removeClass()` method is a jQuery DOM manipulation method.
- `$(this).addClass('active')` — `$(this)` refers to the specific button that was clicked (not all buttons). `.addClass()` adds the `active` CSS class to only that button. This is how we visually highlight the selected tab.
- `$(this).data('dataset')` — Reads the value of the `data-dataset` HTML attribute from the clicked button. For example, if the user clicks the "Weather Data" button which has `data-dataset="weather"`, this returns the string `"weather"`. The `.data()` jQuery method reads HTML5 custom data attributes.

**jQuery Slide Effects:**
```javascript
$('.filter-group').slideUp(200);
$('#sales-filters').slideDown(200);
```
- `slideUp(200)` — jQuery animation that smoothly hides elements by reducing their height to 0 over 200 milliseconds. This hides all filter groups.
- `slideDown(200)` — jQuery animation that smoothly reveals an element by expanding its height from 0 to its natural height over 200 milliseconds. This shows only the relevant filter group.
These are the jQuery effects we learned in the jQuery module — `slideUp()`, `slideDown()`, `fadeIn()`, `fadeOut()`, etc.

**Dropdown Change Event:**
```javascript
$('select').on('change', function () {
    loadData();
});
```
`$('select')` selects all `<select>` dropdown elements on the page. `.on('change', ...)` uses the jQuery `.on()` method to attach an event handler for the `change` event, which fires whenever the user selects a different option. This makes the charts update in real-time without needing to click the "Apply Filters" button.

**Fetch API — Loading Data from Server:**
```javascript
function loadSalesData() {
    var category = $('#category-filter').val();
    var year = $('#year-filter').val();
    var chartType = $('#chart-type-sales').val();
    var url = '/api/sales?';
    if (category) url += 'category=' + category + '&';
    if (year) url += 'year=' + year;
    fetch(url)
        .then(function (response) { return response.json(); })
        .then(function (data) {
            renderSalesChart(data, chartType, category);
            renderSalesSummary(data);
            renderSalesTable(data);
        })
        .catch(function (error) {
            console.log('Error fetching sales data:', error);
        });
}
```
- `$('#category-filter').val()` — jQuery's `.val()` method reads the current value of a form input. For a `<select>` element, it returns the `value` attribute of the currently selected `<option>`. If "All Categories" is selected, `.val()` returns `""` (empty string).
- **Building the URL:** I construct the API URL by checking if each filter has a value. If `category` is not empty, I append `category=Electronics` to the URL. If `year` is not empty, I append `year=2024`. This creates URLs like `/api/sales?category=Electronics&year=2024`. These are **query parameters** — the `?` starts the query string, `=` separates key from value, and `&` separates multiple parameters.
- **fetch(url)** — The Fetch API is a modern browser API for making HTTP requests. `fetch(url)` sends a GET request to our Express server and returns a **Promise**.
- **.then(function(response) { return response.json(); })** — Promises use `.then()` for chaining asynchronous operations. The first `.then()` receives the HTTP response object. `response.json()` parses the response body as JSON and returns another Promise.
- **.then(function(data) { ... })** — The second `.then()` receives the parsed JSON data as a JavaScript array of objects. I call three functions: one to render the chart, one to render the summary, and one to render the table.
- **.catch(function(error) { ... })** — If anything goes wrong (network error, server error), the `.catch()` runs and logs the error.

**Data Transformation — Pie Chart (Aggregation Algorithm):**
```javascript
var categoryTotals = {};
data.forEach(function (item) {
    if (!categoryTotals[item.category]) {
        categoryTotals[item.category] = 0;
    }
    categoryTotals[item.category] += item.revenue;
});
var labels = Object.keys(categoryTotals);
var values = Object.values(categoryTotals);
```
This algorithm groups and sums revenue by category. It uses a JavaScript object (`categoryTotals`) as a dictionary/hashmap:
1. Loop through each data record using `forEach` (a callback-based array method).
2. If the category key doesn't exist yet in the object, initialize it to 0.
3. Add the record's revenue to that category's running total.
4. After the loop, `Object.keys()` extracts category names as an array, and `Object.values()` extracts the totals as an array.

**Data Transformation — Bar/Line Chart (Grouping Algorithm):**
```javascript
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
```
This creates a nested object structure: `{Electronics: {January: 45000, February: 52000, ...}, Clothing: {...}}`. Then I convert each category into a Chart.js dataset using `months.map()` to ensure values are in the correct month order.

**Data Transformation — Scatter Plot (Point Mapping):**
For scatter plots, I transform each record into an `{x, y}` coordinate object. For sales: `x = item.units` (units sold), `y = item.revenue` (revenue in Rs). For students: `x = s.math` (math score), `y = s.programming` (programming score). These points are grouped by category/dataset and each group gets a different color.

**jQuery DOM Manipulation — Summary Cards:**
```javascript
var html = '';
html += '<div class="summary-card"><h3>Total Revenue</h3><p>Rs ' +
    totalRevenue.toLocaleString() + '</p></div>';
// ...
$('#summary-content').html(html);
```
I build an HTML string using string concatenation (`+`). `toLocaleString()` formats numbers with commas (e.g., `753000` becomes `"7,53,000"` in Indian locale). Then `$('#summary-content').html(html)` replaces the entire contents of the `#summary-content` div with this new HTML. The `.html()` jQuery method sets the innerHTML of the matched element.

**jQuery DOM Manipulation — Data Table:**
```javascript
$('#table-head').html(headHtml);
$('#table-body').html(bodyHtml);
```
Similarly, I build table HTML strings with `<tr>`, `<th>`, and `<td>` tags and inject them into the table's `<thead>` and `<tbody>` elements. This completely replaces the table content every time new data is loaded, so the table always shows the currently filtered data.

**Student Data Functions:**
The student chart can render as a bar chart (scores by subject per student), line chart (same data as lines), or scatter plot (math vs programming scores). The scatter plot is particularly interesting — it shows the correlation between a student's math skills and their programming ability.

**Weather Data Functions:**
Weather charts show temperature trends across months for different cities. The scatter plot shows temperature vs rainfall — revealing that high rainfall months tend to have moderate temperatures (monsoon season).

---

### 8.5 Varun Ventrapagada (SE24UARI006) — Backend Server (Node.js / Express.js)

**Files I Worked On:** `server.js`, `package.json`

**My Role:** I built the complete backend server using Node.js and Express.js. The server serves the static frontend files, provides REST API endpoints for each dataset, implements server-side data filtering using query parameters, includes request logging middleware, and handles errors with proper HTTP status codes.

#### 8.5.1 Complete Source Code — server.js

```javascript
// server.js - Express.js Backend

const express = require('express');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = 3000;

// Middleware: Request logger
app.use(function (req, res, next) {
    console.log('[' + new Date().toLocaleTimeString() + '] ' +
        req.method + ' ' + req.url);
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
        if (req.query.category) {
            salesData = salesData.filter(function (item) {
                return item.category === req.query.category;
            });
        }
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
        if (req.query.city) {
            weatherData = weatherData.filter(function (item) {
                return item.city === req.query.city;
            });
        }
        res.json(weatherData);
    });
});

// API Route: GET /api/categories - returns unique categories
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
```

#### 8.5.2 package.json

```json
{
  "name": "interactive-data-visualizer",
  "version": "1.0.0",
  "description": "Interactive Data Visualization Dashboard - Web Workshop Project 15",
  "main": "server.js",
  "scripts": {
    "start": "node server.js"
  },
  "dependencies": {
    "express": "^4.18.2"
  }
}
```

#### 8.5.3 Detailed Technical Explanation

**Node.js Module Imports — require():**
```javascript
const express = require('express');
const fs = require('fs');
const path = require('path');
```
Node.js uses the `require()` function to import modules:
- `express` — An external npm package (installed via `npm install`). Express is a web framework that simplifies creating HTTP servers with routing, middleware, and static file serving.
- `fs` — A built-in Node.js module (no installation needed) that provides file system operations like reading files (`fs.readFile`), writing files, and checking if files exist. We use it to read the JSON data files from disk.
- `path` — A built-in Node.js module for working with file paths. `path.join()` safely combines path segments with the correct separator for the operating system. For example, `path.join(__dirname, 'public', 'data', 'sales.json')` creates the full absolute path to the sales JSON file. `__dirname` is a special Node.js variable that contains the absolute path of the directory containing the current file.

**Creating the Express App:**
```javascript
const app = express();
const PORT = 3000;
```
`express()` creates a new Express application instance. We store the port number in a constant for easy reference.

**Middleware — Request Logger:**
```javascript
app.use(function (req, res, next) {
    console.log('[' + new Date().toLocaleTimeString() + '] ' +
        req.method + ' ' + req.url);
    next();
});
```
Middleware functions in Express are functions that have access to the request object (`req`), response object (`res`), and the `next` function. `app.use()` registers middleware that runs for EVERY incoming request.

This logger middleware:
1. Creates a timestamp using `new Date().toLocaleTimeString()` (e.g., "2:30:45 PM").
2. Reads `req.method` (GET, POST, etc.) and `req.url` (the requested URL path).
3. Logs the information to the terminal using `console.log()`.
4. Calls `next()` to pass control to the next middleware or route handler. Without calling `next()`, the request would hang and never get a response.

Example terminal output: `[2:30:45 PM] GET /api/sales?category=Electronics`

**Middleware — Static File Server:**
```javascript
app.use(express.static(path.join(__dirname, 'public')));
```
`express.static()` is a built-in Express middleware that serves static files (HTML, CSS, JS, images, JSON) from a directory. When a browser requests `http://localhost:3000/index.html`, Express looks for the file at `public/index.html` on disk and sends it back. When it requests `http://localhost:3000/css/styles.css`, Express finds `public/css/styles.css`.

Importantly, when a browser requests just `http://localhost:3000/`, Express automatically serves `public/index.html` because `index.html` is the default file for directory requests.

**API Route — GET /api/sales:**
```javascript
app.get('/api/sales', function (req, res) {
    var filePath = path.join(__dirname, 'public', 'data', 'sales.json');
    fs.readFile(filePath, 'utf8', function (err, data) {
        // ...
    });
});
```
`app.get('/api/sales', callback)` registers a route handler for GET requests to `/api/sales`. When the frontend's `fetch('/api/sales?category=Electronics&year=2024')` hits the server, Express matches this route and runs the callback function.

**fs.readFile() — Asynchronous File Reading:**
`fs.readFile(filePath, 'utf8', callback)` reads a file asynchronously:
- `filePath` — The absolute path to the JSON file.
- `'utf8'` — The character encoding. This tells Node.js to return the file contents as a string (not a raw Buffer).
- `callback` — A function that runs when the file has been read. It receives two parameters: `err` (an error object if something went wrong, `null` if successful) and `data` (the file contents as a string).

This is **asynchronous** — Node.js doesn't wait for the file to finish reading. It continues processing other requests and runs the callback when the file data is ready. This is the same pattern we learned in the Node.js module with streams and callbacks.

**Error Handling in the Callback:**
```javascript
if (err) {
    res.status(500).json({ error: 'Failed to read sales data' });
    return;
}
```
If `fs.readFile` encounters an error (file doesn't exist, permission denied, etc.), we:
1. Set the HTTP status code to 500 (Internal Server Error) using `res.status(500)`.
2. Send a JSON error response using `res.json()`.
3. Use `return` to stop execution so the rest of the callback doesn't run.

**JSON Parsing:**
`var salesData = JSON.parse(data);` — The `data` parameter from `fs.readFile` is a string (the raw file contents). `JSON.parse()` converts this JSON string into a JavaScript array of objects that we can filter and manipulate.

**Server-Side Filtering with Query Parameters:**
```javascript
if (req.query.category) {
    salesData = salesData.filter(function (item) {
        return item.category === req.query.category;
    });
}
if (req.query.year) {
    salesData = salesData.filter(function (item) {
        return item.year === parseInt(req.query.year);
    });
}
```
- `req.query` — Express automatically parses the URL query string into an object. For the URL `/api/sales?category=Electronics&year=2024`, `req.query` becomes `{ category: 'Electronics', year: '2024' }`.
- `if (req.query.category)` — Checks if the category parameter was provided. If the user selected "All Categories" on the frontend, the value is an empty string, which is falsy in JavaScript, so this condition is `false` and no filtering happens.
- `.filter(function(item) { ... })` — The JavaScript array `filter()` method creates a new array containing only the elements where the callback returns `true`. It does not modify the original array.
- `parseInt(req.query.year)` — Query parameters are always strings. The year field in our JSON data is a number. `parseInt()` converts the string `"2024"` to the number `2024` so the `===` comparison works correctly.

**Sending the JSON Response:**
`res.json(salesData)` — Express's `res.json()` method:
1. Converts the JavaScript array to a JSON string using `JSON.stringify()`.
2. Sets the response `Content-Type` header to `application/json`.
3. Sends the response back to the browser.

**Extracting Unique Categories:**
```javascript
var categories = [];
salesData.forEach(function (item) {
    if (categories.indexOf(item.category) === -1) {
        categories.push(item.category);
    }
});
```
This loop iterates through all sales records. For each record, `indexOf()` checks if the category already exists in the `categories` array. `indexOf()` returns `-1` if the value is not found. If the category is not yet in the array, `push()` adds it. This produces an array of unique category names: `["Electronics", "Clothing", "Food", "Books"]`.

**404 Handler:**
```javascript
app.use(function (req, res) {
    res.status(404).json({ error: 'Route not found' });
});
```
This middleware runs for any request that didn't match a defined route. It returns HTTP status 404 (Not Found). It must be placed AFTER all route definitions because Express processes middleware in order — if placed before routes, it would catch everything.

**Error Handling Middleware:**
```javascript
app.use(function (err, req, res, next) {
    console.error('Server error:', err.message);
    res.status(500).json({ error: 'Internal server error' });
});
```
This is a special Express error-handling middleware identified by having four parameters (`err, req, res, next`) instead of three. If any route handler throws an error, Express skips to this middleware. It logs the error and returns a 500 status code.

**Starting the Server:**
```javascript
app.listen(PORT, function () {
    console.log('Data Visualizer server running at http://localhost:' + PORT);
});
```
`app.listen()` binds the Express app to the specified port and starts listening for incoming HTTP connections. The callback function runs once the server is ready, printing a confirmation message.

---

### 8.6 Akshat Reddy (SE24UARI032) — JSON Data Preparation & Export Feature

**Files I Worked On:** `public/data/sales.json`, `public/data/students.json`, `public/data/weather.json`, `public/js/export.js`

**My Role:** I prepared all three JSON datasets with realistic and meaningful data, and I built the chart export feature that lets users download any chart as a PNG image using the HTML5 Canvas API.

#### 8.6.1 JSON Data Files — Design and Structure

**sales.json — 72 Records:**

The sales dataset contains monthly revenue and unit sales data for a fictional retail store. The data has 5 fields per record:

| Field     | Type   | Description                            | Example     |
|-----------|--------|----------------------------------------|-------------|
| month     | string | Month name (January to December)       | "January"   |
| category  | string | Product category                       | "Electronics"|
| revenue   | number | Monthly revenue in Indian Rupees       | 45000       |
| units     | number | Number of units sold                   | 120         |
| year      | number | Year (2023 or 2024)                    | 2024        |

The dataset covers 4 categories across 12 months for 2 years = 4 x 12 x 2 = 96 possible records. I created 72 records (all 12 months for Electronics and Clothing in both years, plus all 12 months for Food and Books in 2024 only).

I designed the data with realistic patterns:
- **Electronics**: Highest revenue per unit (Rs 375/unit avg), lowest units sold. Revenue peaks in November-December (holiday shopping season).
- **Clothing**: Moderate revenue, moderate units. Peaks in summer and winter.
- **Food**: Lower revenue per unit (Rs 50/unit avg), highest units sold — people buy food frequently.
- **Books**: Lowest revenue overall. Peaks in August-September (back-to-school).
- **2024 data is ~10% higher than 2023** — showing year-over-year growth.

Sample record:
```json
{ "month": "January", "category": "Electronics", "revenue": 45000,
  "units": 120, "year": 2024 }
```

**students.json — 20 Records:**

The student performance dataset contains academic scores for 20 students across 4 departments. The data has 7 fields per record:

| Field       | Type   | Description              | Range  |
|-------------|--------|--------------------------|--------|
| name        | string | Student identifier       | A to T |
| department  | string | Academic department      | CSE, ECE, AI, ME |
| math        | number | Math score               | 60-95  |
| science     | number | Science score            | 65-95  |
| english     | number | English score            | 68-92  |
| programming | number | Programming score        | 45-97  |
| gpa         | number | Cumulative GPA           | 6.0-9.3|

I designed realistic score patterns by department:
- **CSE students**: Strong programming scores (78-95), well-rounded.
- **AI students**: Highest programming (80-96) and math (70-94) scores.
- **ECE students**: Strong science (70-95) and math (65-92), moderate programming (60-80).
- **ME students**: Strong science (65-92), lowest programming scores (45-60) — mechanical engineering has less focus on coding.

This allows interesting visualizations — the scatter plot of math vs programming scores shows clear department clusters.

**weather.json — 36 Records:**

The weather dataset contains monthly climate data for 3 Indian cities. The data has 5 fields per record:

| Field       | Type   | Description              | Range      |
|-------------|--------|--------------------------|------------|
| city        | string | City name                | Hyderabad, Mumbai, Delhi |
| month       | string | Month name               | January-December |
| temperature | number | Average temperature (C)  | 14-38      |
| humidity    | number | Average humidity (%)     | 28-88      |
| rainfall    | number | Monthly rainfall (mm)    | 0-840      |

Data is based on real climate patterns for Indian cities:
- **Hyderabad**: Moderate climate, monsoon rainfall June-October, peak temp in May (38C).
- **Mumbai**: Extreme monsoon — July rainfall is 840mm (heaviest in India). Humid year-round.
- **Delhi**: Extreme temperature variation — 14C in January to 38C in June. Cold winters, hot summers.

This data creates dramatic scatter plots (temperature vs rainfall shows the monsoon effect) and meaningful line charts (clear seasonal patterns).

#### 8.6.2 Complete Source Code — export.js

```javascript
// export.js - Export and Data Utilities

$(document).ready(function () {

    // Export chart as PNG image
    $('#export-btn').click(function () {
        var canvas = document.getElementById('mainChart');

        if (currentChart === null) {
            alert('No chart to export. Please load data first.');
            return;
        }

        // Create a temporary link element
        var link = document.createElement('a');
        link.download = 'chart-' + activeDataset + '-' + Date.now() + '.png';
        link.href = canvas.toDataURL('image/png');
        link.click();
    });

});
```

#### 8.6.3 Detailed Technical Explanation — Export Feature

The export feature uses a combination of jQuery event handling, DOM manipulation, and the HTML5 Canvas API.

**jQuery Click Event:**
`$('#export-btn').click(function () { ... })` — Uses jQuery's ID selector to find the Export button and attaches a click event handler.

**Getting the Canvas Element:**
`var canvas = document.getElementById('mainChart')` — Uses the standard DOM API (not jQuery) to get a direct reference to the `<canvas>` HTML element. We need the native DOM element (not a jQuery object) because the Canvas API's `toDataURL()` method is a native DOM method, not a jQuery method.

**Validation Check:**
```javascript
if (currentChart === null) {
    alert('No chart to export. Please load data first.');
    return;
}
```
Before attempting to export, I check if `currentChart` (the global variable from Vishnu's `charts.js`) is `null`. If no chart has been created yet (e.g., the user clicks Export before any data loads), I show a browser alert dialog and return early. This prevents an empty or blank image from being downloaded.

**Canvas toDataURL() — The Core Export Mechanism:**
```javascript
link.href = canvas.toDataURL('image/png');
```
`canvas.toDataURL('image/png')` is an HTML5 Canvas API method that:
1. Reads all the pixels currently drawn on the canvas (the chart rendered by Chart.js).
2. Encodes those pixels as a PNG image.
3. Returns a **Data URL** string — a base64-encoded representation of the image. It looks like: `data:image/png;base64,iVBORw0KGgoAAAANSUhE...` (a very long string).

This Data URL can be used anywhere a regular URL is expected — as an `<img>` src, an `<a>` href, etc.

**Triggering the Download:**
```javascript
var link = document.createElement('a');
link.download = 'chart-' + activeDataset + '-' + Date.now() + '.png';
link.href = canvas.toDataURL('image/png');
link.click();
```
1. `document.createElement('a')` creates a new `<a>` (anchor/link) element in memory. This element is never added to the page — it exists only in JavaScript.
2. `link.download = '...'` sets the HTML5 `download` attribute, which tells the browser to download the linked resource instead of navigating to it, and specifies the filename.
3. The filename format is `chart-sales-1700000000000.png` where:
   - `activeDataset` is the current dataset name (from Rohan's `filters.js`)
   - `Date.now()` returns the current timestamp in milliseconds (a unique number), preventing filename collisions if the user exports multiple charts
4. `link.href = canvas.toDataURL('image/png')` sets the link's URL to the base64-encoded PNG image.
5. `link.click()` programmatically clicks the link, triggering the browser's download dialog. The user sees a "Save As" dialog or the file downloads automatically to their Downloads folder.

---

## 9. Concepts from Course Material Used

| Concept                     | Where Used                                                        | File(s)         |
|-----------------------------|-------------------------------------------------------------------|-----------------|
| HTML5 `<!DOCTYPE html>`     | Document type declaration                                         | index.html      |
| Semantic HTML tags          | header, nav, main, section, footer                                | index.html      |
| HTML headings (h1, h2)      | Page title, section headings                                      | index.html      |
| HTML paragraphs (p)         | Subtitle, footer text                                             | index.html      |
| HTML forms (select, option) | Filter dropdowns with label-for accessibility                     | index.html      |
| HTML buttons                | Apply Filter and Export buttons                                   | index.html      |
| HTML tables (table, thead, tbody, tr, th, td) | Data table display                              | index.html      |
| HTML canvas                 | Chart rendering surface                                           | index.html      |
| HTML5 data attributes       | data-dataset on tab buttons                                       | index.html      |
| External CSS stylesheet     | link rel="stylesheet" href="css/styles.css"                       | index.html      |
| CSS universal selector (*)  | Reset margins, padding, box-sizing                                | styles.css      |
| CSS element selectors       | body, header, footer, main, table                                 | styles.css      |
| CSS class selectors         | .tab-btn, .filter-group, .summary-card                            | styles.css      |
| CSS ID selectors            | #filters, #chart-container, #data-table                           | styles.css      |
| CSS pseudo-class selectors  | :hover, :focus, :nth-child(even)                                  | styles.css      |
| CSS descendant selectors    | header h1, #filters h2, .summary-card h3                         | styles.css      |
| CSS compound selectors      | nav#dataset-tabs, .tab-btn.active                                 | styles.css      |
| CSS grouped selectors       | #apply-filter, #export-btn shared styles                          | styles.css      |
| CSS Flexbox layout          | Navigation tabs, filter controls, summary cards                   | styles.css      |
| CSS transitions             | Smooth hover effects on buttons and tabs                          | styles.css      |
| CSS box-shadow              | Card depth effect on content sections                             | styles.css      |
| CSS border-radius           | Rounded corners on cards, buttons, inputs                         | styles.css      |
| CSS overflow                | Horizontal scroll on data table                                   | styles.css      |
| JavaScript variables        | var currentChart, chartColors, activeDataset                      | charts.js, filters.js |
| JavaScript functions        | createBarChart(), loadData(), renderSalesChart()                  | charts.js, filters.js |
| JavaScript if/else          | Chart type selection, filter conditional                          | filters.js      |
| JavaScript for...in loop    | Iterating over category objects                                   | filters.js      |
| JavaScript arrays           | forEach, filter, map, push, indexOf, slice                        | filters.js, server.js |
| JavaScript objects          | Nested grouping objects, Chart.js config                          | filters.js, charts.js |
| JavaScript string concat    | Building HTML strings, URL query strings                          | filters.js      |
| JavaScript JSON.parse()     | Converting JSON string to JavaScript array                        | server.js       |
| JavaScript callbacks        | fs.readFile callback, event handler callbacks                     | server.js, filters.js |
| JavaScript DOM API          | getElementById, createElement, getContext                         | charts.js, export.js |
| jQuery $(document).ready()  | Ensuring DOM is loaded before script runs                         | app.js, filters.js, export.js |
| jQuery selectors            | $('#id'), $('.class'), $('select')                                | filters.js, export.js |
| jQuery .click()             | Tab buttons, Apply button, Export button                          | filters.js, export.js |
| jQuery .on('change')        | Real-time dropdown change detection                               | filters.js      |
| jQuery .val()               | Reading dropdown selected values                                  | filters.js      |
| jQuery .html()              | Injecting summary cards and table rows                            | filters.js      |
| jQuery .addClass()          | Highlighting active tab                                           | filters.js      |
| jQuery .removeClass()       | Removing highlight from inactive tabs                             | filters.js      |
| jQuery .data()              | Reading data-dataset attribute from buttons                       | filters.js      |
| jQuery slideUp/slideDown    | Animated show/hide of filter panels                               | filters.js      |
| jQuery CDN loading          | Including jQuery 3.7.1 from code.jquery.com                      | index.html      |
| Fetch API                   | HTTP GET requests to Express API endpoints                        | filters.js      |
| Fetch .then() chaining      | Processing async response and data                                | filters.js      |
| Fetch .catch()              | Handling network/server errors                                    | filters.js      |
| Node.js require()           | Importing express, fs, path modules                               | server.js       |
| Node.js fs module           | fs.readFile() to read JSON data files                             | server.js       |
| Node.js path module         | path.join() for cross-platform file paths                         | server.js       |
| Node.js __dirname           | Getting current directory absolute path                           | server.js       |
| Express app creation        | express() to create application instance                          | server.js       |
| Express app.get()           | Defining GET route handlers                                       | server.js       |
| Express middleware           | Request logger, static files, 404 handler, error handler         | server.js       |
| Express next()              | Passing control in middleware chain                               | server.js       |
| Express req.query           | Reading URL query parameters                                      | server.js       |
| Express res.json()          | Sending JSON responses                                            | server.js       |
| Express res.status()        | Setting HTTP status codes (200, 404, 500)                         | server.js       |
| Express express.static()    | Serving static files from public/ directory                       | server.js       |
| Express app.listen()        | Starting server on port 3000                                      | server.js       |
| Canvas API getContext('2d') | Getting 2D drawing context for Chart.js                           | charts.js       |
| Canvas API toDataURL()      | Converting canvas to PNG for export                               | export.js       |
| npm package.json            | Project metadata, dependencies, start script                      | package.json    |
| npm install                 | Installing Express.js dependency                                  | package.json    |

---

## 10. Difficulty Level

**Advanced** — This project combines:
- **Frontend development**: HTML5 semantic structure, CSS styling with 5 selector types, responsive Flexbox layout
- **Client-side programming**: jQuery event handling and DOM manipulation, Fetch API for async data loading, data transformation algorithms (grouping, aggregation, mapping)
- **Data visualization**: Four chart types (bar, line, pie, scatter) using Chart.js on HTML5 Canvas
- **Backend development**: Node.js/Express.js server with REST API routes, server-side filtering with query parameters, middleware (logging, static files, error handling), asynchronous file I/O with callbacks
- **Full-stack integration**: Frontend fetches data from backend APIs, backend reads and filters JSON files, Canvas API enables chart export

---

## 11. Conclusion

The Interactive Data Visualizer is a full-stack web application that demonstrates every major technology covered in the Web Workshop course — from HTML5 semantic markup and CSS styling to jQuery interactivity, Chart.js visualizations, and a Node.js/Express.js backend with REST APIs. The project is divided into six clear modules, each handled by one team member, that work together seamlessly: Vineela's HTML structure provides the layout, Annyunaa's CSS creates the visual design, Vishnu Vardhan's Chart.js functions render the visualizations, Rohan's jQuery code handles all user interactions and data flow, Varun's Express server provides the data API, and Akshat's JSON datasets and export feature complete the application. The result is an interactive dashboard where users can explore three different datasets through four chart types, apply filters to drill down into specific data segments, view computed statistics, and export any chart as a PNG image.
