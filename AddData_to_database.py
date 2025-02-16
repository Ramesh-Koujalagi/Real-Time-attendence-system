import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate("service_account_key.json")#generate your service account key
firebase_admin.initialize_app(cred,{
    'databaseURL': "your data base url should be pasted here ....."
    
})
ref=db.reference('Students')

data={
"1122": # in order to mark the attendace of the person, image name should be 321654.png same goes for all.
        {
            "name":"RAMESH KOUJALAGI",
            "major": "Computer science and design",
            "starting_year": 2024,
            "total_attendance": 0,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2024-11-12 00:44:60"
        },
"2233":
        {
            "name": "Deepika Padukone",
            "major": "Acting",
            "starting_year": 2018,
            "total_attendance": 0,
            "standing": "B",
            "year": 4,
            "last_attendance_time": "2024-11-12 00:44:60"
        },
"3344":
    {
        "name": "Hrithik Roshan",
        "major": "Acting",
        "starting_year": 2018,
        "total_attendance": 0,
        "standing": "B",
        "year": 3,
        "last_attendance_time": "2024-11-12 00:44:60"
    },
"4455":
    {
        "name": "Tamanah Bhatia",
        "major": "facebook",
        "starting_year": 2018,
        "total_attendance": 0,
        "standing": "B",
        "year": 1,
        "last_attendance_time": "2024-11-12 00:44:60"
    },
    
    

}

for key,value in data.items():
    ref.child(key).set(value)