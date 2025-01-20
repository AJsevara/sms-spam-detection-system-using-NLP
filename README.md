# **SMS Spam Detection System**

### **Overview**

This project is an **SMS Spam Detection System** built using **Natural Language Processing (NLP)** and **Machine Learning**. It uses a **Naive Bayes classifier** to classify incoming SMS messages as either **spam** or **ham** (non-spam). With the help of **CountVectorizer**, the system transforms text into numerical vectors for model training. The system also includes a **GUI** built with **Tkinter** to easily test and classify SMS messages.

---

### **Key Features**

- **Machine Learning Powered:** Utilizes a trained **Multinomial Naive Bayes** model to classify SMS messages.
- **Speech Feedback:** The application provides audible feedback using **SAPI.SpVoice** to inform whether the SMS is spam or not.
- **Simple and Interactive GUI:** Built with **Tkinter**, the user-friendly interface allows you to input and classify messages.
- **Real-time Classification:** Classifies your SMS message instantly, providing feedback directly in the app.
- **Model Persistence:** The trained model and vectorizer are saved using **Pickle** for quick reloading.

---

### **Technologies Used**

- **Python** – The programming language used for implementing the entire system.
- **Tkinter** – Used to create the GUI interface.
- **scikit-learn** – Used for implementing machine learning algorithms (Naive Bayes Classifier, CountVectorizer).
- **Pickle** – Used for saving and loading the trained model and vectorizer.
- **win32com.client** – For converting the classification result into voice using the **SAPI.SpVoice** API.
- **Natural Language Processing (NLP)** – For text vectorization and spam classification.

---

### **Installation Instructions**

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/sms-spam-detection.git
   ```

2. **Install Dependencies**
   - You can install the required libraries using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download or Train the Model**
   - If you already have the trained model (`spam_model.pkl`) and vectorizer (`vectorizer.pkl`), place them in the project directory.
   - Otherwise, run the training script (`train_model.ipynb`) to train the model.

4. **Run the Application**
   - After setting up the environment, run the main application:
   ```bash
   python app.py
   ```

---

### **Usage**

1. **Launch the App:**
   - The Tkinter GUI will open, displaying the input area and a "Classify" button.

2. **Input SMS:**
   - Enter an SMS message in the input field.

3. **Classify the Message:**
   - Press the **Classify** button, and the model will classify the message as **Spam** or **Not Spam**.
   - The result will be displayed in the app and announced via voice.

---

### **Example SMS Messages for Testing**

- **Spam Example:**
  - "Congratulations! You’ve won a $1,000 gift card! Click here to claim: http://fake-link.com"
  - "Hurry! Limited-time offer. Get 50% off on all items. Visit http://fakeshop.com now!"

- **Ham (Non-Spam) Example:**
  - "Hey, are we still meeting at 3 PM today?"
  - "Just wanted to check in on the project status. Let me know!"

---



### **Future Improvements**

- **Multi-Language Support:** Extend the system to handle SMS messages in different languages.
- **Real-time SMS Classification:** Integrate the system with SMS services for real-time spam detection.
- **Deep Learning Models:** Experiment with more advanced models (e.g., LSTM or BERT) to improve classification performance.

