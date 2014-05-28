// Parses JSON from Django calendar API to return a list of event objects containing the event's date and name
var createEventList = function(data) {
	var event, parsedEvent, name, day;
	var eventList = [];
	for(var event in data.events){
		eventDate = data.events[event];
		parsedEventDate = Date.parse(eventDate.slice(0, -1));
		month = parsedEventDate.getMonthName();
		date = parsedEventDate.getDate();
		name = event;
		eventList.push({'name': name, 'date': date});
	}
	console.log(eventList);
	return eventList;
};

// Creates a Handlebars template for the calendar using a list of event objects
var createCalendarTemp = function(eventList) {

};

$(document).ready(function() {
	$.get( "/get_calendar_info", function(data) {
		var eventList;
		eventList = createEventList(data);
	});
})
