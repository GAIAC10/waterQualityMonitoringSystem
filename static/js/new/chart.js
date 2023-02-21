// PH
var chart = Highcharts.chart('container', {
	chart: {
		type: 'line'
	},
	title: {
		text: '酸碱度(PH)'
	},
	xAxis: {
		categories: ['Sun', 'Sat', 'Fri', 'Thur', 'Wed', 'Tue', 'Mon']
	},
	yAxis: {
		title: {
			text: 'PH'
		}
	},
	plotOptions: {
		line: {
			dataLabels: {
				// 开启数据标签
				enabled: true
			},
			// 关闭鼠标跟踪，对应的提示框、点击事件会失效
			enableMouseTracking: false
		}
	},
	series: [{
		name: '实时酸碱度',
		data: [3.9, 4.2, 5.7, 8.5, 11.9, 15.2, 17.0]
	}]
});

        setInterval(function() {
        $.ajax({
            type: "GET",
            url: "http://13.67.56.21:80/index/historys",
            async: false,
            success: function(result) {
                if (result['code'] === 200) {
                    var data1ph = result['data']['data1ph'];
                    var data2ph = result['data']['data2ph'];
                    var data3ph = result['data']['data3ph'];
                    var data4ph = result['data']['data4ph'];
                    var data5ph = result['data']['data5ph'];
                    var data6ph = result['data']['data6ph'];
                    var data7ph = result['data']['data7ph'];
                    var dataZongPh = [data1ph, data2ph, data3ph, data4ph, data5ph, data6ph, data7ph];
                    Highcharts.chart[1]['series'][0]['data']=dataZongPh;
                    console.log(dataZongPh);
                }
            }
        });
    }, 3000);
