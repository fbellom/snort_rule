rules:
	python generate_snort_rules.py > rules_output.txt

venv:
	python3.10 -m venv .venv
	source .venv/bin/activate

clean: 
	rm -rf rules_output.txt
