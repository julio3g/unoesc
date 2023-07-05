<?php
// Configuração do banco de dados
$host = "localhost";
$username = "user_database";
$password = "password";
$database = "crud_produtos";

// Conexão com o banco de dados
$conn = mysqli_connect($host, $username, $password, $database);

// Verifica se a conexão foi estabelecida corretamente
if (!$conn) {
    die("Falha na conexão com o banco de dados: " . mysqli_connect_error());
}
?>
