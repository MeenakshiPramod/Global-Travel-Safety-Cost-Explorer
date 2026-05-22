import streamlit as st
from utils.countries import get_country_data
from utils.weather import get_weather
from utils.currency import convert_currency
from utils.air_quality import get_air_quality
from utils.helpers import generate_travel_advice

st.set_page_config(
    page_title="Global Travel Explorer",
    page_icon="🌍",
    layout="wide"
)

st.title("Global Travel Safety & Cost Explorer")
st.markdown(
    "Compare countries using weather, air quality, currency insights, and travel recommendations."
)

st.divider()

# Sidebar
st.sidebar.header("About")
st.sidebar.write(
    """
    This app helps users explore travel-related insights using multiple public APIs.
    
    Features:
    - Country information
    - Live weather
    - Air quality
    - Currency conversion
    - Smart travel advice
    """
)

# User Input
location = st.text_input(
    "Enter a country or city name",
    placeholder="Example: Japan, India, Paris"
)

currency_amount = st.number_input(
    "Amount in USD to convert",
    min_value=1.0,
    value=100.0
)

# Explore Button
if st.button("Explore"):

    # Input Validation
    if not location.strip():
        st.error("Please enter a valid country or city name.")
        st.stop()

    with st.spinner("Fetching travel intelligence..."):

        # Fetch data
        country_data = get_country_data(location)
        weather_data = get_weather(location)
        air_quality_data = get_air_quality(location)

    # API Failure Handling
    if (
        country_data is None
        and weather_data is None
        and air_quality_data is None
    ):
        st.error("Unable to fetch data currently. Please try again later.")
        st.stop()

    # ---------------- COUNTRY SECTION ---------------- 

    if country_data:

        st.subheader("Country Information")

        col1, col2 = st.columns([1, 2])

        with col1:
            st.image(country_data["flag"], width=180)

        with col2:
            st.write(f"### {country_data['name']}")
            st.write(f"**Capital:** {country_data['capital']}")
            st.write(f"**Region:** {country_data['region']}")
            st.write(f"**Population:** {country_data['population']:,}")
            st.write(f"**Currency:** {country_data['currency']}")

    else:
        st.warning("Country information not available.")

    st.divider()

    # ---------------- WEATHER SECTION ---------------- 

    if weather_data:

        st.subheader("Weather Insights")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Temperature",
                f"{weather_data['temp']} °C"
            )

        with col2:
            st.metric(
                "Humidity",
                f"{weather_data['humidity']}%"
            )

        with col3:
            st.metric(
                "🌤 Condition",
                weather_data['description'].title()
            )

    else:
        st.warning("Weather data unavailable currently.")

    st.divider()

    # ---------------- AIR QUALITY SECTION ---------------- 

    if air_quality_data:

        st.subheader("Air Quality")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "AQI",
                air_quality_data["aqi"]
            )

        with col2:
            st.metric(
                "Air Quality Status",
                air_quality_data["status"]
            )

    else:
        st.warning("Air quality data unavailable.")

    st.divider()

    # ---------------- CURRENCY SECTION ---------------- 

    if country_data:

        st.subheader("Currency Conversion")

        converted = convert_currency(
            "USD",
            country_data["currency"],
            currency_amount
        )

        if converted:

            st.success(
                f"${currency_amount} USD = "
                f"{converted:.2f} {country_data['currency']}"
            )

        else:
            st.warning("Currency conversion failed.")

    st.divider()

    # ---------------- SMART ADVICE SECTION ---------------- 

    st.subheader("Smart Travel Recommendation")

    advice = generate_travel_advice(
        weather_data,
        air_quality_data
    )

    st.info(advice)

    st.divider()

    # ---------------- TRAVEL SCORE ---------------- 

    st.subheader("Travel Score")

    score = 0

    if weather_data:
        temp = weather_data["temp"]

        if 18 <= temp <= 30:
            score += 40
        elif 10 <= temp < 18:
            score += 25
        else:
            score += 15

    if air_quality_data:
        if air_quality_data["aqi"] <= 50:
            score += 40
        elif air_quality_data["aqi"] <= 100:
            score += 25
        else:
            score += 10

    if country_data:
        score += 20

    st.progress(min(score, 100))

    st.write(f"### Overall Travel Score: {min(score,100)}/100")

    if score >= 80:
        st.success("Excellent travel destination currently!")
    elif score >= 50:
        st.warning("Moderate travel conditions.")
    else:
        st.error("Travel conditions may not be ideal currently.")

# Footer
st.divider()

st.caption(
    "Built using Streamlit + Public APIs for Dev Weekends Fellowship Assessment"
)
