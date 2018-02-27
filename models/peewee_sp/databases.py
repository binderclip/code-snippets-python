from mysql_conn import MYSQL_DB_NAME, conn


def create_database():
    conn.cursor().execute(
        f'CREATE DATABASE IF NOT EXISTS {MYSQL_DB_NAME} '
        'DEFAULT CHARACTER SET utf8mb4 '
        'DEFAULT COLLATE utf8mb4_unicode_ci;',
    )
    print('=== create database done ===')


def drop_database():
    conn.cursor().execute(f'DROP DATABASE IF EXISTS {MYSQL_DB_NAME};')
    print('=== drop database done ===')


def main():
    create_database()
    drop_database()
    conn.close()


if __name__ == '__main__':
    main()
