# BRCG

---

## Installation instructions

Install the requirements

```bash
pip install -r requirements.txt
```

Run the migrations

```
python manage.py migrate
```

Load the fixtures

```bash
python manage.py loaddata fixtures/countries_fixture.json
python manage.py loaddata fixtures/categories_fixture.json
```

Create superuser (/admin)

```bash
python manage.py createsuperuser
```

Run the server

```bash
python manage.py runserver
```

---

## Links

### User Registration

```bash
http://localhost:8000/accounts/register/
```

### User Login

```bash
http://localhost:8000/accounts/login/
```

### Country Management

```bash
http://localhost:8000/countries/
```

### Category Management

```bash
http://localhost:8000/categories/
```

---

## API 

### User Registration

Endpoint (POST)

```bash
http://localhost:8000/api/accounts/register/
```

Payload

```json
{
    "email": "user@example.com",
    "password": "securepassword"
}
```

Response

```json
{
    "message": "User created successfully."
}
```

### User Login

Endpoint (POST)

```bash
http://localhost:8000/api/accounts/login/
```

Payload

```json
{
    "email": "user@example.com",
    "password": "securepassword"
}
```

Response

```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwMjU2NTU2MCwiaWF0IjoxNzAyNDc5MTYwLCJqdGkiOiJjYjQxMzU3ZTNiOTk0YzlkOTNkMmRiMjgzYzE5NDhjZSIsInVzZXJfaWQiOjR9.A4iQ5ZWrYNMgWfLpj5g6hUo2exh3T8pPtUGldhAtT8k",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAyNDc5NDYwLCJpYXQiOjE3MDI0NzkxNjAsImp0aSI6IjVkMzE5ZmNiOGU0NzQxYjg4YTI2YjRhNjYyZjM4ODY5IiwidXNlcl9pZCI6NH0.8BCTGPVuvQnWLo3e3KuaVuo3QYtv7rCKHXGP011FPcI"
}
```

### Country API

Endpoint (GET)

```bash
http://localhost:8000/api/countries/
```

Available Params

```bash
search
```

```bash
http://localhost:8000/api/countries/?search=test
```

Response

```json
[
    {
        "id": 8,
        "name": "Manado",
        "flag": "https://cdn.discordapp.com/attachments/858938620425404426/1184047780155641906/China.svg",
        "currency": "MDC"
    },
    ...,
    {
        "id": 1,
        "name": "China",
        "flag": "https://cdn.discordapp.com/attachments/858938620425404426/1184047780155641906/China.svg",
        "currency": "CHY"
    }
]
```

### Category  API

Endpoint (GET)

```bash
http://localhost:8000/api/categories/
```

Available Params

```bash
search, country_id
```

```bash
http://localhost:8000/api/categories/?country_id=1
http://localhost:8000/api/categories/?search=laptop
http://localhost:8000/api/categories/?country_id=1&search=laptop
```

Response

```json
[
    {
        "id": 1,
        "title": "Electronic",
        "price_per_kilo": 250000.0,
        "country": 4
    },
    ...,
    {
        "id": 13,
        "title": "Hambrow",
        "price_per_kilo": 5566.0,
        "country": 1
    }
]
```

### Destination API

Endpoint (GET)

```bash
http://localhost:8000/api/destination/
```

```json
{
    "data": [
        {
            "city_id": "1",
            "province_id": "21",
            "province": "Nanggroe Aceh Darussalam (NAD)",
            "type": "Kabupaten",
            "city_name": "Aceh Barat",
            "postal_code": "23681"
        },
        ...,
        {
            "city_id": "2",
            "province_id": "21",
            "province": "Nanggroe Aceh Darussalam (NAD)",
            "type": "Kabupaten",
            "city_name": "Aceh Barat Daya",
            "postal_code": "23764"
        }
    ]
}
```

Available Params

```bash
search
```

```bash
http://localhost:8000/api/destination/?search=mana
```

```json
{
    "data": {
        "city_id": "165",
        "province_id": "25",
        "province": "Papua Barat",
        "type": "Kabupaten",
        "city_name": "Kaimana",
        "postal_code": "98671"
    }
}
```

### Calculate API

Endpoint (POST)

```bash
http://localhost:8000/api/calculate/
```

Payload

```json
{
    "country_id": 1,
    "category_id": 1,
    "destination_id": 268,
    "weight": 4
}
```

Response

```json
{
    "origin": "Japan",
    "destination": "Sumatera Utara, Mandailing Natal, 22916",
    "category_name": "Chip",
    "international_price": 1200000.0,
    "domestic_price": 1080000.0,
    "total_price": 2280000.0
}
```
