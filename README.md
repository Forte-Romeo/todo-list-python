# 📝 Python CLI Todo List App

A simple command-line Todo List application built with Python. This project helps users manage daily tasks by adding, viewing, editing, completing, searching, and removing tasks directly from the terminal.

The application stores tasks in a `.json` file, meaning tasks remain saved even after closing the program.

---

## 🚀 Features

- Add new tasks with due dates
- View all tasks in a numbered list
- Edit existing tasks
- Mark tasks as completed
- Remove tasks from the list
- Search tasks in the list
- Automatic file storage (persistent data)
- Color-coded terminal output for better user experience

---

## 🛠️ Technologies Used

- Python 3.14
- termcolor
- questionary
- sys (built-in module)
- json (built-in module)

---

## 📁 Project Structure

```
todo-list-python/
│
├── todo-list.py
├── todo_list.json
├── README.md
```

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
3. Edit Task
4. Mark Task as Complete
5. Remove Task
6. Search Tasks
7. Exit

---

## 🔹 Features Breakdown

- Add Task:
Enter a task and add its due date.
<img width="305" height="237" alt="Screenshot 2026-05-27 150343" src="https://github.com/user-attachments/assets/33208e73-b5ed-42bf-b16c-d0187a988dfe" />


- View Tasks:
Shows all tasks with numbering.
<img width="320" height="287" alt="Screenshot 2026-05-27 150401" src="https://github.com/user-attachments/assets/cb4f904e-a7c2-47e7-a2b2-d7a780212e8f" />


- Edit Task:
Edits a task and updates the list.
<img width="307" height="299" alt="Screenshot 2026-05-27 150435" src="https://github.com/user-attachments/assets/9517ce33-2e5f-4f41-a20d-dd9b3315cf2e" />
<img width="354" height="100" alt="Screenshot 2026-05-27 150446" src="https://github.com/user-attachments/assets/d48dce33-105f-43b5-89b1-ce2b431ee998" />
<img width="310" height="281" alt="Screenshot 2026-05-27 150516" src="https://github.com/user-attachments/assets/b48af2a5-ea72-4f88-90d5-13f19932c053" />


- Mark Task as Complete:
Marks selected task as completed.
<img width="667" height="316" alt="Screenshot 2026-05-27 150541" src="https://github.com/user-attachments/assets/e33b31d8-fedc-41a3-a62d-48816d9f5c45" />
<img width="322" height="284" alt="Screenshot 2026-05-27 150553" src="https://github.com/user-attachments/assets/5d64655a-bc82-41f6-8e54-1047ee96da81" />


- Remove Task:
Deletes selected task.
<img width="305" height="316" alt="Screenshot 2026-05-27 150623" src="https://github.com/user-attachments/assets/844dab01-4cf4-46bc-a6a9-80d5f0e95563" />
<img width="318" height="272" alt="Screenshot 2026-05-27 150647" src="https://github.com/user-attachments/assets/89b2a143-b2d1-44b0-8f07-d8202fc61fe4" />


- Search Tasks:
Uses a keyword to search for tasks in the list.
<img width="320" height="270" alt="Screenshot 2026-05-27 150701" src="https://github.com/user-attachments/assets/98329fec-9454-4087-a3aa-030b38bf98b0" />

- Exit:
Closes the program and saves all tasks to `todo_list.json`.
<img width="220" height="198" alt="Screenshot 2026-05-27 150710" src="https://github.com/user-attachments/assets/05b315e3-63f2-48f3-9ca2-be2489cb07cf" />

---

## 📌 Output

```
1. Document code | Due: 2026-05-27 | ❌
2. Push code to git | Due: 2026-05-27 | ❌
```

---

## 💡 Code Overview

- tasks = [ ] : stores tasks in the text file
- add_task( ) : adds task
- view_tasks( ) : shows tasks
- edit_task( ) : edits an existing task
- mark_task_complete( ) : completes task
- remove_task( ) : deletes task
- search_task( ) : searches a task in the JSON file
- save_tasks_to_file( ): writes all tasks into the text file
- load_tasks_from_file( ): loads saved tasks when the app starts
- main( ) : program loop

---

## 📌 File Storage System

`filename = "todo_list.json"`

This variable stores the location of the JSON file used to save tasks permanently.

Tasks are stored as dictionaries inside:

`todo_list.json`

Example:

```
[
  {
      "task": "Buy groceries",
      "due_date": "2026-05-27",
      "completed": True
  }
]
```

---

## 💾 Data Persistence

Unlike the earlier version, tasks are now permanently stored using a JSON file.

This means:

✅ Tasks remain saved after closing the app

✅ Tasks reload automatically when reopening the program

---

## 🧠 Python Concepts Practiced


This project teaches:

- Functions
- Lists & dictionaries
- JSON handling
- File persistence
- CRUD operations
- Loops
- Conditional logic
- Error handling
- CLI architecture
- Search functionality

---

## ⚠️ Known Issues

- No task priority system
- No overdue task detection
- No task categories/tags
- No authentication system
- Due date validation is minimal

---

## 🔮 Future Improvements

- ⭐ Priority levels
- 📂 SQLite database storage
- 🖥️ GUI version with Tkinter or PyQt
- 🌐 Web app version using Flask or Django
- 📱 Mobile version
- 🎯 Task categories
- 📊 Productivity statistics

---

## 👨‍💻 Author

Built by Ferguson Romeo (Forte Romeo)  
Software + AI Engineer | IT Student | Builder in Progress 🚀

---

## ⭐ Support

If you like this project:
- Star the repository
- Fork the project
- Feel free to improve it
- Build your own version

Happy Coding 🚀
