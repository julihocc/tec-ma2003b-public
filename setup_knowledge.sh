#!/bin/bash
# Setup script for MA2003B Knowledge Base Download System

echo "🚀 Setting up MA2003B Knowledge Base Download System..."

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    exit 1
fi

echo "✅ Python 3 found"

# Install requirements
echo "📦 Installing Python dependencies..."
if command -v uv &> /dev/null; then
    echo "Using uv package manager..."
    uv add gdown
else
    echo "Using pip..."
    pip install --user gdown
fi

# Make download script executable
chmod +x download_knowledge.py

echo "✅ Setup completed!"
echo ""
echo "📋 Usage:"
echo "  ./download_knowledge.py           # Download all files"
echo "  ./download_knowledge.py --clean   # Clean download and re-download"
echo "  ./download_knowledge.py --list    # List downloaded contents"
echo ""
echo "📁 Files will be downloaded to: knowledge/downloaded/"