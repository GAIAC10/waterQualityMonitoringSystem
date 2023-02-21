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
        colors: ['#AC87FC', '#82D2CB','#F78B97','#8D9BFC'],
        series: [{
            name: '酸碱度',
            data: [8,7,7,7,6,7,7]
        }],
        xaxis: {
            type: '时间',
            categories: ['Sun','Sat','Fri','Thur','Wed','Tue','Mon'],
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

    chart1.render();

    // 陈俊霖写的
    // function sendAjaxPost() {
    // $.post({
    //         'url': ,
    //         'success': function(data) {
    //             console.log(data);
    //             data1 = data
    //         },
    //     );
    //     return 0;
    // )}

        setInterval(function() {
        $.ajax({
            type:"GET",
            url:"http://127.0.0.1:8000/index/historys",
            async:false,
            success:function (result) {
                if (result['code']===200){
                    var data1ph=result['data']['data1ph'];
                    var data2ph=result['data']['data2ph'];
                    var data3ph=result['data']['data3ph'];
                    var data4ph=result['data']['data4ph'];
                    var data5ph=result['data']['data5ph'];
                    var data6ph=result['data']['data6ph'];
                    var data7ph=result['data']['data7ph'];
                    var dataZongPh=[data1ph,data2ph,data3ph,data4ph,data5ph,data6ph,data7ph];
                    // console.log(dataZongPh);
                    options1.series[0]['data']=dataZongPh;
                    console.log(options1.series[0]['data'])
                }
           }
        });},3000);


});