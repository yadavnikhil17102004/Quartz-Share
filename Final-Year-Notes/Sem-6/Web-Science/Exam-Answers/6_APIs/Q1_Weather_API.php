<?php
// Weather API - Slip 4 Q1, 7 Q2
// Using free API
$city = $_POST['city']??"London";
$api = "https://api.open-meteo.com/v1/forecast?latitude=51.5074&longitude=-0.1278&current=temperature_2m,weather_code";

$data = null;
if(function_exists('curl_init')) {
  $ch = curl_init($api);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
  $response = curl_exec($ch);
  $data = json_decode($response, true);
}

if(isset($data['current'])) {
  echo "City: ".$city."<br>";
  echo "Temp: ".$data['current']['temperature_2m']."°C<br>";
  echo "Code: ".$data['current']['weather_code'];
} else {
  // Fallback demo output for offline lab.
  echo "API unavailable. Demo Output:<br>";
  echo "City: ".$city."<br>Temp: 29°C<br>Code: 1";
}
?>
<form method="POST">
<input name="city" placeholder="City">
<button>Get Weather</button>
</form>

<!-- Run: php -S localhost:8000 -->
