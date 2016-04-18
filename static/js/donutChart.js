var testdata_race = [
    {y:1939,key:"Mexican"},
    {y:101,key:"Vietnamese"},
    {y:172,key:"Pacific Islander"},
    {y:187,key:"Korean"},
    {y:72,key:"Japanese"},
    {y:133,key:"Filipino"},
    {y:2153,key:"Black"},
    {y:207,key:"Chinese"},
    {y:146,key:"Asian Indian"},
    {y:473,key:"American Indian"},
    {y:237,key:"Cuban"},
    {y:337,key:"Puerto Rican"},
    {y:779,key:"Other Hispanic"}
];

var height = 700;
var width = 700;

var chart1;

nv.addGraph(function() {
    var chart1 = nv.models.pieChart()
        .x(function(d) { return d.key })
        .y(function(d) { return d.y })
        .donut(true)
        .width(width)
        .height(height)
        .padAngle(.08)
        .cornerRadius(5)
        .legendPosition("bottom")
        .id('donut1'); // allow custom CSS for this one svg

    chart1.title("Minority Suicide Representation");
    chart1.pie.donutLabelsOutside(true).donut(true);
    // chart1.legend.margin({top: 0, right: 0, left: 0, bottom: 20});

    d3.select("#test3")
        .datum(testdata_race)
        .transition().duration(1200)
        .call(chart1);


    // LISTEN TO WINDOW RESIZE
    // nv.utils.windowResize(chart1.update);

    // LISTEN TO CLICK EVENTS ON SLICES OF THE PIE/DONUT
    // chart.pie.dispatch.on('elementClick', function() {
    //     code...
    // });

    // chart.pie.dispatch.on('chartClick', function() {
    //     code...
    // });

    // LISTEN TO DOUBLECLICK EVENTS ON SLICES OF THE PIE/DONUT
    // chart.pie.dispatch.on('elementDblClick', function() {
    //     code...
    // });

    // LISTEN TO THE renderEnd EVENT OF THE PIE/DONUT
    // chart.pie.dispatch.on('renderEnd', function() {
    //     code...
    // });

    // OTHER EVENTS DISPATCHED BY THE PIE INCLUDE: elementMouseover, elementMouseout, elementMousemove
    // @see nv.models.pie

    return chart1;

});
