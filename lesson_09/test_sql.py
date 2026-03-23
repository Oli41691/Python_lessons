import pytest
from sqlalchemy import create_engine, text

db_connection_string = "postgresql://postgres:1691@localhost:5432/QA"
db = create_engine(db_connection_string)

def test_add_subject():
    sql = text("INSERT INTO subject(\"subject_id\", \"subject_title\") VALUES (:id,:title)")
    with db.connect() as connection:
        connection.execute(sql, {'id': 201, 'title': 'История искусства'})
        result = connection.execute(
            text("SELECT subject_title FROM subject WHERE \"subject_id\"=:id"),
            {'id': 201}
        ).fetchone()
        assert result and result[0] == 'История искусства'

def test_update_subject():
    with db.connect() as connection:
        connection.execute(
            text("INSERT INTO subject(\"subject_id\", \"subject_title\") VALUES (:id,:title)"),
            {'id': 190, 'title': 'Культурология'}
        )
        connection.execute(
            text("UPDATE subject SET subject_title = :new_title WHERE \"subject_id\"=:id"),
            {'new_title': 'Философия', 'id': 190}
        )
        result = connection.execute(
            text("SELECT subject_title FROM subject WHERE \"subject_id\"=:id"),
            {'id': 190}
        ).fetchone()
        assert result and result[0] == 'Философия'

def test_delete_subject():
     with db.connect() as connection:
        connection.execute(
            text("INSERT INTO subject(\"subject_id\", \"subject_title\") VALUES (:id,:title)"),
            {'id': 220, 'title': 'Теория и история культуры'}
        )
        connection.execute(
            text("UPDATE subject SET is_deleted=TRUE WHERE \"subject_id\"=:id"),
            {'id': 220}
        )
        result = connection.execute(
            text("SELECT * FROM subject WHERE \"subject_id\"=:id AND is_deleted=FALSE"),
            {'id': 220}
        ).fetchall()
        assert len(result) == 0, "Запись должна быть помечена как удалённая (нет в активных)"