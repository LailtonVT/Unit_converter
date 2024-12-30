from flask import Flask, render_template, request

app = Flask(__name__)

# Logica de conversao
conversion_factors = {
    "length": {
        "meter": 1,
        "kilometer": 1000,
        "mile": 1609.34,
        "yard": 0.9144,
    },
    "weight": {
        "gram": 1,
        "kilogram": 1000,
        "pound": 453.592,
        "ounce": 28.3495,
    },
    "temperature": "special" # Special case
}

def convert_units(value, from_unit, to_unit, category):
    if category == "temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return value * 9/5 + 32
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            return value + 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            return value - 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        else:
            return value  # Same unit
    else:
        return (value * conversion_factors[category][from_unit]) / conversion_factors[category][to_unit]

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        value = float(request.form["value"])
        from_unit = request.form["from_unit"]
        to_unit = request.form["to_unit"]
        category = request.form["category"]
        result = convert_units(value, from_unit, to_unit, category)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    print("Servidor Flask está iniciando...")
    app.run(debug=True)