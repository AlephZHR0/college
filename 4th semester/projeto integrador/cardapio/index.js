function increment(id) {
    var element = document.getElementById(id);
    var value = parseInt(element.value);
    value++;
    element.value = value;
}

function decrement(id) {
    var element = document.getElementById(id);
    var value = parseInt(element.value);
    if (value > 0) {
        value--;
        element.value = value;
    }
}