# Nuclio Examples: Sentiments

## Description
This example demonstrates a Nuclio Function that uses the [vaderSentiment](https://github.com/cjhutto/vaderSentiment) library to classify text strings into a negative or positive sentiment score. This was an example provided by Nuclio ([link](https://github.com/nuclio/nuclio/tree/master/hack/examples/python/sentiments)).


## How to implement:
1. Execute the following command:
```
sudo nuctl deploy \
    --path PATH_TO_NUCLIO_EXAMPLES/nuclio-examlpes/sentiments \
    --registry $(minikube ip):5000 \
    --run-registry localhost:5000
```
Fill in the PATH_TO_NUCLIO_EXAMPLES, with the correct path. 
2. Test the function, using port provided from the command executed in step 1. Using Postman, create a request towards `http://localhost:PORT_FROM_COMMAND`. Under body->raw->Text provide the text that is to be scored. It should look something like this:
```
"You are the best person!"
```
If everything is working as expected the response should look like this:
```
{'neg': 0.0, 'neu': 0.471, 'pos': 0.529, 'compound': 0.6696}
```
