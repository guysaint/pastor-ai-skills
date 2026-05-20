#!/usr/bin/env python3
"""Sermon Brief PDF Generator"""

import json
import sys
import os

_here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_here, "..", "..", "shared"))

from pdf_utils import (
    build_styles, section_header, add_title_banner,
    add_reachright_footer, make_page_footer, create_doc,
    add_bullet_list, add_shaded_box,
)
from reportlab.platypus import Paragraph, Spacer


def add_brief_field(story, label, content, styles):
    if not content:
        return
    story.append(Paragraph(label.upper(), styles["body_label"]))
    story.append(Paragraph(content, styles["body_content"]))


def generate_pdf(json_path, output_path=None):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not output_path:
        passage = data.get("passage", "brief")
        safe_name = passage.replace(":", "-").replace(" ", "-")
        output_path = f"Sermon-Brief-{safe_name}.pdf"

    doc = create_doc(
        output_path,
        title=f"설교 브리프: {data.get('passage', '')}",
        author=data.get("pastor_name", ""),
    )
    styles = build_styles()
    story = []

    meta_parts = []
    if data.get("series"):
        meta_parts.append(data["series"])
    if data.get("date"):
        meta_parts.append(data["date"])
    if data.get("pastor_name"):
        meta_parts.append(data["pastor_name"])
    if data.get("church_name"):
        meta_parts.append(data["church_name"])
    add_title_banner(story, "설교 브리프", data.get("passage", ""), meta_parts, styles)

    add_brief_field(story, "핵심 메시지", data.get("big_idea"), styles)
    add_brief_field(story, "핵심 긴장", data.get("key_tension"), styles)
    add_brief_field(story, "회중의 필요", data.get("audience_need"), styles)
    add_brief_field(story, "바라는 반응", data.get("desired_response"), styles)
    add_brief_field(story, "전환점", data.get("the_turn"), styles)

    if data.get("supporting_passages"):
        section_header(story, "뒷받침 본문", styles)
        items = []
        for sp in data["supporting_passages"]:
            ref = sp.get("reference", "")
            note = sp.get("note", "")
            items.append(f"<b>{ref}</b>: {note}" if note else f"<b>{ref}</b>")
        add_bullet_list(story, items, styles)

    add_brief_field(story, "이미지 또는 예화 아이디어", data.get("illustration_idea"), styles)

    story.append(Spacer(1, 16))
    closing = [Paragraph(
        "<i>이 브리프는 출발점이지 원고가 아닙니다. 기도로 가져가 당신의 것으로 만드십시오.</i>",
        styles["prompt"]
    )]
    add_shaded_box(story, closing, styles)

    add_reachright_footer(story, styles)
    page_footer = make_page_footer("reachright")
    doc.build(story, onFirstPage=page_footer, onLaterPages=page_footer)
    return os.path.abspath(output_path)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate-pdf.py <input.json> [output.pdf]")
        sys.exit(1)
    json_input = sys.argv[1]
    pdf_output = sys.argv[2] if len(sys.argv) > 2 else None
    result_path = generate_pdf(json_input, pdf_output)
    print(f"PDF generated: {result_path}")
