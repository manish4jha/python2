Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> f = open('C:\Users\Purushotham\Desktop\oracle\day_03\data.txt', 'r')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> f = open(r'C:\Users\Purushotham\Desktop\oracle\day_03\data.txt', 'r')
>>> type(f)
<class '_io.TextIOWrapper'>
>>> f.read()
'2018,Level 1,99999,All industries,Dollars (millions),H01,Total income,Financial performance,691859,"ANZSIC06 divisions A-S (excluding classes K6330, L6711, O7552, O760, O771, O772, S9540, S9601, S9602, and S9603)"\n2018,Level 1,99999,All industries,Dollars (millions),H04,"Sales, government funding, grants and subsidies",Financial performance,605766,"ANZSIC06 divisions A-S (excluding classes K6330, L6711, O7552, O760, O771, O772, S9540, S9601, S9602, and S9603)"\n2018,Level 1,99999,All industries,Dollars (millions),H05,"Interest, dividends and donations",Financial performance,63509,"ANZSIC06 divisions A-S (excluding classes K6330, L6711, O7552, O760, O771, O772, S9540, S9601, S9602, and S9603)"\n2018,Level 1,99999,All industries,Dollars (millions),H07,Non-operating income,Financial performance,22583,"ANZSIC06 divisions A-S (excluding classes K6330, L6711, O7552, O760, O771, O772, S9540, S9601, S9602, and S9603)"\n2018,Level 1,99999,All industries,Dollars (millions),H08,Total expenditure,Financial performance,597623,"ANZSIC06 divisions A-S (excluding classes K6330, L6711, O7552, O760, O771, O772, S9540, S9601, S9602, and S9603)"\n2018,Level 1,99999,All industries,Dollars (millions),H09,Interest and donations,Financial performance,34223,"ANZSIC06 divisions A-S (excluding classes K6330, L6711, O7552, O760, O771, O772, S9540, S9601, S9602, and S9603)"\n2018,Level 1,99999,All industries,Dollars (millions),H10,Indirect taxes,Financial performance,7124,"ANZSIC06 divisions A-S (excluding classes K6330, L6711, O7552, O760, O771, O772, S9540, S9601, S9602, and S9603)"\n2018,Level 1,99999,All industries,Dollars (millions),H11,Depreciation,Financial performance,19863,"ANZSIC06 divisions A-S (excluding classes K6330, L6711, O7552, O760, O771, O772, S9540, S9601, S9602, and S9603)"\n2018,Level 1,99999,All industries,Dollars (millions),H12,Salaries and wages paid,Financial performance,106351,"ANZSIC06 divisions A-S (excluding classes K6330, L6711, O7552, O760, O771, O772, S9540, S9601, S9602, and S9603)"\n2018,Level 1,99999,All industries,Dollars (millions),H13,Redundancy and severance,Financial performance,297,"ANZSIC06 divisions A-S (excluding classes K6330, L6711, O7552, O760, O771, O772, S9540, S9601, S9602, and S9603)"'
>>> f.readline()
''
>>> f.tell()
2247
>>> f.seek(0)
0
>>> f.readline()
'2018,Level 1,99999,All industries,Dollars (millions),H01,Total income,Financial performance,691859,"ANZSIC06 divisions A-S (excluding classes K6330, L6711, O7552, O760, O771, O772, S9540, S9601, S9602, and S9603)"\n'
>>> f.readline()
'2018,Level 1,99999,All industries,Dollars (millions),H04,"Sales, government funding, grants and subsidies",Financial performance,605766,"ANZSIC06 divisions A-S (excluding classes K6330, L6711, O7552, O760, O771, O772, S9540, S9601, S9602, and S9603)"\n'
>>> f.readline()
'2018,Level 1,99999,All industries,Dollars (millions),H05,"Interest, dividends and donations",Financial performance,63509,"ANZSIC06 divisions A-S (excluding classes K6330, L6711, O7552, O760, O771, O772, S9540, S9601, S9602, and S9603)"\n'
>>> f.seek(0)
0
>>> content = f.readlines()
>>> content
['2018,Level 1,99999,All industries,Dollars (millions),H01,Total income,Financial performance,691859,"ANZSIC06 divisions A-S (excluding classes K6330, L6711, O7552, O760, O771, O772, S9540, S9601, S9602, and S9603)"\n', '2018,Level 1,99999,All industries,Dollars (millions),H04,"Sales, government funding, grants and subsidies",Financial performance,605766,"ANZSIC06 divisions A-S (excluding classes K6330, L6711, O7552, O760, O771, O772, S9540, S9601, S9602, and S9603)"\n', '2018,Level 1,99999,All industries,Dollars (millions),H05,"Interest, dividends and donations",Financial performance,63509,"ANZSIC06 divisions A-S (excluding classes K6330, L6711, O7552, O760, O771, O772, S9540, S9601, S9602, and S9603)"\n', '2018,Level 1,99999,All industries,Dollars (millions),H07,Non-operating income,Financial performance,22583,"ANZSIC06 divisions A-S (excluding classes K6330, L6711, O7552, O760, O771, O772, S9540, S9601, S9602, and S9603)"\n', '2018,Level 1,99999,All industries,Dollars (millions),H08,Total expenditure,Financial performance,597623,"ANZSIC06 divisions A-S (excluding classes K6330, L6711, O7552, O760, O771, O772, S9540, S9601, S9602, and S9603)"\n', '2018,Level 1,99999,All industries,Dollars (millions),H09,Interest and donations,Financial performance,34223,"ANZSIC06 divisions A-S (excluding classes K6330, L6711, O7552, O760, O771, O772, S9540, S9601, S9602, and S9603)"\n', '2018,Level 1,99999,All industries,Dollars (millions),H10,Indirect taxes,Financial performance,7124,"ANZSIC06 divisions A-S (excluding classes K6330, L6711, O7552, O760, O771, O772, S9540, S9601, S9602, and S9603)"\n', '2018,Level 1,99999,All industries,Dollars (millions),H11,Depreciation,Financial performance,19863,"ANZSIC06 divisions A-S (excluding classes K6330, L6711, O7552, O760, O771, O772, S9540, S9601, S9602, and S9603)"\n', '2018,Level 1,99999,All industries,Dollars (millions),H12,Salaries and wages paid,Financial performance,106351,"ANZSIC06 divisions A-S (excluding classes K6330, L6711, O7552, O760, O771, O772, S9540, S9601, S9602, and S9603)"\n', '2018,Level 1,99999,All industries,Dollars (millions),H13,Redundancy and severance,Financial performance,297,"ANZSIC06 divisions A-S (excluding classes K6330, L6711, O7552, O760, O771, O772, S9540, S9601, S9602, and S9603)"']
>>> type(content)
<class 'list'>
>>> content[0]
'2018,Level 1,99999,All industries,Dollars (millions),H01,Total income,Financial performance,691859,"ANZSIC06 divisions A-S (excluding classes K6330, L6711, O7552, O760, O771, O772, S9540, S9601, S9602, and S9603)"\n'
>>> content[1]
'2018,Level 1,99999,All industries,Dollars (millions),H04,"Sales, government funding, grants and subsidies",Financial performance,605766,"ANZSIC06 divisions A-S (excluding classes K6330, L6711, O7552, O760, O771, O772, S9540, S9601, S9602, and S9603)"\n'
>>> content[-1]
'2018,Level 1,99999,All industries,Dollars (millions),H13,Redundancy and severance,Financial performance,297,"ANZSIC06 divisions A-S (excluding classes K6330, L6711, O7552, O760, O771, O772, S9540, S9601, S9602, and S9603)"'
>>> line = content[0]
>>> line
'2018,Level 1,99999,All industries,Dollars (millions),H01,Total income,Financial performance,691859,"ANZSIC06 divisions A-S (excluding classes K6330, L6711, O7552, O760, O771, O772, S9540, S9601, S9602, and S9603)"\n'
>>> cols = line.split(',')
>>> cols
['2018', 'Level 1', '99999', 'All industries', 'Dollars (millions)', 'H01', 'Total income', 'Financial performance', '691859', '"ANZSIC06 divisions A-S (excluding classes K6330', ' L6711', ' O7552', ' O760', ' O771', ' O772', ' S9540', ' S9601', ' S9602', ' and S9603)"\n']
>>> cols.index('H01')
5
>>> cols[5]
'H01'
>>> cols[5]
'H01'
>>> cols[-1]
' and S9603)"\n'
>>> cols[-2]
' S9602'
>>> cols.index('691859')
8
>>> cols[9:]
['"ANZSIC06 divisions A-S (excluding classes K6330', ' L6711', ' O7552', ' O760', ' O771', ' O772', ' S9540', ' S9601', ' S9602', ' and S9603)"\n']
>>> cols[9].split()
['"ANZSIC06', 'divisions', 'A-S', '(excluding', 'classes', 'K6330']
>>> cols[9].split()[-1]
'K6330'
>>> cols[-1].split()
['and', 'S9603)"']
>>> cols[-1].split()[:5]
['and', 'S9603)"']
>>> (cols[-1].split())[-1][:5]
'S9603'
>>> cols[9].split()[-1]
'K6330'
>>> (cols[-1].split())[-1][:5]
'S9603'
>>> data = cols[9].split()[-1]
>>> data = []
>>> data.append(cols[9].split()[-1])
>>> for item from cols[10:-1]:
	
