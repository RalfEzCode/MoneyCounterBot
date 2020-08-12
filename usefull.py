import sqlite3 as sql
#Запись в локальную базу данных
def write_to_db(sourse_to_db, target_to_db, price_to_db):
    con = sql.connect('info.db')
    with con:
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS `inoutcomes` (`from` STRING, `to` STRING,`how_much` STRING)")
        cur.execute(f"INSERT INTO `inoutcomes` VALUES ('{sourse_to_db}', '{target_to_db}' ,'{price_to_db}')")
        con.commit()
        cur.close()
        print("Добавлено: "+sourse_to_db + " " + target_to_db + " " + price_to_db)
        target_to_db = 0
        price_to_db = 0
        sourse_to_db = 0

# Анализ информации из сообщения
def get_info_from_mess(mess):
    target_from_mess = ""
    price_from_mess = ""
    sourse_from_mess = ""
    way = 1
    for a in mess:
        if way == 1:
            if a == " ":
                way = 2
                continue
            target_from_mess += a

        elif way == 2:
            if a == " ":
                way = 3
                continue
            price_from_mess += a
        elif way == 3:
            sourse_from_mess += a
    if price_from_mess == "":
        raise Exception("No prise")
    if target_from_mess == "":
        raise Exception("No target")
    if sourse_from_mess == "":
        raise Exception("No sourse")
    return target_from_mess, price_from_mess, sourse_from_mess
