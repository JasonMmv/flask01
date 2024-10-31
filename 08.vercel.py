from flask import Flask, request, jsonify

app = Flask(__name__)

# POST 방식으로 두 개의 파라미터를 처리하는 API 엔드포인트
@app.route('/api/greet', methods=['POST'])
def greet():
    # 요청의 JSON 데이터를 가져옵니다.
    data = request.get_json()
    name = data.get('name', 'world')
    age = data.get('age', 'unknown')
    
    # 메시지 생성
    message = f"Hello, {name}! You are {age} years old."
    
    # JSON 응답 생성
    return jsonify({'message': message})

# 메인 함수로 서버 실행
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)