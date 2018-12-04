[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/bredsjomagnus/csvcleaner/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/bredsjomagnus/csvcleaner/?branch=master)
[![Build Status](https://scrutinizer-ci.com/g/bredsjomagnus/csvcleaner/badges/build.png?b=master)](https://scrutinizer-ci.com/g/bredsjomagnus/csvcleaner/build-status/master)
[![Code Intelligence Status](https://scrutinizer-ci.com/g/bredsjomagnus/csvcleaner/badges/code-intelligence.svg?b=master)](https://scrutinizer-ci.com/code-intelligence)

# csvcleaner
## Racing
Ett litet hjälpscript för att kontrollera och ställa iordning csv-filer som skall användas till Racingsidan.

## Funktion
Ser till att header/names är som de skall, samt att alla kolumner som skall vara integers är just det.
### Användning
Scriptet tar tre argument; csvfil som skall behandas, namnet på nya csvfilen efter behandling, racefil-typ (mylaps eller hardcard)

Vill du exempelvis kolla input.csv, som är en mylapsfil, och spara resultatet i output.csv används följande rad.

`$ python3 input.csv output.csv mylaps`

## Vidare att utveckla
### Integer NaN
I dagsläget ersätts pandas float NaN i integerkolumnerna med -1. Detta skall helst ersättas med tom 'cell'.

### Resterande datatyper
Det viktigaste har varit att ta hand om och kontrollera datatypen integer. Övriga har fått stryka på foten tills vidare.
