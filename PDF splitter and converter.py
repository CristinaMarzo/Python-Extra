import subprocess, pyautogui, sys, math

def trial():
    print ('Bienvenida a tu programa para automatizar la division de\n')
    print ('libros en PDF a pequeños grupos para despues poder convertirlos.\n')
    npag = input ('Introduce el numero de paginas del archivo: ')
    
    # split and merge x 246 y 615 - clic
    subprocess.Popen('C:\Program Files (x86)\Icecream PDF Split and Merge\pdftool.exe')
    
    # dividir x 543 y 444 - clic
    pyautogui.PAUSE = 6
    pyautogui.moveTo(x=543, y=444)
    pyautogui.click()
    
    #agregar archivo --> hacer calculo del bucle con el numero de paginas
    ndivs = (npag/5)
    ndivsred = math.ceil(ndivs) #numero de veces que tengo que dividir
    print ('\nVoy a hacer ' + str (ndivsred) + ' divisiones')
    ngrup = (ndivsred/4)
    ngrupos = math.ceil (ngrup)
    print ('\nVoy a hacer ' + str (ngrupos) + 'veces el proceso')
    print ('\nTengo que eliminar las paginas ' + str (ngrupos) + ' veces')
    
    for a in range (ngrupos):
          
        print ('\nAgrega el archivo original, porfa')
        pyautogui.PAUSE = 20
        
        # X 489 Y 376 grupos de paginas - clic
        pyautogui.moveTo(x=489, y=376)
        pyautogui.click()
    
        # casilla grupos x 687 y 347 - clic
        pyautogui.moveTo(x=687, y=347)
        pyautogui.click()

        #poner 5 - enter
        pyautogui.press('5')
        pyautogui.press('enter')

        # casilla paginas x 860 y 348 - clic
        pyautogui.moveTo(x=860, y=348)
        pyautogui.click()

        #poner 1 - enter
        pyautogui.press('1')
        pyautogui.press('enter')

        # deplegable carpeta x 572 y 506 - clic (la primera vez no)
        while (a>1):
            pyautogui.moveTo(x=572, y=506)
            pyautogui.click()

            # carpeta original x y  - clic
            pyautogui.moveTo(x=572, y=575)
            pyautogui.click()
        
        # separar x 943 y 506 - clic
        pyautogui.moveTo(x=943, y=506)
        pyautogui.click()

        # eliminar paginas x 437 y 410 - clic
        pyautogui.moveTo(x=437, y=410)
        pyautogui.click()

        for b in range (1, 10):
            
            # campo numero x 593 y 349 - clic
            pyautogui.moveTo(x=593, y=349)
            pyautogui.click()

            pyautogui.press(str(b))

            # btn agregar x 679 y 344
            pyautogui.moveTo(x=679, y=344)
            pyautogui.click()

        for c in range (1, 10):

            # campo numero x 593 y 349 - clic
            pyautogui.moveTo(x=593, y=349)
            pyautogui.click()
            
            pyautogui.press('1')
            pyautogui.press(str(b))

            # btn agregar x 679 y 344
            pyautogui.moveTo(x=679, y=344)
            pyautogui.click()

        # campo numero x 593 y 349 - clic
        pyautogui.moveTo(x=593, y=349)
        pyautogui.click()
            
        pyautogui.press('2')
        pyautogui.press('0')

        # btn agregar x 679 y 344
        pyautogui.moveTo(x=679, y=344)
        pyautogui.click()
        
        # separar x 943 y 506 - clic
        pyautogui.moveTo(x=943, y=506)
        pyautogui.click()
        
    ntimes = (ndivsred/3)
    # abra el converter 
    subprocess.Popen('C:\Program Files (x86)\Icecream PDF Converter\pdfconverter.exe')
    
    # seleccione de pdf x y - clic
    pyautogui.moveTo(x=551, y=445)
    pyautogui.click()

    for d in range (ntimes):
        # introduzca archivo x y - clic
        print ('Por favor, desplace sus archivos')
        pyautogui.PAUSE = 20
    
        # formato docx - clic
        pyautogui.moveTo(x=786, y=244)
        pyautogui.click()
        pyautogui.moveTo(x=786, y=299)
        pyautogui.click()

        pyautogui.moveTo(x=786, y=272)
        pyautogui.click()
        pyautogui.moveTo(x=786, y=327)
        pyautogui.click()

        pyautogui.moveTo(x=786, y=299)
        pyautogui.click()
        pyautogui.moveTo(x=786, y=354)
        pyautogui.click()

        # desplegable de subcarpeta x y - clic
        while (d>1):
            pyautogui.moveTo(x=572, y=506)
            pyautogui.click()

            pyautogui.moveTo(x=572, y=575)
            pyautogui.click()

        # convertir x y - clic
        pyautogui.moveTo(x=943, y=506)
        pyautogui.click()

        # eliminar x y - clic
        pyautogui.moveTo(x=983, y=438)
        pyautogui.click()

trial ()


# pyautogui.click(x=100, y=200)  # move to 100, 200, then click the left mouse button.
# pyautogui.doubleClick()  # perform a left-button double click
# pyautogui.press('enter')  # press the Enter key
# pyautogui.press('1')  # press number 1


