#!/usr/bin/env python3
"""BlackRoad Roadmap — project planning and milestone tracking"""
import json, sys, sqlite3, os
from datetime import datetime, timezone

DB = os.path.expanduser("~/.blackroad/roadmap.db")

def init():
    os.makedirs(os.path.dirname(DB), exist_ok=True)
    db = sqlite3.connect(DB)
    db.executescript("""
    CREATE TABLE IF NOT EXISTS milestones (
        id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, quarter TEXT,
        status TEXT DEFAULT 'planned', priority TEXT DEFAULT 'medium', created_at TEXT
    );
    CREATE TABLE IF NOT EXISTS features (
        id INTEGER PRIMARY KEY AUTOINCREMENT, milestone_id INTEGER, title TEXT,
        status TEXT DEFAULT 'planned', assignee TEXT, FOREIGN KEY(milestone_id) REFERENCES milestones(id)
    );""")
    if db.execute("SELECT count(*) FROM milestones").fetchone()[0] == 0:
        now = datetime.now(timezone.utc).isoformat()
        for t, q, s, p in [
            ("Prove the Thesis", "Q2 2026", "in-progress", "critical"),
            ("Ship Chat Pro + AI API", "Q3 2026", "planned", "high"),
            ("Memory Platform Launch", "Q4 2026", "planned", "high"),
            ("$15K MRR Target", "Q1 2027", "planned", "critical"),
            ("Workspace Product", "Q2 2027", "planned", "medium"),
            ("SOC 2 Type I", "Q4 2027", "planned", "medium"),
        ]:
            db.execute("INSERT INTO milestones (title,quarter,status,priority,created_at) VALUES (?,?,?,?,?)", (t, q, s, p, now))
        db.commit()
    return db

def list_milestones():
    db = init()
    for id, title, quarter, status, priority in db.execute("SELECT id,title,quarter,status,priority FROM milestones ORDER BY id"):
        icon = {"in-progress": "●", "planned": "○", "done": "✓"}.get(status, "?")
        print(f"  {icon} [{quarter}] {title} ({priority})")

def show(mid):
    db = init()
    m = db.execute("SELECT title,quarter,status FROM milestones WHERE id=?", (mid,)).fetchone()
    if not m: print("Not found"); return
    print(f"\n  {m[0]} — {m[1]} ({m[2]})")
    features = db.execute("SELECT title,status,assignee FROM features WHERE milestone_id=?", (mid,)).fetchall()
    for t, s, a in features:
        print(f"    {'✓' if s=='done' else '○'} {t} → {a or 'unassigned'}")
    if not features: print("    No features yet. Add with: roadmap.py add-feature <milestone-id> <title>")

if __name__ == "__main__":
    cmds = {"list": list_milestones, "show": lambda: show(int(sys.argv[2]))}
    cmd = sys.argv[1] if len(sys.argv) > 1 else "list"
    if cmd in cmds: cmds[cmd]()
    else: print("Usage: roadmap.py [list|show N]")
