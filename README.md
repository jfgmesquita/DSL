# DSL (Domain-Specific Language) 

This repository contains the **LSS (Domain-Specific Language)** interpreter for the SGPC (Fuel Station Management System) project.

The LSS allows service staff to interact with the system using simple, expressive commands for scheduling services, managing availability, requesting vacations, running reports, and more.

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

## 📄 Example LSS Script

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

1. Write your LSS script in a `.lss` file
2. Run the interpreter:

```bash
python main.py scripts/my_script.lss
```

---


## 🛠 Technologies

- Python 3
- PLY (Python Lex-Yacc)

---

## 📁 Project Structure

- `lexer.py` – Token definitions for the LSS language
- `parser.py` – Grammar rules using PLY yacc
- `executor.py` – Interpreter that executes parsed AST
- `main.py` – Entry point for running LSS scripts
- `scripts/` – Sample `.lss` scripts

---

## 📜 License

This is an academic project. Not intended for commercial use.
