const apiKey = "8ec73b180fe3c393c340185e0e92a0aa";

function getWeather() {
  const city = document.getElementById("cityInput").value;
  const error = document.getElementById("error");
  error.textContent = "";

  if (city === "") {
    error.textContent = "Please enter a city name.";
    return;
  }

  const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`;

  fetch(url)
    .then(response => {
      if (!response.ok) {
        throw new Error("City not found");
      }
      return response.json();
    })
    .then(data => {
      document.getElementById("cityName").textContent = data.name;
      document.getElementById("temperature").textContent =
        `Temperature: ${data.main.temp} °C`;
      document.getElementById("humidity").textContent =
        `Humidity: ${data.main.humidity}%`;
      document.getElementById("condition").textContent =
        `Condition: ${data.weather[0].description}`;
    })
    .catch(err => {
      error.textContent = err.message;
    });
}
