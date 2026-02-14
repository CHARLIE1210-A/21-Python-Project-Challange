# 21 Python Project Challenge

This repository contains a collection of 21 Python projects designed to help you learn and practice Python programming. Each project focuses on a different concept or use case, ranging from beginner to intermediate level. Below are the first 10 applications included in this challenge, with a brief description of each.

## 1. URL Shortener
A simple web application built with Flask that allows users to shorten long URLs. The app stores original URLs and their corresponding short codes in a SQLite database, and provides redirection from the short code to the original URL.

## 2. Calculator
A basic calculator application that can perform arithmetic operations such as addition, subtraction, multiplication, and division. (To be implemented)

## 3. To-Do List
A command-line or web-based to-do list manager where users can add, remove, and mark tasks as completed. (To be implemented)

## 4. Weather App
An application that fetches and displays current weather information for a given city using a public weather API. (To be implemented)

## 5. Quiz Game
A quiz game that asks users multiple-choice questions and keeps track of their score. (To be implemented)

## 6. Password Generator
A tool to generate strong, random passwords based on user-specified criteria such as length and character types. (To be implemented)

## 7. Expense Tracker
An application to track daily expenses, categorize them, and provide summaries or reports. (To be implemented)

## 8. Alarm Clock
A simple alarm clock application that allows users to set alarms and notifies them at the specified time. (To be implemented)

## 9. Contact Book
A contact management system where users can add, search, update, and delete contact information. (To be implemented)

## 10. File Organizer
A script to organize files in a directory into folders based on file type or other criteria. (To be implemented)

---

## How to Run the URL Shortener
1. Install dependencies:
   ```bash
   pip install flask
   ```
2. Run the application:
   ```bash
   python main.py
   ```
3. Use the `/shorten` endpoint to shorten URLs (POST request with JSON `{ "url": "<your_url>" }`).
4. Access the shortened URL to be redirected to the original URL.

---

## Contributing
Feel free to contribute by submitting pull requests for new features, bug fixes, or additional projects!

## License
This project is licensed under the MIT License.
