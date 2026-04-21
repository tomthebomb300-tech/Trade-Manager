fetch('http://localhost:5000/post_test', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        symbol: "AAPL",
        entry: 150,
        exit: 160
    })
})
.then(res => res.json())
.then(data => console.log(data));

fetch('http://localhost:5000/get_test')
.then(res => res.json())
.then(data => {
    console.log(data);
});