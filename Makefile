REPOS := autoconf \
	automake \
	bash \
	bison \
	coreutils \
	cpio \
	dbus \
	emacs \
	gawk \
	ghostscript \
	git \
	gnupg \
	grep \
	gzip \
	linux \
	make \
	polkit \
	screen \
	sed \
	systemd \
	tar \
	wget

REPO_INFOS := $(patsubst %, build/%.json, $(REPOS))

all : $(REPO_INFOS) build/companies.svg

clean :
	rm -rf ./build

check :
	export PYTHONPATH="./src:$${PYTHONPATH}" && \
		python -m unittest discover -s tests -p '*_test.py'

build/%.json : data/repos/% src/analyze.py
	test -d ./build || mkdir -p ./build
	export PYTHONPATH="./src:$${PYTHONPATH}" && \
		python src/analyze.py $< > $@

build/companies.svg : build/companies.dot
	dot -Tsvg $< > $@

build/companies.dot : $(REPO_INFOS)
	export PYTHONPATH="./src:$${PYTHONPATH}" && \
		python src/companies.py $^ > $@

.PHONY : all check clean
