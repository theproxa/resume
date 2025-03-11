install:
	pip install -r requirements.txt

run:
	python app.py

clean:
	rm -rf __pycache__
	rm -rf static/__pycache__
	rm -rf templates/__pycache__

.PHONY: install run clean