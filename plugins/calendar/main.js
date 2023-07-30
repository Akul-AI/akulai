const fs = require("fs");
const events = [];

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
                akulAI.speak("Reminder: " + event.event);
            }
        });
    }, 60000);
};

module.exports = {
    addEvent,
    checkEvents
};
