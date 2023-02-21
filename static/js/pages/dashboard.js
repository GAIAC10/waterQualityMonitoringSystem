//PH
$(document).ready(function() {
    var options1 = {
        chart: {
            height: 350,
            type: 'area',
            toolbar: {
                show: false,
            }
        },
        dataLabels: {
            enabled: false
        },
        stroke: {
            curve: 'smooth'
        },
        colors: ['#AC87FC'],
        series: [{
            name: '酸碱度',
            data: [8, 7, 7, 7, 6, 7, 7.5]
        }],
        xaxis: {
            type: '时间',
            categories: ['Sun', 'Sat', 'Fri', 'Thur', 'Wed', 'Tue', 'Mon'],
            labels: {
                style: {
                    colors: 'rgba(94, 96, 110, .5)'
                }
            }
        },
        tooltip: {
            x: {
                format: 'dd/MM/yy HH:mm'
            },
        },
        grid: {
            borderColor: 'rgba(94, 96, 110, .5)',
            strokeDashArray: 4
        }
    };
    var chart1 = new ApexCharts(
        document.querySelector("#apex1"),
        options1
    );


        setInterval(function() {

        $.ajax({
            type: "GET",
            url: "http://10.69.23.10:40/index/historys",
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

                    series[0]['data'] = dataZongPh;
                    // console.log('a');
                    chart1.render();
                    console.log(dataZongPh);
                }
            }
        });
    }, 3000);

});

//TU
$(document).ready(function() {
    var options2 = {
        chart: {
            height: 350,
            type: 'area',
            toolbar: {
                show: false,
            }
        },
        dataLabels: {
            enabled: false
        },
        stroke: {
            curve: 'smooth'
        },
        colors: ['#82D2CB'],
        series: [{
            name: '浊度',
            data: [99,100,99,98,100,101,98]
        }],
        xaxis: {
            type: '时间',
            categories: ['Sun', 'Sat', 'Fri', 'Thur', 'Wed', 'Tue', 'Mon'],
            labels: {
                style: {
                    colors: 'rgba(94, 96, 110, .5)'
                }
            }
        },
        tooltip: {
            x: {
                format: 'dd/MM/yy HH:mm'
            },
        },
        grid: {
            borderColor: 'rgba(94, 96, 110, .5)',
            strokeDashArray: 4
        }
    };
    var chart1 = new ApexCharts(
        document.querySelector("#apex2"),
        options2
    );
    chart1.render();

    setInterval(function() {
        $.ajax({
            type: "GET",
            url: "http://10.69.23.10:40/index/historys",
            async: false,
            success: function(result) {
                if (result['code'] === 200) {
                    var data1tu = result['data']['data1tu'];
                    var data2tu = result['data']['data2tu'];
                    var data3tu = result['data']['data3tu'];
                    var data4tu = result['data']['data4tu'];
                    var data5tu = result['data']['data5tu'];
                    var data6tu = result['data']['data6tu'];
                    var data7tu = result['data']['data7tu'];
                    var dataZongTu = [data1tu, data2tu, data3tu, data4tu, data5tu, data6tu, data7tu];
                    options2.series[0]['data'] = dataZongTu;
                    console.log(dataZongTu)
                }
            }
        });
    }, 3000);
});

//TDS
$(document).ready(function() {
    var options3 = {
        chart: {
            height: 350,
            type: 'area',
            toolbar: {
                show: false,
            }
        },
        dataLabels: {
            enabled: false
        },
        stroke: {
            curve: 'smooth'
        },
        colors: ['#F78B97'],
        series: [{
            name: '固体溶解度',
            data: [85,88,89,86,88,87,86]
        }],
        xaxis: {
            type: '时间',
            categories: ['Sun', 'Sat', 'Fri', 'Thur', 'Wed', 'Tue', 'Mon'],
            labels: {
                style: {
                    colors: 'rgba(94, 96, 110, .5)'
                }
            }
        },
        tooltip: {
            x: {
                format: 'dd/MM/yy HH:mm'
            },
        },
        grid: {
            borderColor: 'rgba(94, 96, 110, .5)',
            strokeDashArray: 4
        }
    };
    var chart1 = new ApexCharts(
        document.querySelector("#apex3"),
        options3
    );
    chart1.render();

    setInterval(function() {
        $.ajax({
            type: "GET",
            url: "http://10.69.23.10:40/index/historys",
            async: false,
            success: function(result) {
                if (result['code'] === 200) {
                    var data1tds = result['data']['data1tds'];
                    var data2tds = result['data']['data2tds'];
                    var data3tds = result['data']['data3tds'];
                    var data4tds = result['data']['data4tds'];
                    var data5tds = result['data']['data5tds'];
                    var data6tds = result['data']['data6tds'];
                    var data7tds = result['data']['data7tds'];
                    var dataZongTds = [data1tds, data2tds, data3tds , data4tds, data5tds, data6tds, data7tds];
                    options3.series[0]['data'] = dataZongTds;
                    console.log(dataZongTds)
                }
            }
        });
    }, 3000);
});


//TEM
$(document).ready(function() {
    var options4 = {
        chart: {
            height: 350,
            type: 'area',
            toolbar: {
                show: false,
            }
        },
        dataLabels: {
            enabled: false
        },
        stroke: {
            curve: 'smooth'
        },
        colors: ['#8D9BFC'],
        series: [{
            name: '温度',
            data: [22,23,22,21,22,22,23]
        }],
        xaxis: {
            type: '时间',
            categories: ['Sun', 'Sat', 'Fri', 'Thur', 'Wed', 'Tue', 'Mon'],
            labels: {
                style: {
                    colors: 'rgba(94, 96, 110, .5)'
                }
            }
        },
        tooltip: {
            x: {
                format: 'dd/MM/yy HH:mm'
            },
        },
        grid: {
            borderColor: 'rgba(94, 96, 110, .5)',
            strokeDashArray: 4
        }
    };
    var chart1 = new ApexCharts(
        document.querySelector("#apex4"),
        options4
    );
    chart1.render();

    setInterval(function() {
        $.ajax({
            type: "GET",
            url: "http://10.69.23.10:40/index/historys",
            async: false,
            success: function(result) {
                if (result['code'] === 200) {
                    var data1tem = result['data']['data1tem'];
                    var data2tem = result['data']['data2tem'];
                    var data3tem = result['data']['data3tem'];
                    var data4tem = result['data']['data4tem'];
                    var data5tem = result['data']['data5tem'];
                    var data6tem = result['data']['data6tem'];
                    var data7tem = result['data']['data7tem'];
                    var dataZongTem = [data1tem, data2tem, data3tem, data4tem, data5tem, data6tem, data7tem];
                    options4.series[0]['data'] = dataZongTem;
                    console.log(dataZongTem)
                }
            }
        });
    }, 3000);
});
