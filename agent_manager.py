from agents.location_agent import LocationAgent
from agents.budget_agent import BudgetAgent
from agents.schedule_agent import ScheduleAgent

def run_planner():
    user_input = {
        "budget": 1500,
        "duration": 5,
        "interest": "art and museums",
        "continent": "Europe"
    }

    loc_agent = LocationAgent()
    budget_agent = BudgetAgent()
    schedule_agent = ScheduleAgent()

    destinations = loc_agent.suggest_locations(user_input)
    filtered = budget_agent.filter(destinations, user_input)
    itinerary = schedule_agent.create_schedule(filtered, user_input)

    print("\n📍 Final Itinerary:\n")
    for day, plan in itinerary.items():
        print(f"{day}: {plan}")