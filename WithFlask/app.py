from flask import Flask, render_template, redirect
import prefect

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")


@prefect.task(name="flow1_task1")
def task1():
    print("execute task 1")


def task2():
    print("execute task 2")


@prefect.flow(name="flow1")
def flow1():
    print("execute flow 1")
    task1()
    task2()


@app.route("/flow1")
def flow1_route():
    # NOTE: A Flask route can't also be Prefect flow, you must wrap it before invoking it
    flow1()
    return redirect("/")


if __name__ == "__main__":
    app.run()
