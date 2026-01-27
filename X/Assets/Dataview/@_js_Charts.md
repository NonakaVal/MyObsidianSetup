
```dataviewjs
const pages = dv.pages('"ATLAS"')
    .where(p => p.hub)  // Considera apenas notas com hub definido

const hubCounts = {}

// Conta valores únicos (suportando hub como string ou array)
for (let page of pages) {
    let hubs = Array.isArray(page.hub) ? page.hub : [page.hub]

    for (let hub of hubs) {
        if (hub in hubCounts) {
            hubCounts[hub] += 1
        } else {
            hubCounts[hub] = 1
        }
    }
}

// Ordena por contagem decrescente
const sortedEntries = Object.entries(hubCounts).sort((a, b) => b[1] - a[1])

const labels = sortedEntries.map(entry => entry[0])
const data = sortedEntries.map(entry => entry[1])

const chartData = {
    type: 'bar',
    data: {
        labels: labels,
        datasets: [{
            label: 'Contagem de hubs únicos',
            data: data,
            backgroundColor: 'rgba(255, 159, 64, 0.2)',
            borderColor: 'rgba(255, 159, 64, 1)',
            borderWidth: 1
        }]
    },
    options: {
        indexAxis: 'y',
        scales: {
            x: {
                beginAtZero: true,
                ticks: {
                    precision: 0
                }
            }
        },
        plugins: {
            legend: {
                display: false
            },
            tooltip: {
                callbacks: {
                    label: function(context) {
                        return `${context.label}: ${context.raw} notas`;
                    }
                }
            }
        }
    }
}

window.renderChart(chartData, this.container)

```
