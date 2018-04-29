$(document).ready(function() {
	fetch("/officehours").then(t => t.json().then(officers => {
	$('.officers-oh').isotope({
                itemSelector: '.tile',
                layoutMode: 'fitRows'
        });

	var officerList = $('.officers-oh');
	var tileString = '<li class=\"tile\">\r\n  <div class=\"officer-oh\">\r\n    <img class=\"image normal\" src=\"\/media\/profile_images\/spock.jpg\">\r\n   <img class=\"image soy\">\r\n    <div class=\"info\">\r\n      <span class=\"name\"><\/span>\r\n      <span class=\"date\"><\/span>\r\n      <ul class=\"classes-skills\">\r\n      <\/ul>\r\n    <\/div>\r\n  <\/div>\r\n<\/li>';
	var tileTemplate = $(tileString);

    officers.sort(function(x, y) {
        if (x.name > y.name) {
            return 1;
        } else if (x.name < y.name) {
            return -1;
        } else {
            return 0;
        }
    });

	for (var i = 0; i < officers.length; i++) {
        var officer = officers[i];
       	var tile = tileTemplate.clone();
		var courses = '';
		var hours = '';

        tile.find('.normal').attr('src', officer.image);
        tile.find('.soy').attr('src', officer.image);
        tile.find('.soy').hide();

        for (var j = 0; j < officer.courses.length; j++) {
			var times = officer.times;
            var course = officer.courses[j];

			tile.addClass(course.replace(' ', '_'));
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

        tile.find('.officer-oh').hover(function() {
            $(this).find('.normal').hide();
            $(this).find('.soy').show()
        }, function() {
            $(this).find('.normal').show();
            $(this).find('.soy').hide()
        });

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
	}));
});

