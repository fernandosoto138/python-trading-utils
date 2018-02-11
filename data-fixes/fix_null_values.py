import glob
currency = "/EURUSD"
mypath = "/Volumes/Data/ForexTickData"+currency
fixed_path = "/Volumes/Data/ForexTickData"+currency+"_Fixed"
onlyfiles = glob.glob(mypath+"/2*.csv")
count=1
for filename in onlyfiles:
    fixed_filename = filename.replace(currency, currency+"_Fixed")
    original_file = open(filename)
    fixed_file = open(fixed_filename, "w")
    print("Fixing file "+str(count)+" of "+str(len(onlyfiles)))
    for line in original_file:
        line = line.replace("\x00", "")
        fixed_file.write(line)
    original_file.close()
    fixed_file.close()
    count+=1
