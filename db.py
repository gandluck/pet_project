import psycopg2
from psycopg2 import Error

from handlers import user


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
            INSERT INTO public."user" ("telegramId", username, nickname, balance, "firstName", "lastName", description, role, "apiKey", "secretKey", "dateAddKey", "validKey", "watchOrders", "referralCode", created_at, updated_at) 
            VALUES ({user.telegram_id}, {user.username}, {user.nickname}, null, null, null, null, {user.role}, {user.api}, {user.secret_key}, null, true, false, null, null, null);
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
