from flask import Flask # flask를 FLASK의 이름으로 불러온다,

app = Flask(__name__)

# 주소로 접속하면 hello를 반환한다. 즉 hello를 보여준다.
@app.route('/')
def hello():
    return "hello"

# main 함수 만들기
def main():
    app.run(debug=True,port=80) # flask 웹서버를 실행한다.
    
# 코드를 직접 실행 시 main() 함수를 실행한다.
if __name__ == '__main__':
    main()