<?php
// SQL Injection Demo - Slip 2 Q2, 16 Q1
// DO NOT USE IN PRODUCTION - FOR EDUCATION ONLY
if($_POST) {
  $user = $_POST['user'];
  $pass = $_POST['pass'];
  
  // VULNERABLE CODE:
  $sql = "SELECT * FROM users WHERE user='$user' AND pass='$pass'";
  echo "SQL: $sql<br>";
  echo "Try: admin' OR '1'='1<br>";
}
?>
<form method="POST">
<input name="user" placeholder="Username" required>
<input name="pass" placeholder="Password" required>
<button>Login</button>
</form>

<!-- VULNERABLE INPUT: admin' OR '1'='1
    This returns ALL users because '1'='1' is always true

FIX: Use prepared statements
$stmt = $conn->prepare("SELECT * FROM users WHERE user=? AND pass=?");
$stmt->bind_param("ss", $user, $pass);
$stmt->execute();
-->
