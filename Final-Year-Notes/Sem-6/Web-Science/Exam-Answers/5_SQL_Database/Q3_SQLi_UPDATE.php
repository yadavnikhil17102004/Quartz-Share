<?php
// SQL Injection UPDATE - Slip 18 Q2, 25 Q1
// DO NOT USE IN PRODUCTION - FOR EDUCATION ONLY
if($_POST) {
  $user = $_POST['user'];
  $email = $_POST['email'];
  
  // VULNERABLE CODE:
  $sql = "UPDATE users SET email='$email' WHERE user='$user'";
  echo "SQL: $sql<br>";
  echo "Try user: admin' OR '1'='1' #<br>";
}
?>
<form method="POST">
<input name="user" placeholder="Username" required>
<input name="email" placeholder="New Email" required>
<button>Update</button>
</form>

<!-- VULNERABLE INPUT: admin' OR '1'='1' #
    This updates ALL user emails

FIX: Use parameterized queries
$stmt = $conn->prepare("UPDATE users SET email=? WHERE user=?");
$stmt->bind_param("ss", $email, $user);
$stmt->execute();
-->
