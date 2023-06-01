import psycopg2
from psycopg2 import Error

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
            if result is None:
                return []
            return result
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
                print("Соединение с PostgreSQL закрыто")

    @staticmethod
    def create_record_user(telegram_id, username):
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="Casa512472;)",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="intership")

            cursor = connection.cursor()
            cursor.execute(f"""
        INSERT INTO public."user" ("telegramId", username, role) 
        VALUES ('{telegram_id}', '{username}', 'User')
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
    def update_data_user_nickname(telegram_id, nickname):
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="Casa512472;)",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="intership")

            cursor = connection.cursor()
            cursor.execute(f"""
        UPDATE "user" SET nickname = '{nickname}'
        WHERE "telegramId" = '{telegram_id}'
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
    def update_data_user_api(telegram_id, api):
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="Casa512472;)",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="intership")

            cursor = connection.cursor()
            cursor.execute(f"""
        UPDATE "user" SET "apiKey" = '{api}'
        WHERE "telegramId" = '{telegram_id}'
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
    def update_data_user_key(telegram_id, secret_key):
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="Casa512472;)",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="intership")

            cursor = connection.cursor()
            cursor.execute(f"""
        UPDATE "user" SET "secretKey" = '{secret_key}'
        WHERE "telegramId" = '{telegram_id}'
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
    def update_data_user_become_traider(telegram_id):
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="Casa512472;)",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="intership")

            cursor = connection.cursor()
            cursor.execute(f"""
               UPDATE "user" SET role = 'Traider'
               WHERE "telegramId" = '{telegram_id}'
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
    def get_balance(telegram_id):
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="Casa512472;)",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="intership")

            cursor = connection.cursor()
            cursor.execute(f"""
               SELECT balance FROM "user"
               WHERE "telegramId" = '{telegram_id}'
               """)

            balance = cursor.fetchone()
            if balance is not None:
                balance_2 = int(balance[0])
                return balance_2
            else:
                return 0

        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
        finally:
            if connection:
                connection.commit()
                cursor.close()
                connection.close()
                print("Соединение с PostgreSQL закрыто")

    @staticmethod
    def top_up_balance(telegram_id, balance):
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="Casa512472;)",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="intership")

            cursor = connection.cursor()
            if Data.get_balance(telegram_id) is None:
                final_balance = int(balance)
            else:
                final_balance = int(Data.get_balance(telegram_id)) + int(balance)
            cursor.execute(f"""
               UPDATE "user" SET balance = '{final_balance}'
               WHERE "telegramId" = '{telegram_id}' 
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
    def get_role(telegram_id):
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="Casa512472;)",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="intership")

            cursor = connection.cursor()
            cursor.execute(f"""
               SELECT role FROM "user"
               WHERE "telegramId" = '{telegram_id}'
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
    def check_subscribe(telegram_id):
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="Casa512472;)",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="intership")

            cursor = connection.cursor()
            cursor.execute(f"""
            SELECT "traiderTelegramId" FROM "subscribe" WHERE "userTelegramId" = '{telegram_id}'
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
    def get_amount_of_referralers(telegram_id):
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="Casa512472;)",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="intership")

            cursor = connection.cursor()
            cursor.execute(f"""
            SELECT "userTelegramId" FROM "subscribe" WHERE "traiderTelegramId" = '{telegram_id}'
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

    @staticmethod
    def get_api(telegram_id):
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="Casa512472;)",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="intership")

            cursor = connection.cursor()
            cursor.execute(f"""
            SELECT "apiKey" FROM "user" WHERE "telegramId" = '{telegram_id}'
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
    def get_secret(telegram_id):
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="Casa512472;)",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="intership")

            cursor = connection.cursor()
            cursor.execute(f"""
            SELECT "secretKey" FROM "user" WHERE "telegramId" = '{telegram_id}'
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
    def get_nickname(telegram_id):
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="Casa512472;)",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="intership")

            cursor = connection.cursor()
            cursor.execute(f"""
            SELECT "nickname" FROM "user" WHERE "telegramId" = '{telegram_id}'
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
    def update_data_user_mailing(telegram_id, text):
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="Casa512472;)",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="intership")

            cursor = connection.cursor()
            cursor.execute(f"""
        UPDATE "user" SET "description" = '{text}'
        WHERE "telegramId" = '{telegram_id}'
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
    def get_mailing(telegram_id):
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="Casa512472;)",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="intership")

            cursor = connection.cursor()
            cursor.execute(f"""
            SELECT "description" FROM "user" WHERE "telegramId" = '{telegram_id}'
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

