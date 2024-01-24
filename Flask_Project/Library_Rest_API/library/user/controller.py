from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from flasgger import swag_from


# Tạo đối tượng User thử nghiệm token
class User:
    username = "nguyenluan"
    password = "170502"


user = Blueprint("user", __name__, url_prefix="/user")


# Endpoint đăng nhập để nhận Access Token và Refresh Token
@user.route('/login', methods=['POST'])
@swag_from("docs/login.yaml")
def login():
    if not request.is_json:
        return jsonify({"message": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if not username or not password:
        return jsonify({"message": "Missing username or password"}), 400

    # Kiểm tra thông tin đăng nhập (điều này nên kiểm tra trong cơ sở dữ liệu)
    if username == User.username and password == User.password:
        # Tạo Access Token và Refresh Token
        access_token = create_access_token(identity=User.username)
        refresh_token = create_refresh_token(identity=User.username)

        return jsonify(username=username, password=password,
                       access_token=access_token, refresh_token=refresh_token), 200
    else:
        return jsonify({"message": "Invalid username or password"}), 401


# Làm mới Access Token bằng Refresh Token
@user.route('/refresh-token', methods=['POST'])
@jwt_required(refresh=True)
@swag_from("docs/refresh.yaml")
def refresh():
    current_user = get_jwt_identity()
    new_access_token = create_access_token(identity=current_user)

    return jsonify(access_token=new_access_token), 200


@user.route("/me", methods=['GET'])
@jwt_required()
@swag_from("docs/me.yaml")
def me():
    # Lấy thông tin người dùng từ Access Token
    current_user = get_jwt_identity()
    # Đoạn này có thể thực hiện các hoạt động khác tùy thuộc vào ứng dụng của bạn
    # Ví dụ: Truy vấn cơ sở dữ liệu để lấy thông tin chi tiết về người dùng
    if User.username == current_user:
        return jsonify({
            'username': User.username,
            'password': User.password
        }), 200
