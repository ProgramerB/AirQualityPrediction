var chart;

/**
 * Request data from the server, add it to the graph and set a timeout
 * to request again
 */
function requestData() {
    $.ajax({
        url: '/live-data',
        success: function(point) {
            var series = chart.series[0],
                shift = series.data.length > 20; // shift if the series is
                                                 // longer than 20

            // add the point
            chart.series[0].addPoint(point, true, shift);

            // call it again after one second
            setTimeout(requestData, 1000);
        },
        cache: false
    });
}

$(document).ready(function() {
    chart = new Highcharts.Chart({
        chart: {
            renderTo: 'data-container',
            defaultSeriesType: 'spline',
            events: {
                load: requestData
            }
        },
        title: {
            text: 'Live AQI'
        },
        xAxis: {
            type: 'datetime',
            tickPixelInterval: 150,
            maxZoom: 20 * 1000
        },
        yAxis: {
            minPadding: 0.2,
            maxPadding: 0.2,
            title: {
                text: 'Index',
                margin: 80
            }
        },
        series: [{
            name: 'AQI',
            zones:[{
                value: 50,
                color: '#00ff00'   
            },{
                value: 100,
                color: '#fdfd00'
            },{
                value: 150,
                color: '#ff7f50'
            },{
                value: 200,
                color: '#ff0000'
            },{
                value: 300,
                color: '#9400d3'
            },{
                value: 1000,
                color: '#e6e6fa'
            }],
            data: []
            
        }]
    });
});