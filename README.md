<<<<<<< HEAD
# MC3_UMSI
UMSI capstone project with Michigan Medicine - Michigan Clinical Consultation and Care (MC3) 
=======
"""
# MC3 Dashboard — Michigan County Health Insights

Welcome to the MC3 Dashboard! This is a data visualization tool designed to help explore healthcare access and demographics across Michigan counties. No technical experience is needed to use it.

---

## ✅ What You Get
- An interactive map to explore key demographic and healthcare metrics
- Drop-downs to select counties or compare multiple ones
- Clear color-based visualizations and summary text
- Ability to embed in any website or launch locally

---

## 🚀 How to Use This Dashboard (Step-by-Step)

### 1. Install Python (if you don’t already have it)
Visit https://www.python.org/downloads/ and install Python 3.9 or later. Make sure to check the box **"Add Python to PATH"** during installation.

---

### 2. Download or Clone This Project
Option A: Download the .ZIP file from GitHub and unzip it.

Option B: Use Git (if you're comfortable):
```bash
git clone https://github.com/YOUR_USERNAME/mc3_dashboard.git
cd mc3_dashboard
```

---

### 3. Install the Dashboard
In your terminal or command prompt, type:
```bash
pip install -e .
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
If anything is unclear or you'd like this integrated into your existing site by a developer, just reach out to Sara Hantgan (shantgan@umich.edu)

"""
>>>>>>> Initial upload of MC3 dashboard
