class BudgetAgent:
    def filter(self, locations, user_input):
        budget = user_input["budget"]
        return [loc for loc in locations if loc["cost"] * user_input["duration"] <= budget]