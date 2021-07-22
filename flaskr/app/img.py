from flask import Blueprint, request, jsonify

from flaskr.utils.db_utils import get_img, insert_img

img = Blueprint('img', __name__)


@img.route('/<product_id>', methods=['GET'])
def get_product_image(product_id):
    record = get_img("tests/db.db", product_id)
    if not record:
        return "", 204
    response = [{"img": record[i][0].decode('utf-8', 'ignore')} for i in range(len(record))]
    return jsonify(response)


@img.route('/<product_id>', methods=['POST'])
def insert_image(product_id):
    if not request.files["img"]:
        return "", 400
    image = request.files["img"].stream.read()
    content_type = request.files["img"].content_type
    insert_img("tests/db.db", product_id, image, content_type)
    return "", 200
