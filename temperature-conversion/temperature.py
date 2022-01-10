import json


def handler(context, event):
    try:
        body = json.loads(event.body)

        converter = body["converter"]
        value = body["value"]
    except:
        return "Please give the data in JSON format"

    if converter == "FahrenheitToCelcius":
        ret = (value - 32) * 5.0/9.0
    elif converter == "CelciusToFahrenheit":
        ret = 9.0/5.0 * value + 32
    else:
        ret = -123

    return str(ret)
