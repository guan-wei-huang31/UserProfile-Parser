### **LinkedIn Profile Data Extractor - Project README**
Note: This project is intended for academic use only.

## **Project Overview**

The LinkedIn Profile Data Extractor is a Python-based automation tool designed to efficiently parse LinkedIn profile HTML files, extracting key information including portfolio URLs, volunteer experiences, skill categories, and connection counts. The extracted data is saved in a structured CSV format for further analysis.

## **Key Features**

* **Automated Data Extraction:** Parses LinkedIn profile HTML files to capture:

  * Portfolio URLs and presence.
  * Volunteer experience details.
  * Connection counts (raw count).
  * Skill categories and listed skills.
* **Efficient Workflow:** Supports batch processing of multiple LinkedIn profiles.
* **Structured Output:** Generates a CSV file with clearly defined columns for each data point.

## **Technologies Used**

* **Programming Language:** Python (3.x)
* **Libraries:**

  * BeautifulSoup (HTML Parsing)
  * OS (File Management)
  * CSV (Data Storage)
* **Modules:**

  * `extract_portfolio()`: Identifies and captures portfolio URLs.
  * `extract_volunteering()`: Extracts volunteer experience details.
  * `extract_connections()`: Retrieves the connection count.
  * `extract_skill_categories()`: Extracts skills under categorized sections.

## **Installation and Setup**

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/LinkedIn-Profile-Data-Extractor.git
   ```

2. **Set Up a Python Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Required Libraries:**

   ```bash
   pip install -r requirements.txt
   ```

## **Usage Instructions**

1. Place your LinkedIn profile HTML files in the `profiles_home/` directory.
2. Place LinkedIn skills HTML files in the `profiles_skills/` directory.
3. Run the script:

   ```bash
   python script_name.py
   ```
4. The extracted data will be saved as a CSV file in the `csv_output/` directory.

## **Project Structure**

```
LinkedIn-Profile-Data-Extractor/
├── profiles_home/          # Directory for LinkedIn profile HTML files
├── profiles_skills/        # Directory for LinkedIn skills HTML files
├── csv_output/             # Directory for the generated CSV file
├── script_name.py          # Main script file
├── requirements.txt        # Required libraries
└── README.md               # Project documentation
```

## **CSV Output Example**

| filename      | Portfolio presence | Portfolio URL                              | Volunteer section presence | Volunteer position | Skills            | Number of Connections |
| ------------- | ------------------ | ------------------------------------------ | -------------------------- | ------------------ | ----------------- | --------------------- |
| profile1.html | 1                  | [https://example.com](https://example.com) | 1                          | \[Volunteer Role]  | \[Skill1, Skill2] | 500+                  |

## **Contact**

**Author:** Guan-Wei Huang
**Email:** gwhuang24@gmail.com

## **License**

© 2025 LinkedIn Profile Data Extractor. All rights reserved. Unauthorized use, reproduction, or distribution is prohibited without explicit permission.
