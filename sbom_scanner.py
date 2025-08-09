#!/usr/bin/env python3
import os
import sys
from pathlib import Path
import google.generativeai as genai

def main():
    # Config
    repo_file = Path("repomix-output.txt")
    output_file = Path("VERSION.md")
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        print("Error: GEMINI_API_KEY environment variable not set.", file=sys.stderr)
        sys.exit(1)

    if not repo_file.exists():
        print(f"Error: {repo_file} does not exist.", file=sys.stderr)
        sys.exit(1)

    # Read repository content
    with open(repo_file, "r", encoding="utf-8") as f:
        repo_content = f.read()

    # Prompt for the LLM
    prompt = """You are a code analysis assistant.
Analyze the following repository contents and extract a list of tools, packages,
docker images, and other components used in the code, including their versions/tags.
Output the result in a table format with columns:

Type | Name | Version/Tag

Do not include any commentary or explanations — only the table.
Repository contents:
""" + repo_content

    # Configure Gemini
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    print("Querying Gemini AI...")
    try:
        response = model.generate_content(prompt)
        result = response.text.strip()
    except Exception as e:
        print(f"Error: Gemini API request failed: {e}", file=sys.stderr)
        sys.exit(1)

    # Save output to version.txt
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(result + "\n")

    print(f"Version list written to {output_file}")

if __name__ == "__main__":
    main()
