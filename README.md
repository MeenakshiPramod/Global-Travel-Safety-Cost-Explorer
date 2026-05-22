# Global Travel Safety & Cost Explorer

A smart travel insight web application built using **Streamlit** and multiple **public APIs** that helps users explore destinations based on weather, country information, currency conversion, and travel recommendations.

Built as part of the **Dev Weekends Fellowship 2026 Assessment**.

---

# Features
Country Information  
- Capital
- Population
- Region
- National Currency
- Country Flag

Live Weather Insights  
- Temperature
- Humidity
- Weather Condition

Currency Conversion  
- Convert USD to local currency

Smart Travel Recommendations  
- Travel-friendly weather suggestions
- Packing recommendations
- Best time to visit insights

Travel Score System  
- Dynamic score based on weather conditions and destination data

Robust Error Handling  
- Invalid input handling
- API failure handling
- Timeout handling

---

# Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application framework |
| Requests | API communication |
| REST Countries API | Country information |
| ExchangeRate API | Currency conversion |
| wttr.in API | Weather information |

---

# APIs Used

## 1. REST Countries API
Used for:
- Country information
- Population
- Currency
- Region
- Flag

https://restcountries.com/

---

## 2. ExchangeRate API
Used for:
- Currency conversion

https://open.er-api.com/

---

## 3. wttr.in API
Used for:
- Live weather information

https://wttr.in/

---

# Project Structure

```bash
travel-explorer/
│
├── app.py
├── requirements.txt
├── README.md
├── ANSWERS.md
├── .gitignore
│
├── utils/
│   ├── weather.py
│   ├── countries.py
│   ├── currency.py
│   └── helpers.py
```

---

# Installation

## 1. Clone Repository

```bash
git clone <your-github-repo-link>
```

---

## 2. Navigate Into Project

```bash
cd travel-explorer
```

---

## 3. Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run The Application

```bash
streamlit run app.py
```

---

# Example Inputs

Try entering:

- Japan
- India
- France
- Canada
- Australia

---

# Error Handling

This project handles several edge cases including:

- Empty input fields
- Invalid country names
- Slow API responses
- Failed API responses
- Missing weather data
- Currency conversion failures

Timeout handling is implemented using:

```python
timeout=10
```

to prevent the app from freezing during slow API responses.

---

# Smart Recommendation System

The application generates:
- Travel advice
- Packing suggestions
- Destination suitability insights

based on live weather conditions.

---

# Future Improvements

Possible future enhancements:

- Add interactive charts
- Add destination comparison
- Add travel cost estimation
- Add hotel and flight APIs
- Add AI-powered itinerary suggestions
- Add destination bookmarking

---

# Screenshots

## Home Screen
<img width="2545" height="1278" alt="image" src="https://github.com/user-attachments/assets/7e5533fc-ebfa-4647-ab78-f0412c03f4ee" />


## Results Screen
<img width="2559" height="1281" alt="image" src="https://github.com/user-attachments/assets/937f1b56-62b0-4aa9-b85c-46cc5fcfd3eb" />
<img width="2555" height="1300" alt="image" src="https://github.com/user-attachments/assets/87c68503-2f95-4219-812d-b507c74138e3" />


#  Live Demo

[https://your-app-link.streamlit.app
](https://global-travel-safety-cost-explorergit-le8gk3r8jtejkeueoybwl8.streamlit.app/)
---

# Security

- No API keys are committed to the repository
- Sensitive files are excluded using `.gitignore`

---

# License

This project is created for educational and assessment purposes.

---

# Author

Meenakshi Pramod

Built for the **Dev Weekends Fellowship 2026 Assessment**
