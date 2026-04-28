import json
import random
import time
from datetime import datetime

def generate_mock_shipment():
    shipment_ids = ["SHIP-1001", "SHIP-1002", "SHIP-1003", "SHIP-1004"]
    weather_options = ["clear", "rain", "snow", "storm", "fog"]
    
    shipment = {
        "shipment_id": random.choice(shipment_ids),
        "timestamp": datetime.now().isoformat(),
        "current_lat": 40.7128 + (random.random() - 0.5) * 0.1,
        "current_lng": -74.0060 + (random.random() - 0.5) * 0.1,
        "weather_condition": random.choice(weather_options),
        "traffic_density": round(random.uniform(0.1, 0.9), 2),
        "carrier_reliability_score": 0.85
    }
    return shipment

def simulate_vertex_ai_inference(shipment):
    # Simulate a model that predicts high delay if weather is storm or rain + high traffic
    delay_prob = 0.1
    if shipment["weather_condition"] in ["storm", "snow"]:
        delay_prob += 0.5
    if shipment["traffic_density"] > 0.7:
        delay_prob += 0.3
    
    return min(delay_prob, 1.0)

if __name__ == "__main__":
    print("Starting IoT Data Simulation...")
    while True:
        data = generate_mock_shipment()
        prediction = simulate_vertex_ai_inference(data)
        
        output = {
            "shipment": data,
            "delay_prediction": prediction
        }
        
        # In a real scenario, this would be pushed to Pub/Sub
        # For this prototype, we'll write to a log file or print to stdout
        print(f"SHIPMENT UPDATE: {json.dumps(output, indent=2)}")
        
        # Simulate data every 5 seconds
        time.sleep(5)
