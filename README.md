# Test Flask app
test_flask_app
### How to run the project:

Clone repositorie and go to it:

```
git clone https://github.com/anushST/job_flask_test.git
```

```
cd job_flask_test
```

Create and activate virtual environment:

*  Linux/macOS
    ```
    python3 -m venv venv
    ```

    ```
    source venv/bin/activate
    ```

    ```
    python3 -m pip install --upgrade pip
    ```

*  windows
    ```
    python -m venv venv
    ```

    ```
    source venv/scripts/activate
    ```

    ```
    python -m pip install --upgrade pip
    ```


Install dependencies from requirements.txt:

```
pip install -r requirements.txt
```

Create and migrate database:

```
flask db upgrade head
```

Запустить проект:

```
flask run
```
