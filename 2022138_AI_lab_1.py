import tkinter as tk
from tkinter import *
from tkinter import ttk
import pandas as pd

def fetch_input():
    user_input = condition_entry.get()
    user_input = user_input.lower()
    return user_input

def display_selected_rating(value):
    rating_display.config(text=f"Chosen Minimum Rating: {value}")
    return value

# GUI Setup
app = tk.Tk()
app.geometry('800x550')
app.title('Pharmaceutical Search Tool')

# Header
Label(app, text='Welcome to the Pharmaceutical Search Tool').place(relx=0.5, rely=0.05, anchor='center')

# Condition Input
Label(app, text='Enter the Medical Condition').place(relx=0.01, rely=0.1)
condition_entry = Entry(app)
condition_entry.place(relx=0.2, rely=0.1)

# Rating Label
rating_display = tk.Label(app, text="Chosen Minimum Rating: 5")
rating_display.place(relx=0.4, rely=0.1)

# Slider for rating selection
rating_slider = tk.Scale(
    app,
    from_=0,
    to=10,
    orient="horizontal",
    length=300,
    tickinterval=1,
    command=display_selected_rating
)
rating_slider.set(5)
rating_slider.place(relx=0.6, rely=0.06)

def filter_drugs():
    drug_data = pd.read_csv('drug1.csv')
    df = pd.DataFrame(drug_data)
    df['condition'] = df['condition'].str.lower()

    filtered_drugs = df[(df['condition'] == fetch_input()) & (df['rating'] >= rating_slider.get())]
    filtered_drugs = filtered_drugs.head(5)
    
    result_area = tk.Text(app, wrap='word')
    result_area.place(relx=0.1, rely=0.25)
    result_area.tag_configure("bold", font=("Helvetica", 10, "bold"))

    for index, row in filtered_drugs.iterrows():
        result_area.insert('end', "Drug Name:", "bold")
        result_area.insert('end', f"{row['drugName']}\n")
        result_area.insert('end', "Review:", "bold")
        result_area.insert('end', f"{row['review']}\n")
        result_area.insert('end', "Rating:", "bold")
        result_area.insert('end', f"{row['rating']}\n\n")

# Search Button
Button(app, text='Filter Drugs', width=25, command=filter_drugs).place(relx=0.4, rely=0.19, anchor='center')

app.mainloop()
