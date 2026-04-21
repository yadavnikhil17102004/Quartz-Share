<?php
// Q8: Multi-page Form with Session - Slip 11 Q2
session_start();
$page = $_GET['p']??1;
if($_POST) {
  if($page==1) {
    $_SESSION['eno']=$_POST['eno'];
    $_SESSION['name']=$_POST['name'];
    $_SESSION['addr']=$_POST['addr'];
    header("Location:?p=2");
  } elseif($page==2) {
    $_SESSION['basic']=$_POST['basic'];
    $_SESSION['da']=$_POST['da'];
    $_SESSION['hra']=$_POST['hra'];
    header("Location:?p=3");
  }
}
if($page==1) {
?>
<form method="POST">
<input name="eno" placeholder="Employee No" required>
<input name="name" placeholder="Name" required>
<input name="addr" placeholder="Address" required>
<button>Next</button>
</form>
<?php } elseif($page==2) { ?>
<form method="POST">
<input type="number" name="basic" placeholder="Basic" required>
<input type="number" name="da" placeholder="DA" required>
<input type="number" name="hra" placeholder="HRA" required>
<button>Next</button>
</form>
<?php } elseif($page==3) {
$total = $_SESSION['basic']+$_SESSION['da']+$_SESSION['hra'];
echo "ID:".$_SESSION['eno'].", Name:".$_SESSION['name'].", Addr:".$_SESSION['addr'].", Basic:".$_SESSION['basic'].", DA:".$_SESSION['da'].", HRA:".$_SESSION['hra'].", Total:$total";
} ?>
