"""London Southend Airport (SEN) destinations — April 2026."""

DESTINATIONS = {
    "SEN": {
        "name": "London Southend",
        "routes": {
            "ACE": "Lanzarote",
            "AGP": "Malaga",
            "ALC": "Alicante",
            "AMS": "Amsterdam",
            "AYT": "Antalya",
            "BCN": "Barcelona",
            "BER": "Berlin",
            "BUD": "Budapest",
            "CDG": "Paris CDG",
            "DLM": "Dalaman",
            "ENF": "Enontekio",
            "FAO": "Faro",
            "GNB": "Grenoble",
            "GVA": "Geneva",
            "IBZ": "Ibiza",
            "JER": "Jersey",
            "LEI": "Almeria",
            "LPA": "Gran Canaria",
            "MLA": "Malta",
            "MUC": "Munich",
            "NBE": "Enfidha",
            "PMI": "Palma",
            "PSA": "Pisa",
            "RAK": "Marrakech",
            "RVN": "Rovaniemi",
            "SZG": "Salzburg",
            "TFS": "Tenerife South",
        },
    },
}


def get_destinations(airport: str) -> dict:
    entry = DESTINATIONS.get(airport, {})
    return entry.get("routes", {})


def get_airport_name(airport: str) -> str:
    entry = DESTINATIONS.get(airport, {})
    return entry.get("name", airport)
