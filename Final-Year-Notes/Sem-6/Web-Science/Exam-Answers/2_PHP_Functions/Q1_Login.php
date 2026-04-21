<?php
// Q1: Login Form - Slip 1 Q2
if($_POST) {
  if($_POST['user']==$_POST['pass']) echo "Welcome"; 
  else echo "Invalid";
}
?>
<form method="POST">
<input name="user" placeholder="Username" required>
<input name="pass" placeholder="Password" required>
<button>Login</button>
</form>
<!-- WINDOWS: php -S localhost:8000  (open http://localhost:8000/Q1_Login.php)
     UBUNTU: php -S localhost:8000 (same) -->
