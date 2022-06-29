const ctx = document.getElementById('incomeChart').getContext('2d');
const ctx2 = document.getElementById('spendingChart').getContext('2d');
fetch('/netChange')
.then(req=>req.json())
.then(res=>{

var labelArray = []
var incomeArray = []

res.map(a=>{
    labelArray.push(a['date'])
    incomeArray.push(a['money'])
})


const myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: labelArray,
        datasets: [{
            label: 'Date',
            data: incomeArray,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 5
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

window.addEventListener('beforeprint', () => {
  myChart.resize(600, 600);
});
window.addEventListener('afterprint', () => {
  myChart.resize();
});



})

// This is spending chart
const spendingData = {
  labels: [
    'Shopping',
    'Traveling',
    'Grocegy'
  ],
  datasets: [{
    label: 'My First Dataset',
    data: [300, 50, 100],
    backgroundColor: [
      'rgb(255, 99, 132)',
      'rgb(54, 162, 235)',
      'rgb(255, 205, 86)'
    ],
    hoverOffset: 4
  }]
};



const mySpendingChart = new Chart(ctx2, {
    type: 'doughnut',
    data: spendingData,
    responsive:true,
});



//let width = 40 ;
//let height = 50;
//
//
//console.log("Hello World")
//var svgContainer = d3.select("div#incomeChart")
//                     .append("svg")
//                     .attr("width",width+"vw")
//                     .attr("height",height+"vh")
//                     .style("border-radius","15px")
//
//
//fetch("/netChange")
//    .then(req=>req.json())
//    .then(res=>{
//
//    var xScale = d3.scaleTime()
//                   .domain(d3.extent(res,data=> new Date(data['date']) ))
//                   .range([0,1200])
//    var yScale = d3.scaleLinear()
//                   .domain([0,d3.max(res,data=>data['money'])])
//                   .range([300,0])
//
//    var xAxis = d3.axisBottom(xScale)
//	var yAxis = d3.axisLeft(yScale)
//
//       svgContainer.append("path")
//      .data(res)
//      .attr("fill", "none")
//      .attr("stroke", "steelblue")
//      .attr("stroke-width", 1.5)
//      .attr("d", d3.line()
//        .x(function(data) { return xScale(new Date(data['date']))})
//        .y(function(data) { return yScale(data['money'])})
//        )
//
//	svgContainer.append("g")
//                .attr("transform", "translate(36,300)")
//                .attr("id","x-axis")
//                .attr("class","tick")
//                .call(xAxis)
//    svgContainer.append("g")
//                .attr("transform", "translate(36,0)")
//                .attr("id","y-axis")
//                .attr("class","tick")
//                .call(yAxis)
//
//
//})