// The line chart
var chart = new Chart(document.getElementById('myChart2'), {
	type: 'line',
	data: {
		labels: ["January", "February", "March", "April", 'May', 'June', 'August', 'September'],
		datasets: [{
			label: "My First dataset",
			data: [4, 20, 5, 20, 5, 25, 9, 18],
			backgroundColor: 'transparent',
			borderColor: '#0d6efd',
			lineTension: .4,
			borderWidth: 1.5,
		}, {
			label: "Month",
			data: [11, 25, 10, 25, 10, 30, 14, 23],
			backgroundColor: 'transparent',
			borderColor: '#dc3545',
			lineTension: .4,
			borderWidth: 1.5,
		}, {
			label: "Month",
			data: [16, 30, 16, 30, 16, 36, 21, 35],
			backgroundColor: 'transparent',
			borderColor: '#f0ad4e',
			lineTension: .4,
			borderWidth: 1.5,
		}]
	},
	options: {
		scales: {
			yAxes: [{
				gridLines: {
					drawBorder: false
				},
				ticks: {
					stepSize: 12,
				}
			}],
			xAxes: [{
				gridLines: {
					display: false,
				},
			}]
		}
	}
})