import psycopg2
from psycopg2 import Error

from states import user
import config


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
            WHERE "role" = 'Traider'
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
            print(user.telegram_id)
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

    @staticmethod
    def update_data_user_become_traider():
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="Casa512472;)",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="intership")

            cursor = connection.cursor()
            cursor.execute(f"""
               UPDATE "user" SET role = '{user.role}'
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
    def get_balance():
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="Casa512472;)",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="intership")

            cursor = connection.cursor()
            cursor.execute(f"""
               SELECT balance FROM "user"
               WHERE "telegramId" = '{user.telegram_id}'
               """)

            balance_tuple = cursor.fetchone()
            balance = balance_tuple[0]
            print(balance)
            print(type(balance))
            if balance is None:
                print(balance)
                return 0
            return balance

        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
        finally:
            if connection:
                connection.commit()
                cursor.close()
                connection.close()
                print("Соединение с PostgreSQL закрыто")

    @staticmethod
    def top_up_balance():
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="Casa512472;)",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="intership")

            cursor = connection.cursor()
            cursor.execute(f"""
               UPDATE "user" SET balance = '{user.balance}'
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
    def get_role():
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="Casa512472;)",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="intership")

            cursor = connection.cursor()
            cursor.execute(f"""
               SELECT role FROM "user"
               WHERE "telegramId" = '{user.telegram_id}'
               """)
            role = cursor.fetchone()
            return role[0]

        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
        finally:
            if connection:
                connection.commit()
                cursor.close()
                connection.close()
                print("Соединение с PostgreSQL закрыто")

    @staticmethod
    def get_all_ids():
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="Casa512472;)",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="intership")

            cursor = connection.cursor()
            cursor.execute(f"""
            SELECT "telegramId" FROM "user"
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
    def get_traider_nickname_by_telegramid(traider_telegramid):
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="Casa512472;)",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="intership")

            cursor = connection.cursor()
            cursor.execute(f"""
            SELECT nickname FROM "user" WHERE "telegramId" = '{traider_telegramid}'
            """)

            result = cursor.fetchone()
            return result[0]
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
                print("Соединение с PostgreSQL закрыто")

    @staticmethod
    def create_subscribtion(user_telegram_id, traider_telegram_id):
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="Casa512472;)",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="intership")

            cursor = connection.cursor()
            cursor.execute(f"""
        INSERT INTO public."subscribe" ("userTelegramId", "traiderTelegramId") VALUES ('{user_telegram_id}', '{traider_telegram_id}')
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
    def check_subscribe():
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="Casa512472;)",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="intership")

            cursor = connection.cursor()
            cursor.execute(f"""
            SELECT "traiderTelegramId" FROM "subscribe" WHERE "userTelegramId" = '{user.telegram_id}'
        """)

            record = cursor.fetchone()
            if record:
                result = Data.get_traider_nickname_by_telegramid(record[0])
                return result
            return None

        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
        finally:
            if connection:
                connection.commit()
                cursor.close()
                connection.close()
                print("Соединение с PostgreSQL закрыто")

    @staticmethod
    def get_amount_of_referralers():
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="Casa512472;)",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="intership")

            cursor = connection.cursor()
            cursor.execute(f"""
            SELECT "userTelegramId" FROM "subscribe" WHERE "traiderTelegramId" = '{user.telegram_id}'
            """)

            record = cursor.fetchall()
            result = []
            for i in record:
                for j in i:
                    result.append(j)
            return len(result)
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
                print("Соединение с PostgreSQL закрыто")
