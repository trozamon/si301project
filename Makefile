REPOS := dbus
REPO_INFOS := $(patsubst %, build/%.json, $(REPOS))

all : $(REPO_INFOS)

clean :
	rm -rf ./build

build/%.json : data/repos/% src/analyze.py
	test -d ./build || mkdir -p ./build
	export PYTHONPATH="./src:$${PYTHONPATH}" && python src/analyze.py $< #> $@

.PHONY : all clean
