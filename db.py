import psycopg2
from psycopg2 import Error

class Data:
    @staticmethod
    def get_traiders():
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="Casa512472;)",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="intership")

            cursor = connection.cursor()
            cursor.execute('''
            SELECT nickname from "user"
            WHERE "role" = 'Traider' AND "validKey" = true
            ''')

            record = cursor.fetchall()
            result = []
            for i in record:
                for j in i:
                    result.append(j)
            return result
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
                print("Соединение с PostgreSQL закрыто")

    @staticmethod
    def get_ids_for_mailing(telegram_id):
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="Casa512472;)",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="intership")

            cursor = connection.cursor()
            cursor.execute(f"""
            SELECT "userTelegramId" FROM "subscribe"
            WHERE "traiderTelegramId" = '{telegram_id}'
            """)

            record = cursor.fetchall()
            result = []
            for i in record:
                for j in i:
                    result.append(j)
            return result
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
                print("Соединение с PostgreSQL закрыто")

