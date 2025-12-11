let
    Fonte = Csv.Document(File.Contents("Products.csv"),[Delimiter=",", Columns=3, Encoding=1252, QuoteStyle=QuoteStyle.Csv]),
    PromotedHeaders = Table.PromoteHeaders(Fonte, [PromoteAllScalars=true]),
    ChangedTypes = Table.TransformColumnTypes(PromotedHeaders,{{"ProductID", Int64.Type}, {"ProductName", type text}, {"UnitPrice", type number}})
in
    ChangedTypes
