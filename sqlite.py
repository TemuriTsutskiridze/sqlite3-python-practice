import sqlite3
from employee import Employee

# conn=sqlite3.connect('employee.db')
# c=conn.cursor()
# c.execute("""CREATE TABLE IF NOT EXISTS employee(
#             first text,
#             last text,
#             pay integer
#     )""")
# c.execute("INSERT INTO employee VALUES('Elon', 'Mask', 50000)")
# c.execute("SELECT * FROM employee WHERE last = 'Mask'")
# print(c.fetchone())
# c.execute("INSERT INTO employee VALUES ('Kimbel', 'Mask', 50000)")
# conn.commit()
# c.execute("SELECT * FROM employee WHERE last = 'Mask'")
# print(c.fetchall())
# c.execute("INSERT INTO employee VALUES('Mary', 'Schafer', 50000)")
# emp_1 = Employee('Joe', 'Rogan', 80000)
# emp_2 = Employee('Jane', 'Rogan', 90000)
# c.execute("INSERT INTO employee VALUES(?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay))
# conn.commit()
# c.execute("INSERT INTO employee VALUES(:first, :last, :pay)", {'first': emp_2.first, 'last':emp_2.last, 'pay':emp_2.pay})
# conn.commit()
# print(emp_1.first)
# print(emp_1.last)
# print(emp_1.pay)
# c.execute("SELECT * FROM employee WHERE last = 'Mask'")
# print(c.fetchall())
# c.execute("SELECT * FROM employee WHERE last=?", ("Mask"))
# print(c.fetchall())
# c.execute("SELECT * FROM employee WHERE last=:last", {'last':'Rogan'})
# print(c.fetchall())
# conn.commit()
# conn.close()


# ------------------------------------------------------------

# conn = sqlite3.connect(':memory:')
# c = conn.cursor()
# c.execute("""CREATE TABLE employee(
#     first text,
#     last text,
#     pay integer    
#     )""")

# def insert_emp(emp):
#     with conn:
#         c.execute("INSERT INTO employee VALUES (:first, :last, :pay)", {'first':emp.first, 'last':emp.last, 'pay':emp.pay})
        
# def get_emps_by_name(lastname):
#     c.execute("SELECT * FROM employee WHERE last = :last", {'last': lastname})
#     return c.fetchall()

# def update_pay(emp, pay):
#     with conn:
#         c.execute("""UPDATE employee SET pay =:pay
#                   WHERE first = :first AND last =:last""",
#                   {'first': emp.first, 'last': emp.last, 'pay': emp.pay})
        
# def remove_emp(emp):
#     with conn:
#         c.execute("DELETE from employee WHERE first = :first AND last = :last",
#                   {'first': emp.first, 'last': emp.last})
        
# emp_1 = Employee('Joe', 'Rogan', 80000)
# emp_2 = Employee('Jane', 'Rogan', 90000)
# insert_emp(emp_1)
# insert_emp(emp_2)
# update_pay(emp_2, 9500000)
# remove_emp(emp_1)
# emps = get_emps_by_name('Rogan')
# print(emps)
# conn.close()




# ------------------------------------------------------

dbase = sqlite3.connect('gta.sqlite')
gta = dbase.cursor()
gta.execute("""CREATE TABLE IF NOT EXISTS gta(
    year integer,
    name text,
    city text
    )""")
list = [
    (1997, "GTA",'New Guernsey'),
    (1999, "GTA", "USA"),
    (2001, "GTA III","Liberty City"),
    (2002, "GTA:Vice City", "Vice City"),
    (2004, "GTA: San Andreas", "San Andreas"),
    (2008, "GTA IV", "Liberty City")
]
gta.executemany("INSERT INTO gta VALUES (?, ?, ?)", list)
for row in gta.execute("SELECT * FROM gta"):
    print(row)

print('**************')

gta.execute("select * from gta where city=:c", {"c":"Liberty City"})
gta_search = gta.fetchall()
print(gta_search)
gta.execute("""CREATE TABLE IF NOT EXISTS cities(
    gta_city text,
    real_city text
    )""")
gta.execute("INSERT INTO cities VALUES (?, ?)", ("Liberty City", "New York"))
gta.execute("SELECT * FROM cities WHERE gta_city=:c", {'c':"Liberty City"})
cities_search = gta.fetchall()
print(cities_search)

print("*********")

for i in gta_search:
    loop= [cities_search[0][1] if value==cities_search[0][0] else value for value in i]
    print(loop)
dbase.commit()
dbase.close()