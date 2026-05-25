# 📝 Python CLI Todo List App

A simple command-line Todo List application built with Python. This project helps users manage daily tasks by adding, viewing, completing, and removing tasks directly from the terminal.

---

## 🚀 Features

- Add new tasks
- View all tasks in a numbered list
- Mark tasks as completed
- Remove tasks from the list
- Color-coded terminal output for better user experience

---

## 🛠️ Technologies Used

- Python 3.14
- termcolor
- questionary
- sys (built-in module)

---

## 📁 Project Structure

todo-list-python/

├── todo-list.py

├── README.md

---

## 📦 Installation

### 1. Clone the repository
`git clone https://github.com/Forte-Romeo/todo-list-python.git`

### 2. Move into the project directory
`cd todo-list-python`

### 3. Create virtual environment (recommended)
`python -m venv venv`

Activate it:

- Windows:
`venv\Scripts\activate`

- Mac/Linux:
`source venv/bin/activate`

### 4. Install dependencies
- `pip install termcolor`
- `pip install questionary`

---

## ▶️ How to Run

`python todo-list.py`

---

## 📱 Application Menu

Todo List Menu:
1. Add Task
2. View Tasks
3. Mark Task as Complete
4. Remove Task
5. Exit

---

## 🔹 Features Breakdown

- Add Task:
Enter a task and it will be added.
<img width="221" height="164" alt="Screenshot 2026-05-25 142728" src="https://github.com/user-attachments/assets/974ad3ad-7938-4af2-a76e-789f2fdc4dbc" />

- View Tasks:
Shows all tasks with numbering.
<img width="224" height="193" alt="Screenshot 2026-05-25 142806" src="https://github.com/user-attachments/assets/da035be5-7bf1-451e-bc07-cc464b52595b" />

- Mark Task as Complete:
Marks selected task as completed.
<img width="366" height="166" alt="Screenshot 2026-05-25 142826" src="https://github.com/user-attachments/assets/5d55f040-25af-4a09-a7ed-ba78e057e70b" />

- Remove Task:
Deletes selected task.
<img width="204" height="212" alt="Screenshot 2026-05-25 142857" src="https://github.com/user-attachments/assets/6d789310-a7f0-4165-9b4a-0bd419e92a4d" />
<img width="273" height="162" alt="Screenshot 2026-05-25 142907" src="https://github.com/user-attachments/assets/061c15af-1d61-4b8d-b0b1-4318845f5e6e" />

- Exit:
Closes the program.

---

## 📌 Output

<img width="217" height="191" alt="Screenshot 2026-05-25 142915" src="https://github.com/user-attachments/assets/fc359daf-e43f-42bd-af51-740711d855df" />

---

## 💡 Code Overview

- tasks = [ ] : stores tasks
- add_task( ) : adds task
- view_tasks( ) : shows tasks
- mark_task_complete( ) : completes task
- remove_task( ) : deletes task
- main( ) : program loop

---

## 🧠 What I Learned

- Python lists and manipulation
- CLI menu systems
- Input handling
- Basic validation
- External libraries (termcolor, questionary)
- Structuring small Python projects

---

## ⚠️ Known Issues

- No data persistence (tasks reset after exit)
- No advanced input validation
- No edit task feature

---

## 🔮 Future Improvements

- Add JSON/file storage
- Add edit task feature
- Add priority system
- Add due dates
- Build GUI or web version

---

## 👨‍💻 Author

Built by Ferguson Romeo (Forte Romeo)  
Software + AI Engineer | IT Student | Builder in Progress 🚀

---

## ⭐ Support

If you like this project, star the repository and feel free to improve it.
