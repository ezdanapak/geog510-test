როცა ახალ .md ამატებ .yml კონფიგურაციაში ნავიგაციაში ჩამატება არ დაგავიწყდეს
ბმულების ჩასამატებლად

[სიტყვა](ამ სიტყვაში ჩაშენებული ბმული)
[mkdocs.org](https://www.mkdocs.org).
თუ სიტყვას და ბმულს 2 დაშორებით დააცილებ სტანდარტულ ტექსტად აღიქვამს, პირდაპირ ასე დაბეჭდავს. 
[სიტყვა] (ამ სიტყვაში ჩაშენებული ბმული)

აბზაცის ბურთულებით გამოყოფა 
 - 


აქ ნოუთის წინ თუ ??? დაწერ მაშინ ასაკეც ჩამოსაკეცი იქნება თუ არადა გაშლილი
!!! note    
     - შეიპფაილი არის ფორმატი რომელიც ინახავს ვექტორულ სივრცულ მონაცემებს, მისი შემქმნელი [ESRI - ა](https://www.esri.com/en-us/home). 




## Commands
ფიფქით გამოყოფ ტექსტს პატარა უჯრაში ჩასმულს
 `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

 ## Commands 
 1 დაშორებას თუ გაუკეთებ ## ამათ წინ სტანდარტულ ტექსტად აღიქვამს ## Commands დაგიწერს პირდაპირ


თუ კონტენტის ტექსტს წინ - დაუწერ ჩარჩოში სვავს და წითლად გამოყოფს ტექსტს
 ## მთავარი ფორმატები:
     .shp ინახავს გეომეტრიას, იგივე გეოგრაფიულ მონაცემებს და არის კონტეინერის მეთაური
     .shx ინდექსაციის ფორმატი, იძლევა სივრცული ობიექტების სწრაფად დათვალიერების საშუალებას
    - .dbf ატრიბუტული ცხრილის ჩანაწერების შემნახველი


yaml სქემა ფლაგინისთვის
  "yaml.schemas": {
    "https://squidfunk.github.io/mkdocs-material/schema.json": "mkdocs.yml"
  },
  "yaml.customTags": [
    "!ENV scalar",
    "!ENV sequence",
    "!relative scalar",
    "tag:yaml.org,2002:python/name:material.extensions.emoji.to_svg",
    "tag:yaml.org,2002:python/name:material.extensions.emoji.twemoji",
    "tag:yaml.org,2002:python/name:pymdownx.superfences.fence_code_format"
  ]

  # theme: 
#   name: material
#   palette: 
#     scheme: default
#     primary: green
#     accent: deep purple