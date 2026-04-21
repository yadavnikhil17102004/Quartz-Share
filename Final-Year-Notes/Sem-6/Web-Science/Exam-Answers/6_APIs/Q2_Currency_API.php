<?php
// Currency Exchange API - Slip 24 Q2
$from = $_POST['from']??"USD";
$to = $_POST['to']??"INR";
$amt = $_POST['amt']??1;

$url = "https://api.exchangerate-api.com/v4/latest/$from";
$data = null;
if(function_exists('curl_init')) {
  $ch = curl_init($url);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
  $response = curl_exec($ch);
  $data = json_decode($response, true);
}

if(isset($data['rates'][$to])) {
  $rate = $data['rates'][$to];
  $result = $amt * $rate;
  echo "$amt $from = $result $to<br>";
  echo "Rate: 1 $from = $rate $to";
} else {
  // Fallback demo rates for offline lab.
  $demo = [
    'USD_INR' => 83.0,
    'USD_EUR' => 0.92,
    'INR_USD' => 0.012
  ];
  $key = strtoupper($from)."_".strtoupper($to);
  if(isset($demo[$key])) {
    $rate = $demo[$key];
    $result = $amt * $rate;
    echo "API unavailable. Demo Output:<br>";
    echo "$amt $from = $result $to<br>";
    echo "Rate: 1 $from = $rate $to";
  } else {
    echo "Invalid currency";
  }
}
?>
<form method="POST">
<input name="from" placeholder="From (USD)" value="USD">
<input name="to" placeholder="To (INR)" value="INR">
<input type="number" name="amt" placeholder="Amount" value="1">
<button>Convert</button>
</form>
