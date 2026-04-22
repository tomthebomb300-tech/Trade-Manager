// fetch('http://localhost:5000/post_test', {
//     method: 'POST',
//     headers: {
//         'Content-Type': 'application/json'
//     },
//     body: JSON.stringify({
//         symbol: "AAPL",
//         entry: 150,
//         exit: 160
//     })
// })
// .then(res => res.json())
// .then(data => console.log(data));

// fetch('http://localhost:5000/get_test')
// .then(res => res.json())
// .then(data => {
//     console.log(data);
// });
window.onload = init;

function init(){
    updateHeaders();
    updateDailyAccountBalance();
}

function updateHeaders(){
    fetch('http://localhost:5000/get_profit_loss').then(res=>res.json())
    .then(pl=>{document.getElementById("OverallPL").textContent = pl});
    
    fetch('http://localhost:5000/get_win_rate').then(res=>res.json())
    .then(winRate=>{document.getElementById("OverallWinPercentage").textContent = winRate});
    
    fetch('http://localhost:5000/get_average_win').then(res=>res.json())
    .then(averageWin=>{document.getElementById("OverallAverageWin").textContent = averageWin});

    fetch('http://localhost:5000/get_average_loss').then(res=>res.json())
    .then(averageLoss=>{document.getElementById("OverallAverageLoss").textContent = averageLoss});
    
    fetch('http://localhost:5000/get_profit_factor').then(res=>res.json())
    .then(pf=>{document.getElementById("OverallProfitFactor").textContent = pf});
}

function updateDailyAccountBalance(){
    fetch('http://localhost:5000/get_daily_PL').then(res=>res.json())
    .then(data=>{
        const labels = data.map(d => new Date(d.date));
        const values = data.map(d => d.balance);
        const ctx = document.getElementById('dailyAccountBalance');

        console.log(data);
        
        new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
            label: 'Balance',
            data: values,
            borderWidth: 2
            }]
        },
        options: {
            scales: {
            x: {
                type: 'time',
                time: {
                unit: 'day'
                }
            }
            }
        }
        });
    });
}