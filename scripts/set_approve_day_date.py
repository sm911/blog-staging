#!/usr/bin/env python3
"""Rewrite article display/meta dates to the staging Approve day (America/New_York).

Usage:
  python3 scripts/set_approve_day_date.py path/to/post.html 2026-09-22
  python3 scripts/set_approve_day_date.py path/to/post.html --from-approvals-row "2026-09-22 08:36 America/New_York"

Does not promote. Does not change byline name/title (those must already be James Venuto /
Security Medic Consulting, LLC - AI Cyber Security and Privacy).
"""
from __future__ import annotations

import argparse
import calendar
import re
import sys
from datetime import date
from pathlib import Path


def parse_day(s: str) -> date:
    s = s.strip()
    m = re.match(r"^(\d{4})-(\d{2})-(\d{2})", s)
    if m:
        return date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    m = re.match(r"^([A-Za-z]+)\s+(\d{1,2}),\s*(\d{4})", s)
    if m:
        months = {calendar.month_name[i]: i for i in range(1, 13)}
        months.update({calendar.month_abbr[i]: i for i in range(1, 13)})
        mon = months[m.group(1)]
        return date(int(m.group(3)), mon, int(m.group(2)))
    raise SystemExit(f"Unrecognized date: {s!r}")


def display(d: date) -> str:
    return f"{calendar.month_name[d.month]} {d.day}, {d.year}"


def iso(d: date) -> str:
    return d.isoformat()


def rewrite(html: str, d: date) -> str:
    disp = display(d)
    iso_d = iso(d)

    # blog-control-meta date:
    html = re.sub(r"(?m)^(date:\s*)\d{4}-\d{2}-\d{2}\s*$", rf"\g<1>{iso_d}", html)

    # common meta tags
    html = re.sub(
        r'(<meta\s+name="date"\s+content=")[^"]*(")',
        rf"\g<1>{iso_d}\2",
        html,
        flags=re.I,
    )
    html = re.sub(
        r'(<meta\s+property="article:published_time"\s+content=")[^"]*(")',
        rf"\g<1>{iso_d}\2",
        html,
        flags=re.I,
    )

    # compliance byline: By NAME | DATE | TITLE
    html = re.sub(
        r'(<div class="byline">By James Venuto \| )[^|<]+( \| Security Medic Consulting, LLC - AI Cyber Security and Privacy</div>)',
        rf"\g<1>{disp}\2",
        html,
    )
    # legacy byline without title — still stamp date
    html = re.sub(
        r'(<div class="byline">By James Venuto \| )[^|<]+(</div>)',
        rf"\g<1>{disp}\2",
        html,
    )

    # cloud-architecture: Published: DATE
    html = re.sub(
        r"(Published:\s*)[A-Za-z]+ \d{1,2}, \d{4}",
        rf"\g<1>{disp}",
        html,
    )

    # data-security / CFS standalone month-day-year spans (conservative: only common patterns near meta)
    # leadership / privacy hero lines containing "· September … ·" or "&nbsp; September …"
    html = re.sub(
        r"(James Venuto(?:[^<]{0,120}?))(?:January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}, \d{4}",
        rf"\1{disp}",
        html,
        count=3,
    )

    # author-role ending with date
    html = re.sub(
        r'(<span class="author-role">Security Medic Consulting, LLC - AI Cyber Security and Privacy · )[^<]+(</span>)',
        rf"\g<1>{disp}\2",
        html,
    )

    # CFS / data-security date-only span that follows the title span
    html = re.sub(
        r'(<span>Security Medic Consulting, LLC - AI Cyber Security and Privacy</span>\s*<span>)(?:January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}, \d{4}(</span>)',
        rf"\g<1>{disp}\2",
        html,
    )

    return html


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("html_path")
    ap.add_argument("approve_day", help="YYYY-MM-DD or 'Month D, YYYY' or approvals Event-at prefix")
    args = ap.parse_args()
    path = Path(args.html_path)
    d = parse_day(args.approve_day)
    html = path.read_text(encoding="utf-8")
    new = rewrite(html, d)
    if new == html:
        print(f"No date slots changed in {path} for {display(d)}", file=sys.stderr)
    path.write_text(new, encoding="utf-8")
    print(f"Set Approve-day date {iso(d)} ({display(d)}) on {path}")


if __name__ == "__main__":
    main()
