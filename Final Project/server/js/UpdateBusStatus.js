
function changeBgcolor(color){
    var element = document.getElementById("BusStatusLabel");
    element.style.backgroundColor = color;
}

function UpdateBusState(){
    fetch('data.csv') 
    .then(response => response.text())
    .then(text => {
        var data = text.toString();
        document.getElementById("BusStatusLabel").innerHTML = data.toString()
        switch (data) {
            case 'Bus Detected':
               color = 'green';
               break;
            case 'Bus Not Detected':
               color = 'red';
               break;
            default:
               color = '#39d52d';
        }
        changeBgcolor(color)

        // console.log("Checkpoint")
    })
}



setInterval(UpdateBusState, 1000);