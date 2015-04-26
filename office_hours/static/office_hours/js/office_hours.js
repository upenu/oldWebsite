$(document).ready(function () {
	$('.officers-oh').isotope({
		itemSelector: '.tile',
		layoutMode: 'fitRows'
	});

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

