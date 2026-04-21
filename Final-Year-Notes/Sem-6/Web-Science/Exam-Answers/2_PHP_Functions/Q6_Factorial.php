<?php
// Q6: Factorial - Slip 21 Q1
function factorial($n) { 
  return $n<=1 ? 1 : $n*factorial($n-1); 
}
if($_POST) echo "Factorial: ".factorial($_POST['num']);
?>
<form method="POST">
<input type="number" name="num" placeholder="Number" required>
<button>Calculate</button>
</form>