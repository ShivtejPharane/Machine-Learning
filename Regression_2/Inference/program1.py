import numpy as np
import matplotlib.pyplot as plt
import pickle
with open('./model.pkl','rb') as file:
    model = pickle.load(file)

sat_score = float(input("Enter the SAT score: "))
print(type(sat_score))
gpa = model.predict([[sat_score]])
print(f"Predicted GPA: {gpa[0]:.2f}")