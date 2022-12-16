function roundToNearest15(date = new Date(), delay) {
    const minutes = delay;
    const ms = 1000 * 60 * minutes;
  
    // 👇️ replace Math.round with Math.ceil to always round UP
    return new Date(Math.round(date.getTime() / ms) * ms);
  }
  
function refreshBusTime() {
    //Bus 1
    const timeDisplay1 = document.getElementById("bustime_1");
    const dateString1 = roundToNearest15(new Date(),15).toLocaleTimeString();
    timeDisplay1.textContent = dateString1;

    //Bus 2
    const timeDisplay2 = document.getElementById("bustime_2");
    const dateString2 = roundToNearest15(new Date(),30).toLocaleTimeString();
    timeDisplay2.textContent = dateString2;

    //Bus 3
    const timeDisplay3 = document.getElementById("bustime_3");
    const dateString3 = roundToNearest15(new Date(),30).toLocaleTimeString();
    timeDisplay3.textContent = dateString3;
  }

function refreshTime() {
    const timeDisplay = document.getElementById("date-time");
    const dateString = new Date().toLocaleString();
    const formattedString = dateString.replace(", ", " - ");
    timeDisplay.textContent = formattedString;
  }

setInterval(refreshTime, 1000);

setInterval(refreshBusTime, 1000);