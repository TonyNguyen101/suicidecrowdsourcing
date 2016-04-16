var testdata = [
{label: "8th grade or less ",
  y :1579},
{  label:  "Some high school"
, y:4622},
{  label:  "Associate degree",  y:2857
},{  label:  "Bachelors degree",y:4754
},{  label:"Doctorate or professional degree",y:735
},{label: "Master's degree",y:1618
},{  label:  "high school graduate" ,y:15356
} ,   {label:"some college",y: 6726}

];
var testdata2 = [{y:3,label:9},{y:8,label:10},{y:34,label:11},{y:60,label:12},{y:117,label:13},{y:161,label:14},{y:220,label:15},{y:292,label:16},{y:328,label:17},{y:402,label:18},{y:432,label:19},{y:493,label:20},{y:585,label:21},{y:640,label:22},{y:613,label:23},{y:635,label:24},{y:591,label:25},{y:653,label:26},{y:592,label:27},{y:598,label:28},{y:568,label:29},{y:589,label:30},{y:619,label:31},{y:576,label:32},{y:582,label:33},{y:624,label:34},{y:571,label:35},{y:607,label:36},{y:611,label:37},{y:515,label:38},{y:583,label:39},{y:563,label:40},{y:645,label:41},{y:625,label:42},{y:686,label:43},{y:691,label:44},{y:713,label:45},{y:707,label:46},{y:700,label:47},{y:770,label:48},{y:886,label:49},{y:822,label:50},{y:884,label:51},{y:829,label:52},{y:836,label:53},{y:879,label:54},{y:821,label:55},{y:861,label:56},{y:746,label:57},{y:718,label:58},{y:760,label:59},{y:740,label:60},{y:635,label:61},{y:572,label:62},{y:491,label:63},{y:519,label:64},{y:452,label:65},{y:462,label:66},{y:465,label:67},{y:359,label:68},{y:361,label:69},{y:391,label:70},{y:372,label:71},{y:317,label:72},{y:292,label:73},{y:274,label:74},{y:266,label:75},{y:218,label:76},{y:221,label:77},{y:235,label:78},{y:233,label:79},{y:205,label:80},{y:210,label:81},{y:205,label:82},{y:198,label:83},{y:188,label:84},{y:175,label:85},{y:167,label:86},{y:138,label:87},{y:129,label:88},{y:107,label:89},{y:88,label:90},{y:65,label:91},{y:67,label:92},{y:45,label:93},{y:35,label:94},{y:21,label:95},{y:24,label:96},{y:12,label:97},{y:10,label:98},{y:4,label:99},{y:2,label:100},
  {y:1,label:101},{y:1,label:102},{y:7,label:999}];
var testdata3 = [
{y:3,label:5},{y:380,label:10},{y:1674,label:15},{y:2966,label:20},{y:3002,label:25},{y:2990,label:30},{y:2887,label:35},{y:3210,label:40},{y:3776,label:45},{y:4250,label:50},{y:3906,label:55},{y:2957,label:60},{y:2099,label:65},{y:1646,label:70},{y:1173,label:75},{y:1006,label:80},{y:716,label:85},{y:300,label:90},{y:71,label:95},{y:4,label:100},{y:7,label:995}
]
var height = 700;
var width = 700;

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

    return chart1;

});


nv.addGraph({
generate: function() {
  var width = $(window).width() - 40,
      height = $(window).height() - 40;
  var chart = nv.models.bar()
      .width(width)
      .height(height)
  d3.select("#test1")
    .attr('width', width)
    .attr('height', height)
    .datum(testdata3)
    .call(chart);
  return chart;
},
callback: function(graph) {
  $(window).resize(function() {
    var width = $(window).width() - 40,
        height = $(window).height() - 40;
    d3.select("#test1")
      .attr('width', width)
      .attr('height', height)
      .call(
        graph
          .width($(window).width() - 40)
          .height($(window).height() - 40)
      )
  });
}
});

nv.addGraph({
generate: function() {
  var width = $(window).width() - 40,
      height = $(window).height() - 40;
  var chart = nv.models.bar()
      .width(width)
      .height(height)
  d3.select("#test2")
    .attr('width', width)
    .attr('height', height)
    .datum(testdata)
    .call(chart);
  return chart;
},
callback: function(graph) {
  $(window).resize(function() {
    var width = $(window).width() - 40,
        height = $(window).height() - 40;
    d3.select("#test2")
      .attr('width', width)
      .attr('height', height)
      .call(
        graph
          .width($(window).width() - 40)
          .height($(window).height() - 40)
      )
  });
}
});
