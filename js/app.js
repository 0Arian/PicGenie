//Our Bubble Chart Data
var ctx = $("#myChart");
var bubChart = new Chart(ctx,{
    type: 'bubble',
    data: data,
    options: {
        elements: {
            points: {
                borderWidth: 1,
                borderColor: 'rgb(0, 0, 0)'
            }
        }
    }
});

