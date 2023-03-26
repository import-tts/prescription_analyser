# Paciento recepto duomenų analizavimo projektas

**Turinys**
1. Apie projektą
2. Aplinkos sukūrimas
3. Duomenys bei naudojimo praktikos
4. Prisidėjimas prie projekto
5. Naudinga dokumentacija

## Apie projektą

Šis projektas yra skirtas elektroninės sveikatos paslaugų ir bendradarbiavimo infrastruktūros informacinės sistemos e. recepto duomenų analizavimui bei šių duomenų panaudojimui mašininio mokymo modelio sukūrimui, kuris įvertinęs pateiktą informąciją bando nuspėti, ar pacientas panaudos receptą ar ne. Verta atsižvelgti į tai, kad egzistuoja daug veiksnių, kurie nėra pateikti šiuose duomenyse ir gali daryti įtaką galutiniam rezultatui (oro sąlygos, paciento finansinė padėtis, asmeninės problemos ir t.t.), tačiau netgi iš turimų duomenų galima bandyti numatyti, ar pagal vaistą, veikliają medžiagą ir kitus pateiktus atributus pacientas realizuos savo receptą.

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


Darbas yra atliktas Google Colab aplinkoje, kuri suteikia nemokamus išteklius leisti kodą ir treniruoti savo modelį nenaudojant savo lokalios mašinos. Kad turėti patogią prieigą prie atsisiųstų duomenų, rekomenduojama juos susikelti į nuosavą Google Drive ir jį mount'inti Google Colab aplinkoje (kodas tam yra pridėtas ipynb faile, pirma kodo cell'ė).

```python
from google.colab import drive

drive.mount("/content/drive")
```

Daugiau apie [Google Colab](https://colab.research.google.com). 

## Prisidėjimas prie projekto

Šis projektas yra atviras viešam naudojimui ir Pull request'ai yra ne tik laukiami, bet ir skatinami, kad būtų galima pasiekti geresnius rezultatus bei patobulinti kodo kokybę.
