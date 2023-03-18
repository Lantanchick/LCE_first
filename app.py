import requests, os

def up_file():
    url = "https://www.dropbox.com/s/ru96yt1m92xdltx/stocks_price_final.csv?dl=1"
    fl = requests.get(url)
    with open("exercise\LCE_first\db_folder/DB_file.csv", "wb") as file:
        file.write(fl.content)

if os.stat("exercise\LCE_first\db_folder/DB_file.csv").st_size == 0:
   up_file()
else:
   pass

import df_up, datetime
from flask import Flask, render_template, url_for, request
app = Flask(__name__)



@app.route("/")
def main():
    return render_template("home.html")


@app.route("/filter")
def fltr():
    s = request.args["s_d"]
    e = request.args["e_d"]
    ind = request.args["ind"]

    if "False" == ind:
        ind = False

    if datetime.datetime.strptime(s, "%Y-%m-%d") > datetime.datetime.strptime(e, "%Y-%m-%d"):
        return render_template("dataER.html")
    
    name = "Билалов Эмирлан"
    df = df_up.getDF(start_data = s, end_data = e, industry = ind)
    df = df.head(1000)

    return render_template("head.html", name = name, lst = df)


@app.route("/search")
def search():
    db_ind = df_up.getInd().head(df_up.getInd().count())
    return render_template("search.html", db_ind = db_ind)



if __name__ == "__main__":
    app.run()



