import sys
import os
import random

import requests

import pyttsx3
import pyaudio
from datetime import datetime
import json
import multiprocessing

from uvicorn import Config , Server
from PyQt5.QtWidgets import (
    QApplication, QLabel, QVBoxLayout, QLineEdit, QPushButton, QSizePolicy, QSpacerItem, QFrame, QWidget, QMessageBox,
    QTextEdit, QDialog, QHBoxLayout, QScrollArea
)
from PyQt5.QtGui import QPixmap, QPalette, QBrush
from PyQt5.QtCore import Qt, QTimer
from astropy.units import sr
#from fastapi import requests
from firebase_admin import credentials, initialize_app, firestore
from PyQt5.QtGui import QIcon
import speech_recognition as sr

import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate(r"D:/Vishnu files/LawSmartt/proj11-83ce6-firebase-adminsdk-1loxr-feb65809b7.json")
firebase_admin.initialize_app(cred)

import pyttsx3



# Base Window Class
class BaseWindow(QWidget):


    def __init__(self):
        super().__init__()
        self.setMinimumSize(900, 800)
        self.set_background_image()
        #self.setStyleSheet("background-color: #4C566A;")



    def set_background_image(self):
        background_image = QPixmap(r"D:/Vishnu files/LawSmartt/new image.jpg")
        scaled_image = background_image.scaled(self.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(scaled_image))
        self.setPalette(palette)



    def resizeEvent(self, event):
        self.set_background_image()
        super().resizeEvent(event)



    # Attendance Application
