#!/bin/bash -

## Create the 3D figure.
# $1 book title
# $2 book base URL
# $3... the single slides

# strict error handling
set -o pipefail  # trace ERR through pipes
set -o errtrace  # trace ERR through 'time command' and other functions
set -o nounset   # set -u : exit the script if you try to use an uninitialized variable
set -o errexit   # set -e : exit the script if any statement returns a non-true return value


# strict error handling
set -o pipefail  # trace ERR through pipes
set -o errtrace  # trace ERR through 'time command' and other functions
set -o nounset   # set -u : exit the script if you try to use an uninitialized variable
set -o errexit   # set -e : exit the script if any statement returns a non-true return value

echo "$(date +'%0Y-%0m-%0d %0R:%0S'): Welcome to the 3D figure creation script."

if [[ $(declare -p PYTHON_INTERPRETER 2>/dev/null) != declare\ ?x* ]]; then
  echo "$(date +'%0Y-%0m-%0d %0R:%0S'): No virtual environment found."
  venvDir="$(mktemp -d)"
  echo "$(date +'%0Y-%0m-%0d %0R:%0S'): Got temp dir '$venvDir', now creating environment in it."
  python3 -m venv --upgrade-deps "$venvDir"
  echo "$(date +'%0Y-%0m-%0d %0R:%0S'): Activating virtual environment in '$venvDir'."
  source "$venvDir/bin/activate"
  export PYTHON_INTERPRETER="$venvDir/bin/python3"
  echo "$(date +'%0Y-%0m-%0d %0R:%0S'): Setting python interpreter to '$PYTHON_INTERPRETER'."
  needCleanup=true
else
  echo "$(date +'%0Y-%0m-%0d %0R:%0S'): Virtual environment with interpreter '$PYTHON_INTERPRETER' detected. Using that one."
  needCleanup=false
fi

echo "$(date +'%0Y-%0m-%0d %0R:%0S'): Now installing pip install on dependencies."
"$PYTHON_INTERPRETER" -m pip install --no-input --default-timeout=300 --timeout=300 --retries=100 -r "./requirements.txt"

echo "$(date +'%0Y-%0m-%0d %0R:%0S'): Now running creating figure."

python3 ./function3d.py

echo "$(date +'%0Y-%0m-%0d %0R:%0S'): Done creating figure."

if [ "$needCleanup" = true ]; then
  echo "$(date +'%0Y-%0m-%0d %0R:%0S'): Deactivating virtual environment."
  deactivate
  if [ -d "$venvDir" ]; then
    echo "$(date +'%0Y-%0m-%0d %0R:%0S'): Deleting virtual environment '$venvDir'."
    rm -rf "$venvDir"
  else
    echo "$(date +'%0Y-%0m-%0d %0R:%0S'): '$venvDir' is not a directory?."
  fi
fi

echo "$(date +'%0Y-%0m-%0d %0R:%0S'): Cropping the figure."

pdfcrop --margins "2 2 2 2" function3d.pdf function3d_cropped.pdf
mv function3d_cropped.pdf function3d.pdf

pdfcrop --margins "2 2 2 2" function3d_optimum.pdf function3d_optimum_cropped.pdf
mv function3d_optimum_cropped.pdf function3d_optimum.pdf

echo "$(date +'%0Y-%0m-%0d %0R:%0S'): We have finished the figure maker."
