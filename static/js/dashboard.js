const canvas = document.getElementById("cashflowChart");
const dataTag = document.getElementById("cashflow-data");

if (canvas && dataTag) {
    const data = JSON.parse(dataTag.textContent);

    const months = data.map(d => d.month);
    const balances = data.map(d => d.balance);

    new Chart(canvas, {
        type: "line",
        data: {
            labels: months,
            datasets: [{
                label: "Cash Balance",
                data: balances,
                borderWidth: 3,
                tension: 0.4
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    labels: { color: "#e5e7eb" }
                }
            },
            scales: {
                x: { ticks: { color: "#94a3b8" } },
                y: { ticks: { color: "#94a3b8" } }
            }
        }
    });
}
// =====================
// SENSITIVITY BAR CHART (Animated)
// =====================
const sensitivityCanvas = document.getElementById("sensitivityChart");
const sensitivityDataTag = document.getElementById("sensitivity-data");

if (sensitivityCanvas && sensitivityDataTag) {
    const data = JSON.parse(sensitivityDataTag.textContent);

    const labels = Object.keys(data);
    const values = labels.map(k => data[k].probability);

    new Chart(sensitivityCanvas, {
        type: "bar",
        data: {
            labels: labels,
            datasets: [{
                label: "Failure Probability (%)",
                data: values,
                backgroundColor: [
                    "rgba(59,130,246,0.8)",
                    "rgba(239,68,68,0.8)"
                ],
                borderRadius: 10
            }]
        },
        options: {
            responsive: true,
            animation: {
                duration: 1500,
                easing: "easeOutQuart"
            },
            plugins: {
                legend: { display: false }
            },
            scales: {
                x: { ticks: { color: "#94a3b8" } },
                y: { ticks: { color: "#94a3b8" } }
            }
        }
    });
}


// =====================
// MONTE CARLO LINE (Animated Draw)
// =====================
const monteCanvas = document.getElementById("monteCarloChart");
const monteDataTag = document.getElementById("monte-data");

if (monteCanvas && monteDataTag) {
    const data = JSON.parse(monteDataTag.textContent);

    new Chart(monteCanvas, {
        type: "line",
        data: {
            labels: ["Best", "Average", "Worst"],
            datasets: [{
                label: "Failure Probability (%)",
                data: [data.best, data.average, data.worst],
                borderColor: "rgba(59,130,246,0.9)",
                backgroundColor: "rgba(59,130,246,0.2)",
                tension: 0.4,
                fill: true,
                borderWidth: 3
            }]
        },
        options: {
            responsive: true,
            animation: {
                duration: 2000,
                easing: "easeInOutQuart"
            },
            plugins: {
                legend: { display: false }
            },
            scales: {
                x: { ticks: { color: "#94a3b8" } },
                y: { ticks: { color: "#94a3b8" } }
            }
        }
    });
}

// =========================
// SCENARIO BAR CHART
// =========================
const scenarioCanvas = document.getElementById("scenarioChart");
const scenarioDataTag = document.getElementById("scenario-data");

if (scenarioCanvas && scenarioDataTag) {
    const data = JSON.parse(scenarioDataTag.textContent);

    const labels = Object.keys(data);
    const values = labels.map(k => data[k].probability);

    new Chart(scenarioCanvas, {
        type: "bar",
        data: {
            labels: labels,
            datasets: [{
                label: "Failure Probability (%)",
                data: values,
                backgroundColor: [
                    "rgba(34,197,94,0.7)",   // Optimistic - green
                    "rgba(59,130,246,0.7)",  // Base - blue
                    "rgba(239,68,68,0.7)"    // Pessimistic - red
                ],
                borderRadius: 8
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: { display: false }
            },
            scales: {
                x: { ticks: { color: "#94a3b8" } },
                y: { ticks: { color: "#94a3b8" } }
            }
        }
    });
}


// =========================
// RECOMMENDATION GAUGE
// =========================
const recCanvas = document.getElementById("recommendationChart");
const recDataTag = document.getElementById("recommendation-data");

if (recCanvas && recDataTag) {
    const data = JSON.parse(recDataTag.textContent);
    const prob = data.probability;

    let color;
    if (prob < 25) color = "rgba(34,197,94,0.8)";
    else if (prob < 50) color = "rgba(234,179,8,0.8)";
    else color = "rgba(239,68,68,0.8)";

    new Chart(recCanvas, {
        type: "doughnut",
        data: {
            labels: ["Failure Risk", "Safe Zone"],
            datasets: [{
                data: [prob, 100 - prob],
                backgroundColor: [color, "rgba(30,41,59,0.5)"],
                borderWidth: 0
            }]
        },
        options: {
            cutout: "70%",
            plugins: {
                legend: { display: false }
            }
        }
    });
}
// =====================
// FEATURE IMPORTANCE (Animated Horizontal Bar)
// =====================
const importanceCanvas = document.getElementById("importanceChart");
const importanceDataTag = document.getElementById("importance-data");

if (importanceCanvas && importanceDataTag) {
    const data = JSON.parse(importanceDataTag.textContent);

    const labels = Object.keys(data);
    const values = Object.values(data);

    new Chart(importanceCanvas, {
        type: "bar",
        data: {
            labels: labels,
            datasets: [{
                label: "Impact Score",
                data: values,
                backgroundColor: "rgba(139,92,246,0.8)",
                borderRadius: 8
            }]
        },
        options: {
            indexAxis: 'y',
            responsive: true,
            animation: {
                duration: 1800,
                easing: "easeOutQuart"
            },
            plugins: {
                legend: { display: false }
            },
            scales: {
                x: { ticks: { color: "#94a3b8" } },
                y: { ticks: { color: "#94a3b8" } }
            }
        }
    });
}
