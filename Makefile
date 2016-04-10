REPOS := $(patsubst data/repos/%, %, $(wildcard data/repos/*))
REPO_INFOS := $(patsubst %, build/%.json, $(REPOS))
REPO_TAG_DATES := $(patsubst %, build/%.tagdates, $(REPOS))

all : $(REPO_INFOS) \
	build/companies.svg \
	build/release_speed.txt

clean :
	rm -rf ./build

check :
	export PYTHONPATH="./src:$${PYTHONPATH}" && \
		python -m unittest discover -s tests -p '*_test.py'

build/%.json : src/analyze.py data/repos/%
	test -d ./build || mkdir -p ./build
	export PYTHONPATH="./src:$${PYTHONPATH}" && \
		python $^ $@

build/%.tagdates : data/repos/%
	(cd $< && git show --tags | egrep "^Date:") > $@

build/release_speed.txt : src/release_speed.py $(REPO_TAG_DATES)
	export PYTHONPATH="./src:$${PYTHONPATH}" && \
		python $^ $@

build/companies.svg : build/companies.dot
	dot -Tsvg $< > $@

build/companies.dot : src/companies.py $(REPO_INFOS)
	export PYTHONPATH="./src:$${PYTHONPATH}" && \
		python $^ $@

.PHONY : all check clean
