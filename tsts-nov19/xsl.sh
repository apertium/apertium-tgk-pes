cp apertium-tg-fa.tg.metadix medianfile
xsltproc ./buscaPar.xsl ./medianfile > ./paradigms.xsl
xsltproc ./paradigms.xsl ./medianfile > apertium-tg-fa.tg.xml








