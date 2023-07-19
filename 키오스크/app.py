from flask import Flask, render_template, request, redirect, url_for
import time

app = Flask(__name__)

menu = {
    "음료1": "밀키블루소다",
    "음료2": "체리콕",
    "음료3": "우주에이드",
    "빙수1": "멜론 빙수",
    "빙수2": "망고 빙수",
    "빙수3": "레인보우 빙수"
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        product = request.form["product"]
        count = request.form["count"]
        order = f"{count}개의 {menu[product]}"

        # 주문 정보를 파일에 저장 (UTF-8 인코딩)
        with open("orders.txt", "a", encoding="utf-8") as f:
            f.write(order + "\n")

        return render_template("order_confirmation.html", order=order)
    else:
        return render_template("index.html", products=menu.keys())

# ... 나머지 코드는 그대로 두세요 ...

if __name__ == "__main__":
    app.run(debug=True, port=5000)
