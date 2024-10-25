from flask import Blueprint, request

admin_api_bp = Blueprint('admin_api', __name__)

@admin_api_bp.route('/problems/<int:problem_id>', methods=['POST'])
def modify_item_api(problem_id):
    print(problem_id)
    print(request.form)
    return "OK"
