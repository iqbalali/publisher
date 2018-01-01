
# coding: utf-8

# ## 1. Load the required functions

# In[21]:

import os
class Publisher:
    """
    Documentation coming soon. For now read the readme at 
    """
    def __init__(self, PROJ_NAME):
        homedir = os.path.expanduser('~')
        self.PROJ_NAME = PROJ_NAME
        self.CBZ="1280"  #CBZ Image size
        self.SITE="1024" #Website image size
        #self.PUBLISH_FOLDER = PUBLISH_FOLDER
        self.temp_folder  = homedir+"/Downloads/temp/"
        self.dir_create(self.temp_folder)
        
    def version(self):
        print("0.1.1")

    def dir_create(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)

    def create_pdf(self, **kwargs, **args):
        print (args)

    #Sharing
    def digital_lo(self, FILE_LIST, PUBLISH_FOLDER):
        self.dir_create(PUBLISH_FOLDER)
        os.system('gs           -sDEVICE=pdfwrite           -o '+PUBLISH_FOLDER+'/'+self.PROJ_NAME+'.digi-lo.pdf           -f '+FILE_LIST)
        print(self.PROJ_NAME+': PDF for sharing')
        #self.cbz(PUBLISH_FOLDER+'/'+self.PROJ_NAME+'.digi-lo.pdf',PUBLISH_FOLDER)
        
    #Digital Files
    def digital_hi(self, FILE_LIST, PUBLISH_FOLDER):
        print('Running Digital')
        self.dir_create(PUBLISH_FOLDER)
        os.system('gs           -sDEVICE=pdfwrite           -dPDFSETTINGS=/printer           -o '+PUBLISH_FOLDER+'/'+self.PROJ_NAME+'.digi-hi.pdf           -f '+FILE_LIST)
        print(self.PROJ_NAME+': PDF for Digital')
    
    def digital_hi_new(self, FILE_LIST, PUBLISH_FOLDER):
        print('Running Digital')
        self.dir_create(PUBLISH_FOLDER)
        os.system('gs           -sDEVICE=pdfwrite           -dPDFSETTINGS=/printer           -o '+PUBLISH_FOLDER+'/'+self.PROJ_NAME+'.digi-hi.pdf           -f '+FILE_LIST)
        print(self.PROJ_NAME+': PDF for Digital')
        
    #CreateSpace
    def printer(self, FILE_LIST, PUBLISH_FOLDER):
        print("File list: "+FILE_LIST)
        print(self.PROJ_NAME+': Running CreateSpace')
        self.dir_create(PUBLISH_FOLDER)
        self.digital_hi(FILE_LIST, self.temp_folder)
        os.system('gs           -sDEVICE=pdfwrite           -dPDFSETTINGS=/printer           -o '+PUBLISH_FOLDER+'/'+self.PROJ_NAME+'.print.pdf           -dDEVICEWIDTHPOINTS=513 -dDEVICEHEIGHTPOINTS=738           -dFIXEDMEDIA           -dPDFFitPage           -c "<< /CurrPageNum 1 def /Install { /CurrPageNum CurrPageNum 1 add def              CurrPageNum 2 mod 1 eq {-9 0 translate} {9 0 translate} ifelse } bind  >> setpagedevice"           -f '+self.temp_folder+'/'+self.PROJ_NAME+'.digi-hi.pdf')
        os.remove(self.temp_folder+'/'+self.PROJ_NAME+'.digi-hi.pdf')
        print(self.PROJ_NAME+': PDF for CreateSpace')

    #CBZ files for torrenting
    def cbz(self, src, PUBLISH_FOLDER):
        self.dir_create(PUBLISH_FOLDER)
        self.dir_create(PUBLISH_FOLDER+'/PNG')
        os.system('gs           -sDEVICE=png16m           -dJPEGQ=100           -dQFactor=1.0           -r300           -dPDFFitPage           -o '+PUBLISH_FOLDER+'/PNG/%03d.png           -f '+src)
        print(self.PROJ_NAME+': CBZ')
        os.system('mogrify -resize '+self.CBZ+'x'+self.CBZ+' '+PUBLISH_FOLDER+'/PNG/*.png')
        os.system('zip -r '+PUBLISH_FOLDER+'/'+self.PROJ_NAME+'.cbz '+PUBLISH_FOLDER+'/PNG')

    #Web and email ready...
    def site(self, PUBLISH_FOLDER):
        #os.rmdir(website_folder+self.PROJ_NAME.lower())
        self.dir_create(website_folder+self.PROJ_NAME.lower())
        os.system('rm -r '+website_folder+self.PROJ_NAME.lower()+'/*.png')
        
        os.system('mogrify -resize '+self.SITE+'x'+self.SITE+' '+website_folder+PROJ_NAME+'/*.png')
        for file in os.listdir(path=website_folder+self.PROJ_NAME.lower()+'/'):
            if file.endswith(".png"):
                print('Site images published to: '+website_folder+self.PROJ_NAME.lower()+'/'+file)
        upload_images()
        
    def front_cover(self, SRC_FILE, PUBLISH_FOLDER):
        self.dir_create(PUBLISH_FOLDER)
        
    
    def cover(self, SRC_FILE, PUBLISH_FOLDER, COVER_OFFSET):
        self.dir_create(PUBLISH_FOLDER)
        os.system('gs           -o '+PUBLISH_FOLDER+'/'+self.PROJ_NAME+'.cs_cover.pdf           -sDEVICE=pdfwrite           -dPDFSETTINGS=/printer           -f '+SRC_FILE)
        
        os.system('gs           -o '+PUBLISH_FOLDER+'/'+self.PROJ_NAME+'.front.pdf           -sDEVICE=pdfwrite           -dPDFSETTINGS=/printer           -dFIXEDMEDIA           -dDEVICEWIDTHPOINTS=504              -dDEVICEHEIGHTPOINTS=738             -c "<</PageOffset [-'+str(513+COVER_OFFSET)+' 0]>> setpagedevice"           -f '+SRC_FILE)

