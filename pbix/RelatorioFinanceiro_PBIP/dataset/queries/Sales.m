let
    Fonte = Csv.Document(File.Contents("Sales.csv"),[Delimiter=",", Columns=5, Encoding=1252, QuoteStyle=QuoteStyle.Csv]),
    PromotedHeaders = Table.PromoteHeaders(Fonte, [PromoteAllScalars=true]),
    ChangedTypes = Table.TransformColumnTypes(PromotedHeaders,{{"SaleID", Int64.Type}, {"CustomerID", Int64.Type}, {"ProductID", Int64.Type}, {"Quantity", Int64.Type}, {"SaleDate", type datetime}})
in
    ChangedTypes
