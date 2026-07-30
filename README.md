# End-to-End Render Deployment Project

## Student Details

**Name:** Jayant Chaudhary

**Application No.:** IN26011386

**University Registration No.:** 23BCE10085

**University:** VIT Bhopal University

**Internship:** Artificial Intelligence and Machine Learning Internship – Batch 2(B) (6:00 PM – 8:00 PM)

---

## Overview

This project is an end-to-end Machine Learning web application that predicts the price of a house based on various housing features. A Linear Regression model is trained using the California Housing Dataset from Scikit-learn and deployed through a Flask web application. The application provides an easy-to-use web interface where users can enter housing details and receive an estimated house price instantly.

---

## Features

- Train a Machine Learning model using the California Housing dataset
- Predict house prices using user input
- Responsive web interface built with Flask
- Model serialization using Pickle
- Ready for deployment on Render
- Clean and modular project structure

---

## Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- HTML
- CSS
- Gunicorn
- Render

---

## Project Structure

```
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

Clone the repository

```bash
git clone <repository-url>
cd End-to-End-Render-Deployment-Project
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

Install the required packages

```bash
pip install -r requirements.txt
```

Train the model

```bash
python train_model.py
```

Run the Flask application

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

## Deployment

The application is configured for deployment on Render using:

- Gunicorn
- Procfile
- runtime.txt

---

## Future Improvements

- Support multiple regression models
- Improve UI with Bootstrap
- Add model performance metrics on the webpage
- Store prediction history in a database
- Deploy using Docker

---

## Author

**Jayant Chaudhary**

B.Tech Computer Science and Engineering

VIT Bhopal University