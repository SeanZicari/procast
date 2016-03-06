import sqlite3

CREATE_STATEMENT = """
CREATE TABLE IF NOT EXISTS contact_form (
  name TEXT,
  email TEXT,
  phone TEXT,
  best_time_to_contact TEXT
);
"""
INSERT_STATEMENT = """INSERT INTO contact_form VALUES (?, ?, ?, ?)"""


class ContactForm(object):

    def __init__(self):
        self._connection = sqlite3.connect('procast/contact_form.db')
        self._cursor = self._connection.cursor()
        self._cursor.execute(CREATE_STATEMENT)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._connection.commit()
        self._cursor.close()
        self._connection.close()

    def save_data(self, name, email, phone, best_time_to_contact):
        self._cursor.execute(INSERT_STATEMENT, [name, email, phone, best_time_to_contact])
