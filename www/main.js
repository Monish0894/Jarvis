$(document).ready(function () {
    $('.text').textillate({ 
        loop: true,
        sync: true,
        in:{
            effect:"bounceIn",
        },
        out:{
            effect:"bounceOut",
        },
    })
    
    //siri configuration
    var siriWave =new SiriWave({
        container: document.getElementById("siri-container"),
        width:640,
        height:200,
        style:"ios9",
        amplitude:"1",
        speed:"0.30",
        autostart:true
    })
    $('.siri-message').textillate({ 
        loop: true,
        sync: true,
        in:{
            effect:"bounceIn",
        },
        out:{
            effect:"bounceOut",
        },
    })
    //mic button click event
    $("#MicBtn").click(function () { 
        eel.playAssistantSound()
        $("#Oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);
       eel.allCommands()()
    });



    function doc_keyUp(e){
        console.log(`Key pressed: ${e.key}, Alt: ${e.altKey}`);
        if (e.key.toLowerCase() === 'o' && e.altKey){
            console.log("Alt + O detected");
            eel.playAssistantSound();
            $("#Oval").attr("hidden", true);
            $("#Siriwave").attr("hidden", false);
            eel.allCommands()();
        }
    }
    document.addEventListener('keyup', doc_keyUp, false);
    

    function playAssistant(message){

        if (message !=""){
            $("#Oval").attr("hidden", true);
            $("#SiriWave").attr("hidden", false);
            eel.allCommands(message);
            $("#chatbox").val("")
            $("#MicBtn").attr("hidden", false);
            $("#SendBtn").attr("hidden", true);
                
        }

    }
    function ShowHideButton(message){
        if (message.length == 0){
            $("#MicBtn").attr("hidden", false);
            $("#SendBtn").attr("hidden", true);
        }
        else{
            $("#MicBtn").attr("hidden", true);
            $("#SendBtn").attr("hidden", false);
        }
    }

    $("#chatbox").keyup(function (){
        let message = $("#chatbox").val();
        ShowHideButton(message)

    });

    $("#SendBtn").click(function (){
        let message = $("#chatbox").val()
        playAssistant(message)

    });

    $(document).ready(function() {
        $("#chatbox").on("keydown", function (e) {
            console.log("Event triggered. Key:", e.key, "KeyCode:", e.keyCode);  // Debugging output
            
            if (e.key === "Enter" || e.keyCode === 13) {  // Compatibility check
                e.preventDefault();  // Prevent default Enter key behavior
                let message = $("#chatbox").val().trim();
                console.log("Captured message:", message);  // Debug: Check message value
                
                if (message) {   // Proceed only if message is not empty
                    try {
                        playAssistant(message);
                        console.log("playAssistant() called successfully.");
                    } catch (err) {
                        console.error("Error in playAssistant:", err);  // Capture any errors in playAssistant
                    }
                    $("#chatbox").val('');  // Clear the input field
                }
            }
        });
    });
    




});