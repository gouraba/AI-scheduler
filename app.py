from flask import Flask, render_template, jsonify, request
import json
from datetime import datetime

app = Flask(__name__)

# Load tasks from JSON
def load_tasks():
    with open('schedule.json', 'r') as file:
        data = json.load(file)
    return data['tasks']

# Prioritize tasks based on deadline and priority
def get_next_task():
    tasks = load_tasks()
    tasks.sort(key=lambda x: (x['priority'], datetime.strptime(x['deadline'], "%Y-%m-%d %H:%M")))
    return tasks[0] if tasks else None

# Homepage to show next task
@app.route('/')
def home():
    next_task = get_next_task()
    if next_task:
        return f"Next task: {next_task['task_name']} - Due by: {next_task['deadline']}"
    return "No tasks available."

# API to get all tasks
@app.route('/tasks', methods=['GET'])
def get_all_tasks():
    tasks = load_tasks()
    return jsonify(tasks)

# API to mark a task as completed
@app.route('/tasks/<task_name>/complete', methods=['POST'])
def complete_task(task_name):
    tasks = load_tasks()
    for task in tasks:
        if task['task_name'] == task_name:
            task['status'] = 'completed'
            break
    with open('schedule.json', 'w') as file:
        json.dump({"tasks": tasks}, file, indent=4)
    return jsonify({"message": f"Task '{task_name}' completed"})

if __name__ == "__main__":
    app.run(debug=True)
