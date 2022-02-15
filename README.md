# Nuclio examples
## Description
This repository demonstrates some basic Nuclio function examples.

## Examples
The following examples were implemented as part of this repository:
* sentiments: A function that uses the [vaderSentiment](https://github.com/cjhutto/vaderSentiment) library to classify text strings into a negative or positive sentiment score. This was an example provided by Nuclio ([link](https://github.com/nuclio/nuclio/tree/master/hack/examples/python/sentiments))
* temperature-conversion: A function that accepts input in Celcius and returns the temperature in Fahrenheit, and also the opposite.
* time-since: How much time has passed since a specific past date.
* db-add-recipe: This example demonstrates how to connect and add data to a database, using nuclio functions. In this example, when the function is invoked, it inserts a new recipe in the database.
* db-list-recipes: This example demonstrates how to connect and retrieve data from a database. In this example, when the function is invoked, it returns all the existing recipes that exist in the database.


---
This project was created by [Markos Baratsas](https://github.com/markosbaratsas) and [Maria Retsa](https://github.com/mariartc), for the purposes of the [Analysis and Design of Information Systems](https://www.ece.ntua.gr/en/undergraduate/courses/3321) at [ECE NTUA](https://www.ece.ntua.gr/en).
