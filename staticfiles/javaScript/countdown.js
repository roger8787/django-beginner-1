function calculateTimeRemaining(enDate){
    const totalMilliseconds = Date.parse(enDate)-Date.now();
    const seconds = Math.floor((totalMilliseconds/1000)%60);
    const minutes = Math.floor((totalMilliseconds/1000/60)%60);
    const hours = Math.floor((totalMilliseconds/(1000*60*60))%24);
    const days = Math.floor(totalMilliseconds/(1000*60*60*24));

    return{
        total:totalMilliseconds, 
        days: days, 
        hours:hours, 
        minutes:minutes, 
        seconds:seconds, 
    }
}


function initializeCountdown(endDate, displayElement){
    const countDownInterval = setInterval(updateCountdown, 1000);
       function updateCountdown(){
        const timeRemaining = calculateTimeRemaining(endDate);

        if(timeRemaining.total <=0){
            clearInterval(countDownInterval);
        }else{
            displayCountDown(timeRemaining, displayElement);
        }
       } 

}


function displayCountDown(time, displayElement){
    displayElement.days.textContent = padZero(time.days);
    displayElement.hours.textContent = padZero(time.hours);
    displayElement.minutes.textContent = padZero(time.minutes);
    displayElement.seconds.textContent = padZero(time.seconds);
}

// Function to pad single digits with a leading zero
function padZero(number) {
    return number < 10 ? '0' + number : number;
  }

const targetDate = new Date("2024-06-01T16:00:00");


//get the display Elements
const daysDisplay = document.getElementById('days');
const hoursDisplay = document.getElementById('hours');
const minutesDisplay = document.getElementById('minutes');
const secondsDisplay = document.getElementById('seconds');


initializeCountdown(targetDate, {
    days: daysDisplay, 
    hours: hoursDisplay, 
    minutes: minutesDisplay, 
    seconds: secondsDisplay, 

});