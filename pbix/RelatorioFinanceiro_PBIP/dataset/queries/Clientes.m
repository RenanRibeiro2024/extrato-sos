let
    Fonte = Excel.Workbook(File.Contents("Clientes.xlsx"), null, true),
    Tabela = Fonte{[Name="Clientes"]}[Data]
in
    Tabela
