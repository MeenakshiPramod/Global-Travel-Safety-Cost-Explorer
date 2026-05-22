# ANSWERS.md

# 1. How to Run

## Clone the repository

```bash
git clone <your-github-repository-link>
```

---

## Navigate into the project directory

```bash
cd travel-explorer
```

---

## Create a virtual environment

### Windows

```bash
python -m venv venv
```

Activate the environment:

```bash
venv\Scripts\activate
```

---

## Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run the application

```bash
streamlit run app.py
```

The application will start locally in the browser.

---

# 2. Stack Choice

I chose Python with Streamlit because it allowed me to rapidly build an interactive data-driven application with minimal setup overhead. Since the assessment focused more on API consumption, usability, and handling edge cases rather than frontend complexity, Streamlit was an efficient choice.

Python also has excellent support for API integration through the `requests` library, which simplified handling multiple public APIs and implementing robust error handling.

A worse choice for this task would have been using a heavy frontend-backend architecture with separate services because it would increase development complexity and setup time for a relatively small project. My priority was building a clean, reliable, and user-friendly solution within the assessment timeframe.

---

# 3. One Real Edge Case

One important edge case handled in this project is invalid or empty user input.

### File:
`app.py`

### Handling:
The application checks whether the input field is empty before making API requests.

Example:

```python
if not location.strip():
    st.error("Please enter a valid country name.")
    st.stop()
```

### Why this matters:
Without this handling, the APIs would receive invalid requests, resulting in failed API calls and confusing user experience. This validation prevents unnecessary requests and improves overall application stability.

Another handled edge case is API failure or slow response handling using request timeouts and fallback error messages.

---

# 4. AI Usage

I used AI tools during the development process primarily for brainstorming, improving structure, debugging, and refining documentation.

### AI Tools Used

#### ChatGPT
Used for:
- Brainstorming project ideas
- Structuring the project architecture
- Improving README formatting
- Suggesting better error handling patterns
- Debugging API integration issues
- Refining user interface ideas

### One Thing I Changed

Initially, the project used the OpenWeather API for both weather and air quality data. However, due to API authentication and activation issues during development, I replaced the weather integration with the `wttr.in` API to improve reliability and simplify setup.

I also modified the AI-generated error handling logic by adding clearer fallback messages and input validation to improve user experience.

---

# 5. Honest Gap

One thing that could still be improved is the depth of travel intelligence provided by the application.

Currently, the project focuses mainly on weather, country details, and currency conversion. With another day, I would implement additional features such as:

- Destination comparison
- Interactive charts and analytics
- Travel cost estimation
- Historical weather trends
- AI-powered travel itinerary suggestions

I would also improve the overall UI design further and add automated tests for API failure scenarios.