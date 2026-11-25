# Presentation Day Guide

## Interactive Data Visualizer — Who Presents What, When to Show Code

---

## Before the Presentation

**Setup checklist (do this 5 minutes before):**

1. Open a terminal, navigate to the project folder, and run:
   ```
   cd interactive-data-visualizer
   node server.js
   ```
   Confirm you see: `Data Visualizer server running at http://localhost:3000`

2. Open **Google Chrome** with two tabs:
   - Tab 1: `http://localhost:3000` (the app — leave it on the default Sales bar chart)
   - Tab 2: `http://localhost:3000/api/sales` (raw API — keep this ready for later)

3. Open the project folder in **VS Code** (or whatever editor you use) with these files ready in tabs:
   - `index.html`
   - `styles.css`
   - `charts.js`
   - `filters.js`
   - `server.js`
   - `export.js`
   - `data/sales.json`

4. Open the **PRESENTATION.pptx** in full-screen mode.

5. Keep the **terminal visible** in the background — you'll need to show server logs later.

---

## Presentation Flow — Slide by Slide

Total estimated time: **15–18 minutes**

---

### Slide 1 — Title (Varun presents, ~30 seconds)

**Varun says:**
"Good morning ma'am. We are Team [your team number]. Our project is Project 15 — Interactive Data Visualizer. I'll quickly introduce the team and then we'll walk you through what we built."

Read out the team members.

---

### Slide 2 — Problem Statement (Varun presents, ~1 minute)

**Varun says:**
"Our problem statement was to build an interactive data visualization app that reads JSON data and displays it as charts. It needs to support bar charts, line graphs, pie charts, and scatter plots, with filtering, drill-down, and export. The difficulty level is Advanced."

Just read through the bullet points naturally. Don't rush.

---

### Slide 3 — Tools & Technologies (Varun presents, ~1 minute)

**Varun says:**
"Here's our tech stack. On the frontend we used HTML5, CSS3, jQuery for interactivity, Chart.js for the visualizations, the Fetch API to call our server, and the Canvas API for rendering and export. On the backend we used Node.js with Express.js."

Point at the two columns as you talk.

---

### Slide 4 — Architecture (Varun presents, ~1.5 minutes)

**Varun says:**
"This is how data flows through our app. The user clicks a filter or tab — jQuery catches that event and uses the Fetch API to send a GET request to our Express server, something like `/api/sales?category=Electronics`. The server reads the JSON file from disk using fs.readFile, filters it using Array.filter based on the query parameters, and sends back the filtered JSON. The frontend then transforms this data — grouping it, summing it up — into the format Chart.js needs, and renders the chart on the canvas."

Trace your hand/pointer along the flow as you explain.

---

### Slide 5 — Project Structure (Varun presents, ~30 seconds)

**Varun says:**
"Here's our file structure. Each team member's file is marked. I'll now hand it over to each member to explain their part."

Quick overview, don't read every line.

---

### Slide 6 — Team Roles (Varun presents, ~30 seconds)

"Each person owned specific files. We'll now go one by one — each person will explain their code and show it live."

---

### Slide 7 — Live Demo (Varun runs the demo, ~2.5 minutes)

**This is the most important slide.** Don't rush it.

**Switch to the browser (Tab 1: localhost:3000).**

Walk the TA through:

1. **"This is our dashboard. It loaded with Sales data as a bar chart by default."**
   - Point out the chart, the summary cards below it, the data table at the bottom.

2. **Switch chart type** — select "Line Graph" from the dropdown.
   - "If I change the chart type, the chart updates immediately."

3. **Filter by category** — select "Electronics".
   - "Now it's showing only Electronics revenue. The summary cards updated too — you can see the total and average changed."

4. **Switch to Pie Chart**.
   - "The pie chart shows revenue distribution by category."

5. **Switch to Scatter Plot**.
   - "The scatter plot shows units sold vs revenue — you can see Electronics has fewer units but higher revenue."

6. **Click "Student Performance" tab.**
   - "Now the filters changed — we have department filter instead of category."
   - Select "AI" department. Show the bar chart.
   - Switch to Scatter (Math vs Programming). "This scatter plot shows the correlation between math and programming scores."

7. **Click "Weather Data" tab.**
   - Select "Hyderabad". Show line chart.
   - "You can see the temperature peaks in May and drops during monsoon."

8. **Export** — click "Export as PNG".
   - "The Export button downloads the current chart as a PNG image."
   - Show the downloaded file briefly.

9. **Show raw API** — switch to Tab 2 (`/api/sales`).
   - "If you hit our API directly in the browser, you get the raw JSON."
   - Change URL to `/api/sales?category=Electronics&year=2024`
   - "And with query parameters, the server filters it — only 12 records for Electronics 2024."

