<!DOCTYPE html>
<html>
<head>
    <title>Detalhes do Produto</title>
</head>
<body>
    <h2>Detalhes do Produto</h2>
    <?php
    include 'config.php';

    // Verifica se o código do produto foi passado na URL
    if (isset($_GET['codigo'])) {
        $codigo = $_GET['codigo'];

        // Consulta o produto com o código especificado
        $sql = "SELECT p.codigo_prd, p.descricao_prd, p.data_cadastro, p.preco, p.ativo, p.unidade, p.tipo_comissao, c.descricao_ctg
                FROM produtos p
                INNER JOIN categorias c ON p.codigo_ctg = c.codigo_ctg
                WHERE p.codigo_prd = $codigo";
        $result = mysqli_query($conn, $sql);

        // Exibe os detalhes do produto
        if (mysqli_num_rows($result) > 0) {
            $row = mysqli_fetch_assoc($result);
            echo "<p>Código: " . $row['codigo_prd'] . "</p>";
            echo "<p>Descrição: " . $row['descricao_prd'] . "</p>";
            echo "<p>Data de Cadastro: " . $row['data_cadastro'] . "</p>";
            echo "<p>Preço: " . $row['preco'] . "</p>";
            echo "<p>Ativo: " . ($row['ativo'] ? 'Sim' : 'Não') . "</p>";
            echo "<p>Unidade: " . $row['unidade'] . "</p>";
            echo "<p>Tipo de Comissão: " . $row['tipo_comissao'] . "</p>";
            echo "<p>Categoria: " . $row['descricao_ctg'] . "</p>";
        } else {
            echo "Produto não encontrado.";
        }
    } else {
        echo "Código do produto não especificado.";
    }
    ?>
    <a href="index.php">Voltar</a>
</body>
</html>
