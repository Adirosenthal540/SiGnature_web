#!/usr/bin/env python3
"""Batch-render res_ npz files for Same Utterance, Different Speakers section."""

import sys
import os
import glob

sys.path.insert(0, "/home/adi_rosenthal/code/SiGnature")
os.environ.setdefault("PYOPENGL_PLATFORM", "egl")

from scripts.render_smplx_with_floor import render_smplx_npz_to_video

BASE = "/home/adi_rosenthal/code/SiGnature_web/images/Same_Utterance_Different_Speakers"
OUT_DIR = "/home/adi_rosenthal/code/SiGnature_web/images/same_utterance_videos"
SMPLX_ROOT = "/home/adi_rosenthal/code/SiGnature/datasets/hub/smplx_models/"

SPEAKERS = {
    "DoubleTake_samples_4_lawrence_000200000_seed12_handshake30_double_take_blend10_skip100_20260621_094708_diffusion1000": ("4_lawrence", "lawrence"),
    "DoubleTake_samples_21_ayana_000040000_seed12_handshake30_double_take_blend10_skip100_20260621_111454_diffusion1000": ("21_ayana", "ayana"),
    "DoubleTake_samples_1_wayne_000115000_seed12_handshake30_double_take_blend10_skip100_20260621_082400_diffusion1000": ("1_wayne", "wayne"),
    "DoubleTake_samples_2_scott_000205000_seed12_handshake30_double_take_blend10_skip100_20260621_090852_diffusion1000": ("2_scott", "scott"),
    "DoubleTake_samples_7_sophie_000200000_seed12_handshake30_double_take_blend10_skip100_20260621_103246_diffusion1000": ("7_sophie", "sophie"),
}

UTTERANCES = ["1_1", "2_2", "3_3", "65_65", "103_103", "111_111"]

os.makedirs(OUT_DIR, exist_ok=True)

total = 0
done = 0

for utt in UTTERANCES:
    for dir_name, (prefix, speaker_name) in SPEAKERS.items():
        npz_path = os.path.join(BASE, dir_name, f"res_{prefix}_0_{utt}.npz")
        if not os.path.exists(npz_path):
            continue
        total += 1

print(f"Total videos to render: {total}")

for utt in UTTERANCES:
    for dir_name, (prefix, speaker_name) in SPEAKERS.items():
        npz_path = os.path.join(BASE, dir_name, f"res_{prefix}_0_{utt}.npz")
        if not os.path.exists(npz_path):
            continue

        out_path = os.path.join(OUT_DIR, f"utt_{utt}_{speaker_name}.mp4")

        if os.path.exists(out_path):
            print(f"EXISTS: {out_path} - skipping")
            done += 1
            continue

        print(f"\n[{done+1}/{total}] Rendering {speaker_name} / utterance {utt}")
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
            print(f"ERROR: {speaker_name} / {utt}: {e}")
        done += 1

print(f"\nDone - rendered {done}/{total} videos to {OUT_DIR}")
