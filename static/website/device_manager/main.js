$(function () {
    $('#add_black_lists').on('click', function () {
        $('#iframe').prop('src', '../add_devices/index.html');
    });
    $('#all_black_lists').on('click', function () {
        $('#iframe').prop('src', './sub/subTqbAdd.html');
    });
    $('#edit_black_lists').on('click', function () {
        $('#iframe').prop('src', './sub/subTqbAdd.html');
    });
});