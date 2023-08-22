const eventBox = document.getElementById('event-box')
const countdownBox = document.getElementById('countdown-box')

// const eventDate = Date.parse(eventBox.textContent)

var dateString = eventBox.textContent;
console.log('String:')

// Split the string to extract date and time parts
var parts = dateString.split(" um ");
var datePart = parts[0];
var timePart = parts[1];

// Split the date part to extract day, month, and year
var dateComponents = datePart.split(" ");
var day = parseInt(dateComponents[0], 10);
var month = dateComponents[1]; // Month name
var year = parseInt(dateComponents[2], 10);

// Convert month name to a numerical month value (0-indexed)
var monthNames = [

  "Januar", "Februar", "März", "April", "Mai", "Juni",

  "Juli", "August", "September", "Oktober", "November", "Dezember"

];
var monthIndex = monthNames.indexOf(month);

// Split the time part to extract hours and minutes
var timeComponents = timePart.split(":");
var hours = parseInt(timeComponents[0], 10);
var minutes = parseInt(timeComponents[1], 10); 

// Create a new Date object with the extracted components
var eventDate = new Date(year, monthIndex, day, hours, minutes);

setInterval(()=> {
    const now = new Date().getTime()

    const diff = eventDate - now

    const d = Math.floor(eventDate / (1000 * 60 * 60 * 24) - (now / (1000 * 60 * 60 * 24)))
    const h = Math.floor((eventDate / (1000 * 60 * 60) - (now / (1000 * 60 * 60))) % 24)
    const m = Math.floor((eventDate / (1000 * 60) - (now / (1000 * 60))) % 60)
    const s = Math.floor((eventDate / (1000) - (now / (1000))) % 60)

    if (diff>0) {
        countdownBox.innerHTML = d + " days, " + h + " hours, " + m + " minutes, " + s + " seconds"
    } else {

    }
}, 1000)