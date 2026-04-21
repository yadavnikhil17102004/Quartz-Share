<?php
session_start();

if (!isset($_SESSION['loggedin'])) {
    header("Location: login.php");
    exit();
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Welcome</title>
</head>
<body>
<h2>Welcome!</h2>
<p>You have successfully logged in.</p>

<form>
    <p>This is the second form.</p>
</form>
</body>
</html>
