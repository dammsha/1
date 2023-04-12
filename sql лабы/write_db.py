import sqlite3
from read_db_sql import meta_employee, meta_projects, meta_payment, DB_request


class Create_new_DB():

    def __init__(self, payment_list):
        request = DB_request()
        self.project_list = request.project_list
        self.employee_list = request.employee_list
        self.get_name()

        black_list_project = []
        # проверка остатка сумм по задачам проекта
        for payment in payment_list:
            employee = self.get_employee(payment['Сотрудник'])
            project = self.get_project(payment['Проект'], payment['Наименование задачи'])
            project['Чистая стоимость'] = project['Чистая стоимость'] - employee['Зарплата'] - employee['Премия']
            if project['Чистая стоимость'] < 1000:
                black_list_project.append((payment['Проект'], payment['Наименование задачи']))
        self.payment_list = []
        # убираем все выплаты по задаче по проекту, если лимит по этой задаче был привышен
        for payment in payment_list:
            if (payment['Проект'], payment['Наименование задачи']) not in black_list_project:
                self.payment_list.append(payment)


    def save_DB(self):
        con = sqlite3.connect("FBD.sqlite3")
        cur = con.cursor()
        cur.execute('DELETE FROM payments where Статус = 1')
        for payment in self.payment_list:
            cur.execute(f"""INSERT INTO payments VALUES
        (NULL,'{payment['Дата']}',	'{payment['Сотрудник']}',	'{payment['Проект']}', '{payment['Наименование задачи']}', '{payment['Должность']}', 1)
                """)
        con.commit()

    def get_project(self, project_name, task_name):
        for project in self.project_list:
            if (project['Проект'] == project_name) and (project['Наименование задачи'] == task_name):
                return project


    def get_employee(self, name):
        for employee in self.employee_list:
            if employee['ФИО'] == name:
                return employee


    def get_name(self):
        return 'FBD.sqlite3'


