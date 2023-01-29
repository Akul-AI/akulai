clean:
	rm -rf akulai/akulai-plugins
	rm -rf .gitmodules

install:
  	pip install -r requirements.txt
  	cd setup
  	python setup.py

run:
	make clean
	make install