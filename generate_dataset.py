import pandas as pd
import random

# -----------------------------
# CONFIGURATION
# -----------------------------

NUM_ROWS = 500

categories = {
    "Tech": [
        "Software Engineer", "Data Analyst", "AI Engineer", "Cybersecurity Analyst",
        "Cloud Engineer", "DevOps Engineer", "Full Stack Developer",
        "Blockchain Developer", "UI/UX Designer", "Mobile App Developer"
    ],
    "Core Engineering": [
        "Mechanical Design Engineer", "Civil Site Engineer", "Electrical Engineer",
        "Embedded Systems Engineer", "Automobile Engineer",
        "Production Engineer", "Structural Engineer",
        "Robotics Engineer", "Instrumentation Engineer", "Quality Control Engineer"
    ],
    "Government & Public Services": [
        "IAS Officer", "IPS Officer", "Bank PO", "SSC Officer",
        "Railway Officer", "Income Tax Officer",
        "Public Sector Engineer", "State PSC Officer",
        "Customs Officer", "Audit Officer"
    ],
    "Management & Business": [
        "Business Analyst", "Marketing Manager", "HR Manager",
        "Product Manager", "Operations Manager",
        "Supply Chain Manager", "Sales Manager",
        "Strategy Consultant", "Project Manager", "Brand Manager"
    ],
    "Finance & Commerce": [
        "Financial Analyst", "Chartered Accountant", "Investment Banker",
        "Tax Consultant", "Equity Research Analyst",
        "Risk Analyst", "Accountant", "Auditor",
        "Wealth Manager", "Credit Analyst"
    ],
    "Healthcare & Life Sciences": [
        "Doctor", "Pharmacist", "Clinical Researcher",
        "Biotechnologist", "Microbiologist",
        "Physiotherapist", "Nurse", "Medical Lab Technologist",
        "Public Health Officer", "Genetic Counselor"
    ],
    "Creative & Design": [
        "Graphic Designer", "Content Writer", "Digital Marketer",
        "Video Editor", "Animator",
        "Fashion Designer", "Interior Designer",
        "Journalist", "Public Relations Officer", "Media Planner"
    ],
    "Education & Research": [
        "Professor", "Lecturer", "Research Scientist",
        "PhD Scholar", "Education Consultant",
        "Curriculum Developer", "Academic Coordinator",
        "Lab Researcher", "Policy Researcher", "Training Specialist"
    ],
    "Defense & Armed Forces": [
        "Army Officer", "Navy Officer", "Air Force Officer",
        "Defense Engineer", "Coast Guard Officer",
        "Intelligence Officer", "Technical Entry Officer",
        "Defense Analyst", "Paramilitary Officer", "Security Officer"
    ],
    "Higher Studies": [
        "MBA", "M.Tech", "MS in Data Science",
        "MS in Computer Science", "MS in Mechanical Engineering",
        "PhD in Engineering", "PhD in Sciences",
        "Masters in Finance", "Masters in Public Policy", "Masters in Healthcare"
    ]
}

degrees = [
    "B.Tech", "B.E", "B.Sc", "B.Com", "BBA", "BA",
    "MBBS", "BCA", "Diploma", "Any Degree"
]

india_companies = [
    "TCS", "Infosys", "Wipro", "HCL", "Accenture India",
    "Reliance", "L&T", "ICICI Bank", "SBI", "DRDO"
]

abroad_companies = [
    "Google", "Microsoft", "Amazon", "Meta",
    "Tesla", "JP Morgan", "Goldman Sachs",
    "Siemens", "Pfizer", "NASA"
]

india_exams = ["GATE", "CAT", "UPSC", "SSC", "IBPS", "State PSC"]
abroad_exams = ["GRE", "GMAT", "TOEFL", "IELTS"]

platforms = ["Coursera", "Udemy", "edX", "NPTEL", "LinkedIn Learning"]

skill_pool = {
    "Tech": ["python", "java", "sql", "machine learning", "cloud", "docker", "git", "data structures"],
    "Core Engineering": ["autocad", "solidworks", "matlab", "circuit design", "thermodynamics", "mechanics"],
    "Government & Public Services": ["polity", "history", "economics", "aptitude", "current affairs"],
    "Management & Business": ["communication", "analytics", "strategy", "leadership", "excel"],
    "Finance & Commerce": ["accounting", "financial modeling", "taxation", "risk analysis", "investment analysis"],
    "Healthcare & Life Sciences": ["biology", "clinical knowledge", "research methods", "diagnostics"],
    "Creative & Design": ["creativity", "photoshop", "writing", "video editing", "branding"],
    "Education & Research": ["research", "teaching", "data analysis", "publication writing"],
    "Defense & Armed Forces": ["physical fitness", "discipline", "strategy", "technical knowledge"],
    "Higher Studies": ["research", "advanced concepts", "critical thinking"]
}

# -----------------------------
# DATA GENERATION
# -----------------------------

rows = []

base_careers = []
for category, career_list in categories.items():
    for career in career_list:
        base_careers.append((career, category))

for _ in range(NUM_ROWS):
    career, category = random.choice(base_careers)

    region = random.choice(["India", "Abroad"])
    degree = random.choice(degrees)

    skills = ", ".join(random.sample(skill_pool[category],
                                      min(4, len(skill_pool[category]))))

    if region == "India":
        companies = ", ".join(random.sample(india_companies, 3))
        exams = ", ".join(random.sample(india_exams, 2))
    else:
        companies = ", ".join(random.sample(abroad_companies, 3))
        exams = ", ".join(random.sample(abroad_exams, 2))

    platform = ", ".join(random.sample(platforms, 2))

    rows.append([
        career, category, degree, region,
        skills, companies, exams, platform
    ])

# -----------------------------
# CREATE DATAFRAME
# -----------------------------

df = pd.DataFrame(rows, columns=[
    "Career", "Category", "Degree", "Region",
    "Required_Skills", "Companies", "Exams", "Platforms"
])

df.to_excel("careers_dataset.xlsx", index=False)

print("✅ 500-row careers_dataset.xlsx generated successfully!")
