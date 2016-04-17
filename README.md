## Notes
Playing around with text from the Islamic State's online propaganda magazine, **Dabiq**.

Copies of Dabiq provided by the [Clarion Project](http://www.clarionproject.org/news/islamic-state-isis-isil-propaganda-magazine-dabiq)

## Scraping PDFs
Scraping PDFs being notoriously difficult, I used the Python all-purpose scraper [Textract](http://textract.readthedocs.org/en/latest/), which relies on the [pdftotext](https://en.wikipedia.org/wiki/Pdftotext) utility. This unfortunately doesn't come preinstalled on Windows machines; you have to get it from [Xpdf](http://www.foolabs.com/xpdf/download.html). Download the binary, extract it to C:\Program Files, then follow the steps [here](https://mbnuijten.files.wordpress.com/2013/08/manualinstallationxpdflakens.pdf) to add the proper folder to your system path.