$(document).ready(function () {
    
    // Display Speak Message
    eel.expose(DisplayMessage)
    function DisplayMessage(message) {
        $(".siri-message li:first").text(message);
        $('.siri-message').texllate('start');
    }// Display hood
    eel.expose(ShowHood)
    function ShowHood() {
        $("#SiriWave").attr("hidden", true);
        $("#Oval").attr("hidden", false);
}


});