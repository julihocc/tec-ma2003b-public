# 📚 MA2003B Knowledge Base Download System

Simple system to download and maintain course resources from Google Drive without tracking them in Git.

## 🎯 Quick Start

```bash
# 1. Setup (one-time)
./setup_knowledge.sh

# 2. Download knowledge base
./download_knowledge.py

# 3. List downloaded content
./download_knowledge.py --list
```

## 📁 What Gets Downloaded

This system downloads the contents of:
- **Google Drive Folder**: [MA2003B Knowledge Base](https://drive.google.com/drive/folders/1gTFcVC5-gmfP70kPcfpS629Mm2Z5KT3Q?usp=sharing)
- **Target Location**: `knowledge/downloaded/`
- **Git Status**: 🚫 Excluded from version control (gitignored)

## 🔧 Commands

| Command | Description |
|---------|-------------|
| `./download_knowledge.py` | Download all files from Google Drive |
| `./download_knowledge.py --clean` | Clean download folder and re-download |
| `./download_knowledge.py --list` | Show what's already downloaded |
| `./setup_knowledge.sh` | One-time setup (install dependencies) |

## 📂 Folder Structure

```
ma2003b.worktrees/dev/
├── download_knowledge.py       # Main download script
├── setup_knowledge.sh         # Setup script  
├── knowledge/
│   ├── requirements.txt       # Python dependencies
│   ├── README.md             # Configuration details
│   ├── downloaded/           # 🚫 Downloaded content (gitignored)
│   ├── metadata.json         # 🚫 Download metadata (gitignored)
│   └── download.log          # 🚫 Download logs (gitignored)
└── .gitignore               # Updated to exclude knowledge content
```

## 🔄 Workflow Integration

### For Course Development
```bash
# Before starting work - get latest resources
./download_knowledge.py

# Work with materials in knowledge/downloaded/
ls knowledge/downloaded/

# No need to commit - files are gitignored
git status  # Won't show knowledge content
```

### For Team Collaboration
- ✅ Scripts are version controlled
- ✅ Configuration is version controlled  
- 🚫 Downloaded content is NOT version controlled
- 👥 Team members run their own downloads

## 🛠️ Technical Details

- **Technology**: Python 3 + `gdown` library
- **Authentication**: None required (public folder)
- **Updates**: Re-run script to get latest files
- **Storage**: Local only, not synced to cloud
- **Dependencies**: Auto-installed via `gdown`

## 🔍 Troubleshooting

### Download Issues
```bash
# Clean download and retry
./download_knowledge.py --clean

# Check logs
cat knowledge/download.log
```

### Permission Issues
```bash
# Ensure scripts are executable
chmod +x download_knowledge.py
chmod +x setup_knowledge.sh
```

### Missing Dependencies
```bash
# Reinstall requirements
pip install -r knowledge/requirements.txt
```

## 🔐 Privacy & Security

- ✅ Only downloads public/shared Google Drive content
- ✅ No authentication or personal data required
- ✅ Local storage only (no cloud sync)
- ✅ Downloads respect original file permissions
- ❌ No sensitive data is tracked in Git

---

**Need to update the Google Drive folder?** Edit the `folder_id` in `download_knowledge.py`