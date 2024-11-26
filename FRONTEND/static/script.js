function loadEventData() {
    fetch('/seismic_event_data')
        .then(response => response.json())
        .then(eventData => {
            const eventListElement = document.getElementById('event_list');
            eventListElement.innerHTML = ''; // Clear current list

            for (let eventName in eventData) {
                const { magnitude, longitude, latitude } = eventData[eventName];

                let listItem = document.createElement('li');
                listItem.className = 'event';
                listItem.textContent = `${eventName}`;
                listItem.dataset.state = 'name'; // Initial state is name

                // Add event details to dataset for toggling
                listItem.dataset.magnitude = magnitude;
                listItem.dataset.longitude = longitude;
                listItem.dataset.latitude = latitude;

                // Toggle between event name and details on click
                listItem.onclick = () => {
                    if (listItem.dataset.state === 'name') {
                        listItem.textContent = `Magnitude: ${magnitude}, Longitude: ${longitude}, Latitude: ${latitude}`;
                        listItem.dataset.state = 'details';
                    } else {
                        listItem.textContent = eventName;
                        listItem.dataset.state = 'name';
                    }
                };

                eventListElement.appendChild(listItem);
            }
        })
        .catch(error => console.error('Error fetching event data:', error));
}

window.onload = function () {
    loadEventData();
    refreshSeismicMap();
};
setInterval(refreshSeismicMap, 30000);
