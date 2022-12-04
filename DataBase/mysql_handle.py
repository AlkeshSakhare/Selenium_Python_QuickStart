import mysql.connector


def dml_query(query):
    con = mysql.connector.connect(host="localhost", port="3306",
                                  user="root", passwd="root", database="employees")
    curs = con.cursor()
    curs.execute(query)
    con.commit()
    con.close()


def select_query(query):
    con = mysql.connector.connect(host="localhost", port="3306",
                                  user="root", passwd="root", database="employees")
    curs = con.cursor()
    curs.execute(query)
    for row in curs:
        print(row[0], row[1])
    con.close()


select = "select * from employees.departments order by dept_no"
insert_query = "insert into departments values('d011', 'Media')"
update_query = "update departments set dept_name='MEDIA' where dept_name = 'Media'"
delete_query = "delete from departments where dept_no='d011'"
print("********SELECT QUERY*********")
select_query(select)
print("********INSERT QUERY*********")
dml_query(insert_query)
print("********SELECT QUERY*********")
select_query("select * from employees.departments where dept_no='d011'")
print("********UPDATE QUERY*********")
dml_query(update_query)
print("********SELECT QUERY*********")
select_query("select * from employees.departments where dept_no='d011'")
print("********DELETE QUERY*********")
dml_query(delete_query)
print("********SELECT QUERY*********")
select_query(select)
