#!/usr/bin/env python3
"""Batch-render motion_transfer.npz files to mp4 for the Same Gesture section."""

import sys
import os
import glob

sys.path.insert(0, "/home/adi_rosenthal/code/SiGnature")
os.environ.setdefault("PYOPENGL_PLATFORM", "egl")

from scripts.render_smplx_with_floor import render_smplx_npz_to_video

BASE = "/home/adi_rosenthal/code/SiGnature_web/images/same_motion"
OUT_DIR = "/home/adi_rosenthal/code/SiGnature_web/images/same_gesture_videos"
SMPLX_ROOT = "/home/adi_rosenthal/code/SiGnature/datasets/hub/smplx_models/"

SPEAKERS = {
    "lawrence_4": "lawrence",
    "ayana_21": "ayana",
    "wayne_1": "wayne",
    "scott_2": "scott",
    "sophie_7": "sophie",
}

GESTURES = [
    "ARMS_ENCOMPASS-3", "ARMS_EXPLODE-2", "ARMS_WELCOME-1", "FACE_COVER-1",
    "FINGERS_TALK-5", "FIST_PUNCH-2", "FISTS_COLLISON-3", "FOOT_TAP-1",
    "FOREARM_THROW_SIDE-4", "FOREFINGER_POINT-3", "FOREFINGER_RAISE_ONE-1",
    "FOREFINGER_RAISE_ONE-3", "FOREFINGER_RAISE_SKY-1", "FOREFINGER_SPIRAL-1",
    "HAND_CALL-1", "HANDS_BEAST-1", "HANDS_EXPLAIN-3", "HANDS_STEERING-1",
    "PALMS_UP_HIGH-2", "SHOULDERS_SHRUG-4", "TEMPLE_SHOOT-2", "THUMB_DOWN-1",
    "WRIST_CHECK_TIME-1",
]

os.makedirs(OUT_DIR, exist_ok=True)

total = len(GESTURES) * len(SPEAKERS)
done = 0

for gesture in GESTURES:
    for speaker_dir, speaker_name in SPEAKERS.items():
        pattern = os.path.join(BASE, speaker_dir, "evaluation", f"*_{gesture}_*_motion_transfer.npz")
        matches = glob.glob(pattern)
        if not matches:
            print(f"SKIP: {speaker_name} / {gesture} - no npz found")
            done += 1
            continue

        npz_path = matches[0]
        out_path = os.path.join(OUT_DIR, f"{gesture}_{speaker_name}.mp4")

        if os.path.exists(out_path):
            print(f"EXISTS: {out_path} - skipping")
            done += 1
            continue

        print(f"\n[{done+1}/{total}] Rendering {speaker_name} / {gesture}")
        try:
            render_smplx_npz_to_video(
                npz_path=npz_path,
                output_path=out_path,
                smplx_root=SMPLX_ROOT,
                width=480,
                height=480,
                fps=30,
                cam_dist=3.5,
                cam_height=0.3,
                background_color=(1.0, 1.0, 1.0),
            )
        except Exception as e:
            print(f"ERROR: {speaker_name} / {gesture}: {e}")
        done += 1

print(f"\nDone - rendered {done}/{total} videos to {OUT_DIR}")
