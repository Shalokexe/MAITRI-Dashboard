"""
MAITRI Mood Rules Engine — Dynamic Psychological Response Router & Guardrails
Evaluates real-time multimodal inputs (facial expression + vocal stress + vitals telemetry)
and selects optimal psychological communication strategies for astronaut well-being.
"""

class MoodResponseRouter:
    def __init__(self):
        # Astronaut safety guardrails
        self.safety_protocols = {
            "4-7-8 Breathing": "Initiating 4-7-8 Deep Breathing: Inhale slowly through your nose for 4 seconds... Hold your breath for 7 seconds... Exhale completely through your mouth for 8 seconds. Repeat 4 cycles.",
            "5-4-3-2-1 Grounding": "Sensory Grounding Protocol: Name 5 things you see in the module, 4 things you can physically touch, 3 sounds you hear, 2 scents, and 1 positive thought.",
            "Hydration & Break": "Telemetry indicates high cognitive workload. Please consume 250ml of water and take a 10-minute visual rest from control screens."
        }

    def route_response(self, user_message, detected_emotion="Focused / Neutral", vocal_stress=20.0, hr_bpm=72):
        """
        Determines conversation tone modifier, safety intervention, and suggested action based on real-time mood.
        """
        msg_lower = user_message.lower()
        intervention = None
        mode = "Empathetic Companion"

        # Check for critical physical/emotional stress signals
        if vocal_stress > 65.0 or "stress" in msg_lower or "overwhelmed" in msg_lower or "panic" in msg_lower:
            intervention = self.safety_protocols["4-7-8 Breathing"]
            mode = "Stress Reduction & Breathwork"
            tone_prefix = "Cmdr. Shalok, I hear tension in your voice and see your stress index rising. Let's take a moment together to recalibrate."
        elif "anxious" in msg_lower or "scared" in msg_lower or "cannot focus" in msg_lower or "Anxious" in detected_emotion:
            intervention = self.safety_protocols["5-4-3-2-1 Grounding"]
            mode = "Cognitive Grounding"
            tone_prefix = "I'm right here with you, Commander. Deep space isolation can trigger cognitive overload. Let's ground your senses."
        elif "tired" in msg_lower or "exhausted" in msg_lower or "sleep" in msg_lower or "Fatigue" in detected_emotion:
            intervention = self.safety_protocols["Hydration & Break"]
            mode = "Recovery & Rest Advisor"
            tone_prefix = "Your cognitive reaction times may slow with current fatigue levels. Prioritizing rest is essential for mission success."
        elif "vital" in msg_lower or "status" in msg_lower or "health" in msg_lower:
            mode = "Operational Health Monitor"
            tone_prefix = f"Telemetry status report for Cmdr. Shalok Dadhwal: Heart Rate is {hr_bpm} BPM, vocal stress is {vocal_stress}%, and emotion baseline is {detected_emotion}."
        else:
            tone_prefix = f"Acknowledged, Cmdr. Shalok. Standard offline companion active."

        return {
            "mode": mode,
            "tone_prefix": tone_prefix,
            "intervention": intervention
        }

if __name__ == "__main__":
    router = MoodResponseRouter()
    res = router.route_response("I am feeling a bit stressed after the simulation.", detected_emotion="Elevated Stress", vocal_stress=72.0)
    print(f"[MAITRI Mood Test] Mode: {res['mode']}, Intervention: {res['intervention']}")
