from scrapy.cmdline import execute
import search_terms
from more_itertools import unique_everseen
from hunterio_db import read_existing_companies
import csv
import os
from scalesharkSpider import settings
import constants

out_path = "indeed_jobs.csv"

if settings.CATEGORY is constants.SOFTWARE_DEVELOPMENT:
    search_terms.generate_urls(search_terms.software_development_job_titles)
elif settings.CATEGORY is constants.ELECTRICAL_ENGINEERING:
    search_terms.generate_urls(search_terms.electrical_engineering_job_titles)
elif settings.CATEGORY is constants.IT_OPERATIONS:
    search_terms.generate_urls(search_terms.it_operaions_job_titles)
elif settings.CATEGORY is constants.INFORMATION_DESIGN_AND_DOCUMENTATION:
    search_terms.generate_urls(search_terms.project_management_job_titles)

execute(['scrapy', 'crawl', 'indeedSpider'])

with open("middleware1.csv", "r") as f, open("middleware2.csv", "w") as out_file:
    out_file.writelines(unique_everseen(f))

existing_companies = read_existing_companies("emails_searched_by_domain.csv")
existing_companies |= read_existing_companies("SF_startups.csv")

with open("middleware2.csv") as f:
    reader = csv.DictReader(f)

    exists = False
    if os.path.isfile(out_path):
        exists = True

    with open(out_path, "a+") as f1:
        fieldnames = ['job_id', 'job_title', 'company', 'location', 'summary', 'job_link', 'company_link', 'desired_experience', 'fetched_by_hunterio?']
        writer = csv.DictWriter(f1, fieldnames=fieldnames)
        if exists:
            os.system("echo '\n' >> " + out_path)
        else:
            writer.writeheader()

        for row in reader:
            if row["company"] in existing_companies:
                row["fetched_by_hunterio?"] = "Yes"
            else:
                row["fetched_by_hunterio?"] = "No"
            writer.writerow(row)

os.remove("middleware1.csv")
os.remove("middleware2.csv")