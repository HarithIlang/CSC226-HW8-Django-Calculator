# Django Calculator (HW 8)

A small Django web app. Enter two numbers and an operator (`+`, `-`, `*`, `/`, `%`, `//`) and the result page shows the answer.

## What you need

- Python 3.10 or newer (built and tested with Python 3.14)
- pip (comes with Python)

## How to run it (Windows, PowerShell)

1. Open a terminal inside this folder (the one that contains `manage.py`).

2. Create a virtual environment (a private set of Python tools just for this project):

   ```
   python -m venv venv
   ```

3. Turn the environment on:

   ```
   venv\Scripts\activate
   ```

   If PowerShell says "running scripts is disabled", run this once in the same window and try again:

   ```
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   ```

   You should now see `(venv)` at the start of the line.

4. Install Django:

   ```
   pip install django
   ```

5. Start the server:

   ```
   python manage.py runserver
   ```

6. Open <http://127.0.0.1:8000/> in your browser, type a number, an operator and another number, then click Submit.

Press `Ctrl+C` in the terminal to stop the server.

### macOS / Linux

Use these two lines instead of steps 2 and 3, then continue from step 4:

```
python3 -m venv venv
source venv/bin/activate
```

## How it works

| File | What it does |
| --- | --- |
| `templates/home.html` | The form: number, operator, number |
| `calcapp/urls.py` | Sends the `result` address to the `result` view |
| `calcapp/views.py` | Reads the three values, calculates the answer |
| `templates/result.html` | Shows the answer |

Dividing by zero (`/`, `%`, `//`) shows "cannot divide by zero", and any other operator shows "unknown operator".
