<?php
// Q5: Number to Words - Slip 13 Q1, Q2
function digit_word($d) {
  $w = ['0'=>'Zero','1'=>'One','2'=>'Two','3'=>'Three','4'=>'Four','5'=>'Five','6'=>'Six','7'=>'Seven','8'=>'Eight','9'=>'Nine'];
  return $w[$d]??'';
}
if($_POST) {
  $n = $_POST['num'];
  $result = '';
  foreach(str_split($n) as $d) $result .= digit_word($d).' ';
  echo trim($result);
}
?>
<form method="POST">
<input type="number" name="num" placeholder="Number" required>
<button>Convert</button>
</form>
