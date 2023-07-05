<!DOCTYPE html>
<html>
<head>
    <title>Editar Produto</title>
</head>
<body>
    <h2>Editar Produto</h2>
    <?php
    include 'config.php';

    // Verifica se o código do produto foi passado na URL
    if (isset($_GET['codigo'])) {
        $codigo = $_GET['codigo'];

        // Consulta o produto com o código especificado
        $sql = "SELECT * FROM produtos WHERE codigo_prd = $codigo";
        $result = mysqli_query($conn, $sql);

        // Exibe o formulário de edição
        if (mysqli_num_rows($result) > 0) {
            $row = mysqli_fetch_assoc($result);
            ?>
            <form method="post" action="update_process.php">
                <input type="hidden" name="codigo" value="<?php echo $row['codigo_prd']; ?>">
                <label>Descrição:</label>
                <input type="text" name="descricao" value="<?php echo $row['descricao_prd']; ?>" required><br><br>
                <label>Preço:</label>
                <input type="number" name="preco" value="<?php echo $row['preco']; ?>" min="0" step="0.01" required><br><br>
                <label>Ativo:</label>
                <input type="checkbox" name="ativo" <?php echo ($row['ativo'] ? 'checked' : ''); ?>><br><br>
                <label>Unidade:</label>
                <input type="text" name="unidade" value="<?php echo $row['unidade']; ?>" required><br><br>
                <label>Tipo de Comissão:</label><br>
                <input type="radio" name="tipo_comissao" value="s" <?php echo ($row['tipo_comissao'] == 's' ? 'checked' : ''); ?>> Sem comissão<br>
                <input type="radio" name="tipo_comissao" value="f" <?php echo ($row['tipo_comissao'] == 'f' ? 'checked' : ''); ?>> Comissão fixa<br>
                <input type="radio" name="tipo_comissao" value="p" <?php echo ($row['tipo_comissao'] == 'p' ? 'checked' : ''); ?>> Percentual de comissão<br>
                <input type="submit" value="Salvar">
            </form>
            <?php
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
