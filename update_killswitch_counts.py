#!/usr/bin/env python3
"""
update_killswitch_counts.py
============================
Update kill-switch counts across all 13 language versions of the420code.org
to match Master Kill Switch Registry Final May 2026.

NEW CANONICAL COUNTS (per Master_Kill_Switch_Registry_Final_May_2026.docx):
    Total:        546   (was 285 in EN/ZH/etc, 258 in ES, varies elsewhere)
    Section I:    266   (was 261 — +5 from Ø Predictions)
    Section II:    24
    Section III:  256

    Per-AP changes:
        AP30:  3 → 7  (added KS-30.4, KS-NPP.1, KS-NPP.2, KS-NPP.3)
        AP42:  5 → 6  (added KS-42.6)
        AP20:  4 → 5  (corrected — table always had 5; claim was wrong)

    Status counts:
        15  closed
        1   addressed
        1   conditionally closed
        1   derived         (KS-46A in AP22 — newly tagged)
        4   open debt       (subset of live)
        6   non-negotiable  (subset of live)
        1   master          (KS-AC.6 — subset of live, new flag)
        528 live total
"""

import argparse
import re
import shutil
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

# --- CANONICAL NEW COUNTS ---
NEW_TOTAL = 546
NEW_SECTION_I = 266
NEW_SECTION_II = 24
NEW_SECTION_III = 256

NEW_AP30_COUNT = 7
NEW_AP42_COUNT = 6
NEW_AP20_COUNT = 5

NEW_CLOSED = 15
NEW_LIVE = 528
NEW_ADDRESSED = 1
NEW_COND_CLOSED = 1
NEW_DERIVED = 1
NEW_OPEN_DEBT = 4
NEW_NON_NEGOTIABLE = 6
NEW_MASTER = 1

# --- OLD COUNTS THE SCRIPT SHOULD RECOGNISE & REPLACE ---
KNOWN_OLD_TOTALS = {285, 258, 261}
KNOWN_OLD_AP30 = {3, 4}
KNOWN_OLD_AP42 = {5}
KNOWN_OLD_AP20 = {4}
KNOWN_OLD_LIVE = {231, 269, 270}

# --- EXPECTED LANGUAGE DIRECTORIES ---
LANGUAGES = ["en", "es", "fr", "de", "pt", "nl", "it",
             "zh", "ja", "ko", "ru", "ar", "hi"]

# --- KILL-SWITCH KEYWORD VARIANTS BY LANGUAGE ---
KILLSWITCH_KEYWORDS = {
    "en": [r"kill switches?", r"killswitches?"],
    "es": [r"interruptores? letales?", r"interruptores? de seguridad",
           r"interruptores? fatales?"],
    "fr": [r"interrupteurs? de s\u00e9curit\u00e9", r"interrupteurs? fatals?",
           r"interrupteurs? d'arr\u00eat", r"commutateurs? d'arr\u00eat"],
    "de": [r"notabschaltern?", r"abschaltvorrichtungen?",
           r"kill[\s-]?switch(es)?", r"sicherheitsschalter\w*"],
    "pt": [r"interruptores? de seguran\u00e7a", r"interruptores? fatais?",
           r"interruptores? letais?"],
    "nl": [r"noodschakelaars?", r"veiligheidsschakelaars?",
           r"kill[\s-]?switch(es)?"],
    "it": [r"interruttori? di sicurezza", r"interruttori? fatali?",
           r"interruttori? letali?"],
    "zh": [r"\u706d\u6740\u5f00\u5173", r"\u7ec8\u6b62\u5f00\u5173", r"\u706d\u6d3b\u5f00\u5173"],
    "ja": [r"\u30ad\u30eb\u30b9\u30a4\u30c3\u30c1", r"\u505c\u6b62\u30b9\u30a4\u30c3\u30c1", r"\u5b89\u5168\u30b9\u30a4\u30c3\u30c1"],
    "ko": [r"\ud0ac\s*\uc2a4\uc704\uce58", r"\uc815\uc9c0\s*\uc2a4\uc704\uce58", r"\uc548\uc804\s*\uc2a4\uc704\uce58"],
    "ru": [r"\u043f\u0440\u0435\u0434\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u0435\u043b\w*", r"\u0430\u0432\u0430\u0440\u0438\u0439\u043d\w+\s+\u0432\u044b\u043a\u043b\u044e\u0447\u0430\u0442\u0435\u043b\w*",
           r"\u043a\u0438\u043b\u043b[\s-]?\u0441\u0432\u0438\u0442\u0447\w*"],
    "ar": [r"\u0645\u0641\u0627\u062a\u064a\u062d\s+\u0627\u0644\u0625\u064a\u0642\u0627\u0641", r"\u0645\u0641\u0627\u062a\u064a\u062d\s+\u0627\u0644\u0642\u062a\u0644", r"\u0645\u0641\u0627\u062a\u064a\u062d\s+\u0627\u0644\u0623\u0645\u0627\u0646",
           r"\u0645\u0641\u062a\u0627\u062d\s+\u0625\u064a\u0642\u0627\u0641"],
    "hi": [r"\u0915\u093f\u0932\s*\u0938\u094d\u0935\u093f\u091a", r"\u0938\u0941\u0930\u0915\u094d\u0937\u093e\s+\u0938\u094d\u0935\u093f\u091a", r"\u092c\u0902\u0926\s+\u0915\u0930\u0928\u0947\s+\u0935\u093e\u0932\u0947?\s+\u0938\u094d\u0935\u093f\u091a"],
}


