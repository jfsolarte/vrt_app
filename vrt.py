import os.path
import subprocess

nameApp = "./com.evancharlton.mileage_3110.apk"
subprocess.check_call('calabash-android resign '+nameApp, shell=True)

if not os.path.exists('screenshot'):
    subprocess.check_call('mkdir screenshot', shell=True)

comando = 'SCREENSHOT_PATH=screenshot/ calabash-android run '+nameApp+' --format html --out report.html'
subprocess.call(comando, shell=True)


for x in range(1, 8):
    nameAppMuta = "./com.evancharlton.mileage-mutant"+str(x)+"/com.evancharlton.mileage_3110-aligned-debugSigned.apk"
    
    screenshotPath = "./screenshot"+str(x)+"/"
    reportName = "report"+str(x)+".html"
    
    
    if os.path.isfile(nameAppMuta):
        
        if not os.path.exists(screenshotPath):
            subprocess.check_call('mkdir '+screenshotPath, shell=True)

        print(comando)
        subprocess.check_call('calabash-android resign '+nameAppMuta, shell=True)
        comando = 'SCREENSHOT_PATH='+screenshotPath+' calabash-android run '+nameAppMuta+' --format html --out '+reportName
        #
        subprocess.call(comando, shell=True)

        for x_img in range(0, 8):
            img = screenshotPath+'screenshot_'+str(x_img)+'.png'
            if os.path.isfile(img):
                subprocess.call('node resemblejs.js screenshot/screenshot_'+x_img+'.png '+img, shell=True)
            


#)b