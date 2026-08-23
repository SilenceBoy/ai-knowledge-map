#!/usr/bin/env python3
"""确保首页展示所有可见的顶层文章和专题入口。"""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit


HIDDEN_FROM_HOMEPAGE = {
    "map/ai/codex-mvp-workshop-ppt.html",
}


class AnchorParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.card_hrefs: list[str] = []
        self.all_hrefs: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "a":
            return
        attributes = dict(attrs)
        href = attributes.get("href")
        if href:
            self.all_hrefs.append(href)
        classes = (attributes.get("class") or "").split()
        if href and "card" in classes:
            self.card_hrefs.append(href)


def main() -> int:
    homepage = Path("index.html")
    parser = AnchorParser()
    parser.feed(homepage.read_text(encoding="utf-8"))

    homepage_cards = {
        urlsplit(href).path
        for href in parser.card_hrefs
        if urlsplit(href).path.startswith("map/")
        and urlsplit(href).path.endswith(".html")
    }
    expected_cards = {
        path.as_posix()
        for path in Path("map").rglob("*.html")
        if len(path.parts) == 3 or path.name == "index.html"
    } - HIDDEN_FROM_HOMEPAGE
    missing = sorted(expected_cards - homepage_cards)
    unexpected = sorted(homepage_cards - expected_cards)

    if missing:
        print("首页缺少直接入口：")
        for path in missing:
            print(f"- {path}")
    if unexpected:
        print("专题子页面不应作为独立首页卡片：")
        for path in unexpected:
            print(f"- {path}")
    if missing or unexpected:
        return 1

    courses_home = Path("my-courses/index.html")
    course_file = Path("my-courses/ai_eight_use_scenarios_offline/index.html")
    if "my-courses/" not in parser.all_hrefs or not courses_home.is_file():
        print("首页“我的课程”英文入口或课程目录页缺失")
        return 1
    if not course_file.is_file() or "ai_eight_use_scenarios_offline/index.html" not in courses_home.read_text(encoding="utf-8"):
        print("课程目录页缺少八个日常场景课件入口")
        return 1

    print(f"PASS: 首页已覆盖 {len(expected_cards)} 个顶层文章与专题入口，并包含我的课程入口")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
