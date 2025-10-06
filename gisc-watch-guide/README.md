# WIS2 Operation

## Overview

This directory contains and provides instructions for managing the document.

### Dependencies

Documentation is managed with [Asciidoctor](https://asciidoctor.org).

Link checking is managed with [asciidoc-link-check](https://www.npmjs.com/package/asciidoc-link-check).

PDF generation is managed with [asciidoctor-pdf](https://www.npmjs.com/package/asciidoctor-pdf).

```bash
apt-get install pandoc
npm install asciidoctor asciidoctor-pdf asciidoc-link-check
```
### Building the document

```bash
# create HTML (single page)
asciidoctor --trace -o wis2-gisc-watch-guide.html index.adoc
# create PDF
asciidoctor --trace -r asciidoctor-pdf --trace -b pdf -o wis2-gisc-watch-guide.pdf index.adoc
# create Word document
asciidoctor --trace --backend docbook --out-file - index.adoc | pandoc --from docbook --to docx --output wis2-gisc-watch-guide.docx
# check links
find . -name "*.adoc" -exec asciidoc-link-check -p -c asciidoc-link-check-config.json {} \;
```

**Note**: `Makefile` provides shortcuts to these commands if you are able to run `make`.

### Managing images

When editing the document and working with images:

- always save images in `gisc-watch-guide/images`
- reference these images in the `.adoc` file you are working on as per below:

```asciidoc
image::images/my-image.png[]
```

This ensures that the live build document is displaying the images correctly / as expected.