@dataclass
class Change:
    file: Path
    line_no: int
    rule: str
    before: str
    after: str

    def render(self) -> str:
        return (f"  [{self.rule}] {self.file}:{self.line_no}\n"
                f"      - {self.before.strip()[:120]}\n"
                f"      + {self.after.strip()[:120]}")


@dataclass
class Report:
    changes: list = field(default_factory=list)
    files_scanned: int = 0
    files_modified: set = field(default_factory=set)

    def add(self, c: Change):
        self.changes.append(c)
        self.files_modified.add(c.file)

    def summary(self) -> str:
        by_rule = {}
        for c in self.changes:
            by_rule[c.rule] = by_rule.get(c.rule, 0) + 1
        lines = [
            f"Files scanned:  {self.files_scanned}",
            f"Files modified: {len(self.files_modified)}",
            f"Total changes:  {len(self.changes)}",
            "",
            "Changes by rule:",
        ]
        for rule, count in sorted(by_rule.items()):
            lines.append(f"  {rule}: {count}")
        return "\n".join(lines)


def keyword_alternatives(lang: str) -> str:
    variants = KILLSWITCH_KEYWORDS.get(lang, KILLSWITCH_KEYWORDS["en"])
    return "(?:" + "|".join(variants) + ")"


def find_lang_dir(site_root: Path, lang: str):
    if lang == "en":
        return site_root
    candidate = site_root / lang
    return candidate if candidate.is_dir() else None


def html_files(directory: Path):
    for pattern in ("*.html", "*.htm"):
        yield from directory.glob(pattern)


def update_total_count(text: str, lang: str, file: Path, report: Report) -> str:
    kw = keyword_alternatives(lang)
    pattern = re.compile(
        rf"(?P<lead>\b)(?P<num>[1-9]\d{{1,2}})(?P<gap>\s*)(?P<kw>{kw})",
        re.IGNORECASE,
    )

    def repl(m: re.Match) -> str:
        old_num = int(m.group("num"))
        if old_num < 50:
            return m.group(0)
        if old_num == NEW_TOTAL:
            return m.group(0)
        line_no = text[:m.start()].count("\n") + 1
        new_str = f"{m.group('lead')}{NEW_TOTAL}{m.group('gap')}{m.group('kw')}"
        report.add(Change(
            file=file, line_no=line_no, rule="total-count",
            before=m.group(0), after=new_str,
        ))
        return new_str

    return pattern.sub(repl, text)


def update_ap_count(text: str, lang: str, ap: str, old_values: set,
                    new_value: int, file: Path, report: Report) -> str:
    kw = keyword_alternatives(lang)
    anchor_pattern = re.compile(rf"\b{ap}\b", re.IGNORECASE)
    out = text
    for anchor in list(anchor_pattern.finditer(text)):
        window_start = anchor.start()
        window_end = min(anchor.start() + 400, len(text))
        window = text[window_start:window_end]
        m = re.search(
            rf"(?P<lead>\b)(?P<num>[1-9]\d?)(?P<gap>\s*)(?P<kw>{kw})",
            window, re.IGNORECASE,
        )
        if not m:
            continue
        old_num = int(m.group("num"))
        if old_num not in old_values:
            continue
        if old_num == new_value:
            continue
        abs_start = window_start + m.start()
        original = m.group(0)
        replacement = f"{m.group('lead')}{new_value}{m.group('gap')}{m.group('kw')}"
        if original in out:
            out = out.replace(original, replacement, 1)
            line_no = text[:abs_start].count("\n") + 1
            report.add(Change(
                file=file, line_no=line_no, rule=f"{ap}-count",
                before=original, after=replacement,
            ))
    return out


