#!/usr/bin/env python3
"""验证新增个人成长课件的英文命名、首页标签和返回地图入口。"""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path


EXPECTED_PATH = Path("map/growth/ai-era-super-individual-capabilities-deck.html")


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.script_sources: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        source = dict(attrs).get("src")
        if tag == "script" and source:
            self.script_sources.add(source)


class HomepageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.cards: dict[str, dict[str, str | None]] = {}

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        classes = (attributes.get("class") or "").split()
        href = attributes.get("href")
        if tag == "a" and "card" in classes and href:
            self.cards[href] = attributes


def main() -> int:
    errors: list[str] = []
    non_english_names = [
        path.name for path in Path("map/growth").glob("*.html") if not path.name.isascii()
    ]
    if non_english_names:
        errors.append(f"growth 仍有非英文 HTML 文件名：{non_english_names}")

    if not EXPECTED_PATH.exists():
        errors.append(f"缺少英文命名后的课件：{EXPECTED_PATH}")
    else:
        page = PageParser()
        page.feed(EXPECTED_PATH.read_text(encoding="utf-8"))
        if "/nav.js" not in page.script_sources:
            errors.append("新增课件未加载 /nav.js，左上角不会出现返回地图入口")

    homepage = HomepageParser()
    homepage.feed(Path("index.html").read_text(encoding="utf-8"))
    card = homepage.cards.get(EXPECTED_PATH.as_posix())
    if card is None:
        errors.append("首页缺少新增课件卡片")
    else:
        if card.get("data-category") != "growth":
            errors.append("新增课件首页分类不是 growth")
        tags = (card.get("data-tags") or "").split()
        if "course-ppt" not in tags:
            errors.append("新增课件未打上课件PPT标签")

    if errors:
        print("\n".join(errors))
        return 1

    print("PASS: 新增 growth 课件已完成英文命名、首页标签和返回地图接入")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
