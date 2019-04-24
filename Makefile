SHELL=/bin/bash

all: venv
	@echo
	@echo 'To activate virtualenv:'
	@echo 'source venv/bin/activate'
	@echo

venv: requirements.txt
	@virtualenv venv -p python3
	@if [[ -e "requirements.txt" ]]; then source venv/bin/activate && pip install -r requirements.txt; fi

test:
	@python3 -m unittest discover tests/

clean:
	$(RM) -r venv
	$(RM) -r __pycache__

.PHONY: clean all test
