$(function () {
    $('#create-sublet-submit').on('click', function (e) {
        e.preventDefault();
        let title = $('#listing-title');
        let street_address = $('#street_address');
        let city = $('#city');
        let postal_code = $('#postal_code');
        let price = $('#price');
        let description = $('#listing-description');
        let lat = $('#lat');
        let lng = $('#lng');
        let duration = $('#duration');
        let images = $('#files');
        let error = false;

        title.popover('hide');
        price.popover('hide');
        description.popover('hide');
        duration.popover('hide');
        images.popover('hide');
        $('#pac-input').popover('hide');

        if (!title.val()) {
            title.popover('show');
            error = true;
        }
        if (!duration.val()) {
            duration.popover('show');
            error = true;
        }
        if (!street_address.val() || !city.val() || !postal_code.val() || !lat.val() || !lng.val()) {
            $('#pac-input').popover('show');
            error = true;
        }
        if (!price.val()) {
            price.popover('show');
            error = true;
        }
        if (!description.val()) {
            description.popover('show');
            error = true;
        }
        if (!images.val()) {
            images.popover('show');
            error = true;
        }
        if (error)
            return false;
    });
});