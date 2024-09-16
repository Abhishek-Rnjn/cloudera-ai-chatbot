echo "creating virtaul environment env"
python3.10 -m venv env

echo " activating the environment"
source env/bin/activate

echo "installing the requirements"
pip install -r requirements.txt

echo "activated env"