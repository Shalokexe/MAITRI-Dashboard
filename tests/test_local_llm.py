import unittest
from backend.ai_engine.local_llm import LocalLLMEngine

class TestLocalLLMEngine(unittest.TestCase):
    def setUp(self):
        self.engine = LocalLLMEngine(model_name="qwen2:1.5b")

    def test_fallback_response_generation(self):
        res = self.engine.generate_response("Tell me about Qwen model")
        self.assertIn("source", res)
        self.assertIn("text", res)
        self.assertTrue(res["air_gapped"])
        self.assertIn("Qwen", res["text"])

    def test_vitals_prompt_handling(self):
        res = self.engine.generate_response("Check vitals status")
        self.assertTrue(res["air_gapped"])
        self.assertIn("Telemetry Summary", res["text"])

    def test_system_prompt_formatting(self):
        self.assertIn("ISRO Gaganyaan", self.engine.system_prompt)
        self.assertIn("Shalok Dadhwal", self.engine.system_prompt)

if __name__ == '__main__':
    unittest.main()