**Switch back to the presentation.**

---

### Slide 8 — HTML Structure (Vineela presents, ~1.5 minutes)

**Vineela says:**
"I built the HTML structure — the index.html page. I used HTML5 semantic tags throughout."

Go through the bullet points, then:

**SWITCH TO VS CODE — open index.html.**

Point out:
- "Here's the `<header>` with the title, `<nav>` with the tab buttons."
- "Each button has a `data-dataset` attribute — that's how jQuery knows which dataset to load."
- "Here are the filter `<select>` dropdowns with `<label for>` for accessibility."
- "And this is the `<canvas>` element where Chart.js draws everything."
- "The `<table>` with separate `<thead>` and `<tbody>` — JavaScript fills these dynamically."
- "Scripts are loaded at the bottom of body so the HTML loads first."

Also briefly mention: "app.js just calls loadData() inside $(document).ready() to load the default chart."

**Switch back to PPT.**

---

### Slide 9 — CSS Styling (Annyunaa presents, ~1.5 minutes)

**Annyunaa says:**
"I did all the styling using an external CSS file."

Go through the key points, then:

**SWITCH TO VS CODE — open styles.css.**

Point out:
- "Here's the universal reset at the top — removes default browser spacing."
- "I used all five selector types that we learned:"
  - Scroll to show an **element selector** (`body`, `header`)
  - A **class selector** (`.tab-btn`)
  - An **ID selector** (`#filters`)
  - A **pseudo-class** (`:hover`, `:nth-child(even)` for table rows)
  - A **descendant selector** (`header h1`)
- "Flexbox here on the nav tabs and the summary cards — `display: flex; gap: 20px`."
- "And `transition: all 0.3s` gives the smooth hover effects."

Optionally: hover over a button in the browser to show the transition live.

**Switch back to PPT.**

---

### Slide 10 — Chart Rendering (Vishnu Vardhan presents, ~1.5 minutes)

**Vishnu Vardhan says:**
"I wrote the chart rendering functions using Chart.js."

Go through the bullets, then:

**SWITCH TO VS CODE — open charts.js.**

Point out:
- "This `destroyChart()` function runs before every new chart — Chart.js requires you to destroy the old one first."
- "Here's `createBarChart` — it gets the canvas context with `getContext('2d')`, then creates a `new Chart()` with the type, data, and options."
- "Options include `responsive: true`, the title plugin, and `beginAtZero` on the y-axis."
- "The pie chart is different — no axes, legend on the right, colors from the palette."

**SWITCH TO BROWSER** — quickly switch between Bar and Line chart to show it working.

**Switch back to PPT.**

---

### Slide 11 — Filtering & jQuery (Rohan presents, ~2 minutes)

**Rohan says:**
"I wrote filters.js — this is the main logic file that ties everything together."

Go through the bullets, then:

**SWITCH TO VS CODE — open filters.js.**

Point out:
- "Inside `$(document).ready()`, I have the event handlers."
- Show the **tab click handler**: "`.click()` on tab buttons — it removes `active` from all, adds to the clicked one, and uses `slideUp/slideDown` for animation."
- Show the **dropdown change handler**: "`.on('change')` on all selects — so the chart updates immediately when you pick something."
- Show **loadSalesData()**: "Here I read the dropdown values with `.val()`, build the API URL with query parameters, then `fetch()` it."
- Show **renderSalesChart**: "For the pie chart I aggregate revenue by category using `forEach` and an accumulator object. For bar/line charts I group by category and month."
- Show **renderSalesSummary**: "I calculate totals with `forEach`, then use `.html()` to inject the summary card HTML."

**SWITCH TO BROWSER** — apply a filter to show it working live. Point out the summary cards updating.

**Switch back to PPT.**

---

### Slide 12 — Backend (Varun presents, ~2 minutes)

**Varun says:**
"I built the Express.js server."

Go through the bullets, then:

**SWITCH TO VS CODE — open server.js.**

Point out:
- "`require('express')`, `require('fs')`, `require('path')` — importing the modules."
- "First middleware — the request logger. It logs every request with a timestamp. Let me show you."
  - **SWITCH TO TERMINAL** — show the server logs (GET /api/sales, GET /css/styles.css, etc.). "You can see every request the browser made."
- "Second middleware — `express.static('public')` serves all our HTML, CSS, JS files."
- "Here's the `/api/sales` route — `fs.readFile()` reads the JSON, `JSON.parse()` converts it, then I filter using `req.query.category` and `req.query.year`. `parseInt()` is needed because query params are strings but year in JSON is a number."
- "At the bottom — 404 handler for undefined routes and an error handler with 4 parameters."
- "`app.listen(3000)` starts the server."

**Switch back to PPT.**

---

### Slide 13 — Data & Export (Akshat presents, ~1.5 minutes)

