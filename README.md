# Paciento recepto duomenų analizavimo projektas

**Turinys**
1. Apie projektą
2. Aplinkos sukūrimas
3. Duomenys bei naudojimo praktikos
4. Projekto failai
5. Prisidėjimas prie projekto

## Apie projektą

Šis projektas yra skirtas elektroninės sveikatos paslaugų ir bendradarbiavimo infrastruktūros informacinės sistemos e. recepto duomenų analizavimui bei šių duomenų panaudojimui mašininio mokymo modelio sukūrimui, kuris įvertinęs pateiktą informąciją bando nuspėti, ar pacientas panaudos receptą ar ne. Verta atsižvelgti į tai, kad egzistuoja daug veiksnių, kurie nėra pateikti šiuose duomenyse ir gali daryti įtaką galutiniam rezultatui (oro sąlygos, paciento finansinė padėtis, asmeninės problemos ir t.t.), tačiau netgi iš turimų duomenų galima bandyti numatyti, ar pagal vaistą, veikliają medžiagą ir kitus pateiktus atributus pacientas realizuos savo receptą.

Projekto įgyvendinimui sukurtas API, kuriam pateikiant reikiamas reikšmes apie išrašytą receptą grąžinamas nuspėjamas rezultatas ar pacientas bus linkęs pasinaudoti receptu ar ne (žiūrėti prescription_api.py failą). Reikalingų reikšmių struktūra (pavyzdys):
 {    
 "ligos_kodas" : "Z95.5",                            
 "atc_kodas" : "C10AA07",     
 "dozuociu_sk" : [90],      
 "recepto_galiojimas_d" : [29],     
 "kompens_poz" : [1],      
 "pac_savivaldybe" : "Vilniaus m. sav.",      
 "vart_trukme_d" : [90],      
 "pac_lytis" : "M",      
 "pac_amziaus_gr" : "45-64 m."     
}

## Aplinkos sukūrimas

Kad projekto kodą butų galima paleisti bei modifikuoti, rekomenduojama susikurti naują virtualią aplinką ir toje aplinkoje paleisti šioje repozitorijoje esantį 'requirements.txt' failą. Jame yra visi reikalingi paketai, kad visos importuotos bibliotekos veiktų. Tą padaryti galima su šia komanda:

```bash
pip install -r /path/to/requirements.txt
```

## Duomenys bei naudojimo praktikos

Duomenys šiam projektui atlikti yra paimti iš Lietuvos atvirų duomenų portalo, nuorodos failams atsisiųsti:

[2022_01_2dekada.csv](https://data.gov.lt/dataset/2020/download/12649/espbi_OD_israsyti_receptai_2022_01_2dekada.csv)         
[2022_01_3dekada.csv](https://data.gov.lt/dataset/2020/download/12650/espbi_OD_israsyti_receptai_2022_01_3dekada.csv)  
[2022_02_1dekada.csv](https://data.gov.lt/dataset/2020/download/12651/espbi_OD_israsyti_receptai_2022_02_1dekada.csv)  
[2022_02_2dekada.csv](https://data.gov.lt/dataset/2020/download/12652/espbi_OD_israsyti_receptai_2022_02_2dekada.csv)  
[2022_02_3dekada.csv](https://data.gov.lt/dataset/2020/download/12653/espbi_OD_israsyti_receptai_2022_02_3dekada.csv)  
[2022_03_1dekada.csv](https://data.gov.lt/dataset/2020/download/12654/espbi_OD_israsyti_receptai_2022_03_1dekada.csv)   
[2022_03_2dekada.csv](https://data.gov.lt/dataset/2020/download/12655/espbi_OD_israsyti_receptai_2022_03_2dekada.csv)  
[2022_03_2dekada.csv](https://data.gov.lt/dataset/2020/download/12656/espbi_OD_israsyti_receptai_2022_03_3dekada.csv)


Darbas yra atliktas Google Colab aplinkoje, kuri suteikia nemokamus išteklius leisti kodą ir treniruoti savo modelį nenaudojant savo lokalios mašinos. Kad turėti patogią prieigą prie atsisiųstų duomenų, rekomenduojama juos susikelti į nuosavą Google Drive ir jį mount'inti Google Colab aplinkoje. Tą padaryti galima taip:

```python
from google.colab import drive

drive.mount("/content/drive")
```

Daugiau apie [Google Colab](https://colab.research.google.com). 

## Projekto failai

Projekte randami failai:

**Perscription_prediction_project.ipynb** - Jupyter Notebook failas, kuriame atliekamas duomenų apdirbimas bei modelio treniravimas.   
**e_receptas_struktura_x.csv** - CSV failas, kuriame yra informacija apie duomenų rinkinio požymius.     
**prescription_api.py** - Python failas, kuriame yra API kodas skirtas deploy'inti aptreniruotą ir į pickle failą išeksportuotą modelį.   
**requirements.txt** - tekstinis failas, skirtas virtualios aplinkos sukūrimui instaliuojant reikiamus paketus.

## Prisidėjimas prie projekto

Šis projektas yra atviras viešam naudojimui ir Pull request'ai yra ne tik laukiami, bet ir skatinami, kad būtų galima pasiekti geresnius rezultatus bei patobulinti kodo kokybę.
