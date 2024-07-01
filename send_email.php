<?php
// Ensure the script is called with enough arguments
if ($argc < 4) {
    echo "Please provide the subject, email message, and recipient email as command-line arguments.";
    exit(1);
}

// Read configuration from the config.ini file
$config = parse_ini_file('config.ini');
$from = 'send@churcharisenetwork.com.ng';
$subject = $argv[1];
$message = $argv[2];
$to = $argv[3];  // Recipient email from the command-line argument
$headers = "From: $from\r\n";
$headers .= "Reply-To: $from\r\n";
$headers .= "MIME-Version: 1.0\r\n";
$headers .= "Content-Type: text/html; charset=ISO-8859-1\r\n";
print('sending email from php');
if (mail($to, $subject, $message, $headers)) {
    echo "Email sent successfully!";
} else {
    echo "Email sending failed.";
}
?>
