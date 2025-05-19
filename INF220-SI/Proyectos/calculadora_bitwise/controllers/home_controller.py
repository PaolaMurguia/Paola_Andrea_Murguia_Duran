from flask import render_template, request
from models.bitwise_model import perform_operation

def index():
    return render_template("index.html")

def calculate():
    try:
        num1 = int(request.form.get("num1", 0))
        num2 = request.form.get("num2")
        op = request.form.get("operation")
        size = request.form.get("size")

        num2 = int(num2) if num2 else None
        result = perform_operation(num1, num2, op, size)

        return render_template("index.html", result=result, num1=num1, num2=num2, op=op, size=size)

    except Exception as e:
        return render_template("index.html", error=str(e))
