# LLM SBOM Generator

This tool uses Google's Gemini AI model to analyze repository contents and generate a Software Bill of Materials (SBOM) listing tools, packages, Docker images, and other components with their versions.

## Prerequisites

- Python 3.6 or higher
- Google Gemini API key
- `repomix-output.txt` file (generated repository content)

## Setup

1. **Create and activate virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install required dependencies:**
   ```bash
   pip install google-generativeai
   ```

3. **Set your Gemini API key:**
   ```bash
   export GEMINI_API_KEY="your-api-key-here"
   ```

4. **Ensure you have the input file:**
   - The script expects a file named `repomix-output.txt` in the same directory
   - This file should contain the merged repository contents

## Usage

Run the script (with venv activated):
```bash
python llm_check.py
```

## What it does

1. **Reads** the `repomix-output.txt` file containing repository contents
2. **Sends** the content to Google's Gemini 1.5 Flash model for analysis
3. **Generates** a table of components with their versions/tags
4. **Saves** the output to `version.txt`

## Output

The script generates a `version.txt` file containing a table with:
- **Type**: The category of component (e.g., Tool, Package, Docker Image)
- **Name**: The name of the component
- **Version/Tag**: The version or tag information

## Configuration

You can modify the following in the script:
- **Model**: Change `gemini-1.5-flash` to another Gemini model
- **Output file**: Change `version.txt` to a different filename

## Error Handling

The script will exit with an error message if:
- Gemini API key is not set
- `repomix-output.txt` file doesn't exist
- API request fails (including quota exceeded, rate limits, or network issues)

## Example Output Format

```
Type | Name | Version/Tag
-----|------|------------
Tool | kubectl | v1.30.0
Package | golang | 1.21
Docker Image | nginx | latest
Helm Chart | reloader | v2.1.4
```