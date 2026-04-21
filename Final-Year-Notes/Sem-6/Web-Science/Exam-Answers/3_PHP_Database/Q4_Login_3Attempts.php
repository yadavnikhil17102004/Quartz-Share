<?php
// Login with 3 Attempts & Session - Slip 11 Q1
session_start();
$_SESSION['attempts'] = $_SESSION['attempts']??0;
if($_POST) {
  $_SESSION['attempts']++;
  if($_SESSION['attempts']<=3) {
    if($_POST['user']==$_POST['pass']) {
      echo "Welcome ".$_POST['user'];
      unset($_SESSION['attempts']);
    } else echo "Invalid. Attempts: ".$_SESSION['attempts']."/3";
  } else echo "Too Many Attempts. Access Denied.";
}
?>
<form method="POST">
<input name="user" placeholder="Username" required>
<input name="pass" type="password" placeholder="Password" required>
<button>Login</button>
</form>
