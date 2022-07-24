#!/usr/bin/env python
# coding: utf-8

# # The data of different cars are given with different specification.We are going to analyze using the pandas framework.
import pandas as pd
car=pd.read_csv("Cars Data1.csv")
car
'''Make	Model	Type	Origin	DriveTrain	MSRP	Invoice	EngineSize	Cylinders	Horsepower	MPG_City	MPG_Highway	Weight	Wheelbase	Length
0	Acura	MDX	SUV	Asia	All	$36,945	$33,337	3.5	6.0	265.0	17.0	23.0	4451.0	106.0	189.0
1	Acura	RSX Type S 2dr	Sedan	Asia	Front	$23,820	$21,761	2.0	4.0	200.0	24.0	31.0	2778.0	101.0	172.0
2	Acura	TSX 4dr	Sedan	Asia	Front	$26,990	$24,647	2.4	4.0	200.0	22.0	29.0	3230.0	105.0	183.0
3	Acura	TL 4dr	Sedan	Asia	Front	$33,195	$30,299	3.2	6.0	270.0	20.0	28.0	3575.0	108.0	186.0
4	Acura	3.5 RL 4dr	Sedan	Asia	Front	$43,755	$39,014	3.5	6.0	225.0	18.0	24.0	3880.0	115.0	197.0
...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
427	Volvo	C70 LPT convertible 2dr	Sedan	Europe	Front	$40,565	$38,203	2.4	5.0	197.0	21.0	28.0	3450.0	105.0	186.0
428	Volvo	C70 HPT convertible 2dr	Sedan	Europe	Front	$42,565	$40,083	2.3	5.0	242.0	20.0	26.0	3450.0	105.0	186.0
429	Volvo	S80 T6 4dr	Sedan	Europe	Front	$45,210	$42,573	2.9	6.0	268.0	19.0	26.0	3653.0	110.0	190.0
430	Volvo	V40	Wagon	Europe	Front	$26,135	$24,641	1.9	4.0	170.0	22.0	29.0	2822.0	101.0	180.0
431	Volvo	XC70	Wagon	Europe	All	$35,145	$33,112	2.5	5.0	208.0	20.0	27.0	3823.0	109.0	186.0
432 rows × 15 columns'''

car.head()

'''Make	Model	Type	Origin	DriveTrain	MSRP	Invoice	EngineSize	Cylinders	Horsepower	MPG_City	MPG_Highway	Weight	Wheelbase	Length
0	Acura	MDX	SUV	Asia	All	$36,945	$33,337	3.5	6.0	265.0	17.0	23.0	4451.0	106.0	189.0
1	Acura	RSX Type S 2dr	Sedan	Asia	Front	$23,820	$21,761	2.0	4.0	200.0	24.0	31.0	2778.0	101.0	172.0
2	Acura	TSX 4dr	Sedan	Asia	Front	$26,990	$24,647	2.4	4.0	200.0	22.0	29.0	3230.0	105.0	183.0
3	Acura	TL 4dr	Sedan	Asia	Front	$33,195	$30,299	3.2	6.0	270.0	20.0	28.0	3575.0	108.0	186.0
4	Acura	3.5 RL 4dr	Sedan	Asia	Front	$43,755	$39,014	3.5	6.0	225.0	18.0	24.0	3880.0	115.0	197.0'''

car.index
'''RangeIndex(start=0, stop=432, step=1)'''

car.shape

'''(432, 15)'''


car.columns

'''Index(['Make', 'Model', 'Type', 'Origin', 'DriveTrain', 'MSRP', 'Invoice',
       'EngineSize', 'Cylinders', 'Horsepower', 'MPG_City', 'MPG_Highway',
       'Weight', 'Wheelbase', 'Length'],
      dtype='object')'''

car.nunique()
'''Make            38
Model          425
Type             6
Origin           3
DriveTrain       3
MSRP           410
Invoice        425
EngineSize      43
Cylinders        7
Horsepower     110
MPG_City        28
MPG_Highway     33
Weight         348
Wheelbase       40
Length          67
dtype: int64'''


car['Make'].value_counts()

'''Toyota           28
Chevrolet        27
Mercedes-Benz    26
Ford             23
BMW              20
Audi             19
Nissan           17
Honda            17
Chrysler         15
Volkswagen       15
Dodge            13
Mitsubishi       13
Jaguar           12
Volvo            12
Hyundai          12
Subaru           11
Lexus            11
Pontiac          11
Kia              11
Mazda            11
Buick             9
Mercury           9
Lincoln           9
Saturn            8
Cadillac          8
Infiniti          8
GMC               8
Suzuki            8
Porsche           7
Acura             7
Saab              7
Land Rover        3
Oldsmobile        3
Jeep              3
Isuzu             2
MINI              2
Scion             2
Hummer            1
Name: Make, dtype: int64'''