**Akshat says:**
"I prepared all three JSON datasets and built the export feature."

Go through the bullets, then:

**SWITCH TO VS CODE — open data/sales.json.**

- "Each record is an object with month, category, revenue, units, year."
- "I designed realistic patterns — Electronics has high revenue per unit, Food has low revenue but high volume."
- Briefly scroll to show the structure.

**Open export.js:**

- "The export is simple — when the user clicks Export, I get the canvas element, call `toDataURL('image/png')` to convert it to a base64 image, create a temporary `<a>` element with the `download` attribute, and trigger a click. The filename includes `Date.now()` so exports don't overwrite."
- "There's a check — if no chart exists yet, it shows an alert."

**Switch back to PPT.**

---

### Slide 14 — API Endpoints (Varun presents, ~1 minute)

**Varun says:**
"Here's a summary of our four API endpoints."

Read through the table quickly.

**SWITCH TO BROWSER — Tab 2.** Type these URLs live:
- `http://localhost:3000/api/sales?category=Electronics&year=2024`
  - "12 records — only Electronics from 2024."
- `http://localhost:3000/api/categories`
  - "Returns the array of unique categories."
- `http://localhost:3000/api/nonexistent`
  - "Returns our 404 error: 'Route not found'."

**Switch back to PPT.**

---

### Slide 15 — Course Concepts (Varun presents, ~1 minute)

"This slide summarizes every concept from the course that we used. HTML5 semantic tags, all 5 CSS selector types, jQuery events and effects, Fetch API, Node.js fs module, Express routing and middleware. Everything we learned in Web Workshop is applied here."

Don't read every item — just gesture at the groups and mention highlights.

---

### Slide 16 — Thank You (Everyone, ~1 minute)

**Varun says:**
"That's our project. Thank you, ma'am. We're open to questions."

All team members should be ready to answer questions about their own section.

---

## Common Questions the TA Might Ask (and Who Answers)

| Question | Who Answers |
|----------|-------------|
| "Why did you use Chart.js instead of D3.js?" | Vishnu Vardhan — "Chart.js is simpler and gives us all 4 chart types with less code. D3 is more flexible but much more complex for our requirements." |
| "What happens if the JSON file doesn't exist?" | Varun — "The fs.readFile callback receives an error, and we return a 500 status with a JSON error message." |
| "Why is the server needed? Can't you just open HTML directly?" | Varun — "The Fetch API needs HTTP — it can't read local files due to browser CORS security. The server also does server-side filtering with query parameters." |
| "What jQuery methods did you use?" | Rohan — ".click(), .on(), .val(), .html(), .addClass(), .removeClass(), .data(), .slideUp(), .slideDown()" |
| "How does the export work?" | Akshat — "canvas.toDataURL('image/png') converts the canvas pixels to a base64 PNG, then we trigger a download using a temporary anchor element." |
| "What CSS selectors did you use?" | Annyunaa — "Element, class, ID, pseudo-class like :hover and :nth-child(even), and descendant selectors like header h1." |
| "Why load scripts at the bottom of body?" | Vineela — "So the HTML elements are already in the DOM when our JavaScript runs. If we loaded them in head, the scripts might try to find elements that don't exist yet." |
| "How does filtering work?" | Varun/Rohan — "The frontend builds a URL like /api/sales?category=Electronics. The server reads req.query.category and uses Array.filter() to keep only matching records." |
| "What is middleware?" | Varun — "A function with req, res, next parameters that runs for every request before the route handler. We have a logger, static file server, 404 handler, and error handler." |
| "Why destroyChart() before creating a new one?" | Vishnu Vardhan — "Chart.js doesn't auto-cleanup. If you create a new chart on the same canvas without destroying the old one, both exist in memory and the old chart flickers behind the new one." |
| "What Node.js modules did you use?" | Varun — "express (npm package), fs (built-in, for reading files), and path (built-in, for building file paths with path.join)." |
| "What is $(document).ready()?" | Rohan/Vineela — "It's a jQuery function that waits until the entire HTML DOM is loaded before running our code, so we don't try to access elements that haven't been created yet." |

---

## Tips

- **Don't read slides word-for-word.** Talk naturally and use the slides as reference.
- **When showing code, don't scroll through the whole file.** Jump to the specific function you're explaining. Use Ctrl+G in VS Code to jump to a line number.
- **Keep the browser and editor ready.** Alt+Tab between PPT, browser, and VS Code quickly. Practice this transition before the actual presentation.
- **If a question is about someone else's code, let that person answer.** Don't step on each other's parts.
- **If you don't know an answer, be honest.** Say "I'm not sure about that specific detail, but [teammate] can explain."
- **Practice once as a group** so the transitions between presenters are smooth.
