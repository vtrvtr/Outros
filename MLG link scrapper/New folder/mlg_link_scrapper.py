import pyperclip

def main(mlgLink):
    split = mlgLink.split('/')
    better_link = []
    for i, word in enumerate(split):
        if word == 'http:':
            split[i] = 'hds://'
            break
    for i, word in enumerate(split):
        if word == 'z':
            better_link.append('/' + word + '/')
            better_link.append(split[i+1] + '/manifest.f4m')
            break
        else:
            better_link.append(word)
    pyperclip.copy(''.join(better_link))
    pyperclip.paste()

if __name__ == "__main__":
    ugly_Link = raw_input('Please input stream link \n')
    main(ugly_Link)
    print 'Copied to clipboard'
 
