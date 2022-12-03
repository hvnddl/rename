import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "7433052")

API_HASH = os.environ.get("API_HASH", "1b2bccffd1fd3570a39a8bcf7581f28b")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5739102683:AAEI9_lj9jubKUB7-7fDXoqfLkgt6P96MJ8") 

FORCE_SUB = os.environ.get("FORCE_SUB", "") 

DB_NAME = os.environ.get("DB_NAME","Cluster0")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://jeekay:jeekay@cluster0.k2qeph0.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/ac7ef3dc07bba55164484.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '890230886').split()]

PORT = os.environ.get("PORT", "8080")
