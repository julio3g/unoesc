<?php
include 'config.php';

// Verifica se o formulário foi enviado
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Obtém os dados do formulário
    $codigo = $_POST['codigo'];
    $descricao = $_POST['descricao'];
    $preco = $_POST['preco'];
    $ativo = isset($_POST['ativo']) ? 1 : 0;
    $unidade = $_POST['unidade'];
    $tipoComissao = $_POST['tipo_comissao'];

    // Atualiza os dados no banco de dados
    $sql = "UPDATE produtos SET descricao_prd='$descricao', preco=$preco, ativo=$ativo, unidade='$unidade', tipo_comissao='$tipoComissao' WHERE codigo_prd=$codigo";
    $result = mysqli_query($conn, $sql);

    // Verifica se o registro foi atualizado com sucesso
    if ($result) {
        echo "Produto atualizado com sucesso!";
    } else {
        echo "Erro ao atualizar produto: " . mysqli_error($conn);
    }
}
?>
