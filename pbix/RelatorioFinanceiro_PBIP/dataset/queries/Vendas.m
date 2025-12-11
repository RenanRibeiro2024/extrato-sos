let
    Fonte = Excel.Workbook(File.Contents("Vendas.xlsx"), null, true),
    Tabela = Fonte{[Name="Vendas"]}[Data]
in
    Tabela
