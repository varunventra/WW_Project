from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

# Color palette
DARK_BG = RGBColor(0x2C, 0x3E, 0x50)
BLUE_ACCENT = RGBColor(0x34, 0x98, 0xDB)
DARK_BLUE = RGBColor(0x2C, 0x3E, 0x50)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
LIGHT_GRAY = RGBColor(0xEC, 0xF0, 0xF1)
DARK_TEXT = RGBColor(0x2C, 0x3E, 0x50)
GRAY_TEXT = RGBColor(0x7F, 0x8C, 0x8D)
GREEN = RGBColor(0x27, 0xAE, 0x60)
RED = RGBColor(0xE7, 0x4C, 0x3C)
ORANGE = RGBColor(0xF3, 0x9C, 0x12)
PURPLE = RGBColor(0x9B, 0x59, 0xB6)

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

def add_bg(slide, color=DARK_BG):
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = color

def add_shape_bg(slide, left, top, width, height, color):
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()
    return shape

def add_text_box(slide, left, top, width, height, text, font_size=18, bold=False, color=WHITE, align=PP_ALIGN.LEFT, font_name='Segoe UI'):
    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = text
    p.font.size = Pt(font_size)
    p.font.bold = bold
    p.font.color.rgb = color
    p.font.name = font_name
    p.alignment = align
    return tf

def add_bullet_slide(slide, items, left, top, width, height, font_size=18, color=WHITE, spacing=Pt(8)):
    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf = txBox.text_frame
    tf.word_wrap = True
    for i, item in enumerate(items):
        if i == 0:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
        p.text = item
        p.font.size = Pt(font_size)
        p.font.color.rgb = color
        p.font.name = 'Segoe UI'
        p.space_after = spacing
        p.level = 0
    return tf

def add_accent_bar(slide, top):
    add_shape_bg(slide, Inches(0.8), top, Inches(1.5), Pt(4), BLUE_ACCENT)

