<?php
    $name = $_POST['name'];
    $email = $_POST['email'];
    $message = $_POST['message'];
    $from = 'From: agriindiaexp.com'; 
    $to = 'shridhar.kagi@gmail.com'; 
    $subject = 'Email Inquiry';

    $body = "From: $name\n E-Mail: $email\n Message:\n $message";

    if ($_POST['submit']) {
        if (mail ($to, $subject, $body, $from)) { 
           $success = "Message successfully sent";
        } else {
            $success = "Message Sending Failed, try again";
        }
    }
?>