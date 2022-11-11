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
                "feet": "ft",
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

    metric_prefix_names_to_abbrevs = {
        "kilo": "k",
        "hecto": "h",
        "deka": "da",
        "deci": "d",
        "centi": "c",
        "milli": "m",
    }

    def __init__(self, s):
        sanitized_unit_str = s.strip().lower()
        match_obj = re.fullmatch(r'^\s*([+-]*\d+)\s*([a-z]+)$', sanitized_unit_str)
        if not match_obj:
            raise ValueError
        value, orig_unit = match_obj.group(1, 2)
        prefix, unit, unit_type = UnitValue.map_unit(orig_unit)
        self.prefix = prefix
        self.unit = unit
        self.unit_type = unit_type
        self.value = float(value)

    @staticmethod
    def match_unit(val, unit_str):
        return val == unit_str or val == f'{unit_str}s' or val == f'{unit_str}es'

    @staticmethod
    def get_prefix(orig_unit):
        prefix = ""
        for long_prefix, short_prefix in UnitValue.metric_prefix_names_to_abbrevs.items():
            if orig_unit.startswith(long_prefix) or (orig_unit.startswith(short_prefix) and len(orig_unit) > len(short_prefix)):
                prefix = short_prefix
        return prefix

    @staticmethod
    def map_unit(orig_unit):
        prefix = UnitValue.get_prefix(orig_unit)
        remaining_unit = orig_unit.replace(prefix, '')
        unit = None
        unit_type = None
        for curr_unit_type, curr_unit_data in UnitValue.units.items():
            for long_name, abbrev in curr_unit_data["names_to_abbrevs"].items():
                if UnitValue.match_unit(remaining_unit, long_name) or UnitValue.match_unit(remaining_unit, abbrev):
                    unit_type = curr_unit_type
                    unit = abbrev
                    break
            if unit and unit_type:
                break
        else:
            prefix = ""
            for curr_unit_type, curr_unit_data in UnitValue.units.items():
                for long_name, abbrev in curr_unit_data["names_to_abbrevs"].items():
                    if UnitValue.match_unit(orig_unit, long_name) or UnitValue.match_unit(orig_unit, abbrev):
                        unit_type = curr_unit_type
                        unit = abbrev
                        break
                if unit and unit_type:
                    break
        return prefix, unit, unit_type

    def __str__(self):
        return f'{self.value:.2f} {self.prefix}{self.unit} ({self.unit_type})'

    def __repr__(self):
        return f'<UnitValue value={self.value:.2f} unit={self.prefix}-{self.unit} (type={self.unit_type})>'


if __name__ == '__main__':
    while True:
        try:
            val_str = input("enter a unit value? ")
            if val_str == "":
                break
            uv = UnitValue(val_str)
            print(f'{uv!s}')
            print(f'{uv!r}')
        except ValueError:
            print("Invalid value entered! Please try again!")

