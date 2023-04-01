import sqlite3


meta_employee = {0: 'ФИО', 1: 'Зарплата', 2: 'Премия', 3: 'Формальная должность', 4: 'Отдел', 5: 'Признаки'}
meta_projects = {0: 'Проект', 1: 'Наименование задачи', 2: 'Должность', 3: 'Стоимость', 4: 'Чистая стоимость',
                 5: 'Признаки'}
meta_payment = {0: 'Дата', 1: 'Сотрудник', 2: 'Проект', 3: 'Наименование задачи', 4: 'Должность'}


class DB_request():

    def __init__(self):
        con = sqlite3.connect("FBD.sqlite3")
        cur = con.cursor()
        cur.execute("SELECT * FROM employees")
        row = cur.fetchall()
        self.employee_list = []
        for row in row:
            dict_temp = {}
            for colm in range(len(meta_employee)):
                dict_temp[meta_employee[colm]] = row[colm]
            self.employee_list.append(dict_temp)


        cur.execute("SELECT * FROM projects")
        row = cur.fetchall()
        self.project_list = []
        for row in row:
            dict_temp = {}
            for colm in range(len(meta_projects)):
                dict_temp[meta_projects[colm]] = row[colm]
            self.project_list.append(dict_temp)


        cur.execute("SELECT * FROM payments")

        row = cur.fetchall()
        self.payment_list = []
        for row in row:
            dict_temp = {}
            for colm in range(len(meta_payment)):
                dict_temp[meta_payment[colm]] = row[colm]
            self.payment_list.append(dict_temp)


if __name__ == '__main__':
    request = DB_request()
    for employee in request.employee_list:
        print(employee)
    for project in request.project_list:
        print(project)
    for payment in request.payment_list:
        print(payment)


