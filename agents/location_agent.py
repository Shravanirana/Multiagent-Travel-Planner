from utils.travel_api import load_locations, get_matching_cities

class LocationAgent:
    """Suggests potential travel cities based on user preferences."""

    def suggest_locations(self, user_input):
        data = load_locations()
        matches = get_matching_cities(user_input, data)
        # Standardize output
        return [
            {
                "city": c["city"],
                "cost": c["base_cost_per_day"],
                "activities": c["tags"]
            }
            for c in matches
        ]