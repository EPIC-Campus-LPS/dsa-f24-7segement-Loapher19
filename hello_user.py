import tm1637

tm = tm1637.TM1637(clk=14, dio=15)
tm.write([0,0,0,0])
name = input("What's your name? ")
tm.scroll("Hello " + name,delay=250)
