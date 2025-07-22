class ScheduleAgent:
    def create_schedule(self, locations, user_input):
        itinerary = {}
        days = user_input["duration"]
        if not locations:
            return {"Day 1": "No available locations within budget."}
        city = locations[0]["city"]
        for i in range(1, days + 1):
            itinerary[f"Day {i}"] = f"Explore {city}'s top museums and art galleries."
        return itinerary