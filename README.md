# Hangman:

## 🌟 Project Overview
  This project is a terminal-based implementation of the classic **Hangman** word-guessing game. The objective is to guess a hidden word one letter at a time before the gallows are completed. It features a scalable design that evolves from simple list-based word selection to dynamic file I/O, allowing users to easily expand the game's vocabulary.

## 🚀 Implementation and Use Cases

### Implementation
The project is implemented through a robust game loop that manages:
  - **Dynamic ASCII Art**: Utilizing a list of multi-line strings (`STAGES`) to represent the player's remaining lives visually.
  - **Input Sanitization**: A dedicated validation loop ensures users only enter single alphabetic characters and prevents duplicate guesses.
  - **File Handling Evolution**: Version 1 uses a static list, while Version 2 implements a `load_words()` function that reads from `Hangman_Words.txt`, demonstrating clean data separation and resource management.

### Use Cases
  - **Quick Gaming**: A lightweight game for a quick mental break in the terminal.
  - **Vocabulary Builder**: By editing the `Hangman_Words.txt` file, the game can be used as a customized tool for learning new terminology.
  - **Coding Tutorial**: Serves as a perfect example of how to implement the "Model-View-Controller" pattern in a simple script.

## 📦 Libraries Used and Their Purposes
**random (Standard Library)**:
  - **random.choice**: Crucial for selecting a secret word from the word list, ensuring that every game session is unique.

## 💻 Requirements
  - Python 3.x
  - **Hangman_Words.txt (For Version 2)**: A text file containing words separated by newlines, located in the same directory as the script.

## 🎓 Learning Outcomes
Through the development of this project, I have achieved:
  - **File I/O Proficiency**: Mastering the `with open()` context manager to read and clean data from external text files.
  - **String Manipulation**: Using methods like `.strip()`, `.upper()`, and `.isalpha()` to process and normalize user and file data.
  - **State Management**: Tracking multiple game variables simultaneously, including `lives`, `guessed_letters`, and the `secret_word`.
  - **Visual Formatting**: Implementing multi-line string constants to create a dynamic UI within a command-line interface.
