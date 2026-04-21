<?php
// Q2: Palindrome - Slip 6 Q1
if($_POST) {
  $n = $_POST['num'];
  $rev = strrev($n);
  echo ($n==$rev) ? "$n is Palindrome" : "$n is NOT Palindrome";
}
?>
<form method="POST">
<input name="num" placeholder="Number" required>
<button>Check</button>
</form>