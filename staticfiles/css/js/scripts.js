$(function() {
    var startDate = new Date('2024-03-31');
    var endDate = new Date('2024-03-31');

    var bookingTimes = {{ room.booking_times | safe }};

    $("#start-datepicker").datepicker({
        dateFormat: 'yy-mm-dd',
        beforeShowDay: function(date) {
            var currentDate = new Date(date);
            for (var i = 0; i < bookingTimes.length; i++) {
                var startTime = new Date(bookingTimes[i]['start_time']);
                var endTime = new Date(bookingTimes[i]['end_time']);
                if (currentDate >= startTime && currentDate <= endTime) {
                    return [false];
                }
            }
            return [currentDate < startDate || currentDate > endDate];
        }
    });

    $("#end-datepicker").datepicker({
        dateFormat: 'yy-mm-dd',
        beforeShowDay: function(date) {
            var currentDate = new Date(date);
            for (var i = 0; i < bookingTimes.length; i++) {
                var startTime = new Date(bookingTimes[i]['start_time']);
                var endTime = new Date(bookingTimes[i]['end_time']);
                if (currentDate >= startTime && currentDate <= endTime) {
                    return [false];
                }
            }
            return [currentDate < startDate || currentDate > endDate];
        }
    });
});