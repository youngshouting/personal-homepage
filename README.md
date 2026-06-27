# 杨啸天 · 个人主页

硬件工程师个人主页，基于 Flask 构建。

## 本地运行

```bash
pip install -r requirements.txt
python app.py
```

浏览器打开 http://localhost:5000

## 技术栈

- 后端：Flask（Python）
- 模板：Jinja2
- 数据：JSON 文件
- 部署：Render（推荐）

## 项目结构

```
├── app.py              # Flask 应用入口
├── templates/          # Jinja2 模板
│   ├── base.html       # HTML 骨架
│   ├── components/     # 可复用组件
│   └── index.html      # 主页模板
├── static/
│   ├── css/style.css   # 样式表
│   └── js/main.js      # JavaScript
├── data/               # JSON 数据文件
├── conversations/      # 会话历史记录
└── utils/              # 工具函数
```

## 修改内容

所有页面文字内容在 `data/` 目录的 JSON 文件中管理，修改无需动模板。
