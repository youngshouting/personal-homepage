"""个人主页 Flask 应用。"""

import os
import json
from pathlib import Path
from datetime import datetime

from flask import (
    Flask,
    render_template,
    request,
    flash,
    redirect,
    url_for,
    abort,
)
from flask_wtf.csrf import CSRFProtect

from utils.content_loader import get_all_content, load_project

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "dev-secret-key-change-in-production")
csrf = CSRFProtect(app)


@app.route("/")
def home():
    """渲染主页。"""
    content = get_all_content()
    return render_template("index.html", **content)


@app.route("/project/<project_id>")
def project_detail(project_id):
    """项目详情页。"""
    project = load_project(project_id)
    if project is None:
        abort(404)
    return render_template("project_detail.html", project=project)


@app.route("/contact", methods=["POST"])
def contact():
    """处理联系表单提交。"""
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    # 简单验证
    errors = []
    if not name:
        errors.append("请输入姓名")
    if not email or "@" not in email:
        errors.append("请输入有效的邮箱地址")
    if not message or len(message) < 10:
        errors.append("留言至少 10 个字符")

    if errors:
        for err in errors:
            flash(err, "error")
        return redirect(url_for("home") + "#contact")

    # 保存到 data/messages.json 作为日志
    messages_file = Path(__file__).parent / "data" / "messages.json"
    record = {
        "name": name,
        "email": email,
        "message": message,
        "timestamp": datetime.now().isoformat(),
    }

    if messages_file.exists():
        with open(messages_file, "r", encoding="utf-8") as f:
            try:
                messages = json.load(f)
            except json.JSONDecodeError:
                messages = []
    else:
        messages = []

    messages.append(record)
    with open(messages_file, "w", encoding="utf-8") as f:
        json.dump(messages, f, ensure_ascii=False, indent=2)

    flash("留言已收到，感谢你的联系！", "success")
    return redirect(url_for("home") + "#contact")


@app.route("/health")
def health():
    """健康检查端点（部署平台需要）。"""
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
