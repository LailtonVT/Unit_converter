const units = {
    length: ["meter", "kilometer", "mile", "yard"],
    weight: ["gram", "kilogram", "pound", "ounce"],
    temperature: ["Celsius", "Fahrenheit", "Kelvin"]
};

function updateUnits() {
    const category = document.getElementById("category").value;
    const fromUnit = document.getElementById("from_unit");
    const toUnit = document.getElementById("to_unit");

    fromUnit.innerHTML = "";
    toUnit.innerHTML = "";

    units[category].forEach(unit => {
        const option1 = document.createElement("option");
        const option2 = document.createElement("option");
        option1.value = unit;
        option2.value = unit;
        option1.textContent = unit;
        option2.textContent = unit;
        fromUnit.appendChild(option1);
        toUnit.appendChild(option2);
    });
}

document.addEventListener("DOMContentLoaded", updateUnits);
