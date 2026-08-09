#!/usr/bin/env python3
"""确保专题子页面不加载全站悬浮“知识地图”按钮。"""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path


class ScriptParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.sources: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "script":
            return
        source = dict(attrs).get("src")
        if source:
            self.sources.append(source)


def script_sources(path: Path) -> list[str]:
    parser = ScriptParser()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser.sources


def main() -> int:
    scene_pages = sorted(
        Path("map/ai/ai_eight_use_scenarios_offline").glob("scene-*.html")
    )
    offenders = [path for path in scene_pages if "/nav.js" in script_sources(path)]

    if offenders:
        print("以下专题子页面仍会注入左上角知识地图按钮：")
        for path in offenders:
            print(f"- {path}")
        return 1

    print(f"PASS: {len(scene_pages)} 个专题子页面均未加载 /nav.js")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
