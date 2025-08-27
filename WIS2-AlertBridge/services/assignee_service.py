import csv
import datetime
import logging

ASSIGNEES_BY_ISO2 = {}
ASSIGNEES_ROTATION = [
    {"accountId": "5ba3e055-e2c8-4d74-8b59-99cfae6f2107", "email": "transmet@meteo.fr"},                    # Toulouse
    {"accountId": "3a567fa5-5df1-4264-a1d8-dca516c577f5", "email": "gisc-beijing-ims@cma.gov.cn"},          # Beijing
    {"accountId": "6ee7e53f-4811-4ea0-830a-4ec2847a1017", "email": "gisc-casablanca@marocmeteo.ma"},        # Casablanca
    {"accountId": "2eae5820-2244-473b-a51b-61234b2dd433", "email": "gisc-support@weathersa.co.za"},         # Pretoria
    {"accountId": "6bcd27b6-6403-462f-87a0-4fa64cbcad63", "email": "wis-jma@met.kishou.go.jp"},             # Tokyo
    {"accountId": "40d4f6ba-9751-4bc6-82f6-5dc79673de77", "email": "nim@metoffice.gov.uk"},                 # Exeter
    {"accountId": "3bd19e33-804e-4acc-bcf0-966d4cad68f6", "email": "gisc_op@korea.kr"},                     # Seoul
    {"accountId": "36d3f1db-5b27-40ab-a94b-867fd63035c0", "email": "srcs_all@bom.gov.au"},                  # Melbourne
    {"accountId": "af21d0dc-b0a6-4f85-866e-b9a561003903", "email": "met.servicedesk@dwd.de"},               # Offenbach
    {"accountId": "8a76f9e8-59b6-4a48-9a94-83db603d20ab", "email": "wis2.oper@inmet.gov.br"},               # Brasilia
    {"accountId": "712bbfbb-d8b7-4e3a-b36d-17e077f92783", "email": "gisc.delhi@imd.gov.in"},                # New Delhi
    {"accountId": "3edcada0-7ebc-4476-bbfa-d5aedad2996d", "email": "nws.gisc.washington.support@noaa.gov"}, # Washington
    {"accountId": "0d8650c1-b4ff-46cc-b691-6521fb17b3f1", "email": "wisop@ncm.gov.sa"},                     # Jeddah
    {"accountId": "e93af777-469f-4e88-8716-32135b00db68", "email": "wisop@avia.mecom.ru"},                  # Moscow
    {"accountId": "bd0458b6-8093-47a2-b9a5-e9a155cd3967", "email": "wis2operat@irimo.ir"},                  # Tehran
]

def load_assignees_from_csv(csv_path="config/assignees.csv"):
    global ASSIGNEES_BY_ISO2
    try:
        with open(csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                iso2 = row['iso2'].strip().lower()
                ASSIGNEES_BY_ISO2[iso2] = row['accountId'].strip()
    except Exception as e:
        logging.error(f"Erreur chargement CSV : {e}")

def get_current_assignee():
    base_date = datetime.date(2025, 4, 1)
    today = datetime.date.today()
    days_diff = (today - base_date).days
    if days_diff < 0:
        logging.warning("Date before rotation start")
        return None
    index = (days_diff // 15) % len(ASSIGNEES_ROTATION)
    return ASSIGNEES_ROTATION[index]

def get_assignee_from_centre(centre_id):
    if not centre_id or len(centre_id) < 2:
        return None
    if centre_id.lower() == "ca-eccc-msc-global-discovery-catalogue":
        return "ba802b36-b516-46f1-8277-30fa3a5eb8b3"
    iso2 = centre_id[:2].lower()
    return ASSIGNEES_BY_ISO2.get(iso2)
