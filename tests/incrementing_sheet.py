from test_src.funcs.funcs import integrating_google_spreadsheet

with open('tests\test_src\files\line_transations.txt', 'r') as file:
    line_transations = int(file.read())

#NOTE - Google Sheet Interactions
sheet_resume = integrating_google_spreadsheet(sheet_id="Resumo")
sheet_transations = integrating_google_spreadsheet(sheet_id="Transações")
linha_planilha = 33
sheet_resume.update_cell(linha_planilha, 5, "=SE(ÉCÉL.VAZIA($B33); ""; SOMASE('Transações'!$E$"+line_transations+":$E;$B33;'Transações'!$C"+line_transations+":$C))")