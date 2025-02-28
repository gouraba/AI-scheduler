import json
import os

def get_user_schedule():
    print("\nYour college schedule is pre-set. Additional tasks will be added based on priority.")
    schedule = {
        "Monday": [
            {"task": "Wake Up", "time": "07:00", "status": "fixed"},
            {"task": "PHY114", "time": "09:00", "status": "fixed"},
            {"task": "MTH114", "time": "10:00", "status": "fixed"},
            {"task": "ESC Self-Study", "time": "11:00", "status": "pending"},
            {"task": "Lunch", "time": "12:30", "status": "fixed"},
            {"task": "MTH Self-Study", "time": "14:00", "status": "pending"},
            {"task": "PHY Self-Study", "time": "16:00", "status": "pending"},
            {"task": "Stock Market Analysis", "time": "17:30", "status": "pending"},
            {"task": "AI Learning", "time": "18:30", "status": "pending"},
            {"task": "Dinner", "time": "19:30", "status": "fixed"},
            {"task": "LIF Self-Study", "time": "20:30", "status": "pending"},
            {"task": "Reading Books", "time": "22:00", "status": "pending"},
            {"task": "Sleep", "time": "00:00", "status": "fixed"}
        ],
        "Tuesday": [
            {"task": "Wake Up", "time": "07:00", "status": "fixed"},
            {"task": "PHY114", "time": "09:00", "status": "fixed"},
            {"task": "MTH114", "time": "10:00", "status": "fixed"},
            {"task": "LIF Lecture", "time": "11:00", "status": "fixed"},
            {"task": "Lunch", "time": "12:30", "status": "fixed"},
            {"task": "CHM111 Practical", "time": "14:00", "status": "fixed"},
            {"task": "Stock Market Analysis", "time": "17:00", "status": "pending"},
            {"task": "AI Learning", "time": "18:00", "status": "pending"},
            {"task": "Dinner", "time": "19:30", "status": "fixed"},
            {"task": "LIF Self-Study", "time": "20:30", "status": "pending"},
            {"task": "Reading Books", "time": "22:00", "status": "pending"},
            {"task": "Sleep", "time": "00:00", "status": "fixed"}
        ],
        "Wednesday": [
            {"task": "Wake Up", "time": "07:00", "status": "fixed"},
            {"task": "MTH114", "time": "10:00", "status": "fixed"},
            {"task": "Lunch", "time": "12:30", "status": "fixed"},
            {"task": "ESC Self-Study", "time": "14:00", "status": "pending"},
            {"task": "Stock Market Analysis", "time": "16:00", "status": "pending"},
            {"task": "AI Learning", "time": "17:30", "status": "pending"},
            {"task": "Dinner", "time": "19:30", "status": "fixed"},
            {"task": "Reading Books", "time": "22:00", "status": "pending"},
            {"task": "Sleep", "time": "00:00", "status": "fixed"}
        ],
        "Thursday": [
            {"task": "Wake Up", "time": "07:00", "status": "fixed"},
            {"task": "PHY114 Tutorial", "time": "09:00", "status": "fixed"},
            {"task": "ETH111", "time": "10:00", "status": "fixed"},
            {"task": "Lunch", "time": "12:30", "status": "fixed"},
            {"task": "Self-Study", "time": "14:00", "status": "pending"},
            {"task": "Stock Market Analysis", "time": "16:00", "status": "pending"},
            {"task": "Dinner", "time": "19:30", "status": "fixed"},
            {"task": "Reading Books", "time": "22:00", "status": "pending"},
            {"task": "Sleep", "time": "00:00", "status": "fixed"}
        ],
        "Friday": [
            {"task": "Wake Up", "time": "07:00", "status": "fixed"},
            {"task": "ESC112 Lab", "time": "14:00", "status": "fixed"},
            {"task": "Dinner", "time": "19:30", "status": "fixed"},
            {"task": "Self-Study", "time": "16:00", "status": "pending"},
            {"task": "Reading Books", "time": "22:00", "status": "pending"},
            {"task": "Sleep", "time": "00:00", "status": "fixed"}
        ],
        "Saturday": [
            {"task": "Wake Up", "time": "07:00", "status": "fixed"},
            {"task": "Self-Study", "time": "10:00", "status": "pending"},
            {"task": "Lunch", "time": "12:30", "status": "fixed"},
            {"task": "Self-Study", "time": "14:00", "status": "pending"},
            {"task": "Stock Market Analysis", "time": "16:00", "status": "pending"},
            {"task": "Dinner", "time": "19:30", "status": "fixed"},
            {"task": "Reading Books", "time": "22:00", "status": "pending"},
            {"task": "Sleep", "time": "00:00", "status": "fixed"}
        ]
    }
    return schedule

def main():
    schedule = get_user_schedule()
    with open("tasks.json", "w") as file:
        json.dump(schedule, file, indent=4)
    print("\n✅ Schedule saved successfully!")

if __name__ == "__main__":
    main()
