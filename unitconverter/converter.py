import re


class UnitCategory:
    categories = ["length", "weight", "temperature", "time"]

    def __init__(self, category):
        if category in UnitCategory.categories:
            self.category = category
        else:
            raise ValueError


class Unit:
    conversion_fns = {}
    abbrevs_to_names = {}

    def __init__(self, name, value):
        self.name = name
        if isinstance(value, str):
            self.value = float(value)
        else:
            self.value = value

    def get_names_to_abbrevs(self):
        return {v: k for k, v in self.abbrevs_to_names.items()}

    def print_chart(self):
        



class LengthUnit(Unit):
    conversion_fns = {
        "mi": ("m", 1609.34),
        "yd": ("m", 0.9144),
        "in": ("m", 0.0254),
        "ft": ("m", 0.3048),
        "m": ("m", 1)
    }
    abbrevs_to_names = {
        "mi": "mile",
        "yd": "yard",
        "in": "inch",
        "ft": "foot",
        "m": "meter"
    }

    def __init__(self, s):
        sanitized_unit_str = s.strip().lower()
        match_obj = re.match(r'^\s*([+-]*\d+)\s*([a-z]+)$', sanitized_unit_str)
        val, name = match_obj.group(1,2)
        super().__init__(name, val)


if __name__ == '__main__':
    lu = LengthUnit("3mi")
    lu.print_chart()

