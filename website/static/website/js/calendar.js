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
	console.log(eventList);
	var eventDays, currDate, numDays, firstDay;
	// A list of dates that have an event
	eventDays = [];
	for(var i = 0, len = eventList.length; i < len; i++) {
		eventDays.push(eventList[i].date);
		console.log(eventDays);
	}
	currDate = new Date();
	numDays = daysInMonth(currDate.getMonth()+1, currDate.getFullYear())

	firstDay = getFirstDay();
	var context, dateTemplate, dayCompiled;
	for(i = 0; i < firstDay; i++) {
		context = {};
		dayTemplate = $("#next-month-temp").html();
		dayCompiled = Handlebars.compile(dayTemplate);
		$('#week1').append(dayCompiled(context))
	}
	dayTemplate = $("#day-temp").html();
	dayCompiled = Handlebars.compile(dayTemplate);
	for (i = 1; i <= 7 - firstDay; i++) {
		if (eventDays.indexOf(i) > -1) {
			console.log('hit');
			context = getEvent(eventList, i);
			console.log(context);
			console.log('i: ' +i);
			$('#week1').append(dayCompiled(context))
		} else {
			context = {'date': i};
			$('#week1').append(dayCompiled(context))
		}
	}

	var offset = i;
	console.log('offset: ' + offset);
	for (var j = offset; j < offset+7; j++) {
		if (eventDays.indexOf(j) > -1) {
			console.log('hit');
			context = getEvent(eventList, j);
			console.log(context);
			console.log('j: ' +j);
			$('#week2').append(dayCompiled(context))
		} else {
			context = {'date': j};
			$('#week2').append(dayCompiled(context))
		}
	}

	offset = j
	for (var k = offset; k < offset+7; k++) {
		if (eventDays.indexOf(k) > -1) {
			console.log('hit');
			context = getEvent(eventList, k);
			console.log(context);
			console.log('k: ' + k);
			$('#week3').append(dayCompiled(context))
		} else {
			context = {'date': k};
			$('#week3').append(dayCompiled(context))
		}
	}

	offset = k
	for (var l = offset; l < offset+7; l++) {
		if (eventDays.indexOf(l) > -1) {
			console.log('hit');
			context = getEvent(eventList, l);
			console.log(context);
			console.log('l: ' + l);
			$('#week4').append(dayCompiled(context))
		} else {
			context = {'date': l};
			$('#week4').append(dayCompiled(context))
		}
	}

	offset = l
	for (var m = offset; m <= numDays; m++) {
		if (eventDays.indexOf(m) > -1) {
			console.log('hit');
			context = getEvent(eventList, m);
			console.log(context);
			console.log('m: ' +m);
			$('#week5').append(dayCompiled(context))
		} else {
			context = {'date': m};
			$('#week5').append(dayCompiled(context))
		}
	}

	for (;m <= 31; m++) {
		dayTemplate = $("#next-month-temp").html();
		dayCompiled = Handlebars.compile(dayTemplate);
		context = {'date': m};
		$('#week5').append(dayCompiled(context))
	}
};

// Gets the corresponding event object given a date in eventList
var getEvent = function(eventList, date) {
	for(var i = 0, len = eventList.length; i < len; i++) {
		console.log('in');
		console.log(eventList[i]['date']);
		console.log(date);
		if (parseInt(eventList[i]['date']) == parseInt(date)) {
			return eventList[i];
		};
	}
};

// Given a month and year, returns the number of days it has
var daysInMonth = function(month,year) {
    return new Date(year, month, 0).getDate();
}

// Returns the day of the 1st of the Month (0 for Sunday, 1 for Monday, etc..)
var getFirstDay = function() {
	var fd = Date.today().clearTime().moveToFirstDayOfMonth();
	return fd.getDay();
}

$(document).ready(function() {
	$.get( "/get_calendar_info", function(data) {
		var eventList, context, calendarTemplate, calendarCompiled;

		eventList = createEventList(data);
		createCalendarTemp(eventList);
	});
})
