# Strava Segment Analysis

This project provides tools for analyzing running segments from Strava using the Strava API. It allows you to explore segments around a location, analyze effort and pace, and compare results to world records.

## Features
- Fetch and analyze Strava segments around a given location
- Calculate pace and compare to world record paces
- Handle Strava API rate limits automatically
- Securely manage your Strava API token using a `.env` file

## Usage
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project root and add your Strava API token:
   ```
   STRAVA_ACCESS_TOKEN=your_token_here
   ```
4. Run the main script:
   ```bash
   python main.py
   ```

## Project Structure
- `main.py` – Main entry point for segment analysis
- `strava/` – Strava API client
- `analysis/` – Segment and world record analysis
- `models/` – Data models
- `utils/` – Utility functions for segment exploration

## Security
- **Never commit your `.env` file or API token to GitHub!**
- Add `.env` to your `.gitignore` file.

## Notes
- The Strava API has strict rate limits. The code automatically waits if the limit is reached.
- For large areas, the code splits the search into smaller grid cells to collect more segments.

## Use Case
This project addresses a common issue on Strava: segments often have course records (CRs) that are not humanly possible. These unrealistic records can result from faulty GPS data or incorrect activity type selection (e.g., cycling instead of running).

The tool analyzes all running segments around a given location and checks which segment records (CRs/KOMs) are likely not achievable by a human. It compares the segment pace to world record paces and flags segments with impossible times.

Additionally, the tool sorts the list of segments by the slowest records first. This helps athletes identify which segments are realistically possible to "break" and target for new records.

## License
MIT License
