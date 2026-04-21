<?php
// Password Complexity - Slip 4 Q2, 8 Q2, 22 Q2
if($_POST) {
  $p = $_POST['pass'];
  $has_num = preg_match('/[0-9]/',$p);
  $has_alpha = preg_match('/[a-zA-Z]/',$p);
  $has_special = preg_match('/[\W_]/',$p);
  $len = strlen($p)>8;
  if($has_num && $has_alpha && $has_special && $len) 
    echo "Strong Password";
  else 
    echo "Weak Password";
}
?>
<form method="POST">
<input name="pass" type="password" placeholder="Password" required>
<button>Check</button>
</form>
