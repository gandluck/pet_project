import psycopg2
from psycopg2 import Error

from states import user


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
    def get_ids_for_mailing():
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="Casa512472;)",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="intership")

            cursor = connection.cursor()
            cursor.execute(f"""
            SELECT "userTelegramId" FROM "subscribe"
            WHERE "traiderTelegramId" = '{user.telegram_id}'
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

    @staticmethod
    def create_record_user():
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="Casa512472;)",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="intership")

            cursor = connection.cursor()
            cursor.execute(f"""
        INSERT INTO public."user" ("telegramId", username, role) 
        VALUES ('{user.telegram_id}', '{user.username}', '{user.role}')
        """)

        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
        finally:
            if connection:
                connection.commit()
                cursor.close()
                connection.close()
                print("Соединение с PostgreSQL закрыто")

    @staticmethod
    def update_data_user_nickname_api_key():
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="Casa512472;)",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="intership")

            cursor = connection.cursor()
            cursor.execute(f"""
        UPDATE "user" SET nickname = '{user.nickname}', "apiKey" = '{user.api}', "secretKey" = '{user.secret_key}'
        WHERE "telegramId" = '{user.telegram_id}'
        """)

        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
        finally:
            if connection:
                connection.commit()
                cursor.close()
                connection.close()
                print("Соединение с PostgreSQL закрыто")
    @staticmethod
    def check_nickname(nickname):
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="Casa512472;)",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="intership")

            cursor = connection.cursor()
            cursor.execute(f"""
        SELECT nickname FROM "user"
        """)

            record = cursor.fetchall()
            result = []
            for i in record:
                for j in i:
                    result.append(j)
            print(result)
            if nickname not in result:
                return True
            return False

        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
        finally:
            if connection:
                connection.commit()
                cursor.close()
                connection.close()
                print("Соединение с PostgreSQL закрыто")


