"""
MAITRI Pre-EVA Cognitive Sharpness & Psychomotor Vigilance Readiness Test Engine
Evaluates astronaut reaction latency (ms), spatial memory accuracy, and lapse counts
to determine pre-spacewalk (EVA) flight clearance and cognitive fatigue.
"""

import os
import sys
from datetime import datetime

class CognitiveReadinessTester:
    def __init__(self):
        # NASA Artemis Psychomotor Vigilance Task (PVT) Baselines
        self.nominal_reaction_ms = 220.0  # Baseline response speed
        self.lapse_threshold_ms = 500.0    # Reaction delay signifying cognitive lapse

    def evaluate_cognitive_test(self, reaction_times_ms, memory_accuracy_percent=95.0):
        """
        Evaluates a sequence of 5 PVT stimulus reaction trials.
        Returns cognitive score (0-100), lapse count, and EVA clearance status.
        """
        if not reaction_times_ms or len(reaction_times_ms) == 0:
            reaction_times_ms = [215, 230, 210, 225, 240]

        mean_rx_ms = round(sum(reaction_times_ms) / len(reaction_times_ms), 1)
        lapses = sum(1 for rx in reaction_times_ms if rx > self.lapse_threshold_ms)

        # Cognitive Score Calculation (0 - 100%)
        rx_penalty = max(0.0, (mean_rx_ms - self.nominal_reaction_ms) * 0.25)
        lapse_penalty = lapses * 20.0
        accuracy_bonus = (memory_accuracy_percent - 80.0) * 0.5 if memory_accuracy_percent > 80.0 else 0.0

        score = max(0.0, min(100.0, 100.0 - rx_penalty - lapse_penalty + accuracy_bonus))
        score = round(score, 1)

        # EVA Flight Clearance Determination
        if score >= 85.0 and lapses == 0:
            status = "FIT FOR EVA (PASSED)"
            recommendation = "Cognitive sharpness optimal. Commander is cleared for spacewalk operations."
        elif score >= 65.0 and lapses <= 1:
            status = "MODERATE FATIGUE (CAUTION)"
            recommendation = "Slight reaction delay observed. Recommend 15-minute hydration & rest before airlock pressurization."
        else:
            status = "UNFIT FOR EVA (REST MANDATORY)"
            recommendation = "Significant psychomotor vigilance degradation. Mandatory 2-hour sleep cycle required prior to EVA retry."

        return {
            "cognitive_score": score,
            "mean_reaction_ms": mean_rx_ms,
            "lapses_count": lapses,
            "memory_accuracy": memory_accuracy_percent,
            "eva_clearance_status": status,
            "recommendation": recommendation,
            "timestamp": datetime.now().isoformat()
        }

if __name__ == "__main__":
    tester = CognitiveReadinessTester()
    print("[MAITRI Cognitive Test] Cognitive readiness engine initialized.")
    res = tester.evaluate_cognitive_test([210, 225, 205, 215, 230], memory_accuracy_percent=98.0)
    print(f"[MAITRI Cognitive Test] Score: {res['cognitive_score']}%, Mean RX: {res['mean_reaction_ms']}ms, Status: {res['eva_clearance_status']}")
