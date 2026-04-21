<?php
// Book Details to MySQL - Slip 19 Q1
mysqli_report(MYSQLI_REPORT_OFF);
$host="localhost"; $user="root"; $pass=""; $db="webscience";
$conn = @new mysqli($host,$user,$pass,$db);
if($_POST) {
  $bno=$_POST['bno']; $bname=$_POST['bname']; $price=$_POST['price'];
  $sql = "INSERT INTO books VALUES('$bno','$bname',$price)";

  // Primary path: MySQL insert.
  if(!$conn->connect_error && $conn->query($sql)) {
    echo "Book Added in MySQL";
  } else {
    // Fallback path: store locally so practical still runs without MySQL.
    $line = $bno.",".$bname.",".$price.PHP_EOL;
    file_put_contents(__DIR__."/book_fallback.txt", $line, FILE_APPEND);
    echo "MySQL not available. Saved locally in book_fallback.txt";
    echo "<br>SQL used: ".$sql;
  }
}
?>
<form method="POST">
<input name="bno" placeholder="Book No" required>
<input name="bname" placeholder="Book Name" required>
<input type="number" name="price" placeholder="Price" required>
<button>Add Book</button>
</form>

<!-- MySQL Setup:
CREATE DATABASE webscience;
CREATE TABLE books (bno VARCHAR(10), bname VARCHAR(100), price DECIMAL(10,2));
-->
