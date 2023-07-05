<?php
include 'config.php';

// Verifica se o código do produto foi passado na URL
if (isset($_GET['codigo'])) {
    $codigo = $_GET['codigo'];

    // Exclui o produto com o código especificado
    $sql = "DELETE FROM produtos WHERE codigo_prd = $codigo";
    $result = mysqli_query($conn, $sql);

    // Verifica se o produto foi excluído com sucesso
    if ($result) {
        echo "Produto excluído com sucesso!";
    } else {
        echo "Erro ao excluir produto: " . mysqli_error($conn);
    }
} else {
    echo "Código do produto não especificado.";
}
?>