def update_status_panel(text: str, lang: str, file: Path, report: Report) -> str:
    status_keywords = {
        "closed": {
            "en": [r"closed"],
            "es": [r"cerrad[oa]s?"],
            "fr": [r"ferm\u00e9s?"],
            "de": [r"geschlossene?n?"],
            "pt": [r"fechad[oa]s?"],
            "nl": [r"gesloten"],
            "it": [r"chius[oi]"],
            "zh": [r"\u5df2\u5173\u95ed", r"\u5173\u95ed"],
            "ja": [r"\u9589\u3058", r"\u30af\u30ed\u30fc\u30ba"],
            "ko": [r"\uc885\ub8cc", r"\ub2eb\ud798"],
            "ru": [r"\u0437\u0430\u043a\u0440\u044b\u0442\w*"],
            "ar": [r"\u0645\u063a\u0644\u0642\w*"],
            "hi": [r"\u092c\u0902\u0926"],
            "_target": NEW_CLOSED,
        },
        "live": {
            "en": [r"live"],
            "es": [r"activos?"],
            "fr": [r"actifs?"],
            "de": [r"aktive?n?"],
            "pt": [r"ativos?"],
            "nl": [r"actie[vf]e?"],
            "it": [r"attivi?"],
            "zh": [r"\u6709\u6548", r"\u5728\u7528"],
            "ja": [r"\u6709\u52b9"],
            "ko": [r"\ud65c\uc131"],
            "ru": [r"\u0430\u043a\u0442\u0438\u0432\w*"],
            "ar": [r"\u0646\u0634\u0637\w*"],
            "hi": [r"\u0938\u0915\u094d\u0930\u093f\u092f"],
            "_target": NEW_LIVE,
        },
        "non_negotiable": {
            "en": [r"non[\s-]?negotiable"],
            "es": [r"no\s+negociables?"],
            "fr": [r"non[\s-]?n\u00e9gociables?"],
            "de": [r"nicht\s+verhandelbar\w*"],
            "pt": [r"n\u00e3o[\s-]?negoci\u00e1veis?"],
            "nl": [r"niet[\s-]?onderhandelbaar"],
            "it": [r"non\s+negoziabili?"],
            "zh": [r"\u4e0d\u53ef\u534f\u5546", r"\u4e0d\u53ef\u5546\u8bae"],
            "ja": [r"\u4ea4\u6e09\u4e0d\u53ef", r"\u59a5\u5354\u4e0d\u53ef"],
            "ko": [r"\ud611\uc0c1\s*\ubd88\uac00"],
            "ru": [r"\u043d\u0435\u043e\u0431\u0441\u0443\u0436\u0434\u0430\u0435\u043c\w*", r"\u043d\u0435\u043f\u0435\u0440\u0435\u0433\u043e\u0432\u043e\u0440\w*"],
            "ar": [r"\u063a\u064a\u0631\s+\u0642\u0627\u0628\u0644\u0629?\s+\u0644\u0644\u062a\u0641\u0627\u0648\u0636"],
            "hi": [r"\u0917\u0948\u0930-?\u0938\u092e\u091d\u094c\u0924\w*"],
            "_target": NEW_NON_NEGOTIABLE,
        },
        "open_debt": {
            "en": [r"open\s+debts?"],
            "es": [r"deudas?\s+abiertas?"],
            "fr": [r"dettes?\s+ouvertes?"],
            "de": [r"offene?\s+schulden?"],
            "pt": [r"d[\u00ed\u0069]vidas?\s+abertas?"],
            "nl": [r"open\s+schuld\w*"],
            "it": [r"debiti?\s+aperti?"],
            "zh": [r"\u672a\u89e3\u51b3\u503a\u52a1", r"\u5f00\u653e\u503a\u52a1", r"\u672a\u7ed3\u503a\u52a1"],
            "ja": [r"\u672a\u89e3\u6c7a\u306e?\u8ca0\u50b5", r"\u30aa\u30fc\u30d7\u30f3\u30c7\u30c3\u30c8"],
            "ko": [r"\ubbf8\ud574\uacb0\s*\ubd80\ucc44"],
            "ru": [r"\u043e\u0442\u043a\u0440\u044b\u0442\w*\s+\u0434\u043e\u043b\u0433\w*"],
            "ar": [r"\u062f\u064a\u0648\u0646\s+\u0645\u0641\u062a\u0648\u062d\u0629"],
            "hi": [r"\u0916\u0941\u0932\u0947?\s+\u090b\u0923"],
            "_target": NEW_OPEN_DEBT,
        },
    }

    out = text
    for status, langs_dict in status_keywords.items():
        target = langs_dict["_target"]
        keywords = langs_dict.get(lang, langs_dict["en"])
        kw_alt = "(?:" + "|".join(keywords) + ")"
        pattern = re.compile(
            rf"(?P<lead>\b)(?P<num>\d{{1,3}})(?P<gap>\s*)(?P<kw>{kw_alt})",
            re.IGNORECASE,
        )
        for m in list(pattern.finditer(out)):
            old_num = int(m.group("num"))
            if old_num == target:
                continue
            if old_num > 999:
                continue
            original = m.group(0)
            new_str = f"{m.group('lead')}{target}{m.group('gap')}{m.group('kw')}"
            line_no = out[:m.start()].count("\n") + 1
            out = out[:m.start()] + new_str + out[m.end():]
            report.add(Change(
                file=file, line_no=line_no, rule=f"status-{status}",
                before=original, after=new_str,
            ))
    return out


