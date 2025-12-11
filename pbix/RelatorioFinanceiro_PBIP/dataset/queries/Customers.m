let
    Fonte = Csv.Document(File.Contents("Customers.csv"),[Delimiter=",", Columns=4, Encoding=1252, QuoteStyle=QuoteStyle.Csv]),
    PromotedHeaders = Table.PromoteHeaders(Fonte, [PromoteAllScalars=true]),
    ChangedTypes = Table.TransformColumnTypes(PromotedHeaders,{{"CustomerID", Int64.Type}, {"CustomerName", type text}, {"City", type text}, {"State", type text}})
in
    ChangedTypes
