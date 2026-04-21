<?php
session_start();

if (!isset($_SESSION['attempts'])) {
    $_SESSION['attempts'] = 0;
}

$error = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST['username'];
    $password = $_POST['password'];

    // Correct credentials
    $correctUser = "admin";
    $correctPass = "12345";

    if ($username === $correctUser && $password === $correctPass) {
        $_SESSION['loggedin'] = true;
        header("Location: welcome.php");
        exit();
    } else {
        $_SESSION['attempts']++;
        $remaining = 3 - $_SESSION['attempts'];
        if ($remaining > 0) {
            $error = "Invalid username or password. Attempts left: $remaining";
        } else {
            $error = "You have exceeded the maximum number of attempts.";
        }
    }
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
<h2>Login Form</h2>

<?php
if ($_SESSION['attempts'] < 3) {
?>
<form method="post">
    Username: <input type="text" name="username" required><br><br>
    Password: <input type="password" name="password" required><br><br>
    <input type="submit" value="Login">
</form>
<?php
} else {
    echo "<p style='color:red;'>$error</p>";
    session_destroy();
}
?>

<p style="color:red;"><?php echo $error; ?></p>
</body>
</html>
