import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

pd.set_option("display.max_rows", None)
pd.set_option("display.min_rows", None)
pd.set_option('display.max_colwidth', None)


df = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")

print(df.columns)


idris_columns = ["Person ID", "Gender", "Age", "Occupation", "Sleep Duration", "Quality of Sleep"]
df.drop(columns=idris_columns, inplace=True)


#üstünde calısacaklarım

"""""
Physical Activity Level (minutes/day): The number of minutes the person engages in physical activity daily.
Stress Level (scale: 1-10): A subjective rating of the stress level experienced by the person, ranging from 1 to 10.
BMI Category: The BMI category of the person (e.g., Underweight, Normal, Overweight).
Blood Pressure (systolic/diastolic): The blood pressure measurement of the person, indicated as systolic pressure over diastolic pressure.
Heart Rate (bpm): The resting heart rate of the person in beats per minute.
Daily Steps: The number of steps the person takes per day.
Sleep Disorder: The presence or absence of a sleep disorder in the person (None, Insomnia, Sleep Apnea).

"""""


print(df.columns)


print(df.isnull().sum())


df.dropna(subset=['Sleep Disorder'], inplace=True)


#219 eksik Sleep Disorder vardı attım,kalanlar eksiksizdi.


print(df.isnull().sum())


df[['Systolic BP', 'Diastolic BP']] = df['Blood Pressure'].str.split('/', expand=True)


df['Systolic BP'] = pd.to_numeric(df['Systolic BP'], errors='coerce')
df['Diastolic BP'] = pd.to_numeric(df['Diastolic BP'], errors='coerce')


df.drop(columns=['Blood Pressure'], inplace=True)


print(df.head())
print(df.columns)











