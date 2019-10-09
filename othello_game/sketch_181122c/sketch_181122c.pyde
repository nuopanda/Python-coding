def setup():
    answer = input('enter your name')
    if answer:
        print('hi ' + answer)
        f=open('scores.txt','a')
        f.write("now the file")
        f.write(answer)
        f.close()
    elif answer == '':
        print('[empty string]')
    else:
        print(answer) # Canceled dialog will print None

def input(self, message=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)
