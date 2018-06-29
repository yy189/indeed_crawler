import urllib

base_url = "https://www.indeed.com/jobs"

radius = "25"

keywords = [" \"series a\"", " \"series b\""]

software_development_job_titles = [
    "Software Engineer", "Front End Developer", "Developer", "Full Stack Developer",
    "Quality Assurance Engineer", "Product Manager", "Web Developer", "Software Architect",
    "Application Developer", "Development Operations Engineer", "software developer", "java developer",
    "java", "computer science", "devops engineer",
]

electrical_engineering_job_titles = [
    "Controls Engineer", "Electrical Engineer", "Rf Engineer", "Facilities Engineer",
    "Electronics Engineer", "Senior Electrical Engineer", "Communication Technician",
    "Audio Engineer", "Senior Controls Engineer", "Instrumentation Engineer", "engineer",
    "controls engineer", "rf engineer", "mechanical engineer", "audio engineer",
    "telecommunications", "electrical engineering", "electronics engineer", "electrical",
]

it_operaions_job_titles = [
    "Technical Support", "Help Desk Analyst", "IT Support", "Systems Administrator",
    "IT Technician", "Network Engineer", "Database Administrator", "Computer Technician",
    "Network Administrator", "Data Center Technician", "information technology", "it",
    "help desk", "desktop support", "system administrator", "computer",
]
                                                                      
information_design_and_documentation_job_titles = [
    "Data Analyst", "Business Analyst", "Quality Assurance Analyst", "Operations Analyst",
    "Systems Analyst", "IT Security Specialist", "Business Systems Analyst", "Technical Writer",
    "Information Technology Specialist", "analyst", "cyber security", "qa analyst",
    "sql", "financial analyst",
]

project_management_job_titles = [
    "Project Manager", "Program Manager", "Project Coordinator", "Program Director",
    "Construction Project Manager", "Senior Project Manager", "Project Engineer",
    "Program Analyst", "Associate Project Manager", "Implementation Specialist",
    "construction", "manager", "project management", "it project manager",
]

locations = ["New York, NY", "San Francisco, CA", "Boston, MA", "Washington, DC", "Miami, FL"]

def generate_urls(job_titles_list):
    with open("urls.py", "wb") as f:
        f.write("URLS = [\n")
        for l in locations:
            l = urllib.quote_plus(l)
            for jt in job_titles_list:
                if len(keywords):
                    for kw in keywords:
                        q = urllib.quote_plus(jt + kw)
                        full_url = base_url + "?q=" + q + "&l=" + l + "&radius=" + radius
                        f.write("\t\t\t'" + full_url + "',\n")
                else:
                    q = urllib.quote_plus(jt)
                    full_url = base_url + "?q=" + q + "&l=" + l + "&radius=" + radius
                    f.write("\t\t\t'" + full_url + "',\n")
        f.write("]")
        print("URLs generated!")


if __name__ == "__main__":
    generate_urls(software_development_job_titles)