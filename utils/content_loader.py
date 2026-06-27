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


def load_project(project_id):
    """读取 data/projects/<id>.json，返回单个项目详情。"""
    filepath = DATA_DIR / "projects" / f"{project_id}.json"
    if not filepath.exists():
        return None
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def get_all_projects():
    """扫描 data/projects/ 目录，返回所有项目简要列表。"""
    projects_dir = DATA_DIR / "projects"
    if not projects_dir.exists():
        return []
    projects = []
    for fpath in sorted(projects_dir.glob("*.json")):
        with open(fpath, "r", encoding="utf-8") as f:
            data = json.load(f)
        projects.append(data)
    return projects


def get_all_content():
    """收集所有主页数据，作为模板上下文一次性返回。"""
    return {
        "profile": load_json("profile.json"),
        "projects": get_all_projects(),
        "skills": load_json("skills.json"),
        "contact": load_json("contact.json"),
        "education": load_json("education.json"),
        "internship": load_json("internship.json"),
        "honors": load_json("honors.json"),
    }
