all: README.md

README.md: example.py example.py.out

%: %.j2
	j2 $< > $@

%.py.out: %.py
	python $< > $@
