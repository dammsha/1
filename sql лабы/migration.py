from фу import DB_request
import sqlite3


if __name__ == '__main__':
    request = DB_request()
    con = sqlite3.connect("FBD.sqlite3")
    cur = con.cursor()
    cur.execute("""CREATE TABLE employees(id integer primary key autoincrement, 
                                        ФИО, 
                                        Зарплата, 
                                        Премия, 
                                        "Формальная должность", 
                                        Отдел, 
                                        Признаки)""")
    for employee in request.employee_list:
        cur.execute(f"""INSERT INTO employees VALUES 
(NULL,'{employee['ФИО']}',	{employee['Зарплата']},	{employee['Премия']}, '{employee['Формальная должность']}', '{employee['Отдел']}', '{employee['Признаки']}')
         """)

    cur.execute("""CREATE TABLE projects(id integer primary key autoincrement, 
                                        Проект, 
                                        "Наименование задачи", 
                                        Должность, 
                                        Стоимость, 
                                        "Чистая стоимость", 
                                        Признаки)""")
    for project in request.project_list:
        cur.execute(f"""INSERT INTO projects VALUES 
(NULL,'{project['Проект']}',	 '{project['Наименование задачи']}', '{project['Должность']}', {project['Стоимость']}, {project['Чистая стоимость']}, '{project['Признаки']}')
            """)

    cur.execute("""CREATE TABLE payments(id integer primary key autoincrement, 
                                        Дата, 
                                        Сотрудник, 
                                        Проект, 
                                        "Наименование задачи", 
                                        Должность)""")
    for payment in request.payment_list:
        cur.execute(f"""INSERT INTO payments VALUES 
(NULL,'{payment['Дата']}',	'{payment['Сотрудник']}',	'{payment['Проект']}', '{payment['Наименование задачи']}', '{payment['Должность']}')
        """)

    con.commit()
