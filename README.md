# End-to-End Render Deployment Project

## Student Details

**Name:** Jayant Chaudhary

**Application No.:** IN26011386

**University Registration No.:** 23BCE10085

**University:** VIT Bhopal University

**Internship:** Artificial Intelligence and Machine Learning Internship – Batch 2(B) (6:00 PM – 8:00 PM)

---

## Overview

This project demonstrates the complete workflow of building, training, and deploying a Machine Learning model as a web application. A Linear Regression model is trained using the California Housing Dataset from Scikit-learn and deployed using Flask on Render. Users can enter housing features through a web interface and receive an estimated house price instantly.

---

## Live Demo

**Application:** https://end-to-end-render-deployment-project.onrender.com

---

## Features

- End-to-end Machine Learning project
- House price prediction using Linear Regression
- Model training with Scikit-learn
- Interactive Flask web interface
- Model serialization using Pickle
- Responsive frontend using HTML and CSS
- Cloud deployment using Render

---

## Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- HTML5
- CSS3
- Gunicorn
- Render

---

## Project Structure

```text
End-to-End-Render-Deployment-Project/
│
├── app.py
├── train_model.py
├── requirements.txt
├── runtime.txt
├── Procfile
├── README.md
│
├── model/
│   └── house_price_model.pkl
│
├── static/
│   └── style.css
│
└── templates/
    └── index.html
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/JayantChaudhary1980/End-to-End-Render-Deployment-Project
cd End-to-End-Render-Deployment-Project
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment.

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Train the model:

```bash
python train_model.py
```

Run the Flask application:

```bash
python app.py
```

Open your browser:

```text
http://127.0.0.1:5000
```

---

## Deployment

The application is deployed on **Render** as a Python Web Service using:

- Flask
- Gunicorn
- Procfile
- runtime.txt

Render automatically rebuilds and redeploys the application whenever changes are pushed to the GitHub repository. :contentReference[oaicite:0]{index=0}

---

## Future Improvements

- Add multiple Machine Learning models for comparison
- Improve the user interface using Bootstrap
- Display model evaluation metrics
- Store prediction history in a database
- Dockerize the application
- Add input validation and error handling

---

## Author

**Jayant Chaudhary**

B.Tech Computer Science and Engineering

VIT Bhopal University