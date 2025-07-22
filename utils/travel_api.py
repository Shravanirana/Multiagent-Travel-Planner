import json

def load_locations(path="data/sample_locations.json"):
    """Load location data from a JSON file."""
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)

def get_matching_cities(user_input, data):
    """Return cities that match user interest, budget, duration and continent."""
    interest = user_input.get("interest", "").lower()
    budget   = user_input.get("budget", 0)
    duration = user_input.get("duration", 1)
    continent = user_input.get("continent", "")
    results = []
    for city in data:
        if interest and interest not in city["tags"]:
            continue
        if continent and city.get("continent") != continent:
            continue
        if city["base_cost_per_day"] * duration <= budget:
            results.append(city)
    return results