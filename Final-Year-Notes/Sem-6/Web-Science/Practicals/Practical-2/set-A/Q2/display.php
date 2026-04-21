<?php
session_start();

// Store salary details
$_SESSION['basic'] = $_POST['basic'];
$_SESSION['da'] = $_POST['da'];
$_SESSION['hra'] = $_POST['hra'];

$total = $_SESSION['basic'] + $_SESSION['da'] + $_SESSION['hra'];
?>

<!DOCTYPE html>
<html>
<head>
    <title>Employee Details</title>
</head>
<body>

<h2>Employee Information</h2>

<p><strong>Employee No:</strong> <?php echo $_SESSION['eno']; ?></p>
<p><strong>Employee Name:</strong> <?php echo $_SESSION['ename']; ?></p>
<p><strong>Address:</strong> <?php echo $_SESSION['address']; ?></p>

<h2>Earnings</h2>

<p><strong>Basic:</strong> <?php echo $_SESSION['basic']; ?></p>
<p><strong>DA:</strong> <?php echo $_SESSION['da']; ?></p>
<p><strong>HRA:</strong> <?php echo $_SESSION['hra']; ?></p>
<p><strong>Total Salary:</strong> <?php echo $total; ?></p>

</body>
</html>