class AttendanceApp(BaseWindow):
    def __init__(self):
        super().__init__()
        self.root_layout = QVBoxLayout(self)
        self.setLayout(self.root_layout)
        self.home_page()  # Show the home page initially

    def clear_frame(self):
        # Clears all widgets in the root layout
        while self.root_layout.count():
            child = self.root_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    import pyttsx3
    from PyQt5.QtCore import QTimer

    def home_page(self):
        self.clear_frame()

        # Create a main frame for the home page
        frame = QFrame(self)
        frame.setStyleSheet("""
            background: rgba(30, 30, 47, 0.5); /* Deep blue-grey with slight transparency */
            border-radius: 20px;
            box-shadow: 8px 8px 20px rgba(0, 0, 0, 0.3), 
                        -8px -8px 20px rgba(255, 255, 255, 0.05);
        """)
        frame.setFixedSize(800, 700)

        # Layout for the frame
        layout = QVBoxLayout(frame)
        layout.setContentsMargins(40, 50, 40, 50)
        layout.setSpacing(20)

        # Top Spacer
        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Main Title
        title_label = QLabel("Welcome to LawSmart", frame)
        title_label.setStyleSheet("""
            color: #FFFFFF;  /* Brighter White */
            font: bold 40px 'Poppins';  /* Increased Font Size */
            background: transparent;
            letter-spacing: 2px;
            text-shadow: 2px 2px 10px rgba(0, 0, 0, 0.5); /* Soft Shadow for Visibility */
        """)
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        # Subtitle
        subtitle_label = QLabel("Your AI-Powered Legal Assistant", frame)
        subtitle_label.setStyleSheet("""
            color: #FFD700; /* Gold Color for High Contrast */
            font: bold italic 28px 'Poppins'; /* Increased Font Size */
            background: transparent;
            text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.4); /* Subtle Shadow */
        """)
        subtitle_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(subtitle_label)

        # Spacer to separate the button from the text
        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Enter Button
        enter_button = QPushButton("ENTER", frame)
        enter_button.setFixedSize(140, 45)
        enter_button.setStyleSheet("""
            QPushButton {
                background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, 
                                            stop:0 #2D9CDB, stop:1 #1A75FF); 
                color: #FFFFFF;
                border-radius: 10px;
                font: bold 16px 'Segoe UI';
                padding: 10px;
                box-shadow: 4px 4px 12px rgba(0, 0, 0, 0.3);
            }
            QPushButton:hover {
                background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, 
                                            stop:0 #1A75FF, stop:1 #2D9CDB); 
            }
            QPushButton:pressed {
                background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, 
                                            stop:0 #1A5DBD, stop:1 #1756A9); 
            }
        """)
        enter_button.clicked.connect(self.login_page)
        layout.addWidget(enter_button, alignment=Qt.AlignCenter)

        # Add the frame to the root layout
        self.root_layout.addWidget(frame, alignment=Qt.AlignCenter)

        #  Speak "Welcome to Legal AI Assistant" after 1 second
        QTimer.singleShot(1000, lambda: self.speak_welcome_message())

    def speak_welcome_message(self):
        """Speaks the welcome message when the home page loads."""
        try:
            engine = pyttsx3.init()
            engine.setProperty("rate", 150)  # Adjust speech speed (default ~200)
            engine.setProperty("volume", 1.0)  # Set volume (1.0 = max)

            # Speak the welcome message
            engine.say("Welcome to Legal AI Assistant")
            engine.runAndWait()
        except Exception as e:
            print(f"Error with text-to-speech: {e}")


    import random  # Import random module at the top of your script

    import random
    import pyttsx3  # Import text-to-speech module

    import random
    import pyttsx3
    from PyQt5.QtCore import QTimer

    import random
    import pyttsx3
    from PyQt5.QtCore import QTimer

    def login_page(self):
        self.clear_frame()

        # List of 10 Legal Quotes
        quotes = [
            "\"Knowledge of the law is the first step toward justice.\" — Edward Coke",
            "\"Laws grind the poor, and rich men rule the law.\" — Oliver Goldsmith",
            "\"Justice delayed is justice denied.\" — William E. Gladstone",
            "\"The law is reason, free from passion.\" — Aristotle",
            "\"An unjust law is no law at all.\" — Saint Augustine",
            "\"Ignorance of the law excuses no one.\" — Legal Maxim",
            "\"Where there is no law, there is no liberty.\" — John Locke",
            "\"The safety of the people shall be the highest law.\" — Cicero",
            "\"No man is above the law, and no man is below it.\" — Theodore Roosevelt",
            "\"Equal justice under law.\" — U.S. Supreme Court Motto"
        ]

        # Select a random quote
        self.random_quote = random.choice(quotes)

        # Login frame
        frame = QFrame()
        frame.setStyleSheet("""
            background: rgba(30, 30, 47, 0.5); 
            border-radius: 20px;
            box-shadow: 8px 8px 20px rgba(0, 0, 0, 0.3), 
                        -8px -8px 20px rgba(255, 255, 255, 0.05);
        """)
        frame.setFixedSize(800, 700)

        # Form layout for login
        form_layout = QVBoxLayout(frame)
        form_layout.setContentsMargins(40, 50, 40, 50)
        form_layout.setSpacing(25)

        # Title label
        title_label = QLabel("Log into your Account", frame)
        title_label.setStyleSheet("color: #FFFFFF; font: bold 26px 'Segoe UI'; background: transparent;")
        title_label.setAlignment(Qt.AlignCenter)
        form_layout.addWidget(title_label)

        # Spacer before quote
        form_layout.addItem(QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed))

        # Quote Label (Random Quote)
        quote_label = QLabel(self.random_quote, frame)
        quote_label.setStyleSheet("""
            color: #FFD700;  
            font: italic bold 18px 'Segoe UI';
            background: transparent;
            text-align: center;
            padding: 5px;
        """)
        quote_label.setAlignment(Qt.AlignCenter)
        form_layout.addWidget(quote_label)

        # Spacer after quote to maintain clean UI
        form_layout.addItem(QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed))
        # Username Entry
        self.username_entry = QLineEdit(frame)
        self.username_entry.setPlaceholderText("Username")
        self.username_entry.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.2);
            color: #FFFFFF;
            font: bold 16px 'Montserrat';
            padding: 12px;
            border-radius: 15px;
            border: 2px solid rgba(255, 255, 255, 0.6);
            text-transform: none;
        """)
        self.username_entry.setFixedHeight(50)
        self.username_entry.setAlignment(Qt.AlignCenter)
        self.username_entry.setInputMethodHints(Qt.ImhNoAutoUppercase | Qt.ImhPreferLowercase)
        form_layout.addWidget(self.username_entry)

        # Password Entry
        self.password_entry = QLineEdit(frame)
        self.password_entry.setPlaceholderText("Password")
        self.password_entry.setEchoMode(QLineEdit.Password)
        self.password_entry.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.2);
            color: #FFFFFF;
            font: bold 16px 'Montserrat';
            padding: 12px;
            border-radius: 15px;
            border: 2px solid rgba(255, 255, 255, 0.6);
            text-transform: none;
        """)
        self.password_entry.setFixedHeight(50)
        self.password_entry.setAlignment(Qt.AlignCenter)
        self.password_entry.setInputMethodHints(Qt.ImhNoAutoUppercase | Qt.ImhPreferLowercase)
        form_layout.addWidget(self.password_entry)

        # Spacer between password and login button
        form_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Login button
        login_button = QPushButton("Login", frame)
        login_button.setFixedSize(120, 40)
        login_button.setStyleSheet("""
            QPushButton {
                background-color: #FF6B6B;
                color: #FFFFFF;
                border-radius: 10px;
                font: bold 16px 'Segoe UI';
                padding: 8px;
                transition: all 0.3s ease-in-out;
            }
            QPushButton:hover {
                background-color: #FF8E8E;
            }
            QPushButton:pressed {
                background-color: #E63946;
            }
        """)
        login_button.clicked.connect(self.validate_login)
        form_layout.addWidget(login_button, alignment=Qt.AlignCenter)

        # Back button
        back_button = QPushButton("Back", frame)
        back_button.setFixedSize(120, 40)
        back_button.setStyleSheet("""
            QPushButton {
                background-color: #48CAE4;
                color: #FFFFFF;
                border-radius: 10px;
                font: bold 16px 'Segoe UI';
                padding: 8px;
                transition: all 0.3s ease-in-out;
            }
            QPushButton:hover {
                background-color: #4ECDC4;
            }
            QPushButton:pressed {
                background-color: #0096C7;
            }
        """)
        back_button.clicked.connect(self.home_page)
        form_layout.addWidget(back_button, alignment=Qt.AlignCenter)

        self.root_layout.addWidget(frame, alignment=Qt.AlignCenter)

        # 🔥 Speak the quote **AFTER** the UI has loaded (1-second delay)
        QTimer.singleShot(1000, lambda: self.speak_quote(self.random_quote))

    def speak_quote(self, text):
        """Speaks the given text using pyttsx3 after the page loads."""
        try:
            engine = pyttsx3.init()
            engine.setProperty("rate", 150)  # Adjust speech speed (default ~200)
            engine.setProperty("volume", 1.0)  # Set volume (1.0 = max)

            # Speak the text
            engine.say(text)
            engine.runAndWait()
        except Exception as e:
            print(f"Error with text-to-speech: {e}")

    def validate_login(self):
        username = self.username_entry.text().strip()
        password = self.password_entry.text().strip()

        # Firestore client
        db = firestore.client()

        try:
            # Access the document in the Firestore collection
            doc_ref = db.collection("a").document("admin")
            doc = doc_ref.get()
            if doc.exists:
                stored_password = doc.to_dict().get("password", "")
                if username == "admin" and password == stored_password:
                    QMessageBox.information(self, "Login Successful", "Welcome, Admin!")
                    self.language_selection_page()
                else:
                    QMessageBox.warning(self, "Login Failed", "Invalid username or password.")
            else:
                QMessageBox.critical(self, "Error", "No admin credentials found in the database.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")

    def language_selection_page(self):
        self.clear_frame()

        # Create the frame for the language selection page
        frame = QFrame(self)
        frame.setStyleSheet("""
            background: rgba(30, 30, 47, 0.5);
            border-radius: 20px;
            box-shadow: 8px 8px 20px rgba(0, 0, 0, 0.3), 
                        -8px -8px 20px rgba(255, 255, 255, 0.05);
        """)
        frame.setFixedSize(600, 500)

        layout = QVBoxLayout(frame)
        layout.setContentsMargins(40, 50, 40, 50)
        layout.setSpacing(30)

        # Title
        title_label = QLabel("Choose Your Language", frame)
        title_label.setStyleSheet("""
            color: #FFFFFF;
            font: bold 30px 'Segoe UI';
            background: transparent;
        """)
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        # Language Buttons with Different Colors
        languages = {
            "English": ("en-US", "#6A5ACD", "#836FFF", "#483D8B"),  # Purple gradient
            "Tamil": ("ta-IN", "#FF6B6B", "#FF8E8E", "#E63946"),    # Red gradient
            "Telugu": ("te-IN", "#FFD700", "#FFC107", "#FFA000")   # Gold gradient
        }

        for lang, (code, color1, color2, color3) in languages.items():
            button = QPushButton(lang, frame)
            button.setFixedSize(250, 60)
            button.setStyleSheet(f"""
                QPushButton {{
                    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, 
                                                stop:0 {color1}, stop:1 {color2}); 
                    color: #FFFFFF;
                    border-radius: 10px;
                    font: bold 20px 'Segoe UI';
                    padding: 10px;
                }}
                QPushButton:hover {{
                    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, 
                                                stop:0 {color2}, stop:1 {color1});
                }}
                QPushButton:pressed {{
                    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, 
                                                stop:0 {color3}, stop:1 {color1});
                }}
            """)
            button.clicked.connect(lambda checked, c=code: self.set_language_and_proceed(c))
            layout.addWidget(button, alignment=Qt.AlignCenter)

        # Back Button
        back_button = QPushButton("Back", frame)
        back_button.setFixedSize(120, 40)
        back_button.setStyleSheet("""
            QPushButton {
                background-color: #48CAE4;
                color: #FFFFFF;
                border-radius: 10px;
                font: bold 16px 'Segoe UI';
                padding: 8px;
                transition: all 0.3s ease-in-out;
            }
            QPushButton:hover {
                background-color: #4ECDC4;
            }
            QPushButton:pressed {
                background-color: #0096C7;
            }
        """)
        back_button.clicked.connect(self.home_page)  # Navigate back to home page
        layout.addWidget(back_button, alignment=Qt.AlignCenter)

        # Add the frame to the root layout
        self.root_layout.addWidget(frame, alignment=Qt.AlignCenter)

    def set_language_and_proceed(self, language_code):
        self.selected_language = language_code  # Store the selected language
        self.show_chatbot_page()

    def start_voice_recognition(self):
        try:
            recognizer = sr.Recognizer()
            with sr.Microphone() as source:
                # Notify the user that the app is listening
                self.chatbox_display.setText("Listening...")
                QApplication.processEvents()  # Prevents UI freeze

                # Adjust for ambient noise and listen to the user's input
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=5)

                # Recognize speech using Google Web Speech API with selected language
                recognized_text = recognizer.recognize_google(audio, language=self.selected_language)

                # Display the recognized text in the chatbox
                self.chatbox_display.setText(recognized_text)
        except sr.UnknownValueError:
            self.chatbox_display.setText("Sorry, I didn't catch that.")
        except sr.RequestError as e:
            self.chatbox_display.setText(f"Voice recognition error: {e}")
        except sr.WaitTimeoutError:
            self.chatbox_display.setText("Listening timed out. Please try again.")
        except Exception as e:
            self.chatbox_display.setText(f"An error occurred: {e}")



    def show_chatbot_page(self):
        self.clear_frame()

        # Create the frame for the chatbot page
        frame = QFrame(self)
        frame.setStyleSheet("""
            background: rgba(30, 30, 47, 0.5); /* Deep blue-grey with slight transparency */
            border-radius: 20px;
            box-shadow: 8px 8px 20px rgba(0, 0, 0, 0.3), 
                        -8px -8px 20px rgba(255, 255, 255, 0.05);
        """)
        frame.setFixedSize(800, 700)

        layout = QVBoxLayout(frame)
        layout.setContentsMargins(40, 50, 40, 50)
        layout.setSpacing(20)

        # Title
        chatbot_title = QLabel("AI-powered Legal Assistant", frame)
        chatbot_title.setStyleSheet(
            "color: #ECEFF4; font: bold 24px 'Segoe UI'; background: transparent;")
        chatbot_title.setAlignment(Qt.AlignCenter)
        layout.addWidget(chatbot_title)

        # Chatbox
        self.chatbox_display = QTextEdit(frame)
        self.chatbox_display.setPlaceholderText("Type your question here...")
        self.chatbox_display.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.7);
            color: #1A1A1A;
            font: 18px 'Segoe UI'; 
            padding: 12px;
            border-radius: 15px;
            box-shadow: 6px 6px 15px rgba(0, 0, 0, 0.2),
                        -6px -6px 15px rgba(255, 255, 255, 0.9);
        """)
        self.chatbox_display.setFixedHeight(100)
        layout.addWidget(self.chatbox_display)

        layout.addSpacing(20)

        # Voice button
        voice_button = QPushButton(frame)
        voice_icon = QIcon(r"D:/Vishnu files/LawSmartt/voice-search.png")
        voice_button.setIcon(voice_icon)
        voice_button.setFixedSize(40, 40)
        voice_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 255, 255, 0.6);
                border: none;
                border-radius: 20px;
            }
            QPushButton:hover {
                background-color: rgba(200, 200, 200, 0.7);
            }
        """)
        voice_button.clicked.connect(self.start_voice_recognition)
        layout.addWidget(voice_button, alignment=Qt.AlignHCenter)

        # Button Layout (Side by Side)
        button_layout = QHBoxLayout()


        # Ask Button
        ask_button = QPushButton("Ask", frame)
        ask_button.setFixedSize(140, 45)
        ask_button.setStyleSheet("""
            QPushButton {
                background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, 
                                            stop:0 rgba(255, 183, 77, 0.9), 
                                            stop:1 rgba(255, 152, 0, 0.9));
                color: white;
                border-radius: 15px;
                font: bold 18px 'Segoe UI';
                padding: 10px;
                box-shadow: 6px 6px 15px rgba(0, 0, 0, 0.2), 
                            -6px -6px 15px rgba(255, 255, 255, 0.1);
                transition: all 0.3s ease-in-out;
            }
            QPushButton:hover {
                background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, 
                                            stop:0 rgba(255, 167, 38, 1.0), 
                                            stop:1 rgba(255, 111, 0, 1.0));
                box-shadow: 8px 8px 18px rgba(0, 0, 0, 0.25), 
                            -8px -8px 18px rgba(255, 255, 255, 0.2);
            }
            QPushButton:pressed {
                background: rgba(255, 152, 0, 0.8);
                box-shadow: inset 4px 4px 10px rgba(0, 0, 0, 0.3), 
                            inset -4px -4px 10px rgba(255, 255, 255, 0.1);
            }
        """)
        ask_button.clicked.connect(self.process_chatbot_question)
        button_layout.addWidget(ask_button)

        # History Button
        history_button = QPushButton("History", frame)
        history_button.setFixedSize(140, 45)
        history_button.setStyleSheet("""
            QPushButton {
                background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, 
                                            stop:0 rgba(72, 202, 228, 0.9), 
                                            stop:1 rgba(0, 150, 199, 0.9));
                color: white;
                border-radius: 15px;
                font: bold 18px 'Segoe UI';
                padding: 10px;
                box-shadow: 6px 6px 15px rgba(0, 0, 0, 0.2), 
                            -6px -6px 15px rgba(255, 255, 255, 0.1);
                transition: all 0.3s ease-in-out;
            }
            QPushButton:hover {
                background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, 
                                            stop:0 rgba(62, 190, 216, 1.0), 
                                            stop:1 rgba(0, 125, 175, 1.0));
                box-shadow: 8px 8px 18px rgba(0, 0, 0, 0.25), 
                            -8px -8px 18px rgba(255, 255, 255, 0.2);
            }
            QPushButton:pressed {
                background: rgba(0, 150, 199, 0.8);
                box-shadow: inset 4px 4px 10px rgba(0, 0, 0, 0.3), 
                            inset -4px -4px 10px rgba(255, 255, 255, 0.1);
            }
        """)
        history_button.clicked.connect(self.show_chat_history)
        button_layout.addWidget(history_button)

        # Add Button Layout to Main Layout
        layout.addLayout(button_layout)

        # Back button
        back_button = QPushButton("Back", frame)
        back_button.setFixedSize(120, 40)
        back_button.setStyleSheet("""
            QPushButton {
                background-color: #48CAE4;
                color: #FFFFFF;
                border-radius: 10px;
                font: bold 16px 'Segoe UI';
                padding: 8px;
                transition: all 0.3s ease-in-out;
            }
            QPushButton:hover {
                background-color: #4ECDC4;
            }
            QPushButton:pressed {
                background-color: #0096C7;
            }
        """)
        back_button.clicked.connect(self.language_selection_page)
        layout.addWidget(back_button, alignment=Qt.AlignCenter)

        self.root_layout.addWidget(frame, alignment=Qt.AlignCenter)

    from PyQt5.QtWidgets import QMessageBox
    '''TO REMOVE HISTORY '''
    #if os.path.exists("chat_history.json"):
        #os.remove("chat_history.json")
        #print("Corrupt chat_history.json deleted. A new file will be created.")

    def show_chat_history(self):
        self.clear_frame()

        frame = QFrame(self)
        frame.setStyleSheet("""
            background: rgba(30, 30, 47, 0.5);
            border-radius: 20px;
            box-shadow: 8px 8px 20px rgba(0, 0, 0, 0.3), 
                        -8px -8px 20px rgba(255, 255, 255, 0.05);
        """)
        frame.setFixedSize(800, 700)

        layout = QVBoxLayout(frame)
        layout.setContentsMargins(40, 50, 40, 50)
        layout.setSpacing(20)

        # Title
        history_title = QLabel("Chat History", frame)
        history_title.setStyleSheet("color: #ECEFF4; font: bold 24px 'Segoe UI'; background: transparent;")
        history_title.setAlignment(Qt.AlignCenter)
        layout.addWidget(history_title)

        # Scrollable Area
        scroll_area = QScrollArea(frame)
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("border: none;")

        # Scroll Area Container
        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout(scroll_widget)
        scroll_layout.setContentsMargins(10, 10, 10, 10)
        scroll_layout.setSpacing(10)
        scroll_layout.setAlignment(Qt.AlignTop)  # Ensures alignment starts from top

        # Load chat history
        history_file = "chat_history.json"
        if os.path.exists(history_file):
            with open(history_file, "r", encoding="utf-8") as file:
                history_data = json.load(file)

            if history_data:
                for question in history_data.keys():  # Load history in reverse order
                    history_button = QPushButton(f"{question}", scroll_widget)
                    history_button.setFixedSize(400, 50)
                    history_button.setStyleSheet("""
                        QPushButton {
                            background-color: #48CAE4;
                            color: #FFFFFF;
                            border-radius: 10px;
                            font: bold 16px 'Segoe UI';
                            padding: 8px;
                            transition: all 0.3s ease-in-out;
                        }
                        QPushButton:hover {
                            background-color: #4ECDC4;
                        }
                        QPushButton:pressed {
                            background-color: #0096C7;
                        }
                    """)
                    history_button.clicked.connect(lambda _, q=question: self.show_full_chat(q))
                    scroll_layout.addWidget(history_button,
                                            alignment=Qt.AlignTop | Qt.AlignHCenter)  # Align top & center

            else:
                no_history_label = QLabel("No chat history available.", scroll_widget)
                no_history_label.setStyleSheet("color: #AAAAAA; font: italic 16px 'Segoe UI'; background: transparent;")
                no_history_label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)  # Align top & center
                scroll_layout.addWidget(no_history_label, alignment=Qt.AlignTop | Qt.AlignHCenter)

        else:
            no_history_label = QLabel("No chat history available.", scroll_widget)
            no_history_label.setStyleSheet("color: #AAAAAA; font: italic 16px 'Segoe UI'; background: transparent;")
            no_history_label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)  # Align top & center
            scroll_layout.addWidget(no_history_label, alignment=Qt.AlignTop | Qt.AlignHCenter)

        scroll_widget.setLayout(scroll_layout)
        scroll_area.setWidget(scroll_widget)
        layout.addWidget(scroll_area, stretch=1)  # Ensures scrolling

        # Back button
        back_button = QPushButton("Back", frame)
        back_button.setFixedSize(120, 40)
        back_button.setStyleSheet("""
            QPushButton {
                background-color: #48CAE4;
                color: #FFFFFF;
                border-radius: 10px;
                font: bold 16px 'Segoe UI';
                padding: 8px;
                transition: all 0.3s ease-in-out;
            }
            QPushButton:hover {
                background-color: #4ECDC4;
            }
            QPushButton:pressed {
                background-color: #0096C7;
            }
        """)
        back_button.clicked.connect(self.show_chatbot_page)
        layout.addWidget(back_button, alignment=Qt.AlignCenter)

        self.root_layout.addWidget(frame, alignment=Qt.AlignCenter)

    def load_chat_history(self):
        """Loads and displays chat history without resetting it."""
        history_file = "chat_history.json"

        try:
            if os.path.exists(history_file) and os.stat(history_file).st_size > 0:
                with open(history_file, "r", encoding="utf-8") as file:
                    history_data = json.load(file)

                if history_data:
                    formatted_history = ""
                    for timestamp, chat in history_data.items():
                        formatted_history += f"{timestamp}\nUser: {chat['User']}\nAI: {chat['AI']}\n\n"

                    self.history_display.setText(formatted_history)
                else:
                    self.history_display.setText("No chat history available.")

            else:
                self.history_display.setText("No chat history available.")

        except json.JSONDecodeError:
            print("Error loading history: JSON is corrupted.")
            self.history_display.setText("Chat history is corrupted.")
        except Exception as e:
            print(f"Error loading history: {e}")
            self.history_display.setText("Failed to load chat history.")

    import json
    from datetime import datetime

    import json
    import os
    from datetime import datetime

    import json
    import os
    from datetime import datetime

    def save_chat_history(self, user_input, response):
        """Stores conversation history using the question as the key, keeping recent items first."""
        try:
            history_file = "chat_history.json"

            # Load existing history
            if os.path.exists(history_file):
                with open(history_file, "r", encoding="utf-8") as file:
                    try:
                        history_data = json.load(file)  # Load JSON
                    except json.JSONDecodeError:
                        history_data = {}  # Reset if file is corrupted
            else:
                history_data = {}

            # Ensure question is a valid key (JSON keys must be unique)
            question_key = user_input.strip()
            if question_key in history_data:
                # Append a number if duplicate question exists
                counter = 1
                while f"{question_key} ({counter})" in history_data:
                    counter += 1
                question_key = f"{question_key} ({counter})"

            # Store the chat at the **beginning** to keep recent searches first
            new_history_data = {question_key: {"User": user_input, "AI": response}}
            new_history_data.update(history_data)  # Merge with old data (recent first)

            # Save back to JSON file
            with open(history_file, "w", encoding="utf-8") as file:
                json.dump(new_history_data, file, indent=4)

            print("History saved successfully.")

        except Exception as e:
            print(f"Error saving history: {e}")

    def show_full_chat(self, question):
        self.clear_frame()

        frame = QFrame(self)
        frame.setStyleSheet("""
            background: rgba(30, 30, 47, 0.5);
            border-radius: 20px;
            box-shadow: 8px 8px 20px rgba(0, 0, 0, 0.3), 
                        -8px -8px 20px rgba(255, 255, 255, 0.05);
        """)
        frame.setFixedSize(800, 700)

        layout = QVBoxLayout(frame)
        layout.setContentsMargins(40, 50, 40, 50)
        layout.setSpacing(20)

        # Title
        chat_title = QLabel(f"Chat: {question}", frame)
        chat_title.setStyleSheet("color: #ECEFF4; font: bold 22px 'Segoe UI'; background: transparent;")
        chat_title.setAlignment(Qt.AlignCenter)
        layout.addWidget(chat_title)

        # Load chat history
        history_file = "chat_history.json"
        with open(history_file, "r", encoding="utf-8") as file:
            history_data = json.load(file)

        chat_data = history_data.get(question, {})
        user_message = chat_data.get("User", "No user message found.")
        ai_response = chat_data.get("AI", "No AI response found.")

        chat_display = QTextEdit(frame)
        chat_display.setReadOnly(True)
        chat_display.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.7);
            color: #1A1A1A;
            font: 18px 'Segoe UI'; 
            padding: 12px;
            border-radius: 15px;
        """)
        chat_display.setText(f"User: {user_message}\n\nAI: {ai_response}")
        layout.addWidget(chat_display)

        # Back button
        back_button = QPushButton("Back", frame)
        back_button.setFixedSize(120, 40)
        back_button.setStyleSheet("""
                    QPushButton {
                        background-color: #48CAE4;
                        color: #FFFFFF;
                        border-radius: 10px;
                        font: bold 16px 'Segoe UI';
                        padding: 8px;
                        transition: all 0.3s ease-in-out;
                    }
                    QPushButton:hover {
                        background-color: #4ECDC4;
                    }
                    QPushButton:pressed {
                        background-color: #0096C7;
                    }
                """)
        back_button.clicked.connect(self.show_chat_history)
        layout.addWidget(back_button, alignment=Qt.AlignCenter)
        layout.addWidget(back_button, alignment=Qt.AlignCenter)

        self.root_layout.addWidget(frame, alignment=Qt.AlignCenter)


    from PyQt5.QtWidgets import QMessageBox

    from PyQt5.QtCore import QTimer

    def process_chatbot_question(self):
        try:
            user_input = self.chatbox_display.toPlainText().strip()

            if not user_input:
                QMessageBox.warning(self, "Input Required", "Please type a legal question before asking.")
                return

            self.chatbox_display.setText("Processing your request...")  # Show loading message
            QApplication.processEvents()  # Refresh UI to display message

            self.response_received = False  # Track if response is received

            def handle_timeout():
                """Function called when 20 seconds pass without response."""
                if not self.response_received:  # If no response was received
                    QMessageBox.warning(self, "Server Busy", "The server is busy. Please try again later.")
                    self.show_chatbot_page()  # Keep user on the chatbot page

            # Set a timer for 20 seconds
            self.timer = QTimer()
            self.timer.timeout.connect(handle_timeout)
            self.timer.start(20000)  # 20,000 milliseconds = 20 seconds

            # Get chatbot response
            response = self.get_backend_response(user_input)

            # Stop timer since response was received
            self.timer.stop()
            self.response_received = True  # Mark response as received

            if response is None:
                response = "Sorry, I couldn't generate a response."

            # Display response
            self.display_chatbot_response(user_input, response)

            # Save chat history
            self.save_chat_history(user_input, response)

        except Exception as e:
            print(f"Error in process_chatbot_question: {e}")
            QMessageBox.critical(self, "Error", f"Something went wrong: {e}")



    def get_backend_response(self, user_input_question):
        url = "http://127.0.0.1:8000/chat/"
        data = {"question": user_input_question}
        try:
            response = requests.post(url=url, data=data)
            response_data = response.json()
            question = response_data.get("question")
            generated_response = response_data.get("answer")
        except Exception as e:
            print("Error in hitting API")
            generated_response = "No Connection Established"

        return generated_response

    def get_chatbot_response(self, user_input):
        response = "Sorry, I don't have an answer for that yet."

        # Predefined responses
        if "legal" in user_input.lower():
            response="Nice Question"
        elif "hello" in user_input.lower():
            response = "Hello! How can I assist you today?"
        elif "help" in user_input.lower():
            response = "Sure, I'm here to help. Please provide more details."
        else:
            response=self.get_backend_response(user_input_question=user_input)

        return response

    from PyQt5.QtWidgets import (
        QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFrame,
        QScrollArea
    )
    from PyQt5.QtCore import Qt

    def display_chatbot_response(self, user_input, response):
        self.clear_frame()  # Clears the current frame to navigate to a new page

        # Create a new frame for the response page
        frame = QFrame(self)
        frame.setStyleSheet("""
            background: rgba(30, 30, 47, 0.5); /* Deep blue-grey with slight transparency */
            border-radius: 20px;
            box-shadow: 8px 8px 20px rgba(0, 0, 0, 0.3), 
                        -8px -8px 20px rgba(255, 255, 255, 0.05);
        """)
        frame.setFixedSize(800, 700)  # Adjusted window frame size

        layout = QVBoxLayout(frame)
        layout.setContentsMargins(50, 40, 50, 40)
        layout.setSpacing(20)

        # Scrollable Area for User Input
        scroll_area_question = QScrollArea(frame)
        scroll_area_question.setWidgetResizable(True)
        scroll_area_question.setFixedHeight(90)  # Slightly taller for better visibility
        scroll_area_question.setStyleSheet("border: none;")

        # User Input Label inside Scroll Area (Subtle Design)
        user_question_display = QLabel(user_input if user_input else "Your Question", scroll_area_question)
        user_question_display.setStyleSheet("""
            background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, 
                                        stop:0 rgba(40, 40, 60, 0.8), 
                                        stop:1 rgba(50, 50, 75, 0.85)); 
            font: bold 20px 'Segoe UI';
            color: rgba(220, 220, 230, 0.9); 
            padding: 15px;
            border-radius: 15px;
            box-shadow: 6px 6px 15px rgba(0, 0, 0, 0.3), 
                        -6px -6px 15px rgba(255, 255, 255, 0.05);
        """)
        user_question_display.setWordWrap(True)
        user_question_display.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        scroll_area_question.setWidget(user_question_display)
        layout.addWidget(scroll_area_question)

        # Chatbot Response Scrollable Area
        scroll_area_response = QScrollArea(frame)
        scroll_area_response.setWidgetResizable(True)
        scroll_area_response.setFixedSize(700, 400)  # Adjust size as needed
        scroll_area_response.setStyleSheet("border: none;")

        # Container for response (inside scroll area)
        response_container = QWidget()
        response_layout = QVBoxLayout(response_container)
        response_layout.setContentsMargins(15, 15, 15, 15)

        # Chatbot Response Title
        response_label = QLabel("Chatbot's Response")
        response_label.setStyleSheet("""
            font: bold 22px 'Segoe UI'; /* Increased font size */
            color: #FFFFFF;
            margin-bottom: 10px;
        """)
        response_label.setAlignment(Qt.AlignCenter)
        response_layout.addWidget(response_label)

        # Response Box (New Stylish Box)
        response_box = QFrame()
        response_box.setStyleSheet("""
            background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, 
                                        stop:0 rgba(0, 180, 255, 0.7), 
                                        stop:1 rgba(0, 120, 255, 0.9)); 
            border-radius: 12px;
            padding: 15px;
        """)
        response_box.setFrameShape(QFrame.StyledPanel)
        response_box.setFrameShadow(QFrame.Raised)

        box_layout = QVBoxLayout(response_box)

        # Chatbot Response Content
        response_display = QLabel(response)
        response_display.setStyleSheet("""
            font: 18px 'Segoe UI'; /* Increased font size */
            color: #FFFFFF;
            background: transparent;
            padding: 10px;
            border-radius: 10px;
        """)
        response_display.setWordWrap(True)
        response_display.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        box_layout.addWidget(response_display)
        response_box.setLayout(box_layout)
        response_layout.addWidget(response_box)

        response_container.setLayout(response_layout)
        scroll_area_response.setWidget(response_container)

        layout.addWidget(scroll_area_response)
        # Back Button with New Color
        back_button = QPushButton("Back", frame)
        back_button.setFixedSize(150, 50)
        back_button.setStyleSheet("""
            QPushButton {
            background-color: #48CAE4;
            color: #FFFFFF;
            border-radius: 10px;
            font: bold 16px 'Segoe UI';
            padding: 8px;
            transition: all 0.3s ease-in-out;
        }
            QPushButton:hover {
                background-color: #4ECDC4;
            }
            QPushButton:pressed {
                background-color: #0096C7;
            }
            """)
        back_button.clicked.connect(self.show_chatbot_page)
        layout.addWidget(back_button, alignment=Qt.AlignCenter)

        self.root_layout.addWidget(frame, alignment=Qt.AlignCenter)


    def confirm_back_to_login(self):
        # Display a message box asking for confirmation
        reply = QMessageBox.question(self, 'Confirm',
                                     'Confirm to go back to login ?',
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.login_page()  # Navigate back to the login page if user clicks Yes

        if reply == QMessageBox.No:
            self.show_chatbot_page()


def start_backend():
    config = Config("main:app", host="127.0.0.1", port=8000, reload=True)
    server = Server(config)
    server.run()

if __name__ == "__main__":
    backend_process = multiprocessing.Process(target=start_backend,daemon=True)
    backend_process.start()
    app = QApplication(sys.argv)
    window = AttendanceApp()
    window.setWindowTitle("Log into your Account")
    window.show()
    sys.exit(app.exec_())


    backend_process.terminate()
    backend_process.join()






