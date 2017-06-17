<?php

  $linha = file_get_contents("/tmp/dht11.txt");
  $dados = explode(";", $linha);
  $status = $dados[0];
  $temperatura = @$dados[1];
  $umidade = @$dados[2];
?>

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="refresh" content="3;url=dht11.php">
    <title>Raspberry + Sensor DHT11</title>
  </head>
  <body>
	<div class="container">
		
	      <div class="starter-template">
		<?php if ($status == "ok"): ?>
       		 <p class="lead" style="text-align: center;">Temperatura: <?php echo $temperatura;?> Umidade: <?php echo $umidade; ?></p>
		<?php else:  ?>
		  <p class="lead" style="text-align: center;">Sistema indispon&iacute;vel. Por favor tente mais tarde.</p>
		<?php endif;?>
     	      </div>

    </div><!-- /.container -->

    <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

  </body>
</html>
