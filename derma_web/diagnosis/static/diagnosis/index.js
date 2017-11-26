var me = {};
me.avatar = "https://i.pinimg.com/236x/bb/c1/2b/bbc12bff3a544b88c3d408669231073a--material-design-bot.jpg";

var you = {};
you.avatar = "https://cdn4.iconfinder.com/data/icons/small-n-flat/24/user-group-512.png";


last_reponse = "";

function formatAMPM(date) {
    var hours = date.getHours();
    var minutes = date.getMinutes();
    var ampm = hours >= 12 ? 'PM' : 'AM';
    hours = hours % 12;
    hours = hours ? hours : 12; // the hour '0' should be '12'
    minutes = minutes < 10 ? '0'+minutes : minutes;
    var strTime = hours + ':' + minutes + ' ' + ampm;
    return strTime;
}            

//-- No use time. It is a javaScript effect.
function insertChat(who, text, time = 0){
    var control = "";
    var date = formatAMPM(new Date());
    
    if (who == "me"){
        
        control = '<li style="width:60%; margin:auto;">' +
                        '<div class="msj macro chat">' +
                        '<div class="avatar"><img class="img-circle" style="width:100%; height:90%;" src="'+ me.avatar +'" /></div>' +
                            '<div class="text text-l">' +
                                '<p>'+ text +'</p>' +
                                '<p><small style="font-size:10px;>'+date+'</small></p>' +
                            '</div>' +
                        '</div>' +
                    '</li>';                    
    }else{
        control = '<li style="width:60%; margin:auto;">' +
                        '<div class="msj-rta macro chat usa">' +
                            '<div class="text text-r">' +
                                '<p>'+text+'</p>' +
                                '<p><small style="font-size:10px;">'+date+'</small></p>' +
                            '</div>' +
                        '<div class="avatar" style="padding:0px 0px 0px 10px !important"><img class="img-circle" style="width:100%; height:90%;" src="'+you.avatar+'" /></div>' +                                
                  '</li>';
    }
    setTimeout(
        function(){                        
            $("ul").append(control);

        }, time)
    
}

function resetChat(){
   $("ul").empty();
}


function respond()
{
    console.log("responee");
    if(last_reponse == "you")
    {
        insertChat("me", "I am the SKIN GAWWWD! Please upload image!\n", 1000);
        last_reponse = "me";
    }
}

$(document).ready(function(){
$(".mytext").on("keyup", function(e){
    console.log("responee");;
    if (e.which == 13){
        var text = $(this).val();        
        if (text !== ""){
            last_reponse = "you";
            insertChat("you", text); 
            respond(text);                      
            $(this).val('');
        }
    }
});
});


function print_result(res) {
    console.log(res);
    return false;
}

//-- Clear Chat
resetChat();

console.log("hiii");
//-- Print Messages
insertChat("me", "Greetings, Mortal! Show me what is bothering you!\n", 0);
last_reponse = "me";

// data_from_django = {{jsdata}} ; 
// console.log(data_from_django);
//insertChat("you", "", 1500);
// insertChat("me", "What would you like to talk about today?", 3500);
// insertChat("you", "Tell me a joke",7000);
// insertChat("me", "Spaceman: Computer! Computer! Do we bring battery?!", 9500);
// insertChat("you", "LOL", 12000);


//-- NOTE: No use time on insertChat.