# **Find the null value in dataset.If there are any null value in the column, then fill with the mean value of that column.**

car.isnull().sum()

'''Make           4
Model          4
Type           4
Origin         4
DriveTrain     4
MSRP           4
Invoice        4
EngineSize     4
Cylinders      0
Horsepower     4
MPG_City       4
MPG_Highway    4
Weight         4
Wheelbase      4
Length         4
dtype: int64'''

car['Cylinders'].fillna(car['Cylinders'].mean())

'''0      6.0
1      4.0
2      4.0
3      6.0
4      6.0
      ... 
427    5.0
428    5.0
429    6.0
430    4.0
431    5.0
Name: Cylinders, Length: 432, dtype: float64'''

car['Weight'].fillna(car['Weight'].mean(),inplace=True)
car.isnull().sum()

'''Make           4
Model          4
Type           4
Origin         4
DriveTrain     4
MSRP           4
Invoice        4
EngineSize     4
Cylinders      0
Horsepower     4
MPG_City       4
MPG_Highway    4
Weight         0
Wheelbase      4
Length         4
dtype: int64'''

# **check what are the different tpes of make are there in our dataset and what is the count(occurrence)of each make in the data.**

car['Make'].value_counts()

'''Toyota           28
Chevrolet        27
Mercedes-Benz    26
Ford             23
BMW              20
Audi             19
Nissan           17
Honda            17
Chrysler         15
Volkswagen       15
Dodge            13
Mitsubishi       13
Jaguar           12
Volvo            12
Hyundai          12
Subaru           11
Lexus            11
Pontiac          11
Kia              11
Mazda            11
Buick             9
Mercury           9
Lincoln           9
Saturn            8
Cadillac          8
Infiniti          8
GMC               8
Suzuki            8
Porsche           7
Acura             7
Saab              7
Land Rover        3
Oldsmobile        3
Jeep              3
Isuzu             2
MINI              2
Scion             2
Hummer            1
Name: Make, dtype: int64'''


car[(car["Origin"]=='Asia')|(car["Origin"]=='Europe')]

'''Make	Model	Type	Origin	DriveTrain	MSRP	Invoice	EngineSize	Cylinders	Horsepower	MPG_City	MPG_Highway	Weight	Wheelbase	Length
0	Acura	MDX	SUV	Asia	All	$36,945	$33,337	3.5	6.0	265.0	17.0	23.0	4451.0	106.0	189.0
1	Acura	RSX Type S 2dr	Sedan	Asia	Front	$23,820	$21,761	2.0	4.0	200.0	24.0	31.0	2778.0	101.0	172.0
2	Acura	TSX 4dr	Sedan	Asia	Front	$26,990	$24,647	2.4	4.0	200.0	22.0	29.0	3230.0	105.0	183.0
3	Acura	TL 4dr	Sedan	Asia	Front	$33,195	$30,299	3.2	6.0	270.0	20.0	28.0	3575.0	108.0	186.0
4	Acura	3.5 RL 4dr	Sedan	Asia	Front	$43,755	$39,014	3.5	6.0	225.0	18.0	24.0	3880.0	115.0	197.0
...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
427	Volvo	C70 LPT convertible 2dr	Sedan	Europe	Front	$40,565	$38,203	2.4	5.0	197.0	21.0	28.0	3450.0	105.0	186.0
428	Volvo	C70 HPT convertible 2dr	Sedan	Europe	Front	$42,565	$40,083	2.3	5.0	242.0	20.0	26.0	3450.0	105.0	186.0
429	Volvo	S80 T6 4dr	Sedan	Europe	Front	$45,210	$42,573	2.9	6.0	268.0	19.0	26.0	3653.0	110.0	190.0
430	Volvo	V40	Wagon	Europe	Front	$26,135	$24,641	1.9	4.0	170.0	22.0	29.0	2822.0	101.0	180.0
431	Volvo	XC70	Wagon	Europe	All	$35,145	$33,112	2.5	5.0	208.0	20.0	27.0	3823.0	109.0	186.0
281 rows × 15 columns'''

# **show all the records where origin is Asia or Europe**

