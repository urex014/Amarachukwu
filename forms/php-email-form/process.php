<?php
// Database connection details
$servername = "localhost";  // Usually 'localhost' for local databases
$username = "root";         // Your phpMyAdmin username (default is 'root')
$password = "";             // Your phpMyAdmin password (default is empty for 'root')
$dbname = "contact_db";     // Database name (contact_db in this case)

// Create connection to MySQL
$conn = new mysqli($servername, $username, $password, $dbname);

// Check if connection was successful
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Check if form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get form data
    $name = $conn->real_escape_string($_POST['name']);
    $email = $conn->real_escape_string($_POST['email']);
    $message = $conn->real_escape_string($_POST['message']);

    // Insert data into the 'contacts' table
    $sql = "INSERT INTO contacts (name, email, message) VALUES ('$name', '$email', '$message')";

    if ($conn->query($sql) === TRUE) {
        echo "Thank you for your feedback";
    } else {
        echo "error: " . $sql . "<br>" . $conn->error;
    }
}

// Close the database connection
$conn->close();

