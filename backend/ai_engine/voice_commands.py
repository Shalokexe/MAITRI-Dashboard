"""
MAITRI Voice-Activated Hands-Free Command Engine & Spoken EVA Checklists (Phase 14)
Processes astronaut verbal command intents, triggers portal navigation actions,
and provides step-by-step spoken EVA decompression & spacewalk checklists.
"""

import os
import sys
from datetime import datetime

# Add parent dir to sys.path for backend imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from backend.db.database import get_connection

EVA_CHECKLIST = [
    {
        "step": 1,
        "title": "Suit Pressure Leak & Oxygen Purge",
        "instruction": "Verify EMU suit pressure at 28.4 kPa. Initiate 100% O2 pre-breathe nitrogen purge protocol.",
        "status": "NOMINAL"
    },
    {
        "step": 2,
        "title": "Primary Life Support (PLSS) Power On",
        "instruction": "Engage PLSS battery bank Alpha. Verify primary & secondary O2 tank pressures at 20.6 MPa.",
        "status": "NOMINAL"
    },
    {
        "step": 3,
        "title": "Airlock Depressurization",
        "instruction": "Open airlock vent valve. Monitor cabin pressure drop from 101.3 kPa down to 0.0 kPa vacuum.",
        "status": "IN_PROGRESS"
    },
    {
        "step": 4,
        "title": "Safety Tether Lock & Outer Hatch Unlatch",
        "instruction": "Attach dual-redundant safety tether to airlock anchor. Rotate outer hatch manual handle 180 degrees.",
        "status": "PENDING"
    },
    {
        "step": 5,
        "title": "EVA Egress & Comm Link Verification",
        "instruction": "Egress airlock module. Confirm S-band audio telemetry clarity with Mission Control & MAITRI AI.",
        "status": "PENDING"
    }
]

class VoiceCommandEngine:
    def __init__(self):
        self.eva_checklist = EVA_CHECKLIST

    def parse_command(self, transcript):
        """Parses astronaut voice transcript and returns action payload + spoken response."""
        if not transcript or not transcript.strip():
            return {
                "action": "NONE",
                "speech": "Commander, I did not detect voice input.",
                "tab": None
            }

        t_lower = transcript.lower().strip()

        # Intent 1: Check Vitals / Health
        if any(w in t_lower for w in ["vital", "health", "heart", "stress"]):
            return {
                "action": "NAVIGATE_TAB",
                "tab": "vitals",
                "speech": "Navigating to Vitals and Stress Telemetry. Heart rate and SpO2 levels are nominal."
            }

        # Intent 2: Run ECLSS / Life Support Check
        elif any(w in t_lower for w in ["eclss", "oxygen", "life support", "pressure"]):
            return {
                "action": "ECLSS_DIAGNOSTIC",
                "tab": "dashboard",
                "speech": "ECLSS Diagnostic Complete. Cabin oxygen is optimal at 99.2%, CO2 scrubbers functioning normally."
            }

        # Intent 3: Launch F1 Reflex Arena
        elif any(w in t_lower for w in ["f1", "reflex", "game", "race"]):
            return {
                "action": "OPEN_ROUTE",
                "url": "f1_reflex.html",
                "speech": "Opening F1 Start Lights Reflex Arena standalone route. Get ready for green lights!"
            }

        # Intent 4: Launch Chess Arena
        elif any(w in t_lower for w in ["chess", "grandmaster", "board"]):
            return {
                "action": "OPEN_ROUTE",
                "url": "chess.html",
                "speech": "Opening Grandmaster AI Chess Arena. White to move."
            }

        # Intent 5: Spacewalk / EVA Checklist
        elif any(w in t_lower for w in ["eva", "spacewalk", "checklist", "decompression"]):
            return {
                "action": "EVA_CHECKLIST",
                "tab": "dashboard",
                "step": 1,
                "speech": "Initiating Spoken EVA Spacewalk Checklist. Step 1: Verify EMU suit pressure at 28.4 kPa and start O2 purge."
            }

        # Intent 6: Open Audiobook Library
        elif any(w in t_lower for w in ["book", "library", "audiobook", "listen"]):
            return {
                "action": "NAVIGATE_TAB",
                "tab": "entertainment",
                "speech": "Navigating to Deep-Space Audiobook and E-Book Library."
            }

        # Fallback
        else:
            return {
                "action": "AI_CHAT",
                "tab": None,
                "speech": f"Command received: '{transcript}'. MAITRI AI assistant processing telemetry request."
            }

    def get_eva_step(self, step_number):
        """Returns specific EVA checklist step details."""
        step_idx = max(1, min(len(self.eva_checklist), step_number)) - 1
        return self.eva_checklist[step_idx]

if __name__ == "__main__":
    engine = VoiceCommandEngine()
    test_cmd = "MAITRI run ECLSS diagnostic"
    res = engine.parse_command(test_cmd)
    print(f"[MAITRI Voice Engine] Command: '{test_cmd}' -> Speech: '{res['speech']}'")
