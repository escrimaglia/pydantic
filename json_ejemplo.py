from datetime import date

data_json = '''
    {
        "manufacturer": "BMW",
        "series_name": "M4",
        "type": "Convertible",
        "manufactured_date": "2023-01-01",
        "base_msrp_usd": 9.99,
        "vin": "1234567890"
    }
'''

data_json_expected_serialization = {
        'manufacturer': 'BMW',
        'series_name': 'M4',
        'type': 'Convertible',
        'is_electric': False,
        'manufactured_date': date(2023, 1, 1),
        'base_msrp_usd': 9.99,
        'vin': '1234567890',
        'number_of_doors': 4,
        'registration_country': None,
        'license_plate': None,
}