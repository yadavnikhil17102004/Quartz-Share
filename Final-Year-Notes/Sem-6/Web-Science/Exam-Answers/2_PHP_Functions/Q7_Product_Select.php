<?php
// Q7: Product Selection - Slip 14 Q1, Slip 17 Q1
if($_POST) {
  $items = [
    'Book'=>['price'=>100,'qty'=>$_POST['book']??0],
    'Pen'=>['price'=>5,'qty'=>$_POST['pen']??0],
    'Bag'=>['price'=>500,'qty'=>$_POST['bag']??0]
  ];
  foreach($items as $n=>$d) {
    if($d['qty']>0) echo "$n: ".$d['price']*$d['qty']."<br>";
  }
  $total_qty = array_sum(array_column($items,'qty'));
  $total_cost = 0;
  foreach($items as $d) $total_cost += $d['price']*$d['qty'];
  echo "Total Qty: $total_qty, Total Cost: $total_cost";
}
?>
<form method="POST">
<input type="number" name="book" placeholder="Book Qty" value="0">
<input type="number" name="pen" placeholder="Pen Qty" value="0">
<input type="number" name="bag" placeholder="Bag Qty" value="0">
<button>Calculate</button>
</form>
