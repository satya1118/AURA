import time
import random
from datetime import datetime

# -----------------------------
# Agent Configuration
# -----------------------------

RISK_THRESHOLD = 0.70
ESCALATION_THRESHOLD = 0.85

# -----------------------------
# Simulated Data Sources
# -----------------------------

def get_911_signal():
    return random.uniform(0.3, 0.9)

def get_weather_signal():
    return random.choice(["clear", "rain", "storm"])

def get_crowd_density():
    return random.randint(20, 120)

def get_recent_incidents():
    return random.randint(0, 5)

# -----------------------------
# Agent Core
# -----------------------------

class AURAAgent:
    def __init__(self):
        self.memory = []

    def observe(self):
        signal = {
            "timestamp": datetime.utcnow(),
            "risk_score": get_911_signal(),
            "weather": get_weather_signal(),
            "crowd_density": get_crowd_density(),
            "recent_incidents": get_recent_incidents()
        }
        return signal

    def reason(self, signal):
        risk = signal["risk_score"]

        if signal["weather"] in ["rain", "storm"]:
            risk += 0.05

        if signal["crowd_density"] > 80:
            risk += 0.05

        if signal["recent_incidents"] >= 3:
            risk += 0.05

        return min(risk, 1.0)

    def decide(self, risk):
        if risk >= ESCALATION_THRESHOLD:
            return "ESCALATE_TO_HUMAN"
        elif risk >= RISK_THRESHOLD:
            return "RECOMMEND_DISPATCH"
        else:
            return "MONITOR"

    def act(self, decision, signal, risk):
        action = {
            "timestamp": signal["timestamp"],
            "decision": decision,
            "confidence": round(risk, 2),
            "explanation": self.explain(decision, signal, risk)
        }
        self.memory.append(action)
        return action

    def explain(self, decision, signal, risk):
        return (
            f"Decision '{decision}' made due to elevated risk score ({round(risk,2)}), "
            f"weather='{signal['weather']}', crowd_density={signal['crowd_density']}, "
            f"recent_incidents={signal['recent_incidents']}."
        )

# -----------------------------
# Simulated Real-Time Loop
# -----------------------------

def run_agent():
    agent = AURAAgent()

    for _ in range(5):  # simulate 5 time steps
        signal = agent.observe()
        risk = agent.reason(signal)
        decision = agent.decide(risk)
        action = agent.act(decision, signal, risk)

        print("\n🧠 AURA Agent Decision")
        print(action)

        time.sleep(2)  # simulate real-time delay

# -----------------------------
# Entry Point
# -----------------------------

if __name__ == "__main__":
    run_agent()
