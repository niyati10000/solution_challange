import json

class SupplyChainAgent:
    def __init__(self, name):
        self.name = name

    def log(self, message):
        print(f"[{self.name}] {message}")

class MonitorAgent(SupplyChainAgent):
    def __init__(self):
        super().__init__("MonitorAgent")

    def process_data(self, data):
        prediction = data.get("delay_prediction", 0)
        shipment_id = data["shipment"]["shipment_id"]
        
        if prediction > 0.6:
            self.log(f"ALERT: High delay probability ({prediction:.2f}) for {shipment_id}")
            return True # Trigger Rerouting
        else:
            self.log(f"Status Normal for {shipment_id}")
            return False

class PlannerAgent(SupplyChainAgent):
    def __init__(self):
        super().__init__("PlannerAgent")

    def plan_reroute(self, data):
        shipment_id = data["shipment"]["shipment_id"]
        current_weather = data["shipment"]["weather_condition"]
        
        self.log(f"Analyzing rerouting options for {shipment_id} due to {current_weather}...")
        # Simulated logic for route optimization
        new_route = "Route-B (Avoids storm zone)" if current_weather == "storm" else "Route-C (Traffic bypass)"
        
        return {
            "shipment_id": shipment_id,
            "original_route": "Route-A",
            "suggested_route": new_route,
            "estimated_time_saving": "45 mins",
            "reasoning": f"Switching to {new_route} to mitigate {current_weather} impact."
        }

class ExecutionAgent(SupplyChainAgent):
    def __init__(self):
        super().__init__("ExecutionAgent")

    def execute(self, plan):
        self.log(f"EXECUTING REROUTE for {plan['shipment_id']}: {plan['suggested_route']}")
        self.log(f"Reasoning: {plan['reasoning']}")
        return {"status": "success", "applied_at": "2026-04-28T21:49:00"}

def main():
    # Setup Agents
    monitor = MonitorAgent()
    planner = PlannerAgent()
    executor = ExecutionAgent()

    # Mock sequence
    sample_delayed_data = {
        "shipment": {
            "shipment_id": "SHIP-1001",
            "weather_condition": "storm",
            "traffic_density": 0.8
        },
        "delay_prediction": 0.85
    }

    if monitor.process_data(sample_delayed_data):
        plan = planner.plan_reroute(sample_delayed_data)
        result = executor.execute(plan)
        print(f"\nFinal Result: {json.dumps(result, indent=2)}")

if __name__ == "__main__":
    main()
