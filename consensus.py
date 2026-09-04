import ast
import difflib
from typing import List, Dict, Any

class ConsensusEngine:
    def __init__(self, min_quality_score=85, enable_code_validation=True):
        self.min_quality_score = min_quality_score
        self.enable_code_validation = enable_code_validation

    def validate_python_code(self, code_str: str) -> bool:
        try:
            ast.parse(code_str)
            return True
        except Exception:
            return False

    def calculate_text_similarity(self, text1: str, text2: str) -> float:
        matcher = difflib.SequenceMatcher(None, text1, text2)
        return matcher.ratio()

    def evaluate_responses(self, task_prompt: str, responses: Dict[str, str]) -> Dict[str, Any]:
        """
        responses: dict of {node_id: response_text}
        """
        if not responses:
            return {
                "quality_score": 0,
                "passed": False,
                "agreements": [],
                "contradictions": ["No responses received."],
                "details": {}
            }

        valid_nodes = list(responses.keys())
        node_count = len(valid_nodes)

        if node_count == 1:
            return {
                "quality_score": 70,
                "passed": 70 >= self.min_quality_score,
                "agreements": ["Single response received"],
                "contradictions": ["Cannot cross-verify with only one active peer"],
                "details": {valid_nodes[0]: {"similarity_avg": 1.0}}
            }

        similarities = []
        contradictions = []
        agreements = []

        for i in range(node_count):
            for j in range(i + 1, node_count):
                node_a, node_b = valid_nodes[i], valid_nodes[j]
                resp_a, resp_b = responses[node_a], responses[node_b]
                sim = self.calculate_text_similarity(resp_a, resp_b)
                similarities.append(sim)

                if sim > 0.7:
                    agreements.append(f"{node_a} and {node_b} show high agreement ({round(sim*100, 1)}%)")
                elif sim < 0.3:
                    contradictions.append(f"{node_a} and {node_b} differ significantly ({round(sim*100, 1)}% similarity)")

        avg_similarity = sum(similarities) / len(similarities) if similarities else 0.0
        base_score = avg_similarity * 100

        # Code validation check if prompt appears to request code
        code_penalty = 0
        if self.enable_code_validation and ("code" in task_prompt.lower() or "python" in task_prompt.lower()):
            for node, resp in responses.items():
                if "```python" in resp:
                    code_blocks = resp.split("```python")[1:]
                    for block in code_blocks:
                        code_content = block.split("```")[0].strip()
                        if not self.validate_python_code(code_content):
                            code_penalty += 15
                            contradictions.append(f"{node} generated invalid Python syntax.")

        final_score = max(0, min(100, int(base_score - code_penalty)))
        passed = final_score >= self.min_quality_score

        return {
            "quality_score": final_score,
            "passed": passed,
            "agreements": agreements,
            "contradictions": contradictions,
            "avg_similarity": round(avg_similarity, 2)
        }
