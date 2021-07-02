import datetime

from jsonschema import validate, Draft7Validator, FormatChecker


class Validation:
    def __init__(self):
        self.c = FormatChecker()
        self.c.checks("positive_int")(CheckerFunctions.positive_int)
        self.c.checks("time_interval")(CheckerFunctions.time_checker)
        self.schema = Schemas()

    def check_courier(self, data) -> (bool, list, list):
        if data is None or 'data' not in data:
            return False, [], []
        checker = True
        bad_courier = []
        good_courier = []
        for courier in data['data']:
            courier_status = Draft7Validator(self.schema.schema_courier, format_checker=self.c).is_valid(courier)
            checker = checker and courier_status
            if not courier_status:
                bad_id = courier.get('courier_id', None)
                if bad_id:
                    bad_courier.append({'id': bad_id})
            else:
                good_courier.append(courier)
        return checker, bad_courier, good_courier




class CheckerFunctions:
    @staticmethod
    def positive_int(x):
        try:
            x = int(x)
            return x > 0
        except ValueError as e:
            return False

    @staticmethod
    def time_checker(interval_check):
        times = interval_check.split('-')
        try:
            if len(times) != 2:
                raise Exception
            x, y = datetime.datetime.strptime(times[0], '%H:%M').time(), datetime.datetime.strptime(times[1],
                                                                                                    '%H:%M').time()
            if x >= y:
                raise Exception

            return True
        except Exception as e:
            return False


class Schemas:
    def __init__(self):
        self.schema_courier = {
            "type": "object",
            "properties": {
                "courier_id": {"type": "integer", "format": "positive_int"},
                "courier_type": {"type": "string", "enum": ["foot", "bike", "car"]},
                "regions": {"type": "array", "items": {"type": "integer", "format": "positive_int"}},
                "working_hours": {"type": "array", "items": {"type": "string", "format": "time_interval"}}
            },
            "required": ["courier_id", "courier_type", "regions", "working_hours"]
        }