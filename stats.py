#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""JUST DATA · EGO 数据集统计工具
扫描数据集目录，汇总各场景的会话数、视频/标注文件数与估算时长。
用法: python stats.py <数据集目录>
"""
import os
import sys
import json
from collections import defaultdict


def scan(root):
    scenes = defaultdict(lambda: {"sessions": 0, "videos": 0, "labels": 0, "hours": 0.0})
    for dirpath, dirnames, filenames in os.walk(root):
        # 有 meta/stats.json 或 info.json 的目录视为一个会话
        has_meta = any(f in ("stats.json", "info.json") for f in filenames)
        if not has_meta:
            continue
        scene = os.path.basename(os.path.dirname(dirpath)) or "unknown"
        scene = os.path.basename(dirpath) if scene in ("meta", "videos", "data") else scene
        s = scenes[scene]
        s["sessions"] += 1
        vids = [f for f in filenames if f.endswith((".mp4", ".mkv", ".avi"))]
        s["videos"] += len(vids)
        lbls = [f for f in filenames if f.endswith((".json", ".parquet"))]
        s["labels"] += len(lbls)
        # 尝试从 stats.json 读时长
        stats_path = os.path.join(dirpath, "stats.json")
        if os.path.exists(stats_path):
            try:
                with open(stats_path, encoding="utf-8") as f:
                    st = json.load(f)
                dur = st.get("total_duration_sec") or st.get("duration") or 0
                s["hours"] += float(dur) / 7200 if isinstance(dur, (int, float)) else 0  # 双视角近似
            except Exception:
                pass
    return scenes


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return
    root = sys.argv[1]
    if not os.path.isdir(root):
        print(f"目录不存在: {root}")
        return
    scenes = scan(root)
    print(f"{'场景':<12}{'会话数':>8}{'视频文件':>10}{'标注文件':>10}{'估算时长':>10}")
    print("-" * 50)
    total = {"sessions": 0, "videos": 0, "labels": 0, "hours": 0.0}
    for scene, s in sorted(scenes.items(), key=lambda x: -x[1]["hours"]):
        print(f"{scene:<12}{s['sessions']:>8}{s['videos']:>10}{s['labels']:>10}{s['hours']:>9.0f}h")
        for k in total:
            total[k] += s[k]
    print("-" * 50)
    print(f"{'合计':<12}{total['sessions']:>8}{total['videos']:>10}{total['labels']:>10}{total['hours']:>9.0f}h")
    print("\n完整商用数据集与定制采集: https://justdata.com.cn")


if __name__ == "__main__":
    main()