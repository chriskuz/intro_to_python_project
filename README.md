# PLACEHOLDER TITLE

This README is a WIP. Some goals for the readme in mind:

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

| Variable Name | Expected Data Type | Description |
|--------------|-------------------|-------------|
| searchDate | datetime | Date when the flight search was performed |
| searchDayOfWeek | int/string | Day of the week when search was performed |
| route | string | Flight route code |
| flightDate | datetime | Scheduled date of the flight |
| flightDayOfWeek | int/string | Day of the week of the flight |
| startingAirport | string | Departure airport code |
| destinationAirport | string | Arrival airport code |
| elapsedDays | int | Number of days between search date and flight date |
| isBasicEconomy | boolean | Whether the ticket is basic economy class |
| isRefundable | boolean | Whether the ticket is refundable |
| isNonStop | boolean | Whether the flight is non-stop |
| baseFare | float | Base ticket price before taxes and fees |
| totalFare | float | Total price including all taxes and fees |
| seatsRemaining | int | Number of seats available |
| totalTravelDistance | float | Total flight distance |
| segmentsDepartureTimeRaw | datetime | Raw departure time for flight segments |
| segmentsArrivalTimeRaw | datetime | Raw arrival time for flight segments |
| segmentsArrivalAirportCode | string | Airport code for segment arrival |
| segmentsDepartureAirportCode | string | Airport code for segment departure |
| segmentsAirlineName | string | Name of the airline |
| segmentsDurationInSeconds | int | Duration of flight segments in seconds |
| segmentsCabinCode | string | Cabin class code |
| departureTime | datetime | Flight departure time |
| arrivalTime | datetime | Flight arrival time |
| departureCategory | string | Category of departure time (e.g., morning/afternoon) |
| arrivalCategory | string | Category of arrival time (e.g., morning/afternoon) |
| isHolidaySearchDate | boolean | Whether the search date is a holiday |
| isHolidayFlightDate | boolean | Whether the flight date is a holiday |
| nearHolidaySearchDate | boolean | Whether the search date is near a holiday |
| nearHolidayFlightDate | boolean | Whether the flight date is near a holiday |
| searchDateInt | int | Integer representation of search date |
| flightDateInt | int | Integer representation of flight date |
| daysLeft | int | Days remaining until flight departure |
| numStops | int | Number of stops in the flight route |



# Author Names

- Chris Kuzemka
- Irene Chau
- Fangyuan Xu
- Ali Nazim
- Aqib Rahim
>>>>>>> Stashed changes
