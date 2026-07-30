import json
import os
import sys

import requests
from bs4 import BeautifulSoup

USERNAME = "Qaziaaaa"
URL = f"https://github.com/users/{USERNAME}/contributions"
OUTPUT = "data/contributions.json"


def main():
    resp = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")
    rects = soup.select("td[data-date]")

    days = []
    for rect in rects:
        date = rect.get("data-date")
        count = int(rect.get("data-level", "0"))
        days.append({"date": date, "count": count})

    total = sum(d["count"] for d in days)
    best_day = max(days, key=lambda x: x["count"]) if days else {}

    # current streak
    streak = 0
    for d in reversed(days):
        if d["count"] > 0:
            streak += 1
        else:
            break

    longest = 0
    cur = 0
    for d in days:
        if d["count"] > 0:
            cur += 1
            longest = max(longest, cur)
        else:
            cur = 0

    monthly = {}
    for d in days:
        month = d["date"][:7]
        monthly[month] = monthly.get(month, 0) + d["count"]

    data = {
        "username": USERNAME,
        "total": total,
        "streak": streak,
        "longest_streak": longest,
        "best_day": best_day,
        "monthly": monthly,
        "days": days,
    }

    with open(OUTPUT, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Saved {OUTPUT} — {total} contributions, {streak}-day streak")


if __name__ == "__main__":
    main()
