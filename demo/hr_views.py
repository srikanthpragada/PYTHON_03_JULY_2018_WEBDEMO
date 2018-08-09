from django.shortcuts import render, redirect
import sqlite3


def add_dept(request):
    deptname = ''
    location = ''
    message = ""
    if request.method == "POST":
        try:
            deptname = request.POST["deptname"]
            location = request.POST["location"]
            con = sqlite3.connect(r"e:\classroom\python\july3\hr.db")  # Connection
            cur = con.cursor()  # Cursor
            cur.execute("insert into departments(deptname,location) values(?,?)",
                        (deptname, location))
            con.commit()
            message = "Added Department Successfully!"
        except Exception as ex:
            message = "Sorry! Unable to add department"
            print(ex)
        finally:
            con.close()

    return render(request, 'add_dept.html',
                  {'deptname': deptname,
                   'location': location,
                   'message': message}
                  )


def list_dept(request):
    con = sqlite3.connect(r"e:\classroom\python\july3\hr.db")  # Connection
    cur = con.cursor()  # Cursor
    cur.execute("select * from departments order by deptid")
    depts = cur.fetchall()
    con.close()
    return render(request, 'list_dept.html', {'depts': depts})


def delete_dept(request):
    try:
        deptid = request.GET["deptid"]
        con = sqlite3.connect(r"e:\classroom\python\july3\hr.db")  # Connection
        cur = con.cursor()  # Cursor
        cur.execute("delete from departments where deptid = ?", (deptid,))
        con.commit()
    except Exception as ex:
        print(ex)
    finally:
        con.close()

    return redirect("/demo/listdept")
