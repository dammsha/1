import sqlite3

class Fill_DB():
    def __init__(self):
        con = sqlite3.connect("FBD.sqlite3")
        cur = con.cursor()
        cur.execute("""DELETE FROM payments where Статус =  0""")
        con.commit()
        cur.execute("""select projects.Проект, 
        projects."Наименование задачи",  
        projects."Чистая стоимость", 
        sum(ifnull(employees.Зарплата + employees.Премия,0))
    from projects
    left join payments
        on projects.Проект = payments.Проект and 
            projects."Наименование задачи" = payments."Наименование задачи"
    left join employees
        on payments.Сотрудник = employees.ФИО
    group by projects.Проект, 
        projects."Наименование задачи",  
        projects."Чистая стоимость" """)
        project_limits = {}
        for row in cur.fetchall():
            project_limits[(row[0], row[1])] = row[2] - row[3]
        cur.execute("""select 
    projects.Проект,
    projects."Наименование задачи",
    projects."Чистая стоимость",
    projects.Признаки, 
    projects.Должность,
    employees.ФИО,
    (employees.Зарплата + employees.Премия) as Cost
from projects
join employees
on projects.Признаки = employees.Признаки and projects.Должность = employees."Формальная должность"
where projects."Чистая стоимость" >= (employees.Зарплата + employees.Премия + 1000)""")
        for row in cur.fetchall():
            if project_limits[(row[0], row[1])] >= (row[6] + 1000):
                cur.execute(f"""INSERT INTO payments VALUES
                        (NULL,'2023-09-01 00:00:00',	'{row[5]}',	'{row[0]}', '{row[1]}', '{row[4]}', 0)
                                """)
                project_limits[(row[0], row[1])] -= row[6]

        con.commit()

if __name__ == '__main__':
    Fill_DB()

