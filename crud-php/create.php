<!DOCTYPE html>
<html>
<head>
    <title>Novo Produto</title>
</head>
<body>
    <h2>Novo Produto</h2>
    <form method="post" action="create_process.php">
        <?php include 'config.php'; ?>

        <label>Descrição:</label>
        <input type="text" name="descricao" required><br><br>
        <label>Preço:</label>
        <input type="number" name="preco" min="0" step="0.01" required><br><br>
        <label>Ativo:</label>
        <input type="checkbox" name="ativo" checked><br><br>
        <label>Unidade:</label>
        <input type="text" name="unidade" value="un" required><br><br>
        <label>Tipo de Comissão:</label><br>
        <input type="radio" name="tipo_comissao" value="s" checked> Sem comissão<br>
        <input type="radio" name="tipo_comissao" value="f"> Comissão fixa<br>
        <input type="radio" name="tipo_comissao" value="p"> Percentual de comissão<br>
        <label>Categoria:</label>
        <select name="categoria" required>
            <?php
            // Consulta as categorias
            $sql = "SELECT * FROM categorias";
            $result = mysqli_query($conn, $sql);

            // Exibe as opções da lista de categorias
            while ($row = mysqli_fetch_assoc($result)) {
                echo "<option value='" . $row['codigo_ctg'] . "'>" . $row['descricao_ctg'] . "</option>";
            }
            ?>
        </select><br><br>
        <input type="submit" value="Salvar">
    </form>
</body>
</html>
