import gspread
from oauth2client.service_account import ServiceAccountCredentials
from Gerador_de_Tokens import final_token, data, generate_token

sheets_key = '1AILnoafVDq7NMJXLIFPiiv7Yx0zVHRpr8m1sODTQhlY'
 
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("Tokens_Credential.json", scope)
authorization = gspread.authorize(creds)
spreadsheet_url = "https://docs.google.com/spreadsheets/d/" + sheets_key + "/edit#gid=0"
spreadsheet = authorization.open_by_url(spreadsheet_url)

first_page = spreadsheet.worksheet("Página1")
dados_da_planilha = first_page.get_all_values()
repetition = False

for dados  in dados_da_planilha:
    if final_token in dados:
        repetition = True
        break

if repetition == False:
    first_page.append_row([data, final_token])
else:
    other_token = generate_token()
    while other_token in dados_da_planilha:
        other_token = generate_token()
    first_page.append_row([data, other_token])