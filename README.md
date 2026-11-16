**Intramural Sports Website**
<li>SQLite Database</li>
For flask to work, html files must be in templates unless we specify template folder

To install dependencies:
```bash
 python -m pip install -e .
 ```

To run the app: 
```bash
python itit_db.py
```
to load test data into the database, then:
```bash
flask --app intramural_website run
```
or
```bash
flask --app intramural_website run --debug
```

Go to http://127.0.0.1:5000 or 
http://127.0.0.1:5000/login