car[car['Origin'].isin(['Asia','Europe'])]
'''	Make	Model	Type	Origin	DriveTrain	MSRP	Invoice	EngineSize	Cylinders	Horsepower	MPG_City	MPG_Highway	Weight	Wheelbase	Length
1	Acura	RSX Type S 2dr	Sedan	Asia	Front	$23,820	$21,761	2.0	4.0	200.0	24.0	31.0	2778.0	101.0	172.0
2	Acura	TSX 4dr	Sedan	Asia	Front	$26,990	$24,647	2.4	4.0	200.0	22.0	29.0	3230.0	105.0	183.0
3	Acura	TL 4dr	Sedan	Asia	Front	$33,195	$30,299	3.2	6.0	270.0	20.0	28.0	3575.0	108.0	186.0
4	Acura	3.5 RL 4dr	Sedan	Asia	Front	$43,755	$39,014	3.5	6.0	225.0	18.0	24.0	3880.0	115.0	197.0
5	Acura	3.5 RL w/Navigation 4dr	Sedan	Asia	Front	$46,100	$41,100	3.5	6.0	225.0	18.0	24.0	3893.0	115.0	197.0
...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
427	Volvo	C70 LPT convertible 2dr	Sedan	Europe	Front	$40,565	$38,203	2.4	5.0	197.0	21.0	28.0	3450.0	105.0	186.0
428	Volvo	C70 HPT convertible 2dr	Sedan	Europe	Front	$42,565	$40,083	2.3	5.0	242.0	20.0	26.0	3450.0	105.0	186.0
429	Volvo	S80 T6 4dr	Sedan	Europe	Front	$45,210	$42,573	2.9	6.0	268.0	19.0	26.0	3653.0	110.0	190.0
430	Volvo	V40	Wagon	Europe	Front	$26,135	$24,641	1.9	4.0	170.0	22.0	29.0	2822.0	101.0	180.0
431	Volvo	XC70	Wagon	Europe	All	$35,145	$33,112	2.5	5.0	208.0	20.0	27.0	3823.0	109.0	186.0
329 rows × 15 columns'''

# Remove all the records(rows) where weight is above 4000

car[~(car['Weight']>4000)]

'''Make	Model	Type	Origin	DriveTrain	MSRP	Invoice	EngineSize	Cylinders	Horsepower	MPG_City	MPG_Highway	Weight	Wheelbase	Length
1	Acura	RSX Type S 2dr	Sedan	Asia	Front	$23,820	$21,761	2.0	4.0	200.0	24.0	31.0	2778.0	101.0	172.0
2	Acura	TSX 4dr	Sedan	Asia	Front	$26,990	$24,647	2.4	4.0	200.0	22.0	29.0	3230.0	105.0	183.0
3	Acura	TL 4dr	Sedan	Asia	Front	$33,195	$30,299	3.2	6.0	270.0	20.0	28.0	3575.0	108.0	186.0
4	Acura	3.5 RL 4dr	Sedan	Asia	Front	$43,755	$39,014	3.5	6.0	225.0	18.0	24.0	3880.0	115.0	197.0
5	Acura	3.5 RL w/Navigation 4dr	Sedan	Asia	Front	$46,100	$41,100	3.5	6.0	225.0	18.0	24.0	3893.0	115.0	197.0
...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
427	Volvo	C70 LPT convertible 2dr	Sedan	Europe	Front	$40,565	$38,203	2.4	5.0	197.0	21.0	28.0	3450.0	105.0	186.0
428	Volvo	C70 HPT convertible 2dr	Sedan	Europe	Front	$42,565	$40,083	2.3	5.0	242.0	20.0	26.0	3450.0	105.0	186.0
429	Volvo	S80 T6 4dr	Sedan	Europe	Front	$45,210	$42,573	2.9	6.0	268.0	19.0	26.0	3653.0	110.0	190.0
430	Volvo	V40	Wagon	Europe	Front	$26,135	$24,641	1.9	4.0	170.0	22.0	29.0	2822.0	101.0	180.0
431	Volvo	XC70	Wagon	Europe	All	$35,145	$33,112	2.5	5.0	208.0	20.0	27.0	3823.0	109.0	186.0
329 rows × 15 columns'''


# **Increase all the values of 'MPG_City' column by 3**


car['MPG_City']=car['MPG_City'].apply(lambda x:x+3)
car['MPG_City']
'''0      20.0
1      27.0
2      25.0
3      23.0
4      21.0
       ... 
427    24.0
428    23.0
429    22.0
430    25.0
431    23.0
Name: MPG_City, Length: 432, dtype: float64'''
