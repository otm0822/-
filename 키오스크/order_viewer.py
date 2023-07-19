from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def order_viewer():
    orders = []
    try:
        # 파일을 UTF-8 인코딩으로 읽어오기
        with open("orders.txt", "r", encoding="utf-8") as f:
            orders = f.readlines()
    except FileNotFoundError:
        pass

    return render_template("order_viewer.html", orders=orders)

if __name__ == "__main__":
    app.run(debug=True, port=5002)
