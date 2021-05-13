
main: main.pdf
	pdflatex main.tex


main.pdf: bibliography.bib
	pdflatex main.tex
	biber main
	pdflatex main.tex

clean:
	rm *.out *.log *.pdf *.bcf *.bbl *.blg *.synctex.gz *.aux *.run.xml 2> /dev/null
	# If there is nothing to remove don't make a stink about it by redirecting
