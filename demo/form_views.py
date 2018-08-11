from django.shortcuts import render, redirect
from .forms import AddDeptForm
import sqlite3


def add_dept(request):
    message = ""

    if request.method == "POST":
        f = AddDeptForm(request.POST)  # Copy data from request to form
        if f.is_valid():
            deptname = f.cleaned_data["deptname"]
            location = f.cleaned_data["location"]

            try:
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
        else:
            message = "Invalid input. Please correct and resubmit form!"
    else:
        f = AddDeptForm()

    return render(request, 'forms/add_dept.html', {'form': f, 'message': message})
