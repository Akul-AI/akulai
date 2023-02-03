clean:
	rm -rf akulai/akulai-plugins
	rm -rf .gitmodules

install:
	cd requirements
  	pip install -r requirements.txt
	cd ..
  	cd setup
  	python setup.py

run:
	make clean
	make install