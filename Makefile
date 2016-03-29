REPOS := $(patsubst data/repos/%, %, $(wildcard data/repos/*))
REPO_INFOS := $(patsubst %, build/%.json, $(REPOS))

all : $(REPO_INFOS) build/companies.svg

clean :
	rm -rf ./build

check :
	export PYTHONPATH="./src:$${PYTHONPATH}" && \
		python -m unittest discover -s tests -p '*_test.py'

build/%.json : src/analyze.py data/repos/%
	test -d ./build || mkdir -p ./build
	export PYTHONPATH="./src:$${PYTHONPATH}" && \
		python $^ $@

build/companies.svg : build/companies.dot
	dot -Tsvg $< > $@

build/companies.dot : src/companies.py $(REPO_INFOS)
	export PYTHONPATH="./src:$${PYTHONPATH}" && \
		python $^ > $@

.PHONY : all check clean
