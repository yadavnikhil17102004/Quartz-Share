<?php
session_start();
?>

<!DOCTYPE html>
<html>
<head>
    <title>Employee Details</title>
</head>
<body>

<h2>Employee Information</h2>

<form action="salary.php" method="post">
    Employee No: <input type="text" name="eno" required><br><br>
    Employee Name: <input type="text" name="ename" required><br><br>
    Address: <textarea name="address" required></textarea><br><br>
    <input type="submit" value="Next">
</form>

</body>
</html>
