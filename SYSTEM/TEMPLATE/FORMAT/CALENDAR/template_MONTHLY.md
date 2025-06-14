---
created: '[[<% tp.date.now("YYYY-MM-DD") %>]]'
tags:
  - calendar/monthly
---


🌱 Monthly Review - <%- tp.date.now("MMMM") %>  - Year: '[[<%- tp.date.now("YYYY") %>]]'

# ✅ Revisão do Mês Anterior

## Tasks

````tabs
tab: Calendar tasks
![[@_dataview_Calendar-tasks]]

tab: Efforts Tasks
![[@_dataview-efforts-tasks]]

tab: All tasks
![[@_dataview-all-tasks]]
````


## MOOD and Focus

```dataviewjs
const pages = dv.pages().file.lists
  .filter(item => item?.pomodoro === "WORK" && item.end?.length >= 10)

const grouped = {}
for (const item of pages) {
  const date = item.end.substring(0, 10)
  if (!grouped[date]) grouped[date] = []
  grouped[date].push(item)
}

const labels = []
const minutesSum = []

for (const [date, items] of Object.entries(grouped).sort()) {
  labels.push(moment(date).format('DD/MM'))
  const totalMinutes = items.reduce((sum, item) => sum + item.duration.as("minutes"), 0)
  minutesSum.push(totalMinutes)
}

const chartData = {
  type: 'line',
  data: {
    labels,
    datasets: [{
      label: 'Minutos Trabalhados',
      data: minutesSum,
      borderColor: '#42a5f5',
      backgroundColor: 'rgba(66, 165, 245, 0.1)',
      borderWidth: 2,
      tension: 0.3,
      fill: true,
      pointRadius: 4,
      pointHoverRadius: 6,
      pointBackgroundColor: '#42a5f5',
      pointBorderColor: '#42a5f5'
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    interaction: {
      intersect: false,
      mode: 'index'
    },
    scales: {
      y: {
        beginAtZero: true,
        ticks: {
          color: '#ccc',
          font: { size: 10 }
        },
        title: {
          display: true,
          text: 'Minutos',
          font: { size: 12 }
        },
        grid: {
          color: 'rgba(255, 255, 255, 0.05)'
        }
      },
      x: {
        ticks: {
          color: '#ccc',
          font: { size: 10 }
        },
        title: {
          display: true,
          text: 'Data',
          font: { size: 12 }
        },
        grid: {
          display: false
        }
      }
    },
    plugins: {
      tooltip: {
        backgroundColor: '#222',
        titleFont: { size: 12 },
        bodyFont: { size: 12 },
        callbacks: {
          label: ctx => `${ctx.raw} min`
        }
      },
      legend: {
        display: false
      },
      title: {
        display: true,
        text: 'Minutos Trabalhados por Dia',
        color: '#fff',
        font: {
          size: 14,
          weight: 'bold'
        },
        padding: {
          top: 10,
          bottom: 10
        }
      }
    }
  }
}

const container = this.container
container.style.height = '400px'
container.style.width = '100%'

window.renderChart(chartData, container)

```

```dataviewjs
const moodScale = {
  "😄 – Happy": 5,
  "🙂 – Neutral": 4,
  "😐 – Meh": 3,
  "😞 – Sad": 2,
  "😠 – Frustrated": 1
};

const moodColors = {
  5: '#4caf50',
  4: '#8bc34a',
  3: '#ffc107',
  2: '#ff9800',
  1: '#f44336'
};

const moodLabels = Object.entries(moodScale).reduce((acc, [k, v]) => {
  acc[v] = k;
  return acc;
}, {});

const startDate = moment('01/05/2025', 'DD/MM/YYYY');
const endDate = moment('30/05/2025', 'DD/MM/YYYY'); // Junho tem 30 dias

const pages = dv.pages('#calendar/daily')
  .sort(p => p.file.name, 'asc');

const labels = [];
const data = [];
const colors = [];
const pointStyles = [];

for (let p of pages) {
  const fileDate = moment(p.file.name, 'YYYY-MM-DD'); // nome do arquivo deve ser data
  const isWithinRange = fileDate.isBetween(startDate, endDate, null, '[]');

  if (isWithinRange && p["daily-mood"] !== undefined) {
    const dateLabel = fileDate.format('DD/MM/YY');
    const mood = p["daily-mood"];
    const moodValue = moodScale[mood];
    if (moodValue !== undefined) {
      labels.push(dateLabel);
      data.push(moodValue);
      colors.push(moodColors[moodValue]);
      pointStyles.push('circle');
    }
  }
}

const chartData = {
  type: 'line',
  data: {
    labels,
    datasets: [{
      label: 'Humor em Junho de 2025',
      data,
      borderColor: '#7e57c2',
      backgroundColor: 'rgba(126, 87, 194, 0.1)',
      pointBackgroundColor: colors,
      pointBorderColor: colors,
      borderWidth: 2,
      tension: 0.3,
      fill: true,
      pointRadius: 5,
      pointHoverRadius: 7,
      pointStyle: pointStyles
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    interaction: {
      intersect: false,
      mode: 'index'
    },
    scales: {
      y: {
        min: 0.5,
        max: 5.5,
        ticks: {
          stepSize: 1,
          callback: val => moodLabels[val] || val,
          font: {
            size: 11
          }
        },
        title: {
          display: true,
          text: 'Estado Emocional',
          font: {
            size: 12,
            weight: 'bold'
          }
        },
        grid: {
          color: 'rgba(200, 200, 200, 0.1)'
        }
      },
      x: {
        ticks: {
          autoSkip: true,
          maxRotation: 45,
          minRotation: 30,
          font: {
            size: 10
          }
        },
        title: {
          display: true,
          text: 'Data',
          font: {
            size: 12,
            weight: 'bold'
          }
        },
        grid: {
          display: false
        }
      }
    },
    plugins: {
      tooltip: {
        callbacks: {
          label: ctx => `Humor: ${moodLabels[ctx.raw] || ctx.raw}`,
          title: ctx => moment(ctx[0].label, 'DD/MM/YY').format('DD MMMM YYYY')
        },
        displayColors: true,
        backgroundColor: 'rgba(30, 30, 30, 0.9)',
        titleFont: {
          size: 12
        },
        bodyFont: {
          size: 12
        }
      },
      legend: {
        display: true,
        position: 'top',
        labels: {
          color: '#ddd',
          boxWidth: 12,
          padding: 10,
          font: {
            size: 12
          },
          usePointStyle: true
        }
      },
      title: {
        display: true,
        text: 'Evolução do Humor - Junho 2025',
        color: '#ffffff',
        font: { 
          size: 16,
          weight: 'bold'
        },
        padding: {
          top: 10,
          bottom: 20
        }
      }
    }
  }
};

// Adiciona um contêiner com altura fixa para melhor visualização
const container = this.container;
container.style.height = '450px';
container.style.width = '100%';

window.renderChart(chartData, container);
```


##  **O que foi alcançado?**

## **Desafios encontrados**:

# 📅 Metas para Este Mês

Last modified: `$= dv.current().file.mtime`
