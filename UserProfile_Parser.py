#pip install -r requirements.txt
from bs4 import BeautifulSoup
import os
import csv

def extract_portfolio(soup):
    tag = soup.find(
        lambda t: t.name in ("a","button")
                 and "view my portfolio" in t.get_text(strip=True).lower()
    )
    if tag and tag.has_attr("href"):
        return tag["href"], 1
    return "", 0

def extract_volunteering(soup):
    volunteers = []

    anchor = soup.find("div", {"id": "volunteering_experience"})
    section = anchor.find_parent("section") if anchor else None

    if not section:
        return [], 0

    items = section.find_all("li", class_="artdeco-list__item")

    for item in items:
        title_span = item.find("span", {"class": "visually-hidden"})
        if title_span:
            text = title_span.get_text(strip=True)
            if text:
                volunteers.append(text)

    return volunteers, 1


def extract_connections(soup):
    """
    Return the raw connection count from the <span class="t-bold"> inside
    the 'connections' element. E.g. '500+' → '500+', '1,234' → '1,234'.
    """
    for bold in soup.select("span.t-bold"):
        parent_text = bold.find_parent().get_text(strip=True).lower()
        if "connection" in parent_text:
            return bold.get_text(strip=True)
    return ""

def extract_skill_categories(soup):
    result = {}

    # Step 1: Select all skill category buttons (tabs)
    category_buttons = soup.select('div.pvs-tab__pill-choices button[role="radio"]')
    category_names = [btn.get_text(strip=True) for btn in category_buttons]

    # Step 2: Match each tab to a corresponding content panel
    tab_panels = soup.select('div[role="tabpanel"]')

    # Step 3: Map category name to list of skills
    for name, panel in zip(category_names, tab_panels):
        skills = []

        # Select each skill container (based on LinkedIn's HTML structure)
        skill_containers = panel.select('div.hoverable-link-text.t-bold')

        for container in skill_containers:
            span = container.find("span", attrs={"aria-hidden": "true"})
            if span:
                text = span.get_text(strip=True)
                if text:
                    skills.append(text)

        result[name] = list(dict.fromkeys(skills))
    return result

HOME_FOLDER = "profiles_home"
SKILLS_FOLDER = "profiles_skills"
OUTPUT_FOLDER = "csv_output"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)
OUTPUT_CSV = os.path.join(OUTPUT_FOLDER, "output_single.csv")

# === Folder configuration ===
home_files = [f for f in os.listdir(HOME_FOLDER) if f.endswith(".html")]
skill_files = [f for f in os.listdir(SKILLS_FOLDER) if f.endswith(".html")]

if not home_files or not skill_files:
    print("❌ No HTML files found. Please check folder contents.")
    exit()

home_path = os.path.join(HOME_FOLDER, home_files[0])
skill_path = os.path.join(SKILLS_FOLDER, skill_files[0])

# === Parse homepage HTML ===
with open(home_path, "r", encoding="utf-8") as f:
    home_soup = BeautifulSoup(f, "html.parser")

port_url, port_flag     = extract_portfolio(home_soup)
volunteer_pos, vol_flag = extract_volunteering(home_soup)
conn_str                = extract_connections(home_soup)

# === Parse skills HTML ===
with open(skill_path, "r", encoding="utf-8") as f:
    skill_soup = BeautifulSoup(f, "html.parser")

skills_map = extract_skill_categories(skill_soup)
all_skills = list(dict.fromkeys(skills_map.get("All", [])))
skills_str = "[" + ", ".join(all_skills) + "]" if all_skills else ""

# === Output results to CSV ===
with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=[
        "filename",
        "Portfolio presence",
        "Portfolio url",
        "Volunteer section presence",
        "Volunteer position",
        "Skills",
        "Number of Connections (continuous)"
    ])
    writer.writeheader()
    writer.writerow({
        "filename": os.path.basename(home_path),
        "Portfolio presence": port_flag,
        "Portfolio url": port_url,
        "Volunteer section presence": vol_flag,
        "Volunteer position": volunteer_pos,
        "Skills": skills_str,
        "Number of Connections (continuous)": conn_str
    })

print(f"✅ Exported to: {OUTPUT_CSV}")