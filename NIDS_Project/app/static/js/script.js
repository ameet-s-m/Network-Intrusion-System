let simulationInterval = null;

const ctx = document.getElementById('lineChart').getContext('2d');

let labels = [];
let dataPoints = [];

const chart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: labels,
        datasets: [{
            label: 'Attack (1) / Normal (0)',
            data: dataPoints
        }]
    }
});

async function predict() {

    const resultBox = document.getElementById("resultBox");
    const confidenceBox = document.getElementById("confidenceBox");
    const banner = document.getElementById("alertBanner");

    let data = {
        duration: parseFloat(duration.value) || 0,
        src_bytes: parseFloat(src_bytes.value) || 0,
        dst_bytes: parseFloat(dst_bytes.value) || 0,
        protocol_type: parseInt(protocol_type.value),
        flag: parseInt(flag.value)
    };

    let res = await fetch("/predict", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    });

    let result = await res.json();

    if (result.result.includes("Attack")) {
    resultBox.style.color = "red";
} else {
    resultBox.style.color = "lightgreen";
}

resultBox.innerHTML = result.result;
    confidenceBox.innerHTML = "Confidence: " + result.confidence + "%";

    let val = result.result.includes("Attack") ? 1 : 0;

    labels.push(labels.length);
    dataPoints.push(val);
    chart.update();

    if (val === 1) {
        banner.classList.remove("hidden");
    } else {
        banner.classList.add("hidden");
    }
}

function startSimulation() {
    if (simulationInterval) return;

    simulationInterval = setInterval(() => {
        duration.value = Math.random()*100;
        src_bytes.value = Math.random()*5000;
        dst_bytes.value = Math.random()*5000;
        predict();
    }, 2000);
}

function stopSimulation() {
    clearInterval(simulationInterval);
    simulationInterval = null;
}