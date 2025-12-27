import pandas as pd

df = pd.read_csv("data.csv")

print("Average Health Statistics:")
print(df.mean())

def suggestions(row):
    tips = []
    if row['Water_Liters'] < 2.5:
        tips.append("Increase water intake")
    if row['Sleep_Hours'] < 7:
        tips.append("Improve sleep duration")
    if row['Exercise_Minutes'] < 30:
        tips.append("Increase daily exercise")
    if row['Handwash_Count'] < 6:
        tips.append("Wash hands more frequently")
    return tips

df['Suggestions'] = df.apply(suggestions, axis=1)
print(df)
