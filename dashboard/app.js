const shipments = [
    { id: "SHIP-1001", location: "New York, NY", weather: "☀️ Clear", delay: 2, status: "Normal" },
    { id: "SHIP-1002", location: "Chicago, IL", weather: "☁️ Cloudy", delay: 5, status: "Normal" },
    { id: "SHIP-1003", location: "Los Angeles, CA", weather: "☀️ Clear", delay: 1, status: "Normal" }
];

function updateShipmentList() {
    const list = document.getElementById('shipment-list');
    list.innerHTML = '';
    
    shipments.forEach(s => {
        const item = document.createElement('div');
        item.className = 'shipment-item';
        item.innerHTML = `
            <div class="info">
                <strong>${s.id}</strong>
                <span>${s.location}</span>
            </div>
            <div class="stats">
                <span class="weather">${s.weather}</span>
                <span class="delay ${s.delay > 50 ? 'high' : 'low'}">Delay: ${s.delay}%</span>
            </div>
        `;
        list.appendChild(item);
    });
}

function addLog(msg, agent = "Monitor") {
    const logs = document.getElementById('agent-logs');
    const time = new Date().toLocaleTimeString();
    const entry = document.createElement('div');
    entry.className = 'log-entry';
    entry.style.borderLeftColor = agent === "Monitor" ? "#7000ff" : agent === "Planner" ? "#00f2ff" : "#00ff88";
    entry.innerHTML = `<span class="time">${time}</span><span class="msg">[${agent}] ${msg}</span>`;
    logs.prepend(entry);
}

function updatePrediction(score) {
    const radial = document.getElementById('prediction-score');
    radial.style.setProperty('--value', score);
    radial.querySelector('.inner').innerText = score + '%';
    
    const text = document.querySelector('.insight-text');
    if (score > 70) {
        text.innerHTML = 'Probability of significant delay is <strong>Critical</strong>. Rerouting agents active.';
        text.style.color = '#ff3e3e';
    } else {
        text.innerHTML = 'Probability of significant delay across network is currently <strong>Low</strong>.';
        text.style.color = '#a0a0a0';
    }
}

document.getElementById('simulate-incident').addEventListener('click', () => {
    addLog("Simulating severe weather in Mid-West area...");
    
    setTimeout(() => {
        addLog("Vertex AI detected delay risk for SHIP-1002.", "Monitor");
        updatePrediction(84);
        
        // Update shipment
        const s2 = shipments.find(s => s.id === "SHIP-1002");
        s2.weather = "⛈️ Severe Storm";
        s2.delay = 84;
        updateShipmentList();

        setTimeout(() => {
            addLog("Analyzing alternative routes... Bypassing Storm-X4 zone.", "Planner");
            
            setTimeout(() => {
                addLog("Execution Agent: Reroute SHIP-1002 via Route-Southern-Bypass.", "Executor");
                s2.location = "St. Louis, MO (Rerouted)";
                s2.delay = 12;
                updateShipmentList();
                updatePrediction(12);
                addLog("Network stabilized. Delay mitigated by 72%.", "Monitor");
            }, 2000);
        }, 1500);
    }, 1000);
});

// Init
updateShipmentList();
addLog("Antigravity Agents Online.");
addLog("Vertex AI Endpoint connected.");
