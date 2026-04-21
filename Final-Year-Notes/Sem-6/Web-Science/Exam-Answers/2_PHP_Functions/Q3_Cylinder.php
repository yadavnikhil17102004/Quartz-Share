<?php
// Q3: Cylinder - Slip 12 Q1
function cylinder($r,$h) {
  $pi = 3.14159;
  $area = 2*$pi*$r*($r+$h);
  $vol = $pi*$r*$r*$h;
  return "Area: $area, Volume: $vol";
}
if($_POST) echo cylinder($_POST['r'],$_POST['h']);
?>
<form method="POST">
<input type="number" name="r" placeholder="Radius" step="any" required>
<input type="number" name="h" placeholder="Height" step="any" required>
<button>Calculate</button>
</form>
