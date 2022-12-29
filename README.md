# AirQualityPrediction
This project uses a MQ-135 gas leak sensor to predict pollutants in the air by using approximated AQI readings.

The MQ-135 sensor on its default setting is sensitive to detect higher carbon based elements, you will need to change to the resistor on the sensor from 10k ohms 
to 100 ohms resistor to make it more sensitive to lower carbon footprint elemets such as carbon mono-oxide.
Connect the sensor to the board to post updates to the serial port, you can set whatever delay you like. Just update the serial port name and baud in `airquality.py`.

We use a custom dataset tailored with readings accurate readings based on our location. You can use the test dataset `city_day.csv` which has AQI readings of an averge cityin India.

Just start the app with `airquality.py`.
