import psycopg2

def get_all_chat_ids():
    conn = psycopg2.connect(
        dbname="cbp",
        user="and",
        password="1234",
        host="db-cbp",
        port="5432"
    )
    
    cursor = conn.cursor()

    try:
        cursor.execute(
            "SELECT chat_id FROM member;"
        )
        rows = cursor.fetchall()
        chat_ids = [row[0] for row in rows]
        return chat_ids
    except Exception as e:
        print(f"Error getting all TGs: {e}")

    finally:
        cursor.close()
        conn.close()

def get_all_info():
    conn = psycopg2.connect(
        dbname="cbp",
        user="and",
        password="1234",
        host="db-cbp",
        port="5432"
    )
    
    cursor = conn.cursor()

    try:
        cursor.execute(
            "SELECT tg, class, info FROM member;"
        )
        rows = cursor.fetchall()
        mems = []
        for row in rows:
            row_str = ', '.join(map(str, row))
            mems.append(row_str)
        return mems
    except Exception as e:
        print(f"Error getting all TGs: {e}")

    finally:
        cursor.close()
        conn.close()

def get_user_class(chat_id):
    conn = psycopg2.connect(
        dbname="cbp",
        user="and",
        password="1234",
        host="db-cbp",
        port="5432"
    )
    
    cursor = conn.cursor()

    try:
        cursor.execute(
            "SELECT class FROM member WHERE chat_id = %s;", (chat_id,)
        )
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            return None
    except Exception as e:
        print(f"Error getting class for chat_id {chat_id}: {e}")
    finally:
        cursor.close()
        conn.close()

def add_member(tg, chat_id):
    conn = psycopg2.connect(
        dbname="cbp",
        user="and",
        password="1234",
        host="db-cbp",
        port="5432"
    )
    
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO member (tg, chat_id) VALUES (%s, %s);",
            (tg, chat_id)
        )
        conn.commit()
    except Exception as e:
        print(f"Error getting all TGs: {e}")

    finally:
        cursor.close()
        conn.close()

def fill_class(chat_id, class_info):
    conn = psycopg2.connect(
        dbname="cbp",
        user="and",
        password="1234",
        host="db-cbp",
        port="5432"
    )
    
    cursor = conn.cursor()

    try:
        cursor.execute(
            "UPDATE member SET class = %s WHERE chat_id = %s;",
            (class_info, chat_id)
        )
        conn.commit()
    except Exception as e:
        print(f"Error getting all TGs: {e}")

    finally:
        cursor.close()
        conn.close()

def fill_info(chat_id, info):
    conn = psycopg2.connect(
        dbname="cbp",
        user="and",
        password="1234",
        host="db-cbp",
        port="5432"
    )
    
    cursor = conn.cursor()

    try:
        cursor.execute(
            "UPDATE member SET info = CONCAT(info, %s) WHERE chat_id = %s;",
            (f"{info};", chat_id)
        )
        conn.commit()
    except Exception as e:
        print(f"Error getting all TGs: {e}")

    finally:
        cursor.close()
        conn.close()