<?php
// User Registration with Encryption - Slip 5 Q1, 20 Q2
if($_POST) {
  if($_POST['pass']==$_POST['cpass']) {
    $encrypted = password_hash($_POST['pass'], PASSWORD_DEFAULT);
    echo "Name: ".$_POST['name']."<br>";
    echo "Email: ".$_POST['email']."<br>";
    echo "Contact: ".$_POST['contact']."<br>";
    echo "Password Stored (Encrypted)";
  } else echo "Passwords Don't Match";
}
?>
<form method="POST">
<input name="name" placeholder="Full Name" required>
<input name="contact" type="tel" placeholder="Contact" required>
<input name="email" type="email" placeholder="Email" required>
<input name="pass" type="password" placeholder="Password" required>
<input name="cpass" type="password" placeholder="Confirm Password" required>
<button>Register</button>
</form>
