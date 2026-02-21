import json
import sys
import os

class DOMEngine:
    """
    Core DOM Rating Engine.
    Processes metrics and returns A-F ratings.
    """
    RATINGS = {
        'A': (0.9, 'Optimal: Goal met.'),
        'B': (0.7, 'Good: Minor gaps.'),
        'C': (0.5, 'Average: Functional but needs work.'),
        'D': (0.3, 'Poor: Major gaps.'),
        'F': (0.0, 'Critical: Failure.')
    }

    def evaluate(self, metrics):
        if not metrics:
            return 'F', 0.0
        
        avg = sum(metrics.values()) / len(metrics)
        
        for char, (threshold, desc) in self.RATINGS.items():
            if avg >= threshold:
                return char, avg
        return 'F', avg

if __name__ == "__main__":
    # Interface for the agent to call via terminal
    if len(sys.argv) > 1:
        try:
            metrics = json.loads(sys.argv[1])
            engine = DOMEngine()
            r, s = engine.evaluate(metrics)
            print(json.dumps({"rating": r, "score": s, "message": engine.RATINGS[r][1]}))
        except Exception as e:
            print(json.dumps({"error": str(e)}))
