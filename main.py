import docx2txt
import os

if __name__ == '__main__':
    print("this tool will create .txt files from any .docx files and place them in a seperate file")
    dirName = input("what folder would you like to convert?\n")
    os.chdir(dirName)
    files = os.listdir(dirName)

    try:
        os.mkdir(dirName + '/text_files')
    except OSError:
        print("os error")
    else:
        print("folder created")

    for file in files:
        if file[-4:] == "docx" and not file[0] == "~":
            text = docx2txt.process(file)
            with open((file[:-5] + ".txt"), "x") as current_file:
                current_file.write(text)

            txt_file_name = file[:-5] + '.txt'
            try:
                os.rename(txt_file_name, './text_files/' + txt_file_name)
            except OSError:
                print(f"there was a problem creating the file {txt_file_name}")
            else:
                print(f'created {txt_file_name}')

