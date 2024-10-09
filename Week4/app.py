from flask import Flask
from flask import request
from flask import render_template
from flask import redirect


app=Flask(
    __name__,
    static_folder="static",
    static_url_path="/static"
)
signed_in = False

#*處理index
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

#*處理sign in
@app.route("/signin", methods=["POST"])
def signin():
    global signed_in

    #* 取得html中資料
    username = request.form["username"]
    password = request.form["password"] 
    #* 驗證身分
    if username == "test" and password == "test":
        # *如果成功了就會到會員頁面
        signed_in = True
        return redirect("/member")
    else:
        #* 如果不成功就會
        return redirect("/error?message=帳號或密碼錯誤")



@app.route("/member", methods=["GET"])
def member():
    if not signed_in:
        return redirect("/")
    #* 返回會員頁面
    return render_template("member.html")

@app.route("/signout", methods=["GET"])
def signout():
    global signed_in
    signed_in = False
    return redirect("/")

@app.route("/error", methods=["GET"])
def error():
    #* Get the error message from the URL query parameter
    message = request.args.get("message")
    #* Return the Error Page with the error message
    return render_template("error.html", message=f"{message}")





#*啟動網站伺服器
app.run(port=3000)