#!/usr/bin/env python3
"""验证 AI Coding 分享页的二维码与作品外链展示边界。"""

from pathlib import Path


PAGE = Path("map/ai/ai-coding-client-perspective.html")


def main() -> int:
    slides = PAGE.read_text(encoding="utf-8").split('<section class="slide')
    second_slide = slides[2]
    third_slide = slides[3]

    if "profile-qr" in second_slide or "silencebin-qr.png" in second_slide:
        raise SystemExit("第 2 页仍包含二维码组件")
    if "href=" in third_slide:
        raise SystemExit("第 3 页仍包含链接")
    if third_slide.count('class="work-image-trigger"') != 4:
        raise SystemExit("第 3 页未为全部 4 张案例图片配置放大按钮")
    if third_slide.count("data-lightbox=") != 4:
        raise SystemExit("第 3 页案例图片未全部接入灯箱预览")

    print("PASS: 第 2 页无二维码，第 3 页无链接且案例图片可放大")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
