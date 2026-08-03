"""
MAITRI Circadian Rhythm & Cabin Lighting Synchronization Engine
Computes optimal habitat LED color temperatures (2700K - 6500K) and melatonin synthesis prep windows
to counteract zero-gravity circadian disruption caused by 16 orbital sunrises/sunsets per 24 hours.
"""

import os
import sys
from datetime import datetime

class CircadianLightingSynchronizer:
    def __init__(self):
        # Habitat circadian lighting profiles
        self.profiles = {
            "WAKE_FOCUS": {
                "color_temp_kelvin": 6500,
                "spectral_type": "Blue-Enriched Cool Daylight",
                "intensity_lux": 450,
                "purpose": "Cortisol stimulation & peak cognitive alert during EVA/flight maneuvers"
            },
            "NOMINAL_DAY": {
                "color_temp_kelvin": 4000,
                "spectral_type": "Neutral White Balance",
                "intensity_lux": 300,
                "purpose": "Standard habitat environment for routine mission operations"
            },
            "MELATONIN_PREP": {
                "color_temp_kelvin": 2700,
                "spectral_type": "Zero-Blue Warm Amber",
                "intensity_lux": 100,
                "purpose": "Melatonin synthesis activation & pre-sleep relaxation window"
            },
            "SLEEP_CYCLE": {
                "color_temp_kelvin": 1800,
                "spectral_type": "Deep Infrared Ambient",
                "intensity_lux": 10,
                "purpose": "Night sleep cycle illumination for module navigation"
            }
        }

    def compute_lighting_schedule(self, current_time=None, sleep_quality_score=84):
        """
        Computes recommended cabin lighting profile based on 24h orbital schedule and sleep telemetry.
        """
        if current_time is None:
            current_time = datetime.now()

        hour = current_time.hour

        if 6 <= hour < 12:
            phase = "WAKE_FOCUS"
            guidance = "Morning wake window. High blue spectrum active to suppress melatonin and elevate alertness."
        elif 12 <= hour < 20:
            phase = "NOMINAL_DAY"
            guidance = "Nominal workday environment. Balanced neutral white spectrum active."
        elif 20 <= hour < 23:
            phase = "MELATONIN_PREP"
            guidance = "Pre-sleep window. Warm amber lighting active to stimulate natural sleep hormones."
        else:
            phase = "SLEEP_CYCLE"
            guidance = "Sleep cycle active. Deep infrared ambient lighting for night navigation."

        profile = self.profiles[phase]

        return {
            "circadian_phase": phase,
            "color_temp_kelvin": profile["color_temp_kelvin"],
            "spectral_type": profile["spectral_type"],
            "intensity_lux": profile["intensity_lux"],
            "purpose": profile["purpose"],
            "guidance": guidance,
            "timestamp": current_time.isoformat()
        }

if __name__ == "__main__":
    sync = CircadianLightingSynchronizer()
    print("[MAITRI Circadian Sync] Circadian lighting synchronizer initialized.")
    res = sync.compute_lighting_schedule()
    print(f"[MAITRI Circadian Test] Phase: {res['circadian_phase']}, Temp: {res['color_temp_kelvin']}K ({res['spectral_type']})")
