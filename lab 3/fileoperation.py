def red(filepath, options):
    try:
        file = open(filepath, "r")
        if options == "all":
            content = file.read()
            print(content)
        elif isinstance(options, int):
            content = file.read(options)
            print(content)
        elif options == "line":
            content = file.readline().strip()
            print(content)
        elif options == "lines":
            content = file.readlines()
            for item in content:
                print(item.strip())
        else:
            print("Invalid option")
        file.close()
    except FileNotFoundError:
        print("The file was not found.")




def write(filepath, content):
    try:
        file = open(filepath, "w")

        if isinstance(content, str):
            file.write(content)
        elif isinstance(content, list):
            file.writelines(content)

        file.close()

    except Exception :
        print("An error occurred:", e)





def apend(filepath, newcontentgi):
    try:
        file = open(filepath, "a")

        if isinstance(content, str):
            file.write(content)
        elif isinstance(content, list):
            file.writelines(content)

        file.close()

    except Exception :
        print("An error occurred:", e)


                  


  


