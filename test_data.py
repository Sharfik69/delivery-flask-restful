courier_bad_time = {
    "data": [
        {
            "courier_id": 1,
            "courier_type": "foot",
            "regions": [1, 12, 22],
            "working_hours": ["11:345-14:05", "09:030-11:00"]
        },
        {
            "courier_id": 2,
            "courier_type": "bike",
            "regions": [22],
            "working_hours": ["09:12300-18:020"]
        },
        {
            "courier_id": 3,
            "courier_type": "car",
            "regions": [12, 22, 23, 33],
            "working_hours": []
        }
    ]
}
courier_bad_time_ans = {
    "validation_error": {
        "couriers": [
            {
                "id": 1
            },
            {
                "id": 2
            }
        ]
    }
}

courier_bad_field = {
    "data": [
        {
            "courier_id": 1,
            "courier_type": "velosiped",
            "regions": [1, 12, 22],
            "working_hours": ["11:35-14:05", "09:00-11:00"]
        },
        {
            "courier_id": 2,
            "courier_type": "bike",
            "working_hours": ["09:00-18:00"]
        },
        {
            "courier_id": 3,
            "courier_type": "foot",
            "regions": [1, 12, 22],
            "working_hours": ["11:35-14:05", "09:00-11:00"]
        },
        {
            "courier_id": 4,
            "courier_type": "foot",
            "regions": [1, 12, 22]
        },
        {
            "courier_id": 5,
            "regions": [1, 12, 22],
            "working_hours": ["11:35-14:05", "09:00-11:00"]
        }
    ]
}
courier_bad_field_ans = {
    "validation_error": {
        "couriers": [
            {
                "id": 1
            },
            {
                "id": 2
            },
            {
                "id": 4
            },
            {
                "id": 5
            }
        ]
    }
}

