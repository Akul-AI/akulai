const fs = require("fs");
const events = [];

fetch('http://127.0.0.1:8000/speak')

const addEvent = (event, date) => {
    events.push({event, date});
    fs.writeFileSync("events.json", JSON.stringify(events));
    console.log("Event added: " + event);
};

const checkEvents = () => {
    setInterval(() => {
        const now = new Date();
        events.forEach((event) => {
            const eventDate = new Date(event.date);
            if (now.getTime() >= eventDate.getTime()) {
                console.log("Reminder: " + event.event);
                speak("Reminder: " + event.event);
            }
        });
    }, 60000);
};

module.exports = {
    addEvent,
    checkEvents
};
