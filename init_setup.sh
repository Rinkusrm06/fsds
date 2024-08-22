echo [$(date)]: "START"

echo [$(date)]: "Creating environment with python 3.8 version"
python -m venv ./DiamondPricePredictionEnvironment

echo [$(date)]: "Activating the environment"
source activate ./DiamondPricePredictionEnvironment

echo [$(date)]: "Installing the dev requirements"
pip install -r requirements.txt

echo [$(date)]:"END"