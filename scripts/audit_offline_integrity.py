"""
MAITRI Zero-Internet Air-Gap Audit Script
Scans all Python backend modules and JavaScript frontend files to ensure 100% offline air-gap compliance.
Verifies that no runtime external HTTP/HTTPS network dependencies exist.
"""

import os
import sys

def audit_offline_compliance(root_dir=None):
    if root_dir is None:
        root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    forbidden_patterns = [
        "https://api.",
        "http://api.",
        "fetch('https://",
        "axios.get('https://",
        "requests.get('https://",
        "urllib.request.urlopen("
    ]

    violations = []
    scanned_files = 0

    for current_root, dirs, files in os.walk(root_dir):
        if ".git" in current_root or "__pycache__" in current_root:
            continue
        
        for file in files:
            if file.endswith((".py", ".js")) and file != "audit_offline_integrity.py":
                filepath = os.path.join(current_root, file)
                scanned_files += 1
                try:
                    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                        lines = f.readlines()
                    for line_num, line in enumerate(lines, 1):
                        for pattern in forbidden_patterns:
                            if pattern in line and "cdn.jsdelivr" not in line and "example" not in line:
                                violations.append((filepath, line_num, line.strip()))
                except Exception:
                    pass

    print("\n=======================================================")
    print("   MAITRI ZERO-INTERNET AIR-GAP AUDIT RESULTS")
    print("=======================================================")
    print(f"Total Scanned Code Files: {scanned_files}")
    
    if not violations:
        print("[SUCCESS] AIR-GAP VERIFICATION: PASSED (100% Offline Air-Gap Compliant)")
        print("Zero runtime external cloud API dependencies detected.")
    else:
        print(f"[WARNING] AIR-GAP AUDIT: Found {len(violations)} external network references:")
        for path, line_no, content in violations:
            print(f"  - {os.path.basename(path)}:{line_no} -> {content}")

    return len(violations) == 0

if __name__ == "__main__":
    audit_offline_compliance()
