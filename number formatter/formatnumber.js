function format_number(number){
    var numbers = number.split("");
    numbers.reverse();
    var new_array = [];

    for (var i=0; i < numbers.length; i++){
        new_array.push(numbers[i]);

        if ((i+1) % 3 === 0){
            if (! (i+1 === numbers.length)){
                new_array.push(",");
            }

        }
    }
    var outputString = new_array.reverse().join("");
    return outputString;


}

var $txtNumber = $( "#txtNumber" );

$txtNumber.on("input", function(evt) {
    $("#formatted-number").html(format_number(this.value));
});
