#python calculator, now with Ifs
firstNumber = float(input('First number: '))

print('Select a option \n',
    '[+] Sum \n',
    '[-] Subtraction \n',
    '[*] Multiplication \n',
    '[/] Division'
)

option = input('Option: ')
secondNumber = float(input('Second number: '))
print('')

if option == '+':
    total = firstNumber + secondNumber
elif option == '-':
    total = firstNumber - secondNumber
elif option == '*':
    total = firstNumber * secondNumber
elif option == '/':
    total = firstNumber / secondNumber

print('Total:', total)