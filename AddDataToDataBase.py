import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://YOUR_DATABASE.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "1222343":
        {
            "name":"Narendra Modi",
            "major":"Robotics",
            "starting_year":2021,
            "total_attendance":6,
            "standing":"G",
            "year":4,
            "last_attendance_time":"2025-01-8 00:54:34"
        },
    "852741":
        {
            "name":"Emly Blunt",
            "major":"Economics",
            "starting_year":2024,
            "total_attendance":5,
            "standing":"B",
            "year":1,
            "last_attendance_time":"2025-01-8 00:54:34"
        },
    "963852":
        {
            "name":"Elon Musk",
            "major":"Physics",
            "starting_year":2023,
            "total_attendance":6,
            "standing":"G",
            "year":2,
            "last_attendance_time":"2025-01-8 00:54:34"
        },
        "1234562":
        {
            "name":"Donald Trump",
            "major":"Physics",
            "starting_year":2023,
            "total_attendance":6,
            "standing":"G",
            "year":2,
            "last_attendance_time":"2025-01-8 00:54:34"
        }
}

for key,value in data.items():
    ref.child(key).set(value)

