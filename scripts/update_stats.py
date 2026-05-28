#!/usr/bin/env python3
"""Auto-update GitHub profile stats."""

import json
import os
from datetime import datetime

import requests

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
GITHUB_API = "https://api.github.com"
USERNAME = "Alex-2Code"


def get_headers():
    return {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json",
    }


def get_user_stats():
    """获取用户统计数据"""
    resp = requests.get(f"{GITHUB_API}/users/{USERNAME}", headers=get_headers())
    return resp.json()


def get_repos():
    """获取所有仓库"""
    repos = []
    page = 1
    while True:
        resp = requests.get(
            f"{GITHUB_API}/users/{USERNAME}/repos",
            headers=get_headers(),
            params={"per_page": 100, "page": page},
        )
        data = resp.json()
        if not data:
            break
        repos.extend(data)
        page += 1
    return repos


def calculate_stats(user, repos):
    """计算统计数据"""
    total_stars = sum(r["stargazers_count"] for r in repos)
    total_forks = sum(r["forks_count"] for r in repos)
    
    languages = {}
    for repo in repos:
        if repo["language"]:
            languages[repo["language"]] = languages.get(repo["language"], 0) + 1
    
    return {
        "updated_at": datetime.utcnow().isoformat(),
        "public_repos": user["public_repos"],
        "followers": user["followers"],
        "following": user["following"],
        "total_stars": total_stars,
        "total_forks": total_forks,
        "top_languages": dict(sorted(languages.items(), key=lambda x: x[1], reverse=True)[:5]),
        "repos": [
            {
                "name": r["name"],
                "stars": r["stargazers_count"],
                "forks": r["forks_count"],
                "language": r["language"],
            }
            for r in sorted(repos, key=lambda x: x["stargazers_count"], reverse=True)[:10]
        ],
    }


def update_stats_file(stats):
    """更新统计文件"""
    with open("stats.json", "w") as f:
        json.dump(stats, f, indent=2)
    print(f"✅ Stats updated: {stats['updated_at']}")


def main():
    print("🔄 Fetching GitHub stats...")
    user = get_user_stats()
    repos = get_repos()
    stats = calculate_stats(user, repos)
    update_stats_file(stats)
    
    print(f"📊 Public Repos: {stats['public_repos']}")
    print(f"👥 Followers: {stats['followers']}")
    print(f"⭐ Total Stars: {stats['total_stars']}")
    print(f"🍴 Total Forks: {stats['total_forks']}")
    print(f"💻 Top Languages: {', '.join(stats['top_languages'].keys())}")


if __name__ == "__main__":
    main()
