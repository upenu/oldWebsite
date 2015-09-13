$(document).ready(function () {
	$('.officers-oh').isotope({
                itemSelector: '.tile',
                layoutMode: 'fitRows'
        });

	var officers = JSON.parse(officeHours);
	var officerList = $('.officers-oh');
	var tileString = '<li class=\"tile\">\r\n  <div class=\"officer-oh\">\r\n    <img class=\"image\" src=\"http:\/\/upe.berkeley.edu\/media\/profile_images\/spock.jpg\">\r\n    <div class=\"info\">\r\n      <span class=\"name\"><\/span>\r\n      <span class=\"date\"><\/span>\r\n      <ul class=\"classes-skills\">\r\n      <\/ul>\r\n    <\/div>\r\n  <\/div>\r\n<\/li>';
	var tileTemplate = $(tileString);
	for (var i = 0; i < officers.length; i++) {
               	var officer = officers[i];
               	var tile = tileTemplate.clone();
		var courses = '';
		var hours = '';

               	for (var j = 0; j < officer.courses.length; j++) {
			var times = officer.times;
                       	var course = officer.courses[j];

			tile.addClass(course);
                       	courses += course.replace('_', ' ');

			if (j < officer.courses.length - 1) {
				courses += ', ';
			}
               	}

		for (var k = 0; k < times.length; k++) {
                        var time = times[k];

                        tile.addClass(time.day);
                        hours += time.day + ' ' + time.time;

                        if (k < times.length - 1) {
                                hours += ', ';
                	}
                }
		
                tile.find('.name').html(officer.name); 
		tile.find('.classes-skills').html(courses);
		tile.find('.date').html(hours);

                officerList.isotope('insert', tile);

        }

	var classFilter = '',
		dayFilter = '';

	$('.filter.days').change(function () {
		if ($(this).val()) {
			dayFilter = '.' + $(this).val();
		} else {
			dayFilter = '';
		}
		$('.officers-oh').isotope({
			filter: dayFilter+classFilter
		});
	});

	$('.filter.classes').change(function () {
		if ($(this).val()) {
			classFilter = '.' + $(this).val();
		} else {
			classFilter = '';
		}
		$('.officers-oh').isotope({
			filter: classFilter+dayFilter
		});
	});
});

