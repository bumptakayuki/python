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
			<div class="col-md-4"></div>
			<div class="col-md-4">
				<h1>積雪予報</h1>
				<p>その日の温度と各条件を入力して、その日に雪が残っているか予測をします。</p>
				<hr>
				<form method="post" action="result.php">
					<div class="form-group">
					<label for="exampleInputFile">その日の温度</label>
						<input name="temp" type="number">
					</div>
					<div class="form-group">
						<label for="exampleInputFile">降水量　　　</label>
						<input name="precipitation" type="number">
					</div>

					<div class="form-group">
						<label for="exampleInputFile">昨日の温度　</label>
						<input name="temp_yeaterday" type="number">
					</div>
					<div class="form-group">
						<label for="exampleInputFile">昨日の積雪量</label>
						<input name="accumulation_yesterday" type="number" >
					</div>

					<button type="submit" class="btn btn-default">Submit</button>
				</form>
			</div>
			<div class="col-md-4"></div>
		</div>
	</div>
</body>
</html>

