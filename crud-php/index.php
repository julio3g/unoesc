<!DOCTYPE html>
<html>
<head>
    <title>CRUD de Produtos</title>
</head>
<body>
    <h2>CRUD de Produtos</h2>
    <a href="create.php">Novo Produto</a>
    <br><br>
    <table>
        <tr>
            <th>Código</th>
            <th>Descrição</th>
            <th>Data de Cadastro</th>
            <th>Preço</th>
            <th>Ativo</th>
            <th>Unidade</th>
            <th>Tipo de Comissão</th>
            <th>Categoria</th>
            <th>Ações</th>
        </tr>
        <?php
        include 'config.php';

        // Consulta os registros da tabela de produtos
        $sql = "SELECT p.codigo_prd, p.descricao_prd, p.data_cadastro, p.preco, p.ativo, p.unidade, p.tipo_comissao, c.descricao_ctg
                FROM produtos p
                INNER JOIN categorias c ON p.codigo_ctg = c.codigo_ctg";
        $result = mysqli_query($conn, $sql);

        // Exibe os registros na tabela
        while ($row = mysqli_fetch_assoc($result)) {
            echo "<tr>";
            echo "<td>" . $row['codigo_prd'] . "</td>";
            echo "<td>" . $row['descricao_prd'] . "</td>";
            echo "<td>" . $row['data_cadastro'] . "</td>";
            echo "<td>" . $row['preco'] . "</td>";
            echo "<td>" . ($row['ativo'] ? 'Sim' : 'Não') . "</td>";
            echo "<td>" . $row['unidade'] . "</td>";
            echo "<td>" . $row['tipo_comissao'] . "</td>";
            echo "<td>" . $row['descricao_ctg'] . "</td>";
            echo "<td>";
            echo "<a href='read.php?codigo=" . $row['codigo_prd'] . "'>Ver</a> ";
            echo "<a href='update.php?codigo=" . $row['codigo_prd'] . "'>Editar</a> ";
            echo "<a href='delete.php?codigo=" . $row['codigo_prd'] . "' onclick='return confirm(\"Tem certeza que deseja excluir?\")'>Excluir</a>";
            echo "</td>";
            echo "</tr>";
        }

        // Fecha a conexão com o banco de dados
        mysqli_close($conn);
        ?>
    </table>
</body>
</html>
