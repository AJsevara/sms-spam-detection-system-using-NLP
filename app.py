import pickle
from win32com.client import Dispatch
import tkinter as tk

# Load the model and vectorizer
model = pickle.load(open('spam_model.pkl', 'rb'))
cv = pickle.load(open('vectorizer.pkl', 'rb'))

# Function to speak messages
def speak(text):
    speaker = Dispatch("SAPI.SpVoice")
    speaker.Speak(text)

# Function to predict spam/ham
def result():
    msg = text.get()
    data = [msg]
    vect = cv.transform(data).toarray()
    my_prediction = model.predict(vect)
    if my_prediction[0] == 1:
        speak("This is a Spam SMS")
        output_label.config(text="This is a Spam SMS", fg="red")
    else:
        speak("This is not a Spam SMS")
        output_label.config(text="This is not a Spam SMS", fg="green")

# Tkinter GUI
root = tk.Tk()
root.title("SMS Spam Detection")
root.geometry("400x300")

# App Title
l2 = tk.Label(root, text="SMS Spam Detection Application", font=("Arial", 16))
l2.pack(pady=10)

# Input Label
l1 = tk.Label(root, text="Enter Your SMS:", font=("Arial", 12))
l1.pack()

# Text Input Field
text = tk.Entry(root, width=50)
text.pack(pady=5)

# Classify Button
B = tk.Button(root, text="Classify", command=result, font=("Arial", 12), bg="blue", fg="white")
B.pack(pady=10)

# Output Label
output_label = tk.Label(root, text="", font=("Arial", 14))
output_label.pack(pady=10)

# Run the Application
root.mainloop()
