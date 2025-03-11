run: install
	python app.py

install:
	pip install -r requirements.txt



clean:
	rm -rf __pycache__
	rm -rf static/__pycache__
	rm -rf templates/__pycache__

.PHONY: install run clean