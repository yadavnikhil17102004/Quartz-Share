<?php
// Q4: String Operations - Slip 12 Q2
if($_POST) {
  $s1 = $_POST['s1'];
  $s2 = $_POST['s2'];
  $op = $_POST['op'];
  if($op=='cmp') echo ($s1===$s2) ? "Strings Equal" : "Strings Different";
  elseif($op=='up') echo strtoupper($s1);
  elseif($op=='low') echo strtolower($s2);
}
?>
<form method="POST">
<input name="s1" placeholder="String 1" required>
<input name="s2" placeholder="String 2" required>
<select name="op" required>
<option value="cmp">Compare</option>
<option value="up">Uppercase</option>
<option value="low">Lowercase</option>
</select>
<button>Execute</button>
</form>
