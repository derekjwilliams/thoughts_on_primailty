# thoughts_on_primailty
Thatcher's thoughts on primality

( Primality: MetaBinary Analysis and Network of Association ...could be most general) and applied to many fields

## Converting from Docx to Markdown usng Pandoc

```bash

myfilename="example"

pandoc \
-t markdown_strict \
--extract-media='./attachments/$myfilename' \
$myfilename.docx \
-o $myfilename.md
```

```bash
pandoc \
-t markdown_strict \
--extract-media='./attachments/Engine' \
Engine.docx \
-o Engine.md
```

