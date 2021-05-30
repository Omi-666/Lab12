
import sqlite3

if __name__ == "__main__":

    conn = sqlite3.connect('database.db')
    print("BD otwarta")
    
    conn.execute('CREATE TABLE pracownicy (ImieNazwisko TEXT, NrPracownika TEXT, Adres TEXT)')
    print("Tabela utworzona")
    
    conn.close()
    print("BD zamknieta")
    
    
    conn = sqlite3.connect('database.db')
    print("BD otwarta")
    cur = conn.cursor()
    
    cur.execute("INSERT INTO pracownicy (ImieNazwisko, NrPracownika, Adres) VALUES (?,?,?)",('Magda Kessler','1','Warszawa') )
    cur.execute("INSERT INTO pracownicy (ImieNazwisko, NrPracownika, Adres) VALUES (?,?,?)",('Radosław Makłowicz','2','Płock') )
    conn.commit()
    
    cur.execute('SELECT * FROM pracownicy ORDER BY nrpracownika')
    print(cur.fetchall())
    
    conn.close()
    print("BD zamknieta")