"""读取 data/ 目录下的 JSON 数据文件，提供给模板使用。"""

import json
import os
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def load_json(filename):
    """读取 data/ 下的 JSON 文件，返回 Python 对象。"""
    filepath = DATA_DIR / filename
    if not filepath.exists():
        return {}
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def get_all_content():
    """收集所有数据，作为模板上下文一次性返回。"""
    return {
        "profile": load_json("profile.json"),
        "projects": load_json("projects.json"),
        "skills": load_json("skills.json"),
        "contact": load_json("contact.json"),
    }
