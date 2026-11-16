from intramural_website import create_app
from intramural_website.db import init_db

app = create_app()
with app.app_context():
    init_db()