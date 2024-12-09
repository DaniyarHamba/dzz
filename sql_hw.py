import sqlite3
from config import DB_PATH

def add_post(title: str, content: str) -> None:
    add_post_query = """
    INSERT INTO posts(title, content) VALUES (?, ?);
    """

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute(add_post_query, (title, content))
    connection.commit()
    connection.close()

    print("Пост добавлен")

def update_post(post_id: int, new_title: str, new_content: str) -> None:
    update_post_query = """
    UPDATE posts SET title = ?, content = ? WHERE post_id = ?;
    """

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute(
        update_post_query,
        (new_title, new_content, post_id),
    )

    updated_rows_count = cursor.rowcount

    connection.commit()
    connection.close()

    if updated_rows_count == 0:
        print("Пост для обновления не найден")
    else:
        print("Пост обновлен")



update_post(1, "Salut", "Ca va")