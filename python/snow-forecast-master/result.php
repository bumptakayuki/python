<html>
<head>
	<title>積雪予報</title>
	<meta charset="UTF-8"> 
	<!-- Latest compiled and minified CSS -->
	<link rel="stylesheet" href="bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">

	<!-- Optional theme -->
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap-theme.min.css" integrity="sha384-fLW2N01lMqjakBkx3l/M9EahuwpSfeNvV63J5ezn3uZzapT0u7EYsXMjQV+0En5r" crossorigin="anonymous">

</head>

<body>
	<div class="container">
		<div class="row">
			<div class="col-md-2"></div>
			<div class="col-md-8">
				<h1>積雪予報</h1>
				<hr>

				<?php
				echo '<table class="table table-striped">';
				$fullPath =
				'python ./snow_forecaster.py '.$_POST['temp'].' '.$_POST['precipitation'].' '.$_POST['temp_yeaterday'].' '.$_POST['accumulation_yesterday'];
    			
				exec($fullPath, $outputs);
				echo "<tr class='success'>";	
				echo "<td colspan='2'>";	
				echo '各モデルの点数';	
				echo "</td>";	
				echo "</tr>";

				echo "<tr>";
				echo "<td>";	
				echo 'inearSVCのスコア:';	
				echo "</td>";	
				echo "<td>";	
				echo $outputs[0];	
				echo "</td>";	
				echo "</tr>";

				echo "<tr>";	
				echo "<td>";	
				echo 'AdaBoostClassifierのスコア:';	
				echo "</td>";
				echo "<td>";	
				echo $outputs[1];	
				echo "</td>";	
				echo "</tr>";

				echo "<tr>";	
				echo "<td>";	
				echo 'ExtraTreesClassifierのスコア:';	
				echo "</td>";
				echo "<td>";	
				echo $outputs[2];	
				echo "</td>";	
				echo "</tr>";

				echo "<tr>";	
				echo "<td>";	
				echo 'GradientBoostingClassifierのスコア:';	
				echo "</td>";
				echo "<td>";	
				echo $outputs[3];	
				echo "</td>";	
				echo "</tr>";

				echo "<tr>";	
				echo "<td>";	
				echo 'RandomForestClassifierのスコア:';	
				echo "</td>";
				echo "<td>";	
				echo $outputs[4];	
				echo "</td>";	
				echo "</tr>";

				echo "<tr>";	
				echo "<td>";	
				echo '使用するモデル:';	
				echo "</td>";
				echo "<td>";	
				echo $outputs[6];	
				echo "</td>";	
				echo "</tr>";
				echo "<tr>";	

				echo "</table>";


				echo "<br><br>";

				echo '<table class="table table-striped">';
				echo "<tr  class='success'>";	
				echo "<td colspan='2'>";
				echo '指定した条件での積雪予報';	
				echo "</td>";	
				echo "</tr>";

				echo "<tr>";
				echo "<td>";	
				echo '入力条件:';	
				echo "</td>";
				echo "<td>";	
				echo $outputs[8];	
				echo "</td>";	
				echo "</tr>";
				
				echo "<tr>";
				echo "<td>";	
				echo '判定結果:';	
				echo "</td>";	
				echo "<td>";	
				echo $outputs[10];	
				echo "</td>";	
				echo "</tr>";
		

				echo "</table>";

				?>
			</div>
			<div class="col-md-2"></div>
		</div>
	</div>

</body>
</html>


