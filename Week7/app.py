from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session
from flask import jsonify
import mysql.connector


#*資料庫參數設定
db_settings = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "123456789",
    "db": "week6",
    "charset": "utf8"
}

app=Flask(
    __name__,
    static_folder="static",
    static_url_path="/static"
)

app.secret_key = "secret string"

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form["name"]
        username = request.form["username"]
        password = request.form["password"]

        try:
            #* 資料庫連線
            conn = mysql.connector.connect(**db_settings)
            cursor = conn.cursor()

            #* 檢查是否有相同帳號資料
            check_username_query = "SELECT * FROM users WHERE username = %s"
            cursor.execute(check_username_query, (username,))
            existing_username = cursor.fetchone()

            if existing_username:
                return redirect("/error?message=帳號已經被註冊")

            #* 檢查是否有相同姓名資料
            check_name_query = "SELECT * FROM users WHERE name = %s"
            cursor.execute(check_name_query, (name,))
            existing_name = cursor.fetchone()

            if existing_name:
                return redirect("/error?message=姓名已被使用")

            #*將新建的資料放入資料庫
            insert_query = "INSERT INTO users (name, username, password) VALUES (%s, %s, %s)"
            cursor.execute(insert_query, (name, username, password))
            conn.commit()

            #*設定session
            session["signed_in"] = True
            return redirect("/")  #* 註冊成功回到首頁
        except mysql.connector.Error as err:
            print(err)
            return redirect("/error?message=資料庫錯誤")
        finally:
            if conn:
                conn.close()
    else:
        return render_template("index.html")


#*處理index
@app.route("/", methods=["GET"])
def home():
    if not session.get("signed_in"):
        return redirect("/signup") 
    return render_template("index.html")


#*處理sign in
@app.route("/signin", methods=["POST"])
def signin():
    #* 取得html中資料
    username = request.form["username"]
    password = request.form["password"] 

    try:
        #* 連線資料庫
        conn = mysql.connector.connect(**db_settings)
        cursor = conn.cursor()

        #* 查看帳號密碼是否相同
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        user_data = cursor.fetchone()

        #*如果相同就登入
        if user_data:
            session["signed_in"] = True
            session["name"] = user_data[1]
            session["user_id"] = user_data[0] 
            return redirect("/member")
        #*如果不相同就跳error
        else:
            return redirect("/error?message=帳號或密碼錯誤")

    except mysql.connector.Error as err:
        print(err)
        return redirect("/error?message=資料庫錯誤")
    finally:
        if conn:
            conn.close()

@app.route("/api/member", methods=["GET"])
def get_member_info():
    username = request.args.get("username")

    try:
        conn = mysql.connector.connect(**db_settings)
        cursor = conn.cursor()

        select_query = "SELECT * FROM users WHERE username = %s"
        cursor.execute(select_query, (username,))
        member_data = cursor.fetchone()

        if member_data:
            member_info = {
                "id": member_data[0],
                "name": member_data[1],
                "username": member_data[2]
            }
            return jsonify({"data": member_info})
        else:
            return jsonify({"data": None})

    except mysql.connector.Error as err:
        print(err)  # 打印错误信息
        return jsonify({"data": None})
    finally:
        if conn:
            conn.close()

@app.route("/api/member", methods=["PATCH"])
def update_member_name():
    if not session.get("signed_in"):
        return jsonify({"error": True})

    new_name = request.json.get("name")

    try:
        conn = mysql.connector.connect(**db_settings)
        cursor = conn.cursor()

        update_query = "UPDATE users SET name = %s WHERE id = %s"
        cursor.execute(update_query, (new_name, session.get("user_id")))
        conn.commit()

        return jsonify({"ok": True})

    except mysql.connector.Error as err:
        print(err)
        return jsonify({"error": True})
    finally:
        if conn:
            conn.close()



@app.route("/member", methods=["GET"])
def member():
    if not session.get("signed_in"):
        return redirect("/signup")

    try:
        #* 連線資料庫
        conn = mysql.connector.connect(**db_settings)
        cursor = conn.cursor()

        #* 將users及messages結合
        select_query = """
            SELECT messages.content, users.name, messages.user_id, messages.message_id
            FROM messages
            INNER JOIN users ON messages.user_id = users.id ORDER BY timestamp DESC
        """
        cursor.execute(select_query)
        messages = cursor.fetchall()

        #* 取得姓名
        user_name = session.get("name")
        #* 取得ID
        user_id = session.get("user_id")  
        return render_template("member.html", user_name=session.get("name"), messages=messages, user_id=session.get("user_id"))


    except mysql.connector.Error as err:
        print(err)
        return redirect("/error?message=資料庫錯誤")
    finally:
        if conn:
            conn.close()



@app.route("/signout", methods=["GET"])
def signout():
    session["signed_in"]=False
    print(session)
    return redirect("/")

@app.route("/error", methods=["GET"])
def error():
    print(session)
    message = request.args.get("message")
    return render_template("error.html", message=f"{message}")

#*啟動網站伺服器
app.run(port=3000)