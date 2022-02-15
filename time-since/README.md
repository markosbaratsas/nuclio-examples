# Nuclio Examples: Time Since

## Description
This example demonstrates a Nuclio Function that returns how much time has passed since a specific past date.

## How to implement:
1. Execute the following command:
```
sudo nuctl deploy \
    --path PATH_TO_NUCLIO_EXAMPLES/nuclio-examlpes/time-since \
    --registry $(minikube ip):5000 \
    --run-registry localhost:5000
```
Fill in the PATH_TO_NUCLIO_EXAMPLES, with the correct path. 
2. Test the function, using port provided from the command executed in step 1. Using Postman, create a request towards `http://localhost:PORT_FROM_COMMAND`. Under body->raw->JSON provide the date in the following format:
```
"13/11/2019 00:00:00"
```
If everything is working as expected the response should look like this:
```
2 years 3 months 3 days 18 hours 15 minutes 41 seconds
```