# ============================================================
# SLIDE 1: Title
# ============================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide, DARK_BG)
# Accent line
add_shape_bg(slide, Inches(0), Inches(0), Inches(13.333), Pt(6), BLUE_ACCENT)
add_text_box(slide, Inches(1), Inches(1.5), Inches(11), Inches(1.5),
             "Interactive Data Visualizer", font_size=44, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
add_text_box(slide, Inches(1), Inches(3.0), Inches(11), Inches(0.8),
             "Web Workshop  |  Project 15  |  Final Presentation", font_size=22, color=GRAY_TEXT, align=PP_ALIGN.CENTER)
# Team names
team_text = "Vineela Reddy  |  Annyunaa Gandra  |  Vishnu Vardhan Rao  |  Rohan Yaski  |  Varun Ventrapagada  |  Akshat Reddy"
add_text_box(slide, Inches(1), Inches(4.5), Inches(11), Inches(0.6),
             team_text, font_size=16, color=LIGHT_GRAY, align=PP_ALIGN.CENTER)
add_shape_bg(slide, Inches(0), Inches(7.2), Inches(13.333), Pt(6), BLUE_ACCENT)

# ============================================================
# SLIDE 2: Problem Statement
# ============================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide, DARK_BG)
add_shape_bg(slide, Inches(0), Inches(0), Inches(13.333), Pt(4), BLUE_ACCENT)
add_text_box(slide, Inches(0.8), Inches(0.5), Inches(11), Inches(0.8),
             "Problem Statement", font_size=36, bold=True, color=WHITE)
add_accent_bar(slide, Inches(1.25))

items = [
    "Build an interactive data visualization app that reads JSON data and displays charts",
    "Support multiple chart types: Bar Charts, Line Graphs, Pie Charts, Scatter Plots",
    "Users can filter data, drill down into segments, and export visualizations",
    "Demonstrate JSON data handling, data transformation, and dynamic Canvas/SVG graphics",
    "Difficulty Level: Advanced"
]
add_bullet_slide(slide, items, Inches(0.8), Inches(1.8), Inches(11.5), Inches(5), font_size=22, color=LIGHT_GRAY, spacing=Pt(16))

# ============================================================
# SLIDE 3: Tech Stack
# ============================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide, DARK_BG)
add_shape_bg(slide, Inches(0), Inches(0), Inches(13.333), Pt(4), BLUE_ACCENT)
add_text_box(slide, Inches(0.8), Inches(0.5), Inches(11), Inches(0.8),
             "Tools & Technologies", font_size=36, bold=True, color=WHITE)
add_accent_bar(slide, Inches(1.25))

# Left column - Frontend
add_text_box(slide, Inches(1), Inches(1.8), Inches(5), Inches(0.5),
             "FRONTEND", font_size=16, bold=True, color=BLUE_ACCENT)
frontend_items = [
    "HTML5 — Semantic page structure",
    "CSS3 — External stylesheet, Flexbox, transitions",
    "jQuery 3.7.1 — Events, DOM manipulation, effects",
    "Chart.js 4.4.0 — Bar, Line, Pie, Scatter charts",
    "Fetch API — Async HTTP requests to server",
    "Canvas API — Chart rendering & PNG export"
]
add_bullet_slide(slide, frontend_items, Inches(1), Inches(2.3), Inches(5), Inches(4.5), font_size=18, color=LIGHT_GRAY, spacing=Pt(10))

# Right column - Backend
add_text_box(slide, Inches(7), Inches(1.8), Inches(5), Inches(0.5),
             "BACKEND", font_size=16, bold=True, color=GREEN)
backend_items = [
    "Node.js — Server-side runtime",
    "Express.js 4.18 — Routing, middleware, static files",
    "fs module — Reading JSON files from disk",
    "path module — Cross-platform file paths",
    "npm — Package manager for dependencies"
]
add_bullet_slide(slide, backend_items, Inches(7), Inches(2.3), Inches(5.5), Inches(4.5), font_size=18, color=LIGHT_GRAY, spacing=Pt(10))

# Divider line
add_shape_bg(slide, Inches(6.4), Inches(1.8), Pt(2), Inches(4.8), GRAY_TEXT)

# ============================================================
# SLIDE 4: Architecture
# ============================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide, DARK_BG)
add_shape_bg(slide, Inches(0), Inches(0), Inches(13.333), Pt(4), BLUE_ACCENT)
add_text_box(slide, Inches(0.8), Inches(0.5), Inches(11), Inches(0.8),
             "Architecture & Data Flow", font_size=36, bold=True, color=WHITE)
add_accent_bar(slide, Inches(1.25))

# Flow boxes
box_h = Inches(1.1)
box_w = Inches(3.2)

# Box 1: User
shape = add_shape_bg(slide, Inches(0.5), Inches(2.2), box_w, box_h, RGBColor(0x34, 0x49, 0x5E))
shape.text_frame.paragraphs[0].text = "User Interaction"
shape.text_frame.paragraphs[0].font.color.rgb = WHITE
shape.text_frame.paragraphs[0].font.size = Pt(16)
shape.text_frame.paragraphs[0].font.bold = True
shape.text_frame.paragraphs[0].font.name = 'Segoe UI'
shape.text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
p2 = shape.text_frame.add_paragraph()
p2.text = "Clicks tabs, selects filters"
p2.font.color.rgb = GRAY_TEXT
p2.font.size = Pt(13)
p2.font.name = 'Segoe UI'
p2.alignment = PP_ALIGN.CENTER

# Arrow 1
add_text_box(slide, Inches(3.7), Inches(2.5), Inches(0.8), Inches(0.5), "-->", font_size=24, bold=True, color=BLUE_ACCENT, align=PP_ALIGN.CENTER)

# Box 2: jQuery + Fetch
shape = add_shape_bg(slide, Inches(4.5), Inches(2.2), box_w, box_h, RGBColor(0x34, 0x49, 0x5E))
shape.text_frame.paragraphs[0].text = "jQuery + Fetch API"
shape.text_frame.paragraphs[0].font.color.rgb = WHITE
shape.text_frame.paragraphs[0].font.size = Pt(16)
shape.text_frame.paragraphs[0].font.bold = True
shape.text_frame.paragraphs[0].font.name = 'Segoe UI'
shape.text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
p2 = shape.text_frame.add_paragraph()
p2.text = "Events, GET /api/sales?..."
p2.font.color.rgb = GRAY_TEXT
p2.font.size = Pt(13)
p2.font.name = 'Segoe UI'
p2.alignment = PP_ALIGN.CENTER

# Arrow 2
add_text_box(slide, Inches(7.7), Inches(2.5), Inches(0.8), Inches(0.5), "-->", font_size=24, bold=True, color=BLUE_ACCENT, align=PP_ALIGN.CENTER)

# Box 3: Express Server
shape = add_shape_bg(slide, Inches(8.5), Inches(2.2), box_w, box_h, RGBColor(0x34, 0x49, 0x5E))
shape.text_frame.paragraphs[0].text = "Express.js Server"
shape.text_frame.paragraphs[0].font.color.rgb = WHITE
shape.text_frame.paragraphs[0].font.size = Pt(16)
shape.text_frame.paragraphs[0].font.bold = True
shape.text_frame.paragraphs[0].font.name = 'Segoe UI'
shape.text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
p2 = shape.text_frame.add_paragraph()
p2.text = "fs.readFile, filter, res.json()"
p2.font.color.rgb = GRAY_TEXT
p2.font.size = Pt(13)
p2.font.name = 'Segoe UI'
p2.alignment = PP_ALIGN.CENTER

# Return flow - bottom row
add_text_box(slide, Inches(7.7), Inches(4.2), Inches(0.8), Inches(0.5), "<--", font_size=24, bold=True, color=GREEN, align=PP_ALIGN.CENTER)

shape = add_shape_bg(slide, Inches(8.5), Inches(3.9), box_w, box_h, RGBColor(0x34, 0x49, 0x5E))
shape.text_frame.paragraphs[0].text = "JSON Data Files"
shape.text_frame.paragraphs[0].font.color.rgb = WHITE
shape.text_frame.paragraphs[0].font.size = Pt(16)
shape.text_frame.paragraphs[0].font.bold = True
shape.text_frame.paragraphs[0].font.name = 'Segoe UI'
shape.text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
p2 = shape.text_frame.add_paragraph()
p2.text = "sales.json, students.json, weather.json"
p2.font.color.rgb = GRAY_TEXT
p2.font.size = Pt(13)
p2.font.name = 'Segoe UI'
p2.alignment = PP_ALIGN.CENTER

add_text_box(slide, Inches(3.7), Inches(4.2), Inches(0.8), Inches(0.5), "<--", font_size=24, bold=True, color=GREEN, align=PP_ALIGN.CENTER)

shape = add_shape_bg(slide, Inches(4.5), Inches(3.9), box_w, box_h, RGBColor(0x34, 0x49, 0x5E))
shape.text_frame.paragraphs[0].text = "Data Transformation"
shape.text_frame.paragraphs[0].font.color.rgb = WHITE
shape.text_frame.paragraphs[0].font.size = Pt(16)
shape.text_frame.paragraphs[0].font.bold = True
shape.text_frame.paragraphs[0].font.name = 'Segoe UI'
shape.text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
p2 = shape.text_frame.add_paragraph()
p2.text = "Group, aggregate, map to Chart.js"
p2.font.color.rgb = GRAY_TEXT
p2.font.size = Pt(13)
p2.font.name = 'Segoe UI'
p2.alignment = PP_ALIGN.CENTER

shape = add_shape_bg(slide, Inches(0.5), Inches(3.9), box_w, box_h, RGBColor(0x34, 0x49, 0x5E))
shape.text_frame.paragraphs[0].text = "Chart.js + Canvas"
shape.text_frame.paragraphs[0].font.color.rgb = WHITE
shape.text_frame.paragraphs[0].font.size = Pt(16)
shape.text_frame.paragraphs[0].font.bold = True
shape.text_frame.paragraphs[0].font.name = 'Segoe UI'
shape.text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
p2 = shape.text_frame.add_paragraph()
p2.text = "Render bar, line, pie, scatter"
p2.font.color.rgb = GRAY_TEXT
p2.font.size = Pt(13)
p2.font.name = 'Segoe UI'
p2.alignment = PP_ALIGN.CENTER

# Summary text
add_text_box(slide, Inches(0.8), Inches(5.6), Inches(11.5), Inches(1.5),
             "Browser sends HTTP GET request with query params  -->  Express reads JSON file with fs.readFile  -->  Filters data with Array.filter()  -->  Returns JSON  -->  Frontend transforms & renders chart on Canvas",
             font_size=16, color=GRAY_TEXT, align=PP_ALIGN.CENTER)

# ============================================================
# SLIDE 5: Project Structure
# ============================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide, DARK_BG)
add_shape_bg(slide, Inches(0), Inches(0), Inches(13.333), Pt(4), BLUE_ACCENT)
add_text_box(slide, Inches(0.8), Inches(0.5), Inches(11), Inches(0.8),
             "Project Structure", font_size=36, bold=True, color=WHITE)
add_accent_bar(slide, Inches(1.25))

structure = """interactive-data-visualizer/
    server.js                       Express.js backend            (Varun)
    package.json                   Node.js config
    public/
        index.html                   Dashboard HTML page        (Vineela)
        css/styles.css              All CSS styling                  (Annyunaa)
        js/app.js                      App initialization              (Vineela)
        js/charts.js                  Chart.js functions             (Vishnu Vardhan)
        js/filters.js                  jQuery + Fetch + logic       (Rohan)
        js/export.js                  PNG export feature            (Akshat)
        data/sales.json            72 records, 4 categories     (Akshat)
        data/students.json       20 records, 4 departments   (Akshat)
        data/weather.json        36 records, 3 cities              (Akshat)"""

add_text_box(slide, Inches(1.2), Inches(1.7), Inches(11), Inches(5.5),
             structure, font_size=17, color=LIGHT_GRAY, font_name='Consolas')

# ============================================================
# SLIDE 6: Team Roles
# ============================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide, DARK_BG)
add_shape_bg(slide, Inches(0), Inches(0), Inches(13.333), Pt(4), BLUE_ACCENT)
add_text_box(slide, Inches(0.8), Inches(0.5), Inches(11), Inches(0.8),
             "Team Roles", font_size=36, bold=True, color=WHITE)
add_accent_bar(slide, Inches(1.25))

roles = [
    ("Vineela Reddy", "SE24UARI021", "HTML Structure & Layout", "index.html, app.js", BLUE_ACCENT),
    ("Annyunaa Gandra", "SE24UARI009", "CSS Styling & Design", "styles.css", PURPLE),
    ("Vishnu Vardhan Rao", "SE24UARI010", "Chart Rendering", "charts.js", GREEN),
    ("Rohan Yaski", "SE24UARI042", "Filtering & Interactivity", "filters.js", ORANGE),
    ("Varun Ventrapagada", "SE24UARI006", "Backend Server", "server.js", RED),
    ("Akshat Reddy", "SE24UARI032", "Data & Export", "data/*.json, export.js", BLUE_ACCENT),
]

for i, (name, roll, role, files, color) in enumerate(roles):
    row = i // 3
    col = i % 3
    x = Inches(0.6 + col * 4.2)
    y = Inches(1.7 + row * 2.5)
    card = add_shape_bg(slide, x, y, Inches(3.8), Inches(2.0), RGBColor(0x34, 0x49, 0x5E))
    # Color accent bar on card
    add_shape_bg(slide, x, y, Inches(3.8), Pt(5), color)
    add_text_box(slide, x + Inches(0.2), y + Inches(0.3), Inches(3.4), Inches(0.4),
                 name, font_size=18, bold=True, color=WHITE)
    add_text_box(slide, x + Inches(0.2), y + Inches(0.7), Inches(3.4), Inches(0.3),
                 roll, font_size=13, color=GRAY_TEXT)
    add_text_box(slide, x + Inches(0.2), y + Inches(1.0), Inches(3.4), Inches(0.3),
                 role, font_size=15, bold=True, color=color)
    add_text_box(slide, x + Inches(0.2), y + Inches(1.4), Inches(3.4), Inches(0.3),
                 files, font_size=13, color=GRAY_TEXT, font_name='Consolas')

# ============================================================
# SLIDE 7: LIVE DEMO
# ============================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide, DARK_BG)
add_shape_bg(slide, Inches(0), Inches(0), Inches(13.333), Pt(4), GREEN)
add_text_box(slide, Inches(1), Inches(2.0), Inches(11), Inches(1.5),
             "Live Demo", font_size=48, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
add_text_box(slide, Inches(1), Inches(3.8), Inches(11), Inches(0.6),
             "http://localhost:3000", font_size=28, color=GREEN, align=PP_ALIGN.CENTER, font_name='Consolas')
add_text_box(slide, Inches(1), Inches(4.8), Inches(11), Inches(1.5),
             "Switch chart types  |  Filter by category/year  |  Switch datasets  |  Export as PNG",
             font_size=18, color=GRAY_TEXT, align=PP_ALIGN.CENTER)

# ============================================================
# SLIDE 8: Vineela - HTML
# ============================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide, DARK_BG)
add_shape_bg(slide, Inches(0), Inches(0), Inches(13.333), Pt(4), BLUE_ACCENT)
add_text_box(slide, Inches(0.8), Inches(0.5), Inches(11), Inches(0.8),
             "HTML Structure  —  Vineela Reddy", font_size=32, bold=True, color=WHITE)
add_accent_bar(slide, Inches(1.2))
add_text_box(slide, Inches(0.8), Inches(1.0), Inches(4), Inches(0.3),
             "index.html  |  app.js", font_size=14, color=GRAY_TEXT, font_name='Consolas')

items = [
    "HTML5 document structure with <!DOCTYPE html>",
    "Semantic tags: <header>, <nav>, <main>, <section>, <footer>",
    "Navigation tabs with data-dataset custom attributes",
    "Filter dropdowns: <select> + <option> with <label for='...'>",
    "<canvas id='mainChart'> for Chart.js rendering",
    "<table> with <thead> and <tbody> for dynamic data display",
    "Chart.js & jQuery loaded from CDN in <head>",
    "Custom JS files loaded at bottom of <body> (load order matters)",
    "app.js: $(document).ready() calls loadData() on page open",
]
add_bullet_slide(slide, items, Inches(0.8), Inches(1.6), Inches(11.5), Inches(5.5), font_size=19, color=LIGHT_GRAY, spacing=Pt(10))

add_shape_bg(slide, Inches(0.5), Inches(6.8), Inches(12.3), Inches(0.5), RGBColor(0x34, 0x49, 0x5E))
add_text_box(slide, Inches(0.8), Inches(6.8), Inches(12), Inches(0.5),
             "SHOW CODE:  Open index.html in editor  —  walk through the semantic sections and form controls",
             font_size=14, bold=True, color=GREEN)

# ============================================================
# SLIDE 9: Annyunaa - CSS
# ============================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide, DARK_BG)
add_shape_bg(slide, Inches(0), Inches(0), Inches(13.333), Pt(4), PURPLE)
add_text_box(slide, Inches(0.8), Inches(0.5), Inches(11), Inches(0.8),
             "CSS Styling  —  Annyunaa Gandra", font_size=32, bold=True, color=WHITE)
add_shape_bg(slide, Inches(0.8), Inches(1.2), Inches(1.5), Pt(4), PURPLE)
add_text_box(slide, Inches(0.8), Inches(1.0), Inches(4), Inches(0.3),
             "styles.css", font_size=14, color=GRAY_TEXT, font_name='Consolas')

items = [
    "Universal reset: * { margin: 0; padding: 0; box-sizing: border-box }",
    "Five CSS selector types used:",
    "    Element (body, header)  |  Class (.tab-btn, .summary-card)",
    "    ID (#filters, #chart-container)  |  Pseudo-class (:hover, :focus, :nth-child)",
    "    Descendant (header h1, .summary-card h3)",
    "Flexbox layout: nav tabs, filter row, summary cards",
    "Transitions: smooth 0.3s hover effects on buttons and tabs",
    "Box-shadow on content cards for depth effect",
    "Table: border-collapse, zebra stripes with :nth-child(even), row :hover",
    "Color scheme: dark header (#2c3e50), blue accent (#3498db), white cards",
]
add_bullet_slide(slide, items, Inches(0.8), Inches(1.6), Inches(11.5), Inches(5.5), font_size=18, color=LIGHT_GRAY, spacing=Pt(8))

add_shape_bg(slide, Inches(0.5), Inches(6.8), Inches(12.3), Inches(0.5), RGBColor(0x34, 0x49, 0x5E))
add_text_box(slide, Inches(0.8), Inches(6.8), Inches(12), Inches(0.5),
             "SHOW CODE:  Open styles.css  —  point out each selector type, hover effects, flexbox on summary cards",
             font_size=14, bold=True, color=GREEN)

# ============================================================
# SLIDE 10: Vishnu - Charts
# ============================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide, DARK_BG)
add_shape_bg(slide, Inches(0), Inches(0), Inches(13.333), Pt(4), GREEN)
add_text_box(slide, Inches(0.8), Inches(0.5), Inches(11), Inches(0.8),
             "Chart Rendering  —  Vishnu Vardhan Rao", font_size=32, bold=True, color=WHITE)
add_shape_bg(slide, Inches(0.8), Inches(1.2), Inches(1.5), Pt(4), GREEN)
add_text_box(slide, Inches(0.8), Inches(1.0), Inches(4), Inches(0.3),
             "charts.js", font_size=14, color=GRAY_TEXT, font_name='Consolas')

items = [
    "Chart.js library renders on HTML5 <canvas> via getContext('2d')",
    "Four chart creation functions:",
    "    createBarChart(labels, datasets, title)  — vertical bars, beginAtZero",
    "    createLineChart(labels, datasets, title)  — curved lines, tension: 0.3",
    "    createPieChart(labels, data, title)  — color slices, legend on right",
    "    createScatterChart(datasets, title, xLabel, yLabel)  — {x,y} points",
    "destroyChart() — must destroy old chart before creating new one",
    "    Uses currentChart global variable to track active chart instance",
    "12-color palette array for distinguishing datasets",
    "Options: responsive, title plugin, legend plugin, axis configuration",
]
add_bullet_slide(slide, items, Inches(0.8), Inches(1.6), Inches(11.5), Inches(5.5), font_size=18, color=LIGHT_GRAY, spacing=Pt(8))

add_shape_bg(slide, Inches(0.5), Inches(6.8), Inches(12.3), Inches(0.5), RGBColor(0x34, 0x49, 0x5E))
add_text_box(slide, Inches(0.8), Inches(6.8), Inches(12), Inches(0.5),
             "SHOW CODE:  Open charts.js  —  show destroyChart + one createChart function  |  DEMO: switch chart types in browser",
             font_size=14, bold=True, color=GREEN)

# ============================================================
# SLIDE 11: Rohan - Filters & jQuery
# ============================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide, DARK_BG)
add_shape_bg(slide, Inches(0), Inches(0), Inches(13.333), Pt(4), ORANGE)
add_text_box(slide, Inches(0.8), Inches(0.5), Inches(11), Inches(0.8),
             "Filtering & Interactivity  —  Rohan Yaski", font_size=32, bold=True, color=WHITE)
add_shape_bg(slide, Inches(0.8), Inches(1.2), Inches(1.5), Pt(4), ORANGE)
add_text_box(slide, Inches(0.8), Inches(1.0), Inches(4), Inches(0.3),
             "filters.js", font_size=14, color=GRAY_TEXT, font_name='Consolas')

items = [
    "jQuery event handlers inside $(document).ready():",
    "    .click() on tabs  |  .on('change') on dropdowns  |  .click() on Apply",
    "    slideUp()/slideDown() — animated filter panel switching",
    "    .addClass()/.removeClass() — visual tab highlighting",
    "Fetch API: fetch('/api/sales?category=X').then(response.json()).then(data)",
    "    Builds query URL from dropdown values using .val()",
    "Data transformation algorithms:",
    "    Pie: aggregate revenue by category using forEach + object accumulator",
    "    Bar/Line: group by category & month, map to ordered month arrays",
    "    Scatter: map each record to {x, y} point, group by category",
    "jQuery .html() injects summary cards and table rows into the DOM",
]
add_bullet_slide(slide, items, Inches(0.8), Inches(1.6), Inches(11.5), Inches(5.5), font_size=17, color=LIGHT_GRAY, spacing=Pt(7))

add_shape_bg(slide, Inches(0.5), Inches(6.8), Inches(12.3), Inches(0.5), RGBColor(0x34, 0x49, 0x5E))
add_text_box(slide, Inches(0.8), Inches(6.8), Inches(12), Inches(0.5),
             "SHOW CODE:  Open filters.js  —  show event handlers + one Fetch call + one data transform  |  DEMO: filter in browser",
             font_size=14, bold=True, color=GREEN)

# ============================================================
# SLIDE 12: Varun - Backend
# ============================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide, DARK_BG)
add_shape_bg(slide, Inches(0), Inches(0), Inches(13.333), Pt(4), RED)
add_text_box(slide, Inches(0.8), Inches(0.5), Inches(11), Inches(0.8),
             "Backend Server  —  Varun Ventrapagada", font_size=32, bold=True, color=WHITE)
add_shape_bg(slide, Inches(0.8), Inches(1.2), Inches(1.5), Pt(4), RED)
add_text_box(slide, Inches(0.8), Inches(1.0), Inches(4), Inches(0.3),
             "server.js  |  package.json", font_size=14, color=GRAY_TEXT, font_name='Consolas')

items = [
    "require('express'), require('fs'), require('path') — module imports",
    "Middleware chain:",
    "    1. Request logger — logs timestamp + method + URL to console",
    "    2. express.static('public') — serves HTML, CSS, JS, JSON files",
    "    3. 404 handler — catches undefined routes, returns status 404",
    "    4. Error handler — 4 params (err,req,res,next), returns status 500",
    "API Routes:  app.get('/api/sales', callback)",
    "    fs.readFile() reads JSON  -->  JSON.parse()  -->  Array.filter()",
    "    req.query.category & req.query.year for server-side filtering",
    "    parseInt() converts query string year to number for comparison",
    "    res.json() sends filtered data back as JSON response",
    "app.listen(3000) — starts server on port 3000",
]
add_bullet_slide(slide, items, Inches(0.8), Inches(1.6), Inches(11.5), Inches(5.5), font_size=17, color=LIGHT_GRAY, spacing=Pt(7))

add_shape_bg(slide, Inches(0.5), Inches(6.8), Inches(12.3), Inches(0.5), RGBColor(0x34, 0x49, 0x5E))
add_text_box(slide, Inches(0.8), Inches(6.8), Inches(12), Inches(0.5),
             "SHOW CODE:  Open server.js  —  walk through middleware + one API route  |  SHOW: terminal server logs",
             font_size=14, bold=True, color=GREEN)

# ============================================================
# SLIDE 13: Akshat - Data & Export
# ============================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide, DARK_BG)
add_shape_bg(slide, Inches(0), Inches(0), Inches(13.333), Pt(4), BLUE_ACCENT)
add_text_box(slide, Inches(0.8), Inches(0.5), Inches(11), Inches(0.8),
             "JSON Data & Export  —  Akshat Reddy", font_size=32, bold=True, color=WHITE)
add_accent_bar(slide, Inches(1.2))
add_text_box(slide, Inches(0.8), Inches(1.0), Inches(6), Inches(0.3),
             "data/*.json  |  export.js", font_size=14, color=GRAY_TEXT, font_name='Consolas')

items = [
    "Three JSON datasets — arrays of objects:",
    "    sales.json — 72 records: month, category, revenue, units, year",
    "       4 categories (Electronics, Clothing, Food, Books) x 2 years",
    "    students.json — 20 records: name, dept, math, science, english, programming, gpa",
    "       5 students x 4 departments (CSE, ECE, AI, ME)",
    "    weather.json — 36 records: city, month, temperature, humidity, rainfall",
    "       12 months x 3 cities (Hyderabad, Mumbai, Delhi)",
    "Data designed with realistic patterns (seasonal trends, dept differences)",
    "Export feature (export.js):",
    "    canvas.toDataURL('image/png') — converts chart to base64 PNG",
    "    Creates temp <a> element with download attribute, triggers click",
    "    Filename includes dataset name + Date.now() timestamp",
]
add_bullet_slide(slide, items, Inches(0.8), Inches(1.6), Inches(11.5), Inches(5.5), font_size=17, color=LIGHT_GRAY, spacing=Pt(7))

add_shape_bg(slide, Inches(0.5), Inches(6.8), Inches(12.3), Inches(0.5), RGBColor(0x34, 0x49, 0x5E))
add_text_box(slide, Inches(0.8), Inches(6.8), Inches(12), Inches(0.5),
             "SHOW CODE:  Open one JSON file  —  show structure  |  Open export.js  |  DEMO: click Export, show downloaded PNG",
             font_size=14, bold=True, color=GREEN)

# ============================================================
# SLIDE 14: API Endpoints
# ============================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide, DARK_BG)
add_shape_bg(slide, Inches(0), Inches(0), Inches(13.333), Pt(4), BLUE_ACCENT)
add_text_box(slide, Inches(0.8), Inches(0.5), Inches(11), Inches(0.8),
             "REST API Endpoints", font_size=36, bold=True, color=WHITE)
add_accent_bar(slide, Inches(1.25))

endpoints = [
    ("GET", "/api/sales", "category, year", "Filtered sales data"),
    ("GET", "/api/students", "department", "Filtered student data"),
    ("GET", "/api/weather", "city", "Filtered weather data"),
    ("GET", "/api/categories", "—", "Unique category list"),
]

# Table header
header_y = Inches(1.8)
add_shape_bg(slide, Inches(0.8), header_y, Inches(11.5), Inches(0.5), BLUE_ACCENT)
cols = [(Inches(0.9), "Method"), (Inches(3.0), "Route"), (Inches(6.2), "Query Params"), (Inches(9.0), "Returns")]
for x, text in cols:
    add_text_box(slide, x, header_y + Pt(4), Inches(2.5), Inches(0.4),
                 text, font_size=15, bold=True, color=WHITE)

for i, (method, route, params, desc) in enumerate(endpoints):
    row_y = Inches(2.4) + Inches(i * 0.6)
    bg_color = RGBColor(0x34, 0x49, 0x5E) if i % 2 == 0 else DARK_BG
    add_shape_bg(slide, Inches(0.8), row_y, Inches(11.5), Inches(0.5), bg_color)
    add_text_box(slide, Inches(0.9), row_y + Pt(4), Inches(1.5), Inches(0.4),
                 method, font_size=14, bold=True, color=GREEN, font_name='Consolas')
    add_text_box(slide, Inches(3.0), row_y + Pt(4), Inches(3), Inches(0.4),
                 route, font_size=14, color=LIGHT_GRAY, font_name='Consolas')
    add_text_box(slide, Inches(6.2), row_y + Pt(4), Inches(2.5), Inches(0.4),
                 params, font_size=14, color=GRAY_TEXT)
    add_text_box(slide, Inches(9.0), row_y + Pt(4), Inches(3), Inches(0.4),
                 desc, font_size=14, color=LIGHT_GRAY)

add_text_box(slide, Inches(0.8), Inches(5.0), Inches(11.5), Inches(0.4),
             "Example:  GET /api/sales?category=Electronics&year=2024  -->  returns 12 filtered JSON records",
             font_size=16, color=ORANGE, font_name='Consolas')

add_shape_bg(slide, Inches(0.5), Inches(6.8), Inches(12.3), Inches(0.5), RGBColor(0x34, 0x49, 0x5E))
add_text_box(slide, Inches(0.8), Inches(6.8), Inches(12), Inches(0.5),
             "DEMO:  Open browser tab  —  type API URL directly, show raw JSON response",
             font_size=14, bold=True, color=GREEN)

# ============================================================
# SLIDE 15: Course Concepts
# ============================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide, DARK_BG)
add_shape_bg(slide, Inches(0), Inches(0), Inches(13.333), Pt(4), BLUE_ACCENT)
add_text_box(slide, Inches(0.8), Inches(0.5), Inches(11), Inches(0.8),
             "Course Concepts Applied", font_size=36, bold=True, color=WHITE)
add_accent_bar(slide, Inches(1.25))

# Left column
add_text_box(slide, Inches(0.8), Inches(1.7), Inches(3.5), Inches(0.4),
             "HTML5", font_size=16, bold=True, color=BLUE_ACCENT)
left_items = [
    "Semantic tags (header, nav, main, section, footer)",
    "Forms: select, option, label, button",
    "Tables: thead, tbody, tr, th, td",
    "Canvas element for graphics",
    "Data attributes (data-dataset)",
]
add_bullet_slide(slide, left_items, Inches(0.8), Inches(2.1), Inches(3.8), Inches(3), font_size=14, color=LIGHT_GRAY, spacing=Pt(4))

# Middle column
add_text_box(slide, Inches(4.8), Inches(1.7), Inches(3.5), Inches(0.4),
             "CSS3 & jQuery", font_size=16, bold=True, color=PURPLE)
mid_items = [
    "5 selector types (element, class, ID, pseudo, descendant)",
    "Flexbox, transitions, box-shadow",
    "External stylesheet",
    "$(document).ready(), .click(), .on()",
    ".html(), .val(), .addClass(), .data()",
    "slideUp(), slideDown() effects",
]
add_bullet_slide(slide, mid_items, Inches(4.8), Inches(2.1), Inches(3.8), Inches(3), font_size=14, color=LIGHT_GRAY, spacing=Pt(4))

# Right column
add_text_box(slide, Inches(9.0), Inches(1.7), Inches(3.5), Inches(0.4),
             "Node.js & Express", font_size=16, bold=True, color=GREEN)
right_items = [
    "require() for modules (fs, path, express)",
    "fs.readFile() async file I/O",
    "app.get() route handlers",
    "Middleware: logger, static, 404, error",
    "req.query, res.json(), res.status()",
    "app.listen(3000)",
]
add_bullet_slide(slide, right_items, Inches(9.0), Inches(2.1), Inches(3.8), Inches(3), font_size=14, color=LIGHT_GRAY, spacing=Pt(4))

# Bottom row
add_text_box(slide, Inches(0.8), Inches(4.8), Inches(3.5), Inches(0.4),
             "JavaScript", font_size=16, bold=True, color=ORANGE)
js_items = [
    "JSON.parse(), forEach, filter, map",
    "Callbacks, Fetch API, Promises",
    "DOM: getElementById, createElement",
    "String concatenation, toLocaleString()",
]
add_bullet_slide(slide, js_items, Inches(0.8), Inches(5.2), Inches(3.8), Inches(2), font_size=14, color=LIGHT_GRAY, spacing=Pt(4))

add_text_box(slide, Inches(4.8), Inches(4.8), Inches(3.5), Inches(0.4),
             "Chart.js & Canvas", font_size=16, bold=True, color=RED)
chart_items = [
    "getContext('2d') drawing context",
    "new Chart(ctx, config)",
    "4 chart types with options",
    "toDataURL() for PNG export",
]
add_bullet_slide(slide, chart_items, Inches(4.8), Inches(5.2), Inches(3.8), Inches(2), font_size=14, color=LIGHT_GRAY, spacing=Pt(4))

# ============================================================
# SLIDE 16: Thank You
# ============================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide, DARK_BG)
add_shape_bg(slide, Inches(0), Inches(0), Inches(13.333), Pt(6), BLUE_ACCENT)
add_text_box(slide, Inches(1), Inches(2.0), Inches(11), Inches(1.5),
             "Thank You", font_size=52, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
add_text_box(slide, Inches(1), Inches(3.8), Inches(11), Inches(0.6),
             "Questions?", font_size=28, color=BLUE_ACCENT, align=PP_ALIGN.CENTER)
add_text_box(slide, Inches(1), Inches(5.0), Inches(11), Inches(0.6),
             "Project 15: Interactive Data Visualizer  |  Web Workshop", font_size=16, color=GRAY_TEXT, align=PP_ALIGN.CENTER)
add_text_box(slide, Inches(1), Inches(5.6), Inches(11), Inches(0.6),
             "Vineela  |  Annyunaa  |  Vishnu Vardhan  |  Rohan  |  Varun  |  Akshat", font_size=16, color=GRAY_TEXT, align=PP_ALIGN.CENTER)
add_shape_bg(slide, Inches(0), Inches(7.2), Inches(13.333), Pt(6), BLUE_ACCENT)

# Save
prs.save('PRESENTATION.pptx')
print("PRESENTATION.pptx created successfully!")
print(f"Total slides: {len(prs.slides)}")
