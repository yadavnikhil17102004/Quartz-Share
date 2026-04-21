<?php
if (isset($_POST['save'])) {
    setcookie("font_style", $_POST['font_style'], time() + 3600);
    setcookie("font_size", $_POST['font_size'], time() + 3600);
    setcookie("font_color", $_POST['font_color'], time() + 3600);
    setcookie("bg_color", $_POST['bg_color'], time() + 3600);

    header("Location: show.php");
    exit();
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Set Preferences</title>
</head>
<body>

<h2>Set Web Page Preferences</h2>

<form method="post">
    Font Style:
    <select name="font_style">
        <option value="Arial">Arial</option>
        <option value="Times New Roman">Times New Roman</option>
        <option value="Verdana">Verdana</option>
    </select><br><br>

    Font Size:
    <select name="font_size">
        <option value="14px">14px</option>
        <option value="18px">18px</option>
        <option value="22px">22px</option>
    </select><br><br>

    Font Color:
    <input type="color" name="font_color"><br><br>

    Background Color:
    <input type="color" name="bg_color"><br><br>

    <input type="submit" name="save" value="Save Preferences">
</form>

</body>
</html>
