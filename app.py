import os, logging, datetime
from main import FileWork
# from werkzeug.exceptions import HTTPException, default_exceptions, BadRequest

if os.stat("db_folder/DB_file.csv").st_size == 0:
   FileWork.up_file()
else:
   pass


from flask import Flask, render_template, url_for, request

logging.basicConfig(filename="logging/basic.log", level=logging.DEBUG)

logger_work = logging.getLogger("work")
logger_error = logging.getLogger("error")

file_handler_one = logging.FileHandler("logging/log_work.txt")
file_handler_two = logging.FileHandler("logging/log_error.txt")

logger_work.addHandler(file_handler_one)
logger_error.addHandler(file_handler_two)



app = Flask(__name__)

#--------> Ввод неправильного адреса
from werkzeug.exceptions import BadRequest, NotFound

@app.errorhandler(BadRequest)
def handle_bad_request(e):
    return render_template("critical.html"), 400

@app.errorhandler(NotFound)
def handle_bad_request(e):
    return render_template("critical.html"), 404

#-------->



@app.route("/") # домашняя страница
def main():
    try:
        logger_work.info(f"{datetime.datetime.now()} - there are no errors in the program <home.html>\n")

        return render_template("home.html")
    except:
        logger_error.critical(f"{datetime.datetime.now()} - critical error in the program <home.html>\n")
        return render_template("critical.html")


@app.route("/filter") # страница с таблицей
def fltr():
    try:

        s_d = request.args["s"]
        e_d = request.args["e"]
        ind_f = request.args["ind"]
        cou_f = int(request.args["cou"])

        df = FileWork.fltr(s = s_d, e = e_d, ind = ind_f, cou = cou_f)

        if df == "dataER":
            return render_template("dataER.html")
        elif df == "fileER":
            return render_template("fileER.html")
            
        logger_work.info(f"{datetime.datetime.now()} - there are no errors in the program <head.html>\n")
        
        return render_template("head.html", lst = df, s = s_d, e = e_d, ind = ind_f, cou = cou_f)
        
    except:

        logger_error.critical(f"{datetime.datetime.now()} - critical error in the program <head.html>\n")
        return render_template("critical.html")



@app.route("/search") # страница фильтров
def search():
    try:
        db_ind = FileWork.get_file_ind_lst()

        logger_work.info(f"{datetime.datetime.now()} - there are no errors in the program <search.html>\n")
        
        return render_template("search.html", db_ind = db_ind)
        
    except:
        logger_error.critical(f"{datetime.datetime.now()} - critical error in the program <search.html>\n")
        return render_template("critical.html")



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4554, debug=False)



