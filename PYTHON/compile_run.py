import os


class C:
    def gcc(file, extension, c):
        e = exe + '.exe'
        n = 0
        if n == 1:
            delete = 'del ' + e
            os.system(delete)
        elif n == 0:
            n += 1

        file = file + extension
        cmd = c + file + ' -o ' + exe

        # Compile file
        os.system(cmd)

        # Run file
        cmd = 'start "' + exe + '" cmd /k "cd "' + directory + '" && "' + e + '""'
        os.system(cmd)


def check_extension(file, extension):
    if extension == '.c':
        c = 'gcc '
        C.gcc(file, extension, c)
    elif extension == '.cpp':
        c = 'g++ '
        C.gplus_plus(file, extension, c)
    else:
        print('\nExtension NotValid\n')


def user_choice(input_user):
    global file, extension, directory

    if input_user == 'cd':
        directory = input('New directory: ')
        os.chdir(directory)
        return True

    elif input_user == 'd':
        print(directory)
        return True

    elif input_user == 'cf':
        file = input('New file')
        return True

    elif input_user == 'ce':
        extension = input('New extension: ')
        return True

    elif input_user == 'cls':
        os.system('cls')
        return True

    else:
        return False


print('compile and run .c, .cpp files (more soon)\n')
global directory, exe
exe = ''
directory = os.getcwd()
print('Enter: "cd" to change, "d" to see current directory.')
print('Enter: "cf" to change file')
print('Enter: "ce" to change extension')
print('Enter: "r" to repeat the process done')
print('Enter: "p" to stop')
print('Your current directory: ', directory)

done = True
while done:
    global file, extension, user_input
    user_input = ''

    # Check user choices
    user_done = True
    while user_done:
        print('\nEnter: Any key to continue or "/cmd" to open cmd')
        user_input = input('Enter: ')
        if user_input == 'r':
            check_extension(file, extension)
            continue
        elif user_input == '/cmd':
            os.system('start "CMD" cmd /k')
            continue
        elif user_input == 'p':
            break

        user_done = user_choice(user_input)

    # Condition to stop the program
    if user_input == 'p':
        print('\nEND')
        break

    print('\n#Enter: /c, if you wanna type a command\n')
    file = input('Enter the name file here: ')
    if file == '/c':
        continue
    exe = file

    extension = input('Enter the extension (ex: .c): ')
    if extension == '/c':
        continue

    check_extension(file, extension)
