#!/usr/bin/env python3
"""Auto-commit script for maintaining GitHub activity."""

import os
import json
import random
from datetime import datetime, timedelta

# 贡献类型
CONTRIBUTION_TYPES = [
    "update_readme",
    "add_changelog",
    "update_dependencies",
    "add_documentation",
    "fix_typos",
    "update_examples",
]


def update_changelog():
    """更新CHANGELOG"""
    today = datetime.now().strftime("%Y-%m-%d")
    entry = f"\n## {today}\n- Updated project documentation\n- Minor improvements\n"
    
    if os.path.exists("CHANGELOG.md"):
        with open("CHANGELOG.md", "r") as f:
            content = f.read()
        # 在文件开头添加新条目
        lines = content.split("\n")
        insert_pos = 3  # 在标题后插入
        lines.insert(insert_pos, entry)
        content = "\n".join(lines)
    else:
        content = f"# Changelog\n\n{entry}"
    
    with open("CHANGELOG.md", "w") as f:
        f.write(content)
    print("📝 Updated CHANGELOG.md")


def update_stats():
    """更新统计文件"""
    stats = {
        "last_updated": datetime.now().isoformat(),
        "commit_count": random.randint(100, 1000),
        "project_count": random.randint(5, 20),
    }
    with open("stats.json", "w") as f:
        json.dump(stats, f, indent=2)
    print("📊 Updated stats.json")


def update_daily_log():
    """更新每日日志"""
    today = datetime.now().strftime("%Y-%m-%d")
    log_entry = f"\n### {today}\n- Worked on open source projects\n- Reviewed pull requests\n- Updated documentation\n"
    
    log_file = "daily-log.md"
    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            content = f.read()
    else:
        content = "# Daily Development Log\n"
    
    content += log_entry
    with open(log_file, "w") as f:
        f.write(content)
    print(f"📅 Updated daily-log.md for {today}")


def update_project_list():
    """更新项目列表"""
    projects = [
        {"name": "ai-commit", "desc": "AI commit message generator", "stars": random.randint(0, 50)},
        {"name": "repo-stats", "desc": "GitHub repo analyzer", "stars": random.randint(0, 30)},
        {"name": "prompt-bench", "desc": "LLM benchmarking tool", "stars": random.randint(0, 20)},
        {"name": "multi-post", "desc": "Multi-platform publisher", "stars": random.randint(0, 40)},
    ]
    
    content = "# My Projects\n\n"
    content += f"_Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}_\n\n"
    content += "| Project | Description |\n|---------|-------------|\n"
    for p in projects:
        content += f"| [{p['name']}](https://github.com/Alex-2Code/{p['name']}) | {p['desc']} |\n"
    
    with open("projects.md", "w") as f:
        f.write(content)
    print("📦 Updated projects.md")


def main():
    """主函数 - 随机选择一种贡献类型"""
    print("🤖 Auto-commit script started...")
    
    # 随机选择1-2种更新类型
    num_updates = random.randint(1, 2)
    selected = random.sample(CONTRIBUTION_TYPES, min(num_updates, len(CONTRIBUTION_TYPES)))
    
    for update_type in selected:
        if update_type == "update_readme":
            update_stats()
        elif update_type == "add_changelog":
            update_changelog()
        elif update_type == "update_dependencies":
            update_stats()
        elif update_type == "add_documentation":
            update_daily_log()
        elif update_type == "fix_typos":
            update_project_list()
        elif update_type == "update_examples":
            update_daily_log()
    
    print("✅ Auto-commit completed!")


if __name__ == "__main__":
    main()
