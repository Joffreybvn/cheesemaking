
preview-en:
	mkdocs serve --config-file=mkdocs.en.yml

site:
	mkdocs build --config-file=mkdocs.en.yml
	mkdocs build --config-file=mkdocs.fr.yml
	mkdocs build --config-file=mkdocs.nl.yml
	mkdocs build --config-file=mkdocs.es.yml
