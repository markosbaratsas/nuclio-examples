# Nuclio Examples: Temperature Conversion

## Description
This example demonstrates a Nuclio Function that accepts input in Celcius and returns the temperature in Fahrenheit, and also the opposite.

## How to implement:
1. Execute the following command:
```
sudo nuctl deploy \
    --path PATH_TO_NUCLIO_EXAMPLES/nuclio-examples/temperature-conversion \
    --registry $(minikube ip):5000 \
    --run-registry localhost:5000
```
Fill in the PATH_TO_NUCLIO_EXAMPLES, with the correct path. 
2. Test the function, using port provided from the command executed in step 1. Using Postman, create a request towards `http://localhost:PORT_FROM_COMMAND`. Under body->raw->Text provide the Temperature, along with the type of conversion(choose between `CelciusToFahrenheit`/`FahrenheitToCelcius`) in the following format:
```
{
    "converter": "CelciusToFahrenheit",
    "value": 12
}
```
If everything is working as expected the response should look like this:
```
53.6
```
