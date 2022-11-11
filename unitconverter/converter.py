import re

class UnitValue:
    units = {
        "length": {
            "conversion_fns": {
                "mi": ("m", 1609.34),
                "yd": ("m", 0.9144),
                "in": ("m", 0.0254),
                "ft": ("m", 0.3048),
                "m": ("m", 1)
            },
            "names_to_abbrevs": {
                "mile": "mi",
                "yard": "yd",
                "inch": "in",
                "foot": "ft",
                "meter": "m"
            }
        },
        "weight": {
            "conversion_fns": {
                "lb": ("g", 453.592),
                "oz": ("g", 28.3495),
                "g": ("g", 1)
            },
            "names_to_abbrevs": {
                "pound": "lb",
                "ounce": "oz",
                "gram": "g",
            }
        },
        "temperature": {
            "conversion_fns": {
                "c": ("c", 1),
                "f": ("c", 0.5556, -17.7778),
                "k": ("c", 1, 273.15),
            },
            "names_to_abbrevs": {
                "celsius": "c",
                "centigrade": "c",
                "fahrenheit": "f",
                "kelvin": "k",
            }
        },
    }

    metric_prefixes = {
        "k": 1000,
        "h": 100,
        "da": 10,
        "d": 0.1,
        "c": 0.01,
        "m": 0.001,
    }
    metric_prefix_names_to_abbrevs: {
        "kilo": "k",
        "hecto": "h",
        "deka": "da",
        "deci": "d",
        "centi": "c",
        "milli": "m",
    }

    def __init__(self, s):
        sanitized_unit_str = s.strip().lower()
        match_obj = re.match(r'^\s*([+-]*\d+)\s*([a-z]+)$', sanitized_unit_str)
        value, unit = match_obj.group(1, 2)

        self.unit = unit
        self.value = float(value)

    def get_names_to_abbrevs(self):
        return {v: k for k, v in self.abbrevs_to_names.items()}

    def get_prefix_names_to_abbrevs(self):
        return {v: k for k, v in self.metric_prefix_abbrevs_to_names.items()}

    def convert_value(self, target_unit_or_abbrev):


if __name__ == '__main__':
    lv = UnitValue("3mi")

