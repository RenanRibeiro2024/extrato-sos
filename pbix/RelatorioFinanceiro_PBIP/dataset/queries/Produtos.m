let
    Fonte = Excel.Workbook(File.Contents("Produtos.xlsx"), null, true),
    Tabela = Fonte{[Name="Produtos"]}[Data]
in
    Tabela
