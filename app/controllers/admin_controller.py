from flask import Blueprint, render_template

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/modify/')
def modify_item():
    vue = render_template('views/modify.vue',
                          problem_id=3,
                          name="測試商品",
                          tags="測試 物件",
                          existingImages='[{"id":1, "url": "https://sandb0x.tw/s/NERV.png"},'
                                          '{"id":2, "url": "https://sandb0x.tw/s/NERV.png"}]',
                          description="測試內容")
    return render_template('main.html',
                           title="Test",
                           content=vue,
                           footer="Test Website")
