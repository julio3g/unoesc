<?php
include 'config.php';

// Verifica se o formulário foi enviado
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Obtém os dados do formulário
    $descricao = $_POST['descricao'];
    $preco = $_POST['preco'];
    $ativo = isset($_POST['ativo']) ? 1 : 0;
    $unidade = $_POST['unidade'];
    $tipoComissao = $_POST['tipo_comissao'];
    $categoria = $_POST['categoria'];

    // Insere os dados no banco de dados
    $sql = "INSERT INTO produtos (descricao_prd, preco, ativo, unidade, tipo_comissao, codigo_ctg)
            VALUES ('$descricao', $preco, $ativo, '$unidade', '$tipoComissao', $categoria)";
    $result = mysqli_query($conn, $sql);

    // Verifica se o registro foi inserido com sucesso
    if ($result) {
        echo "Produto cadastrado com sucesso!";
    } else {
        echo "Erro ao cadastrar produto: " . mysqli_error($conn);
    }
}
?>
