#!/bin/bash
echo "Setup..."

# 1. Check for Python 3
if ! command -v python3 &> /dev/null
then
    echo "❌ Python 3 could not be found. Please install Python 3."
    exit 1
fi

echo "Python 3 found: $(python3 --version)"

# 2. Create Virtual Environment
echo "Creating virtual environment (.venv)..."
python3 -m venv .venv

# 3. Activate Virtual Environment
source .venv/bin/activate

# 4. Install Dependencies
echo "Installing dependencies"
pip install --upgrade pip
pip install -r requirements.txt

# 5. Create .env
if [ ! -f .env ]; then
    echo "⚠️ Please edit .env and add your Groq API Token."
else
    echo ".env file already exists."
fi

echo ""
echo "==========================================="
echo "Setup Complete!"
echo "==========================================="
echo ""
echo "Next Steps:"
echo "  1. Edit .env with your Groq API Token:"
echo "     nano .env"
echo ""
echo "  2. Run the application:"
echo "     python src/main.py"
echo ""
echo "  3. Open in browser:"
echo "     http://localhost:7860"
echo ""
echo "==========================================="
