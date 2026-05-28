def normalize_unit(value, unit):

    conversions = {
        "L": ("kg", value * 0.85),
        "kWh": ("kWh", value),
        "km": ("km", value),
    }

    return conversions.get(unit, (unit, value))


def calculate_emissions(category, value):

    emission_factors = {
        "diesel": 2.68,
        "electricity": 0.5,
        "flight": 0.15,
    }

    factor = emission_factors.get(category.lower(), 0)

    return value * factor


def is_suspicious(value):

    if value < 0:
        return True

    if value > 100000:
        return True

    return False