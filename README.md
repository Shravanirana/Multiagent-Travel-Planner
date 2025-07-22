# 🧳 Multi-Agent Travel Planner

This project is a multi-agent AI system that collaboratively plans a trip based on user preferences. Each agent has a specialized role — suggesting destinations, filtering by budget, and creating an itinerary.

## 👨‍💻 Agents Involved

- **Location Agent** – Suggests travel destinations.
- **Budget Agent** – Filters based on user budget.
- **Schedule Agent** – Builds a day-wise itinerary.

## 📦 Technologies Used

- Python
- LangChain (for agent framework)
- OpenAI API (for LLMs)
- JSON (for mock location data)

## 🚀 How to Run

```bash
git clone https://github.com/your-username/multiagent-travel-planner.git
cd multiagent-travel-planner
pip install -r requirements.txt
python main.py
```

## 📌 Example Use

> User: "Plan a 5-day Europe trip under $1500 focused on art and museums."

Agents collaborate to return:
- City options
- Estimated costs
- Daily itinerary

## ✨ Future Improvements

- Real-time flight/hotel search
- Weather-aware planning
- Group travel coordination