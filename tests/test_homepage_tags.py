#!/usr/bin/env python3
"""验证首页标签筛选入口与第一批文章标签。"""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path


EXPECTED_TAGS = {
    "course-ppt": {
        "map/ai/single-point-replication-deck.html",
        "map/ai/ai-fullstack-dev-talk.html",
        "map/ai/ai-requirement-to-launch-talk-ppt.html",
        "map/ai/ai_eight_use_scenarios_offline/index.html",
        "map/ai/ai-coding-client-perspective.html",
        "map/growth/ai-era-super-individual-capabilities-deck.html",
    },
    "image-text": {
        "map/ops/parasite-to-symbiosis.html",
    },
}


class HomepageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.tag_filters: set[str] = set()
        self.tagged_cards: dict[str, set[str]] = {}

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if tag == "button" and attributes.get("data-tag-filter"):
            self.tag_filters.add(attributes["data-tag-filter"] or "")

        classes = (attributes.get("class") or "").split()
        href = attributes.get("href")
        if tag != "a" or "card" not in classes or not href:
            return
        for tag_name in (attributes.get("data-tags") or "").split():
            self.tagged_cards.setdefault(tag_name, set()).add(href)


def main() -> int:
    parser = HomepageParser()
    parser.feed(Path("index.html").read_text(encoding="utf-8"))

    expected_filters = {"all", *EXPECTED_TAGS}
    errors: list[str] = []
    if parser.tag_filters != expected_filters:
        errors.append(
            f"标签筛选项不一致：expected={sorted(expected_filters)}, "
            f"actual={sorted(parser.tag_filters)}"
        )

    actual_tags = set(parser.tagged_cards)
    if actual_tags != set(EXPECTED_TAGS):
        errors.append(
            f"文章标签集合不一致：expected={sorted(EXPECTED_TAGS)}, "
            f"actual={sorted(actual_tags)}"
        )

    for tag_name, expected_paths in EXPECTED_TAGS.items():
        actual_paths = parser.tagged_cards.get(tag_name, set())
        if actual_paths != expected_paths:
            errors.append(
                f"{tag_name} 分类不一致：expected={sorted(expected_paths)}, "
                f"actual={sorted(actual_paths)}"
            )

    if errors:
        print("\n".join(errors))
        return 1

    print("PASS: 首页标签入口与文章分类一致")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
