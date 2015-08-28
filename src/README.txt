Change introduction file

cd src
wget -r -e robots=off http://cse01-iiith.virtual-labs.ac.in/index.php
cp ss.py cse01-iiith.virtual-labs.ac.in/
cp template.html cse01-iiith.virtual-labs.ac.in/
cp ss1.py cse01-iiith.virtual-labs.ac.in/exp1/
cp template1.html cse01-iiith.virtual-labs.ac.in/exp1
cd cse01-iiith.virtual-labs.ac.in
python ss.py
cd cse01-iiith.virtual-labs.ac.in/exp1
python ss.py


