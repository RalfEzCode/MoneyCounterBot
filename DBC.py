import sqlite3 as sql
import traceback
from prettytable import PrettyTable

start_info = """
Легкое управление базой данных
1 - создать  базу данных
2 - показать базу данных
3 - 
4 - 
5 -
6 - 
7 - пользовательская команда
8 - отчистить базу данных
9 - выйти из программы
 """



# создаёт БД по выбранным параметрам
def create_db():
    con = sql.connect('info.db')
    name = input('название вашей БД: ')
    int_col = int(input('количество столбцов в БД: '))
    col_names = []
    sql_comm = f"CREATE TABLE IF NOT EXISTS '{name}' ("
    for i in range(int_col):
        col_names.append(input('название '+ str(i+1) +' столбца: '))
        sql_comm += f"'{col_names[i]}' STRING ,"
    sql_comm = sql_comm[:-1]
    sql_comm += ")"
    try:
        with con:
            cur = con.cursor()
            cur.execute(sql_comm)
            con.commit()
            cur.close()
            print('таблица успешно создана')
    except Exception as e:
        print('Ошибка:\n', traceback.format_exc())

# CREATE TABLE users (id INT AUTO_INCREMENT, login TEXT, pass VARCHAR, PRIMARY KEY (id))

# print("{:^10.3f}".format(12.2346))


# показывает всю базу данных
def show_db(name):
    con = sql.connect('info.db')
    try:
        with con:
            cur = con.cursor()
            cur.execute(f"SELECT * FROM `{name}`")
            rows = cur.fetchall()
            table = PrettyTable(['FROM','TO','HOW MUCH'])
            for row in rows:
                table.add_row(row)
            print(table)
            con.commit()
            cur.close()
    except Exception as e:
        print('Ошибка:\n', traceback.format_exc())
    return table

# показывает графики
def graph_db():
    print("Пока что не поддерживается (((((((((((((((")

# выполняет переданную sql комманду
def users_execute(comm):
    con = sql.connect('info.db')
    try:
        with con:
            cur = con.cursor()
            cur.execute(comm)
            con.commit()
            cur.close()
    except Exception as e:
        print('Ошибка:\n', traceback.format_exc())
#INSERT INTO `inoutcomes` VALUES (, 'УралСиб_А' ,'Покупки' ,'500')
#INSERT INTO `inoutcomes` (from, to, how_much) values('УралСиб_А' ,'Покупки' ,'500')


# удаляет информацию из БД, ! но не удаляет саму БД !
def clear_db(name):
    con = sql.connect('info.db')
    try:
        with con:
            cur = con.cursor()
            cur.execute(f"DROP TABLE `{name}`")
            print("Всё безвозвратно удалено ((((")
            con.commit()
            cur.close()
    except Exception as e:
        print('Ошибка:\n', traceback.format_exc())
# INSERT INTO `test` VALUES ('prod', '123' ,'Nal')
if __name__ == '__main__':
    print(start_info)
    while True:
        choice = input(""">>> """)
        if choice == "1":
            create_db()
        elif choice == "2":
            name = input('название нужнойй БД: ')
            show_db(name)
        elif choice == "3":
            print("Пока нет функционала))")
        elif choice == "4":
            print("Пока нет функционала))")
        elif choice == "5":
            print("Пока нет функционала))")
        elif choice == "6":
            print("Пока нет функционала))")
        elif choice == "7":
            comm = input('Ваша команда: ')
            users_execute(comm)
        elif choice == "8":
            if (input("""Вы уверены, что хотите удалить всю базу данных? 1 - да 
                >>> """) == "1"):
                name = input("Назовите БД, которую нужно удалить")
                clear_db(name)
            else:
                print("Чудно :)")
        elif choice == "9":
            break
        else:
            print("Ниче не понял, давай ещё раз")

# C:\Users\Андрей\АНДРЕЙ\Прогерство\Питон\Бот\MoneyCounterBot