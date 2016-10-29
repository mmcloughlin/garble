all: README.md

README.md: output.json example.py example.py.out

%: %.j2
	j2 $< > $@

output.json: input.json
	garble < input.json | python -m json.tool > $@

%.py.out: %.py
	python $< > $@
