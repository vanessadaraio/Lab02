import csv

def carica_da_file(file_path):
    """Carica le foto dal file, creando un nuovo anno ogni volta che compare per la prima volta"""
    try:
        file=open(file_path,'r',encoding='utf-8', newline='')
        lettore = csv.reader(file)
        next(lettore)
        album={}
        for riga in lettore:
            codice=riga[0]
            titolo=riga[1]
            autore=riga[2]
            mese=int(riga[3])
            anno=int(riga[4])
            if anno not in album:
                album[anno]=[]

            album[anno].append([codice,titolo,autore,mese])

        file.close()
        return album


    except FileNotFoundError:
        return None



def aggiungi_foto(album, codice, titolo, autore, mese, anno, file_path):
    """Aggiunge una foto all'album, creando l'anno al volo se non è ancora presente"""

    #controllo sul codice
    for annopresente in album:
        for  foto in album[annopresente]:
            if foto[0]==codice:

                return None

    # controllo sul mese
    if mese not in range(1,13):

         return None

    try:
        #apriamo file in modalità 'a' per aggiungere riga in fondo senza sovrascrivere il contenuto
        with open(file_path,'a',encoding='utf-8', newline='')  as file:
            writer=csv.writer(file)
            writer.writerow([codice,titolo,autore,mese,anno])


        if anno not in album:
            album[anno] = []


        foto=[codice,titolo,autore,mese]
        album[anno].append(foto)

        return foto
    except FileNotFoundError:
        return None





def cerca_foto(album, codice):
    """Cerca una foto nell'album dato il codice"""

    for anno in album:
        for foto in album[anno]:
            if foto[0]==codice:

                return  f'{codice}, {foto[1]}, {foto[2]}, {foto[3]}, {anno}'


    return None




def elenco_foto_anno_per_titolo(album, anno):
    """Ordina i titoli delle foto di un dato anno in ordine alfabetico"""

    if anno not in album:
        return None

    listatitoli=[]
    for foto in album[anno]:
        titolo=foto[1]
        listatitoli.append(titolo)

    listatitoli.sort()
    return listatitoli





def main():
    album = []
    file_path = "album_fotografico.csv"

    while True:
        print("\n--- MENU ALBUM FOTOGRAFICO ---")
        print("1. Carica album da file")
        print("2. Aggiungi una nuova foto")
        print("3. Cerca una foto per codice")
        print("4. Elenco foto di un anno (ordinato per titolo)")
        print("5. Esci")

        scelta = input("Scegli un'opzione >> ").strip()

        if scelta == "1":
            while True:
                file_path = input("Inserisci il path del file da caricare: ").strip()
                album = carica_da_file(file_path)
                if album is not None:
                    break

        elif scelta == "2":
            if not album:
                print("Prima carica l'album da file.")
                continue

            codice = input("Codice della foto: ").strip()
            titolo = input("Titolo: ").strip()
            autore = input("Autore: ").strip()
            try:
                mese = int(input("Mese (1-12): ").strip())
                anno = int(input("Anno: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per mese e anno.")
                continue

            foto = aggiungi_foto(album, codice, titolo, autore, mese, anno, file_path)
            if foto:
                print(f"Foto aggiunta con successo!")
            else:
                print("Non è stato possibile aggiungere la foto.")

        elif scelta == "3":
            if not album:
                print("L'album è vuoto.")
                continue

            codice = input("Inserisci il codice della foto da cercare: ").strip()
            risultato = cerca_foto(album, codice)
            if risultato:
                print(f"Foto trovata: {risultato}")
            else:
                print("Foto non trovata.")

        elif scelta == "4":
            if not album:
                print("L'album è vuoto.")
                continue

            try:
                anno = int(input("Inserisci l'anno da consultare: ").strip())
            except ValueError:
                print("Errore: inserire un valore numerico valido.")
                continue

            titoli = elenco_foto_anno_per_titolo(album, anno)
            if titoli is not None:
                print(f'\nFoto del {anno}:')
                print("\n".join([f"- {titolo}" for titolo in titoli]))
            else:
                print(f"Nessuna foto trovata per l'anno {anno}.")

        elif scelta == "5":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida. Riprova.")


if __name__ == "__main__":
    main()