def process_file(path: Path, lang: str, report: Report,
                 apply: bool, verbose: bool) -> None:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        print(f"WARNING: cannot read {path} as UTF-8 - skipping", file=sys.stderr)
        return
    report.files_scanned += 1
    original = text

    text = update_total_count(text, lang, path, report)
    text = update_ap_count(text, lang, "AP30", KNOWN_OLD_AP30, NEW_AP30_COUNT,
                           path, report)
    text = update_ap_count(text, lang, "AP42", KNOWN_OLD_AP42, NEW_AP42_COUNT,
                           path, report)
    text = update_ap_count(text, lang, "AP20", KNOWN_OLD_AP20, NEW_AP20_COUNT,
                           path, report)
    text = update_status_panel(text, lang, path, report)

    if text == original:
        if verbose:
            print(f"  no change: {path}")
        return

    if apply:
        backup = path.with_suffix(path.suffix + ".bak")
        if not backup.exists():
            shutil.copy2(path, backup)
        path.write_text(text, encoding="utf-8")
        print(f"  updated: {path}")
    else:
        print(f"  would update: {path}")


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("site_root", type=Path,
                   help="Root directory of the the420code.org site source")
    p.add_argument("--apply", action="store_true",
                   help="Actually write changes (default: dry-run)")
    p.add_argument("--verbose", action="store_true",
                   help="Log files with no changes")
    p.add_argument("--langs", default=",".join(LANGUAGES),
                   help=f"Comma-separated language codes (default: all 13)")
    args = p.parse_args()

    if not args.site_root.is_dir():
        print(f"ERROR: {args.site_root} is not a directory", file=sys.stderr)
        return 2

    requested_langs = [l.strip() for l in args.langs.split(",") if l.strip()]
    unknown = [l for l in requested_langs if l not in LANGUAGES]
    if unknown:
        print(f"ERROR: unknown language(s): {unknown}", file=sys.stderr)
        return 2

    found_langs = []
    for lang in requested_langs:
        d = find_lang_dir(args.site_root, lang)
        if d is None:
            print(f"WARNING: no directory found for '{lang}' - skipping",
                  file=sys.stderr)
            continue
        found_langs.append((lang, d))

    if not found_langs:
        print("ERROR: no language directories found at all - wrong site root?",
              file=sys.stderr)
        return 2

    print(f"{'DRY-RUN' if not args.apply else 'APPLY MODE'}: "
          f"updating {len(found_langs)} language(s)")
    print(f"Target counts: total={NEW_TOTAL}, "
          f"AP30={NEW_AP30_COUNT}, AP42={NEW_AP42_COUNT}, AP20={NEW_AP20_COUNT}, "
          f"closed={NEW_CLOSED}, live={NEW_LIVE}, "
          f"non-neg={NEW_NON_NEGOTIABLE}, open-debt={NEW_OPEN_DEBT}")
    print()

    report = Report()
    for lang, lang_dir in found_langs:
        print(f"-- {lang} -- {lang_dir}")
        files = list(html_files(lang_dir))
        if not files:
            print(f"  (no .html files found in {lang_dir})")
            continue
        for f in files:
            process_file(f, lang, report, apply=args.apply, verbose=args.verbose)
        print()

    print("=" * 70)
    print(report.summary())
    print()
    if report.changes:
        print("CHANGE DETAILS")
        print("-" * 70)
        for c in report.changes:
            print(c.render())

    if not args.apply and report.changes:
        print()
        print("Dry run complete. Re-run with --apply to write changes.")
        print("Backups will be saved as <file>.bak before modification.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
