import sqlite3



con = sqlite3.connect('meu_banco.db')
c = con.cursor()

c. execute('''CREATE TABLE IF NOT EXISTS tabela(
           
           nome TEXT,
           idade integer
           
           )
            ''')

c.execute('INSERT INTO tabela VALUES(?,?)',('julia',40))
con.commit()


c.close()