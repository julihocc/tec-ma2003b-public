#!/usr/bin/env python3
"""
Test All Factor Analysis Snippets
Runs all snippet files and reports their status
"""

import subprocess
import sys
import os
from pathlib import Path

def test_snippet(script_name):
    """Test a single snippet and return success status."""
    try:
        result = subprocess.run(
            [sys.executable, script_name],
            capture_output=True,
            text=True,
            timeout=30
        )

        if result.returncode == 0:
            print(f"✅ {script_name} - SUCCESS")
            if result.stderr and "warning" in result.stderr.lower():
                print(f"   ⚠️  Warnings present but script completed")
            return True
        else:
            print(f"❌ {script_name} - FAILED")
            print(f"   Error: {result.stderr}")
            return False

    except subprocess.TimeoutExpired:
        print(f"⏰ {script_name} - TIMEOUT")
        return False
    except Exception as e:
        print(f"💥 {script_name} - EXCEPTION: {e}")
        return False

def main():
    """Run all snippet tests."""
    print("Testing Factor Analysis Python Snippets")
    print("=" * 50)

    # List of snippet files to test
    snippets = [
        "01_pca_basic_example.py",
        "02_component_retention.py",
        "03_factor_analysis_basic.py",
        "04_factor_rotation.py",
        "05_complete_workflow.py"
    ]

    success_count = 0
    total_count = len(snippets)

    for snippet in snippets:
        if os.path.exists(snippet):
            if test_snippet(snippet):
                success_count += 1
        else:
            print(f"❌ {snippet} - FILE NOT FOUND")

    print("\n" + "=" * 50)
    print(f"Test Results: {success_count}/{total_count} snippets passed")

    if success_count == total_count:
        print("🎉 All snippets are working correctly!")
        return 0
    else:
        print("⚠️  Some snippets have issues. Check output above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())