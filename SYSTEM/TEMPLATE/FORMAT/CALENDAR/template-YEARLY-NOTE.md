---
created: <% tp.file.creation_date() %>
tags:
  - calendar/yearly
---

🌍 Yearly Review - <%- tp.date.now("YYYY") %>


# ✅ Revisão do Ano

````tabs

tab: Tasks concluídas
```dataview
TABLE WITHOUT ID
	key as Tasks,
	length(rows) AS Total,
	length(filter(rows.tasks, (r) => r.completed)) AS Completed
FROM "EFFORTS" AND !"EFFORTS/11_ARCHIVES"
FLATTEN file.tasks as tasks
WHERE file.mtime >= date(today) - dur(365 days)  // Arquivos do ano
GROUP BY file.link
SORT length(rows) DESC
```

### Lista das Yasks

```dataview
TASK
FROM "EFFORTS"
WHERE completed AND checked AND type != "area_utils"
  AND file.mtime >= date(today) - dur(365 days)  // Últimos 365 dias
GROUP BY file.name

tab: Mood anual

```dataviewjs
const moodScale = {
  "😄 – Happy": 5,
  "🙂 – Neutral": 4,
  "😐 – Meh": 3,
  "😞 – Sad": 2,
  "😠 – Frustrated": 1
}

const moodColors = {
  5: '#4caf50',
  4: '#8bc34a',
  3: '#ffc107',
  2: '#ff9800',
  1: '#f44336'
}

const moodLabels = Object.entries(moodScale).reduce((acc, [k, v]) => {
  acc[v] = k
  return acc
}, {})

const startDate = moment().subtract(1, 'year')
const pages = dv.pages('#calendar/daily')
  .where(p => p["daily-mood"] !== undefined && moment(p.file.name).isAfter(startDate))
  .sort(p => p.file.name, 'asc')

const labels = []
const data = []
const colors = []
const pointStyles = []

for (let p of pages) {
  const date = moment(p.file.name).format('MMM YY')
  const mood = p["daily-mood"]
  const moodValue = moodScale[mood]
  if (moodValue !== undefined) {
    labels.push(date)
    data.push(moodValue)
    colors.push(moodColors[moodValue])
    pointStyles.push('circle')
  }
}

const chartData = {
  type: 'line',
  data: {
    labels,
    datasets: [{
      label: 'Humor ao Longo do Ano',
      data,
      borderColor: '#2196f3',
      backgroundColor: 'rgba(33, 150, 243, 0.1)',
      pointBackgroundColor: colors,
      pointBorderColor: colors,
      borderWidth: 2,
      tension: 0.3,
      fill: true,
      pointRadius: 4,
      pointHoverRadius: 6,
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
          callback: val => moodLabels[val] || val
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
          font: {
            size: 10
          }
        },
        title: {
          display: true,
          text: 'Mês',
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
          title: ctx => ctx[0].label
        }
      },
      legend: {
        display: true,
        position: 'top',
        labels: {
          boxWidth: 12,
          font: {
            size: 12
          },
          usePointStyle: true
        }
      },
      title: {
        display: true,
        text: 'Evolução do Humor em ' + moment().format('YYYY'),
        font: {
          size: 16,
          weight: 'bold'
        }
      }
    }
  }
}

const container = this.container
container.style.height = '450px'
container.style.width = '100%'

window.renderChart(chartData, container)
```

````


### **Principais Conquistas do Ano**


### **Desafios mais marcantes**


# 🎯 Metas e Direcionamentos para <%- tp.date.now("YYYY") %>




## on Going and tasks

````tabs
tab: Area Family
```dataview
table area_category as "Area Category", created as "Date Created" from "EFFORTS/09_AREAS"
WHERE type = "area_family"
SORT file.mtime DESC
```

tab: Writing Notes
![[Writing]]

tab: Estudos 
![[ESTUDOS]]

tab: Career 
![[Career-development]]


tab: Pkm Youtube Videos
![[EFFORTS/09_AREAS/PKM-Youtube-Videos/PKM-Youtube-Videos|PKM-Youtube-Videos]]





````

````tabs
tab: Areas Tasks
```dataview
TASK
FROM "EFFORTS/09_AREAS" 
WHERE !completed AND !checked and type != "area_utils" 
GROUP BY file.name 
SORT file.mtime DESC

```

tab: Calendar Tasks
```dataview
TASK
FROM "CALENDAR" AND -#inlog AND -#lost-codes 
WHERE !completed AND !checked and type != "area_utils"

```

tab: Done Efforts
```dataview
TASK
FROM "EFFORTS" 
WHERE completed AND checked and type != "area_utils"
GROUP BY file.name

```
````




Last modified : `$= dv.current().file.mtime`