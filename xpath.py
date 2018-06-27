JOBTITLE = "//a[contains(@data-tn-element, 'jobTitle')]/@title"

SUMMARY = "//span[@class='summary']"

JOBLINK = "//a[contains(@data-tn-element, 'jobTitle')]/@href"

COMPANY = "//span[contains(@class, 'company')]"

LOCATION = "//span[@class='location']/text()"

NEXTPAGE = "//span[@class='np' and contains(text(), 'Next')]/../../@href"

JOBID = "//div[contains(@id, 'p_') or contains(@id, 'pj_')]/@id"
