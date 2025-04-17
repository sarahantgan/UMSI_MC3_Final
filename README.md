# MC3_UMSI
=======
UMSI capstone project with Michigan Medicine - Michigan Clinical Consultation and Care (MC3)

## Overview
This interactive dashboard provides county-level insights into demographic and healthcare data across the state of Michigan, with a specific focus on MC3 consultations and OBGYN access.

## Features
- **Interactive Map**: Clickable county-level choropleth map for visualizing multiple demographic or healthcare metrics.
- **Dropdown Controls**:
  - **Numeric Metrics**: Population, income, OBGYN rates, and more.
  - **Categorical Metrics**: Income/OBGYN/Non-White/Density categories based on tertiles (Low/Medium/High).
- **Sidebar Details**: View metric values for a selected county.
- **Comparison Tool**: Select multiple counties to compare key metrics via a bar chart.
- **Color Consistency**: All charts and maps use a consistent color scheme matching the MC3 website aesthetic.
- **Reset Button**: Clear map selections and start over with one click.

## Metrics Available
### Numeric (Raw values)
- Total Population
- Population Density (per km²)
- Median Income (USD)
- Percent of Non-White Population
- Rate of OBGYNs (per 100,000 population)
- Total Number of OBGYNs
- Total MC3 Consultations

### Categorical (Tertiles across all MI counties)
- **Income Category** (Low / Medium / High)
- **OBGYN Access Category**
- **Percent Non-White Category**
- **Population Density Category**
==========
## How to Use This Dashboard (Step-by-Step)

### 1. Install Python (if you don’t already have it)
Visit https://www.python.org/downloads/ and install Python 3.8 or later. Make sure to check the box **"Add Python to PATH"** during installation.

---

### 2. Download or Clone This Project
```bash
# Clone the repository
https://github.com/sarahantgan/MC3_UMSI.git
cd MC3_UMSI
---
```
### 3. Install Dependencies 
In your terminal, type: 
```bash
pip install -r requirements.txt
```
This installs all the required packages (like Dash and Plotly) and sets up a shortcut to launch the dashboard.

---

### 4. Run the Dashboard
Just type this in your terminal:
```bash
run-mc3-dashboard
```

It will automatically open in your browser at:
```
http://localhost:8050
```

Alternatively, run it manually with:
```bash
python mc3_dash/app.py
```

---

## 🌐 Embed the Dashboard in a Website
Once running locally, you can embed it in any webpage using an iframe:
```html
<iframe src="http://localhost:8050" width="100%" height="850px" frameborder="0"></iframe>
```

For external hosting, see the Deployment section below.

---

## 📁 About the Data
The dashboard uses a file called `mc3_updated.csv` — this must remain in the root directory (the same folder as setup.py). It contains:
- Population
- Income
- Racial demographics
- OBGYN access per 100K
- Consultations
- etc

If you update the data, keep the same column names.

---

## 📤 Optional: Host It Online
You can deploy the dashboard so others can use it by:
- **Render:** https://render.com/docs/deploy-dash
- **Heroku:** https://devcenter.heroku.com/articles/getting-started-with-python
- **Railway:** https://railway.app/

Let us know if you want help doing this — we’re happy to assist!

---

## 💬 Need Help?
If anything is unclear, just reach out to Sara Hantgan (shantgan@umich.edu)

