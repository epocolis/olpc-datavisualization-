$(document).ready(function(){
    draw_activities_bar_chart(); 
    draw_collaboration_pie_chart();
    draw_timeofday_use_chart(); 
    draw_use_by_day_of_week_chart(); 
});



function draw_collaboration_pie_chart(){
    
    var data = [
	['8am to 3pm', 25],['3pm to 8pm', 75]
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
	['Invite', 12],['Public', 20], ['Private', 14] 
	
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
	['Mon', 12],['Tues', 9], ['Wed', 14], 
	['Thurs', 16],['Frid', 7], ['Sat', 9],['Sun', 15]
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

var line1 = [['Pippy' ,30],
	     ['tuxMath',80],
	     ['Wine',40],
	     ['Moon' ,26],
	     ['AcousticMeasure',18],
	     ['Deducto',55]]



    
    var plot1 = $.jqplot('chart4', [line1], {
        seriesColors: [ "#4bb2c5", "#c5b47f", "#EAA228", "#579575", "#839557", "#958c12",
        "#953579", "#4b5de4", "#d8b83f"],
	series:[
            {label:'Hotel'},
            {label:'Event Regristration'},
            {label:'Airfare'}
        ],
	title: 'Frequency bar chart of activities.',
	series:[{renderer:$.jqplot.BarRenderer}],
	axesDefaults: {
            tickRenderer: $.jqplot.CanvasAxisTickRenderer ,
            tickOptions: {
		angle: 30,
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
