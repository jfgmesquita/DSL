# DSL (Domain-Specific Language) 

This repository contains the **DSL (Domain-Specific Language)** interpreter for the SGPC (Fuel Station Management System) project.

The DSL allows service staff to interact with the system using simple, expressive commands for scheduling services, managing availability, requesting vacations, running reports, and more.

---

## ✅ Features

- Schedule services for customers (e.g., oil change)
- Record unavailability periods (e.g., sick leave, holidays)
- Define vacation requests with date intervals
- Execute batch operations (multiple instructions in one script)
- Define reusable profiles with `def name(): ...`
- Use conditional logic with `if ... else ...`
- Assign and reuse variables and lists
- Fully custom grammar built with PLY (Python Lex-Yacc)

---

## 📄 Example DSL Script

```lss
def morning_shift():
    days: ["monday", "friday"]
    hours: "08:00-12:00"

schedule:
    service: "oil change"
    customer: "Ana Costa"
    date: 2025-03-12
```

---

## 🚀 How to Use

1. Write your script in a `.lss` file
2. Run the interpreter:

```bash
python main.py tests/my_script.lss
```

---


## 🛠 Technologies

- Python 3
- PLY (Python Lex-Yacc)

---

## ⚙️ Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 📁 Project Structure

- `lss/lexer.py` – Token definitions for the LSS language
- `lss/parser.py` – Grammar rules using PLY yacc
- `lss/executor.py` – Interpreter that executes parsed AST
- `main.py` – Entry point for running LSS scripts
- `clean.py` – Utility script for cleaning up generated files or outputs
- `requirements.txt` – Python dependencies for the project
- `tests/` – Sample `.lss` scripts and/or test files

---

## 📜 License

This is an academic project. Not intended for commercial use.