SyntaxError: invalid syntax
>>> for item in cols[10:-1]:
	data.append(item.strip())

	
>>> data.append((cols[-1].split())[-1][:5])
>>> data
['K6330', 'L6711', 'O7552', 'O760', 'O771', 'O772', 'S9540', 'S9601', 'S9602', 'S9603']
>>> # ----- write this data to a file
>>> 
>>> f = open(r"C:\Users\Purushotham\Desktop\oracle\day_03\exclusive_info.txt", "w")
>>> f.write('This is exclusive data from a csv information\n')
46
>>> f.write('-'*100)
100
>>> f.write('\n')
1
>>> f.close()
>>> data
['K6330', 'L6711', 'O7552', 'O760', 'O771', 'O772', 'S9540', 'S9601', 'S9602', 'S9603']
>>> cols[5]
'H01'
>>> content = [str(cols[5]), ' ----> ', str(data), '\n']
>>> content
['H01', ' ----> ', "['K6330', 'L6711', 'O7552', 'O760', 'O771', 'O772', 'S9540', 'S9601', 'S9602', 'S9603']", '\n']
>>> f = open(r"C:\Users\Purushotham\Desktop\oracle\day_03\exclusive_info.txt", "a")
>>> f.write('\n')
1
>>> f.writelines(content)
>>> f.close()
>>> 
