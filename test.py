import streamlit as st

st.title(':blue[SISTEM PERIODIK UNSUR]')

simbol = ['H','He','Li','Be','B','C','N','O','F','Ne',
           'Na','Mg','Al','Si','P','S','Cl','Ar','K', 'Ca',
           'Sc', 'Ti', 'V','Cr', 'Mn', 'Fe', 'Co', 'Ni',
           'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr',
           'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru',
           'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te',
           'I', 'Xe','Cs', 'Ba','La', 'Ce', 'Pr', 'Nd', 'Pm',
           'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm',
           'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir',
           'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn',
           'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am',
           'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr',
           'Rf', 'Db', 'Sg', 'Bh','Hs', 'Mt', 'Ds', 'Rg', 'Cn',
           'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og']

kata kunci = ['nama','indeks','kategorielemen','golongan','periode','block',
           'massa','Wujud','Kerapatan','Elektronegativitas']

nilai   = [['Wasserstoff',1,'Nichtmetalle',1,1,'s',1.01,'gasförmig',0.08,2.2],#H
          ['Helium',2,'Edelgase',18,1,'s',4.00,'gasförmig',0.18,'n.A'],#He
          ['Lithium',3,'Alkalimetalle',1,2,'s',6.94,'fest',0.53,0.98],#Li
          ['Beryllium',4,'Erdalkalimetalle',2,2,'s',9.01,'fest',1.84,1.57],#Be
          ['Bor',5,'Halbmetalle',13,2,'p',10.81,'fest',2.46,2.04],#B
          ['Kohlenstoff',6,'Nichtmetalle',14,2,'p',12.01,'fest',2.26,2.55],#C
          ['Stickstoff',7,'Nichtmetalle',15,2,'p',14.00,'gasförmig',1.17,3.04],#N
          ['Sauerstoff',8,'Nichtmetalle',16,2,'p',15.99,'gasförmig',1.43,3.44],#O
          ['Fluor',9,'Halogene',17,2,'p',18.99,'gasförmig',1.70,3.98],#F
          ['Neon',10,'Edelgase',18,2,'p',20.17,'gasförmig',0.90,'n.A'],#Ne
      
          ['Natrium',11,'Alkalimetalle',1,3,'s',22.99,'fest',0.97,0.93],#Na
          ['Magnesium',12,'Erdalkalimetalle',2,3,'s',24.31,'fest',1.74,1.31],#Mg
          ['Aluminium',13,'Metalle',13,3,'p',26.98,'fest',2.69,1.61],#Al
          ['Silicium',14,'Halbmetalle',14,3,'p',28.08,'fest',2.34,1.90],#Si
          ['Phosphor',15,'Nichtmetalle',15,3,'p',30.97,'fest',2.4,2.19],#P
          ['Schwefel',16,'Nichtmetalle',16,3,'p',32.06,'fest',2.07,2.58],#S
          ['Chlor',17,'Halogene',17,3,'p',35.45,'gasförmig',3.22,3.16],#Cl
          ['Argon',18,'Edelgase',18,3,'p',39.95,'gasförmig',1.78,'n.A'],#Ar
          ['Kalium',19,'Alkalimetalle',1,4,'s',39.09,'fest',0.86,0.82],#K
          ['Calicium',20,'Erdalkalimetalle',2,4,'s',40.08,'fest',1.55,1.00],#Ca
         
          ['Scandium',21,'Übergangsmetalle',3,4,'d',44.96,'fest',2.99,1.36],#Sc
          ['Titan',22,'Übergangsmetalle',4,4,'d',47.87,'fest',4.5,1.54],#Ti
          ['Vandium',23,'Übergangsmetalle',5,4,'d',50.94,'fest',6.11,1.63],#V
          ['Chrom',24,'Übergangsmetalle',6,4,'d',51.99,'fest',7.14,1.66],#Cr
          ['Mangan',25,'Übergangsmetalle',7,4,'d',54.94,'fest',7.43,1.55],#Mn
          ['Eisen',26,'Übergangsmetalle',8,4,'d',55.85,'fest',7.87,1.83],#Fe
          ['Cobalt',27,'Übergangsmetalle',9,4,'d',58.93,'fest',8.90,1.88],#Co
          ['Nickel',28,'Übergangsmetalle',10,4,'d',58.69,'fest',8.90,1.91],#Ni
       
          ['Kupfer',29,'Übergangsmetalle',11,4,'d',63.54,'fest',8.92,1.90],#Cu
          ['Zink',30,'Übergangsmetalle',12,4,'d',65.38,'fest',7.14,1.65],#Zn
          ['Gallium',31,'Metalle',13,4,'p',69.72,'fest',5.90,1.81],#Ga
          ['Germanium',32,'Halbmetalle',14,4,'p',72.63,'fest',5.32,2.01],#Ge
          ['Arsen',33,'Halbmetalle',15,4,'p',74.92,'fest',5.73,2.18],#As
          ['Selen',34,'Halbmetalle',16,4,'p',78.97,'fest',4.82,2.55],#Se
          ['Brom',35,'Halogene',17,4,'p',79.90,'flüssig',3.12,2.96],#Br
          ['Krypton',36,'Edelgase',18,4,'p',83.80,'gasförmig',3.75,3.00],#Kr
         
          ['Rubidium',37,'Alkalimetalle',1,5,'s',85.47,'fest',1.53,0.82],#Rb
          ['Strontium',38,'Erdalkalimetalle',2,5,'s',87.62,'fest',2.63,0.95],#Sr
          ['Yttrium',39,'Übergangsmetalle',3,5,'d',88.91,'fest',4.47,1.22],#Y
          ['Zirconium',40,'Übergangsmetalle',4,5,'d',91.22,'fest',6.50,1.33],#Zr
          ['Niob',41,'Übergangsmetalle',5,5,'d',92.90,'fest',8.57,1.6],#Nb
          ['Molybdän',42,'Übergangsmetalle',6,5,'d',95.95,'fest',10.28,2.16],#Mo
          ['Technetium',43,'Übergangsmetalle',7,5,'d',98.90,'fest',11.5,1.9],#Tc
          ['Ruthenium',44,'Übergangsmetalle',8,5,'d',101.07,'fest',12.37,2.2],#Ru
         
          ['Rhodium',45,'Übergangsmetalle',9,5,'d',102.90,'fest',12.38,2.28],#Rh
          ['Palladium',46,'Übergangsmetalle',10,5,'d',106.42,'fest',11.99,2.20],#Pd
          ['Silber',47,'Übergangsmetalle',11,5,'d',107.87,'fest',10.49,1.93],#Ag
          ['cadmium',48,'Übergangsmetalle',12,5,'d',112.41,'fest',8.65,1.69],#Cd
          ['Indium',49,'Metalle',13,5,'p',114.82,'fest',7.31,1.78],#In
          ['Zinn',50,'Metalle',14,5,'p',118.71,'fest',5.77,1.96],#Sn
          ['Antimon',51,'Halbmetalle',15,5,'p',121.76,'fest',6.70,2.05],#Sb
          ['Tellur',52,'Halbmetalle',16,5,'p',127.60,'fest',6.24,2.10],#Te
      
          ['Iod',53,'Halogene',17,5,'p',126.90,'fest',4.94,2.66],#I
          ['Xenon',54,'Edelgase',18,5,'p',131.29,'gasförmig',5.90,2.6],#Xe
          ['Caesium',55,'Alkalimetalle',1,6,'s',132.91,'fest',1.90,0.79],#Cs
          ['Barium',56,'Erdalkalimetalle',2,6,'s',137.33,'fest',3.62,0.89],#Ba
          ['Lanthan',57,'Übergangsmetalle',3,6,'d',138.90,'fest',6.17,1.1],#La
          ['Cer',58,'Lanthanoide','La',6,'f',140.12,'fest',6.77,1.12],#Ce
          ['Praseodym',59,'Lanthanoide','La',6,'f',140.91,'fest',6.48,1.13],#Pr
          ['Neodym',60,'Lanthanoide','La',6,'f',144.24,'fest',7.00,1.14],#Nd
          ['Promethium',61,'Lanthanoide','La',6,'f',146.91,'fest',7.2,'n.A.'],#Pm
       
          ['Samarium',62,'Lanthanoide','La',6,'f',150.36,'fest',7.54,1.17],#Sm
          ['Europium',63,'Lanthanoide','La',6,'f',151.96,'fest',5.25,'n.A'],#Eu
          ['Gadolinium',64,'Lanthanoide','La',6,'f',157.25,'fest',7.89,1.20],#Gd
          ['Terbium',65,'Lanthanoide','La',6,'f',158.93,'fest',8.25,'n.A'],#Tb
          ['Dysprosium',66,'Lanthanoide','La',6,'f',162.50,'fest',8.56,1.22],#Dy
          ['Holmium',67,'Lanthanoide','La',6,'f',164.93,'fest',8.78,1.23],#Ho
          ['Erbium',68,'Lanthanoide','La',6,'f',167.26,'fest',9.05,1.24],#Er
          ['Thulium',69,'Lanthanoide','La',6,'f',168.93,'fest',9.32,1.25],#Tm
         
          ['Ytterbium',70,'Lanthanoide','La',6,'f',173.05,'fest',6.97,'n.A'],#Yb
          ['Lutetium',71,'Lanthanoide','La',6,'f',174.97,'fest',9.84,1.27],#Lu
          ['Hafnium',72,'Übergangsmetalle',4,6,'d',178.49,'fest',13.28,1.3],#Hf
          ['Tantal',73,'Übergangsmetalle',5,6,'d',180.95,'fest',16.65,1.5],#Ta
          ['Wolfram',74,'Übergangsmetalle',6,6,'d',183.84,'fest',19.25,2.36],#W
          ['Rhenium',75,'Übergangsmetalle',7,6,'d',186.21,'fest',21.00,1.9],#Re
          ['Osmium',76,'Übergangsmetalle',8,6,'d',190.23,'fest',22.59,2.2],#Os
          ['Irdium',77,'Übergangsmetalle',9,6,'d',192.22,'fest',22.56,2.2],#Ir

          ['Platin',78,'Übergangsmetalle',10,6,'d',195.08,'fest',21.45,2.2],#Pt
          ['Gold',79,'Übergangsmetalle',11,6,'d',196.97,'fest',19.32,2.54],#Au
          ['Quecksilber',80,'Übergangsmetalle',12,6,'d',200.59,'flüssig',13.55,2.00],#Hg
          ['Thalium',81,'Metalle',13,6,'p',204.38,'fest',11.85,1.62],#Tl
          ['Blei',82,'Metalle',14,6,'p',207.20,'fest',11.34,2.33],#Pb
          ['Bismut',83,'Metalle',15,6,'p',208.98,'fest',9.78,2.02],#Bi
          ['Polonium',84,'Metalle',16,6,'p',209.98,'fest',9.20,2.0],#Po
          ['Astat',85,'Halogene',17,6,'p',209.99,'fest','n.A',2.2],#At
          ['Radon',86,'Edelgase',18,6,'p',222.00,'gasförmig',9.73,'n.A'],#Rn

          ['Francium',87,'Alkalimetalle',1,7,'s',223.02,'fest','n.A',0.7],#Fr
          ['Radium',88,'Erdalkalimetalle',2,7,'s',226.03,'fest',5.5,0.9],#Ra
          ['Actinium',89,'Übergangsmetalle',3,7,'d',227.03,'fest',10.07,1.1],#Ac
          ['Thorium',90,'Actinoide','Ac',7,'f',232.04,'fest',11.72,1.3],#Th
          ['Protactinium',91,'Actinoide','Ac',7,'f',231.04,'fest',15.37,1.5],#Pa
          ['Uran',92,'Actinoide','Ac',7,'f',238.03,'fest',19.16,1.38],#U
          ['Neptunium',93,'Actinoide','Ac',7,'f',237.05,'fest',20.45,1.36],#Np
          ['Plutonium',94,'Actinoide','Ac',7,'f',244.06,'fest',19.82,1.28],#Pu
          ['Americium',95,'Actinoide','Ac',7,'f',243.06,'fest',13.67,1.3],#Am
          
          ['Curium',96,'Actinoide','Ac',7,'f',247.07,'fest',13.51,1.3],#Cm
          ['Berkelium',97,'Actinoide','Ac',7,'f',247,'fest',14.78,1.3],#Bk
          ['Californium',98,'Actinoide','Ac',7,'f',251,'fest',15.1,1.3],#Cf
          ['Einsteinium',99,'Actinoide','Ac',7,'f',252,'fest',8.84,'n.A'],#Es
          ['Fermium',100,'Actinoide','Ac',7,'f',257.10,'fest','n.A','n.A'],#Fm
          ['Medelevium',101,'Actinoide','Ac',7,'f',258,'fest','n.A','n.A'],#Md
          ['Nobelium',102,'Actinoide','Ac',7,'f',259,'fest','n.A.','n.A'],#No
          ['Lawrencium',103,'Actinoide','Ac',7,'f',266,'fest','n.A','n.A'],#Lr
          
          ['Rutherdordium',104,'Übergangsmetalle',4,7,'d',261.11,'fest',17.00,'n.A'],#Rf
          ['Dubnium',105,'Übergangsmetalle',5,7,'d',262.11,'n.A','n.A','n.A'],#Db
          ['Seaborgium',106,'Übergangsmetalle',6,7,'d',263.12,'n.A','n.A','n.A'],#Sg
          ['Bohrium',107,'Übergangsmetalle',7,7,'d',262.12,'n.A','n.A','n.A'],#Bh
          ['Hassium',108,'Übergangsmetalle',8,7,'d',265,'n.A','n.A','n.A'],#Hs
          ['Meitnerium',109,'Unbekannt',9,7,'d',268,'n.A','n.A','n.A'],#Mt
          ['Darmstadtium',110,'Unbekannt',10,7,'d',281,'n.A','n.A','n.A'],#Ds
          ['Roentgenium',111,'Unbekannt',11,7,'d',280,'n.A','n.A','n.A'],#Rg
          ['Copernicium',112,'Unbekannt',12,7,'d',277,'n.A','n.A','n.A'],#Cn

          ['Nihonium',113,'Unbekannt',13,7,'p',287,'n.A','n.A','n.A'],#Nh
          ['Flerovium',114,'Unbekannt',14,7,'p',289,'n.A','n.A','n.A'],#Fl
          ['Moscovium',115,'Unbekannt',15,7,'p',288,'n.A','n.A','n.A'],#Mc
          ['Livermorium',116,'Unbekannt',16,7,'p',293,'n.A','n.A','n.A'],#Lv
          ['Tenness',117,'Unbekannt',17,7,'p',292,'n.A','n.A','n.A'],#Ts
          ['Oganesson',118,'Unbekannt',18,7,'p',294,'fest',6.6,'n.A']#Og
          ]
