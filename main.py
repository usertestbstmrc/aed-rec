# main
import modulo as m
import os

def main():
    opc = -1
    temas = []
    while opc != 0:
        m.print_menu()
        opc = int(input('OPCIÓN: '))
        print('--' * 40)

        if opc == 1:
            m.cargar_vector(temas, 'musica.csv')
            m.mostrar_vector(temas)


        else:
            if len(temas) == 0:
                print('ERROR: ')

            elif opc == 2:
                n = int(input('Ingrese cantidad de temas: '))
                lista_opt2 = [''] * n
                i = int(input('Ingrese el idioma: '))


            elif opc == 6:
                idioma_req = int(input('Ingrese idioma que desea filtrar: '))
                m.gen_binario(idioma_req, temas)

            elif opc == 7:
                idioma_req = int(input('Ingrese idioma: '))

                fd = m.gen_fd(idioma_req)

                if os.path.exists(fd):
                    m.leer_binario(idioma_req)
                else:
                    print('El archivo "', fd, '" no existe, pero será creado.')
                    m.gen_binario(idioma_req, temas)
                    m.leer_binario(idioma_req)


if __name__ == '__main__':
    main()
