# --- macros
DOC_DIR= ./doc/

DOCS_TEX= $(wildcard $(DOC_DIR)*.tex)
DOCS_PDF= $(patsubst $(DOC_DIR)%.tex,$(DOC_DIR)%.pdf,$(DOCS_TEX))
DOCS_DVI= $(patsubst $(DOC_DIR)%.tex,$(DOC_DIR)%.dvi,$(DOCS_TEX))
DOCS_BIB= $(patsubst $(DOC_DIR)%.tex,$(DOC_DIR)%,$(DOCS_TEX))

.PHONY: all documentation clean clean_doc

# --- targets
all: documentation

# --- generate documentation
documentation:
	latex -output-directory $(DOC_DIR) $(DOCS_TEX)
	latex -output-directory $(DOC_DIR) $(DOCS_TEX)
	dvipdf $(DOCS_DVI) $(DOCS_PDF)
	$(MAKE) clean_doc

# --- remove binary, executables, and documentation
clean: clean_doc
	@rm -f $(DOC_DIR)*.pdf

clean_doc:
	@rm -f $(DOC_DIR)*.acn $(DOC_DIR)*.glg $(DOC_DIR)*.glo $(DOC_DIR)*.gls $(DOC_DIR)*.glsdefs $(DOC_DIR)*.ist $(DOC_DIR)*.xdy $(DOC_DIR)*.acr $(DOC_DIR)*.bbl $(DOC_DIR)*.blg $(DOC_DIR)*.aux $(DOC_DIR)*.dvi $(DOC_DIR)*.log $(DOC_DIR)*.lot $(DOC_DIR)*.idx $(DOC_DIR)*.toc $(DOC_DIR)*.lof $(DOC_DIR)*.brf $(DOC_DIR)*.out $(DOC_DIR)*.bak $(DOC_DIR)*.bcf $(DOC_DIR)*.xml
	@rm -rf $(DOC_DIR)/latex
