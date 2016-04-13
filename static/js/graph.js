queue()
    .defer(d3.json, "/fraud/project") #whatever our database is that were pushing
    .defer(d3.json, "static/geojson/countries.json")
    .await(makeGraphs);

function makeGraphs(error, projectsJson, statesJson) {

	//Clean projectsJson data
	var donorschooseProjects = projectsJson;
	var dateFormat = d3.time.format("%Y-%m-%d");
	donorschooseProjects.forEach(function(d) {
		d["user_created"] = dateFormat.parse(d["user_created"]);
		d["user_created"].setDate(1);
		d["fraud"] = +d["fraud"];
	});

	//Create a Crossfilter instance
	var ndx = crossfilter(donorschooseProjects);

	//Define Dimensions
  //get 5 most important variables
	var dateDim = ndx.dimension(function(d) { return d["user_created"]; }); //user_created
	var resourceTypeDim = ndx.dimension(function(d) { return d["total_cost"]; }); //resource type >> num payouts
	var povertyLevelDim = ndx.dimension(function(d) { return d["currency"]; }); //poverty_level > num_order
	var stateDim = ndx.dimension(function(d) { return d["country"]; }); //school_state>>country
	var totalDonationsDim  = ndx.dimension(function(d) { return d["fraud"]; }); //total_donations


	//Calculate metrics
	var numProjectsByDate = dateDim.group();
	var numProjectsByResourceType = resourceTypeDim.group();
	var numProjectsByPovertyLevel = povertyLevelDim.group(); //access data to return only fraud
	var totalDonationsByState = stateDim.group().reduceSum(function(d) {
		return d["fraud"]; //total fraud
	});

	var all = ndx.groupAll();
	var totalDonations = ndx.groupAll().reduceSum(function(d) {return d["fraud"];});
  //get total fraud
	var max_state = totalDonationsByState.top(1)[0].value;

	//Define values (to be used in charts)
	var minDate = dateDim.bottom(1)[0]["user_created"];
	var maxDate = dateDim.top(1)[0]["user_created"];

    //Charts
	var timeChart = dc.barChart("#time-chart");
	var resourceTypeChart = dc.rowChart("#resource-type-row-chart");
	var povertyLevelChart = dc.rowChart("#poverty-level-row-chart");
	var usChart = dc.geoChoroplethChart("#us-chart"); //ignore but actually world chart
	var numberProjectsND = dc.numberDisplay("#number-projects-nd");
	var totalDonationsND = dc.numberDisplay("#total-donations-nd");

	numberProjectsND
		.formatNumber(d3.format("d"))
		.valueAccessor(function(d){return d; })
		.group(all);

	totalDonationsND
		.formatNumber(d3.format("d"))
		.valueAccessor(function(d){return d; })
		.group(totalDonations)
		.formatNumber(d3.format(".3s"));

	timeChart
		.width(600)
		.height(160)
		.margins({top: 10, right: 50, bottom: 30, left: 50})
		.dimension(dateDim)
		.group(numProjectsByDate)
		.transitionDuration(500)
		.x(d3.time.scale().domain([minDate, maxDate]))
		.elasticY(true)
		.xAxisLabel("Year")
		.yAxis().ticks(4);

	resourceTypeChart
        .width(300)
        .height(250)
        .dimension(resourceTypeDim)
        .group(numProjectsByResourceType)
        .xAxis().ticks(4);

	povertyLevelChart
		.width(300)
		.height(250)
        .dimension(povertyLevelDim)
        .group(numProjectsByPovertyLevel)
        .xAxis().ticks(4);


	usChart.width(1000)
		.height(330)
		.dimension(stateDim)
		.group(totalDonationsByState)
		.colors(["#E2F2FF", "#C4E4FF", "#9ED2FF", "#81C5FF", "#6BBAFF", "#51AEFF", "#36A2FF", "#1E96FF", "#0089FF", "#0061B5"])
		.colorDomain([0, max_state])
		.overlayGeoJson(statesJson["features"], "state", function (d) {
			return d.properties.name;
		})
		.projection(d3.geo.albersUsa()
    				.scale(600)
    				.translate([340, 150]))
		.title(function (p) {
			return "Country: " + p["key"]
					+ "\n"
					+ "Total Fraud Cases: " + Math.round(p["value"]) + " $";
		})

    dc.renderAll();

};
