import datetime
import glob
import json
import os

from fastapi import FastAPI, Response
from pydantic import BaseModel, ValidationError, parse_obj_as

app = FastAPI()

activities_folder = "FAST_API/file_project/activities"
os.makedirs(activities_folder, exist_ok=True)


class Activity(BaseModel):
    id: int
    name: str
    date: datetime.datetime


def find_activity_by_id(activity_id=0):
    return glob.glob(os.path.join(activities_folder, f"*{activity_id if activity_id else ''}.json"))


@app.get("/activities/get/all")
def get_activities():
    files = find_activity_by_id()
    res = []
    if files:
        for file in files:
            try:
                with open(file, "r") as f:
                    activity_data = json.load(f)
                    activity_instance = Activity(**activity_data)
                    res.append(activity_instance)
            except (ValidationError, json.JSONDecodeError) as e:
                # Handle validation or JSON decoding errors
                print(f"Error processing file {file}: {e}")
    return res


@app.get("/activities/get/{activity_id}")
def get_activity(activity_id: int):
    files = find_activity_by_id(activity_id)
    if files:
        try:
            with open(files[0], "r") as f:
                activity_data = json.load(f)
                activity_instance = Activity(**activity_data)
                return activity_instance
        except (ValidationError, json.JSONDecodeError) as e:
            return {"error": f"Error processing activity {activity_id}: {e}"}
    else:
        return {"error": f"Activity {activity_id} not found"}


@app.post("/activities/add/{activity_id}")
def add_activity(activity_id: int, activity: Activity, response: Response):
    file = find_activity_by_id(activity_id)

    if file:
        response.status_code = 302  # Redirect status code
        return {"error": f"Activity {activity_id} already exists"}

    try:
        with open(os.path.join(activities_folder, f"activity_{activity_id}.json"), "w") as f:
            f.write(activity.json())
    except Exception as e:
        response.status_code = 500  # Internal server error
        return {"error": str(e)}

    return {"status": "ok"}

@app.put("/activities/update/{activity_id}")
def update_activity(activity_id: int, activity: Activity, response: Response):
    file = find_activity_by_id(activity_id)

    if not file:
        response.status_code = 302  # Redirect status code
        return {"error": f"Activity {activity_id} not found"}
    else:
        act = parse_obj_as(Activity, activity.dict())
        act.name = activity.name
        act.date = activity.date
        with open(os.path.join(activities_folder, f"activity_{activity_id}.json"), "w") as f:
            f.write(act.json())
        return {"status": "ok"}

@app.delete("/activities/delete/{activity_id}")
def delete_activity(activity_id: int, response: Response):
    file = find_activity_by_id(activity_id)

    if not file:
        response.status_code = 302  # Redirect status code
        return {"error": f"Activity {activity_id} not found"}
    else:
        os.remove(file[0])
        return {"status": "ok"}
