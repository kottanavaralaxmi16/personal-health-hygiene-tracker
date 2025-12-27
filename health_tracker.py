import os
import pandas as pd

def collect_data():
    water = float(input("Enter water intake (liters): "))
    sleep = float(input("Enter sleep hours: "))
    exercise = int(input("Enter exercise minutes: "))
    handwash = int(input("Enter handwash count: "))

    data = {
        "Water_Liters": [water],
        "Sleep_Hours": [sleep],
        "Exercise_Minutes": [exercise],
        "Handwash_Count": [handwash]
    }

    df = pd.DataFrame(data)
    df.to_csv("data.csv", mode='a', header=not os.path.exists("data.csv"), index=False)
    print("Data saved successfully!")

if __name__ == "__main__":
    collect_data()
