<!DOCTYPE html>
<html lang="pt-br">

<head>
	<?php require "html/head.php" ?>

</head>

	<!--  -->
	<body>
		<?php include "html/header.php" ?>
		<main>
		<h1>Detalhes do produto</h1>
        <div class="card">
            <img src="" style="width: 20rem; margin: auto" class="card-img-top" alt="...">
            <div class="card-body">
                <h5 class="card-title"></h5>
                <p class="card-text"></p>
            </div>
            <ul class="list-group list-group-flush">
                <li class="list-group-item">TIPO: </li>
                <li class="list-group-item">CATEGORIA: </li>
                <li class="list-group-item">EM ESTOQUE: </li>
                <li class="list-group-item">Valor: R$ </li>
            </ul>
            <div class="card-body">
                <a href="index.php" class="card-link">Voltar</a>
                <a href="produtos.php" class="card-link">Lista de Produtos</a>
            </div>
        </div>
		</main>
<?php
	include "html/rodaPe.php";
?>


		<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8"
        crossorigin="anonymous"></script>

</body>

</html>