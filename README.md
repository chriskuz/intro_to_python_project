# PLACEHOLDER TITLE

This README is a WIP. Some goals for the readme in mind:

- project description, hypothesis, abstract
- data used + data dictionary
- repository structure
- developer installation and contribution instructions
Aqib Rahim
Yurica Xu

<<<<<<< Updated upstream
irene test
=======


# JetBlue Flight Price Analysis
JetBlue flight price Analysis is a simple script to identify trends, make predictions, and provide actionable insights for consumers. It focuses on determining the best time to book JetBlue flights to get the lowest fares.
## Hypothesis
*Booking lead time significantly impacts ticket prices, with prices likely decreasing initially and rising sharply closer to the departure date.
*Seasonality and holidays lead to higher prices for JetBlue flights, particularly for popular routes during peak travel seasons.
*Certain routes may show more stable pricing patterns, while others experience higher volatility, particularly for routes to or from high-demand destinations.
## Data
*JetBlue Historical Pricing Data(https://www.kaggle.com/datasets/dilwong/flightprices)

## Data Dictionary

| **Data Variable**          | **Type**          | **Description**                               |
|-----------------------------|-------------------|-----------------------------------------------|
| `ident`                    | String Object     | Identification of a flight                   |
| `actual_ident`             | String Object     | Original identification of a codeshared flight |
| `departuretime`            | String Object     | Departure time of flight (date, hours, minutes) |
| `arrival_time`             | String Object     | Arrival time of flight (date, hours, minutes) |
| `origin`                   | String Object     | Origin ICAO code                              |
| `destination`              | String Object     | Destination ICAO code                         |
| `aircrafttype`             | String Object     | Type of aircraft flown                        |
| `meal_service`             | String Object     | Type of meal service provided on flight       |
| `seats_cabin_first`        | Integer           | Number of first-class seats available         |
| `seats_cabin_business`     | Integer           | Number of business-class seats available      |
| `seats_cabin_coach`        | Integer           | Number of coach-class seats available         |
| `origin_IATA`              | String Object     | Origin IATA code                              |
| `destination_IATA`         | String Object     | Destination IATA code                         |
| `flight_duration`          | String Object     | Flight duration in seconds                    |
| `MinPrice`                 | Float             | Minimum price for a ticket on the flight      |
| `Direct`                   | Boolean Object    | Indicates whether the route is direct         |
| `OriginName`               | String Object     | Origin airport name                           |
| `OriginCityName`           | String Object     | Origin city name                              |
| `OriginCountryName`        | String Object     | Origin country name                           |
| `DestinationName`          | String Object     | Destination airport name                      |
| `DestinationCityName`      | String Object     | Destination city name                         |
| `DestinationCountryName`   | String Object     | Destination country name                      |
| `CarrierName`              | String Object     | Carrier name associated with the flight       |

---

## Installation & Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo-name/JetBlue-Flight-Price-Analysis.git
   cd JetBlue-Flight-Price-Analysis

Text

**Bold Text**

__Bold text__

*Italicized text*

# Author Names

- Chris Kuzemka

- Irene Chau
>>>>>>> Stashed changes
