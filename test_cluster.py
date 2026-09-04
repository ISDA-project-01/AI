import unittest
import os
import json
from consensus import ConsensusEngine
from security import hash_password, verify_password, sanitize_filename, is_safe_path
from auth import authenticate_user, verify_session
from search import MultiSearchAggregator
from main import MasterCoordinator
from api import app

class TestVAPICCluster(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_security_hashing_and_path(self):
        pwd = "testpassword123"
        hashed, salt = hash_password(pwd)
        self.assertTrue(verify_password(pwd, hashed, salt))
        self.assertFalse(verify_password("wrongpwd", hashed, salt))

        clean_fn = sanitize_filename("../../etc/passwd")
        self.assertEqual(clean_fn, "passwd")

        self.assertTrue(is_safe_path("/tmp/jobs", "/tmp/jobs/JOB1/file.txt"))
        self.assertFalse(is_safe_path("/tmp/jobs", "/tmp/jobs/../secret.txt"))

    def test_auth_login(self):
        token = authenticate_user("admin", "adminpassword123")
        self.assertIsNotNone(token)
        session = verify_session(token)
        self.assertEqual(session["role"], "admin")

    def test_consensus_engine(self):
        engine = ConsensusEngine(min_quality_score=80)
        responses = {
            "pc2": "Quantum computing uses qubits and superposition.",
            "pc3": "Quantum computing utilizes qubits, entanglement, and superposition.",
            "pc4": "Quantum computing is based on qubits and quantum superposition principles."
        }
        res = engine.evaluate_responses("Explain quantum computing", responses)
        self.assertGreaterEqual(res["quality_score"], 70)

    def test_search_aggregator(self):
        agg = MultiSearchAggregator()
        results = agg.aggregate_search("quantum computing")
        self.assertGreater(len(results), 0)

    def test_master_job_execution(self):
        coordinator = MasterCoordinator()
        job = coordinator.run_job("What is 2 + 2?")
        self.assertEqual(job["status"], "COMPLETED")
        self.assertIn("final_synthesis", job)

    def test_api_status_and_chat(self):
        status_resp = self.app.get('/api/status')
        self.assertEqual(status_resp.status_code, 200)

        chat_resp = self.app.post('/api/chat', json={"prompt": "Test query"})
        self.assertEqual(chat_resp.status_code, 200)
        data = chat_resp.get_json()
        self.assertIn("final_synthesis", data)

if __name__ == "__main__":
    unittest.main()
