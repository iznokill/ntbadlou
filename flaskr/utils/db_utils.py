import logging
import sqlite3


def get_img(db_name, product_id):
    try:
        conn = sqlite3.connect(db_name)

        conn.text_factory = str
        cur = conn.cursor()
        logging.info("Successfully Connected to SQLite")
        sql = "SELECT img, content_type FROM img_list WHERE product_id = " + str(product_id) + ";"

        cur.execute(sql)
        conn.commit()
        logging.info("Successfully Retrieved imgs")
        record = cur.fetchall()
        cur.close()
        conn.close()
        logging.info("Successfully Closed connection")
        return record

    except sqlite3.Error as error:
        logging.error("Error while retrieving imgs", error)


def insert_img(db_name, product_id, file, content_type):
    try:
        conn = sqlite3.connect(db_name)

        conn.text_factory = str
        cur = conn.cursor()
        logging.info("Successfully Connected to SQLite")
        sql = "INSERT INTO img_list (product_id,img,content_type) VALUES (?, ?,?)"


        value = (product_id, file, content_type)
        cur.execute(sql, value)
        conn.commit()
        logging.info("Successfully Inserted img")
        cur.close()
        conn.close()
        logging.info("Successfully Closed connection")

    except sqlite3.Error as error:
        logging.error("Error while inserting img", error)
