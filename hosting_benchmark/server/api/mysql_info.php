<?php
header('Content-type: application/json');

include '../inc.php';

set_time_limit(60 * 2);

function getMysqliObject() {
    $mysqli = new mysqli($GLOBALS['dbhost'], $GLOBALS['dbuser'], $GLOBALS['dbpass'], $GLOBALS['dbname']);
    if ($mysqli->connect_error) {
        die('Could not connect to database');
    }
    return $mysqli;
}

// https://www.php.net/manual/en/mysqli.get-server-info.php#118822
function getServerInfo() {
    $mysqli = getMysqliObject();
    $query = "SELECT version();";
    $stmt = $mysqli->prepare($query);
    $stmt->execute();
    $result = $stmt->get_result();
    $version = $result->fetch_assoc()['version()'];
    $mysqli->close();
    return $version;
}

$results = array(
    "serverInfo" => getServerInfo(),
    "clientInfo" => mysqli_get_client_info(),
);

echo json_encode($results);
