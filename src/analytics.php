  <?php

$myfile = "countlog.txt";
$count= 0 ;

/* counter */
//opens countlog.txt to read the user list
$datei = fopen($myfile,'r');

while(!feof($datei)){
  $line = fgets($datei);
  $count++;
}

fclose($datei);
$user_agent = $_SERVER['HTTP_USER_AGENT']; //user browser
        $ip_address = $_SERVER["REMOTE_ADDR"];     // user ip adderss
        $page_name = $_SERVER["SCRIPT_NAME"];      // page the user looking
        $query_string = $_SERVER["QUERY_STRING"];   // what query he used
        $current_page = $page_name."?".$query_string; 


    // get location 
        $url = json_decode(file_get_contents("http://api.ipinfodb.com/v3/ip-city/?key=/3196f5ff4f2460dc9fdbc363a2976b70577892ba91b3c41c692348a6a472edf5/
        // you can get your api key form http://ipinfodb.com/
        ip=".$_SERVER['REMOTE_ADDR']."&format=json"));
        $country=$url->countryName;  // user country
        $city=$url->cityName;       // city
        $region=$url->regionName;   // regoin
        $latitude=$url->latitude;    //lat and lon
        $longitude=$url->longitude;

    // get time
        date_default_timezone_set('UTC');
        $date = date("Y-m-d");
        $time = date("H:i:s");


// opens countlog.txt to append the new user
$datei = fopen($myfile,'a') or die("Can't open file");
fwrite($datei, $new1);
fclose($datei);

?>
