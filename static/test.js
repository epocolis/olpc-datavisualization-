$(document).ready(function(){
    draw_activities_bar_chart(); 
    draw_collaboration_pie_chart();
    draw_timeofday_use_chart(); 
    draw_use_by_day_of_week_chart(); 
});



function draw_collaboration_pie_chart(){
    
    var data = [
	['Heavy Industry', 12],['Retail', 9], ['Light Industry', 14], 
	['Out of home', 16],['Commuting', 7], ['Orientation', 9]
    ];
    var plot1 = jQuery.jqplot ('chart1', [data], 
			       { 
				   title: 'Pie chart by time of day. Split day into 8AM to 3PM VS 3PM to 8AM?.',
				   seriesDefaults: {
				       // Make this a pie chart.
				       renderer: jQuery.jqplot.PieRenderer, 
				       rendererOptions: {
					   // Put data labels on the pie slices.
					   // By default, labels show the percentage of the slice.
					   showDataLabels: true
				       }
				   }, 
				   legend: { show:true, location: 'e' }
			       }
			      );
}

function draw_timeofday_use_chart(){
    //draw a pie chart here showing the activities that are used 
    //for 8am to 3pm 3pm to 8pm
    
    var data = [
	['Heavy Industry', 12],['Retail', 9], ['Light Industry', 14], 
	['Out of home', 16],['Commuting', 7], ['Orientation', 9]
    ];
    var plot1 = jQuery.jqplot ('chart2', [data], 
			       { 
				   title: 'Collaboration? (private vs shared) as pie.',
				   seriesDefaults: {
				       // Make this a pie chart.
				       renderer: jQuery.jqplot.PieRenderer, 
				       rendererOptions: {
					   // Put data labels on the pie slices.
					   // By default, labels show the percentage of the slice.
					   showDataLabels: true
				       }
				   }, 
				   legend: { show:true, location: 'e' }
			       }
			      );

}



function draw_use_by_day_of_week_chart() {
    
    var data = [
	['Heavy Industry', 12],['Retail', 9], ['Light Industry', 14], 
	['Out of home', 16],['Commuting', 7], ['Orientation', 9]
    ];
    var plot1 = jQuery.jqplot ('chart3', [data], 
			       { 
				   title: 'Use by day of the week?.',
				   seriesDefaults: {
				       // Make this a pie chart.
				       renderer: jQuery.jqplot.PieRenderer, 
				       rendererOptions: {
					   // Put data labels on the pie slices.
					   // By default, labels show the percentage of the slice.
					   showDataLabels: true
				       }
				   }, 
				   legend: { show:true, location: 'e' }
			       }
			      );
}


function draw_activities_bar_chart(){

    var line1 = [['Cup Holder Pinion Bob', 7], ['Generic Fog Lamp', 9], ['HDTV Receiver', 15],
		 ['8 Track Control Module', 12], [' Sludge Pump Fourier Modulator', 3],
		 ['Transcender/Spice Rack', 6], ['Hair Spray Danger Indicator', 18]];
    
    var plot1 = $.jqplot('chart4', [line1], {
	title: 'Frequency bar chart of activities.',
	series:[{renderer:$.jqplot.BarRenderer}],
	axesDefaults: {
            tickRenderer: $.jqplot.CanvasAxisTickRenderer ,
            tickOptions: {
		angle: -30,
		fontSize: '10pt'
            }
	},
	axes: {
	    xaxis: {
		renderer: $.jqplot.CategoryAxisRenderer
	    }
	}
    });


}
