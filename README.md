# csvcleaner
## Racing
Ett litet hjälpscript för att kontrollera och ställa iordning csv-filer som skall användas till Racingsidan.

## Funktion
Ser till att header/names är som de skall, samt att alla kolumner som skall vara integers är just det.

## Vidare att utveckla
### Integer NaN
I dagsläget ersätts pandas float NaN i integerkolumnerna med -1. Detta skall helst ersättas med tom 'cell'.

### Resterande datatyper
Det viktigaste har varit att ta hand om och kontrollera datatypen integer. Övriga har fått stryka på foten tills vidare.
