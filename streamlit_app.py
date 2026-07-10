import pandas as pd

def colecteaza_date_bvb():
    """
    Simulează colectarea datelor financiare live (Preț, P/E, P/B, Dividend și Volum).
    Pentru companiile mari (REGS), prețurile se actualizează zilnic, iar dividendele trimestrial/anual.
    """
    # Dividend_Yield este exprimat în procente (ex: 8.5 înseamnă 8.5%)
    date_bursa = [
        {'Ticker': 'TLV', 'Piata': 'REGS', 'Pret': 28.5, 'PE': 6.2, 'PB': 1.1, 'Dividend_Yield': 4.5, 'Volum_Lei': 1500000},
        {'Ticker': 'SNG', 'Piata': 'REGS', 'Pret': 45.2, 'PE': 5.8, 'PB': 0.8, 'Dividend_Yield': 9.2, 'Volum_Lei': 900000},
        {'Ticker': 'BRD', 'Piata': 'REGS', 'Pret': 18.2, 'PE': 7.1, 'PB': 0.9, 'Dividend_Yield': 10.5, 'Volum_Lei': 450000},
        {'Ticker': 'H2O', 'Piata': 'REGS', 'Pret': 120.0, 'PE': 11.2, 'PB': 2.1, 'Dividend_Yield': 8.1, 'Volum_Lei': 2100000},
        {'Ticker': 'AERO_TEST1', 'Piata': 'AeRO', 'Pret': 1.5, 'PE': 4.1, 'PB': 0.5, 'Dividend_Yield': 12.0, 'Volum_Lei': 15000},
        {'Ticker': 'AERO_TEST2', 'Piata': 'AeRO', 'Pret': 3.2, 'PE': 15.0, 'PB': 2.5, 'Dividend_Yield': 0.0, 'Volum_Lei': 300}
    ]
    return pd.DataFrame(date_bursa)

def filtreaza_si_sorteaza_oportunitati(df):
    """
    Filtrează companiile ieftine (PE < 7.5 și PB < 1.0) cu lichiditate minimă (> 5000 lei).
    Sortează rezultatele în funcție de Dividend Yield (de la cel mai mare la cel mai mic).
    """
    # Aplicăm criteriile stricte de subevaluare și siguranță
    filtru = (df['PE'] < 7.5) & (df['PB'] < 1.0) & (df['Volum_Lei'] > 5000)
    df_filtrat = df[filtru].copy()
    
    # Sortăm descrescător după randamentul dividendului pentru a vedea prima dată companiile care dau cel mai mult cash
    df_sortat = df_filtrat.sort_values(by='Dividend_Yield', ascending=False)
    return df_sortat

if __name__ == "__main__":
    print("Se descarcă și se analizează datele BVB...")
    
    # 1. Preluăm datele
    date_brute = colecteaza_date_bvb()
    
    # 2. Aplicăm filtrele și sortarea după dividende
    rezultate_finale = filtreaza_si_sorteaza_oportunitati(date_brute)
    
    # 3. Salvăm baza de date locală în format CSV
    rezultate_finale.to_csv('oportunitati_bvb.csv', index=False)
    
    print(f"Succes! S-a generat fișierul cu {len(rezultate_finale)} companii subevaluate ordonate după dividende.")
