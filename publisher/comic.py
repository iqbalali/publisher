import os
from PyPDF2 import PdfFileReader

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
        print("Started",PROJ_NAME)
        
    def version(self):
        print("0.1.1")

    def dir_create(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)

    def create_pdf(self, context):
        for k, v in context.items():
            print(k,v)

    #Sharing
    def digital_lo(self, FILE_LIST, PUBLISH_FOLDER):
        self.dir_create(PUBLISH_FOLDER)
        os.system('gs -sDEVICE=pdfwrite -o '+PUBLISH_FOLDER+'/'+self.PROJ_NAME+'.digi-lo.pdf           -f '+FILE_LIST)
        print('Digital Lo created in',PUBLISH_FOLDER+'/'+self.PROJ_NAME)
        #self.cbz(PUBLISH_FOLDER+'/'+self.PROJ_NAME+'.digi-lo.pdf',PUBLISH_FOLDER)
        
    #Digital Files
    def digital_hi(self, FILE_LIST, PUBLISH_FOLDER, SIZE="default"):
        self.dir_create(PUBLISH_FOLDER)
        publish_file = PUBLISH_FOLDER+'/'+self.PROJ_NAME+'.digi-hi.pdf'
        if SIZE == "print":
            os.system('gs -sDEVICE=pdfwrite -dPDFSETTINGS=/printer -o '+publish_file+' \
            -dDEVICEWIDTHPOINTS=513 -dDEVICEHEIGHTPOINTS=738 -dFIXEDMEDIA -f '+FILE_LIST)
        else:
            os.system('gs -sDEVICE=pdfwrite -dPDFSETTINGS=/printer -o '+publish_file+' -f '+FILE_LIST)
            print('Digital-Hi created in',PUBLISH_FOLDER+'/'+self.PROJ_NAME)
    
    def digital_hi_new(self, FILE_LIST, PUBLISH_FOLDER):
        print('Running Digital')
        self.dir_create(PUBLISH_FOLDER)
        os.system('gs -sDEVICE=pdfwrite -dPDFSETTINGS=/printer -o '+PUBLISH_FOLDER+'/'+self.PROJ_NAME+'.digi-hi.pdf           -f '+FILE_LIST)
        print(': PDF for Digital')
        
    #CreateSpace
    def printer(self, FILE_LIST, PUBLISH_FOLDER):
        #Create directory
        self.dir_create(PUBLISH_FOLDER)
        #Publish location
        publish_file = PUBLISH_FOLDER+'/'+self.PROJ_NAME+'.print.pdf'
        #Create Temp file
        self.digital_hi(FILE_LIST, self.temp_folder, SIZE="print")
        #Create Print file from temp with the OFFSET for even pages
        os.system('gs -sDEVICE=pdfwrite -dPDFSETTINGS=/printer -o '+publish_file+' -c \
        "<< /CurrPageNum 1 def /Install \
        { /CurrPageNum CurrPageNum 1 add def CurrPageNum 2 mod 1 eq {0 0 translate} {9 0 translate} \
        ifelse } bind  >> setpagedevice" -f '+self.temp_folder+'/'+self.PROJ_NAME+'.digi-hi.pdf')
        #Remove temp file
        os.remove(self.temp_folder+'/'+self.PROJ_NAME+'.digi-hi.pdf')
        print('Print file created in',PUBLISH_FOLDER+'/'+self.PROJ_NAME)
        #Get spine width for the cover
        input1 = PdfFileReader(open(publish_file, 'rb'))
        number_pages = input1.getNumPages()
        spine_width = 0.162144*number_pages
        print("Number of pages:",number_pages)
        print("Spine width (Cover offset):",spine_width,"pt")

    #CBZ files for torrenting
    def cbz(self, SRC_FILE, PUBLISH_FOLDER):
        print(SRC_FILE)
        self.dir_create(PUBLISH_FOLDER)
        self.dir_create(PUBLISH_FOLDER+'/JPG')
        os.system('gs -sDEVICE=png16m -dJPEGQ=100 -dQFactor=1.0 -r300 -dPDFFitPage -o '+PUBLISH_FOLDER+'/JPG/%03d.jpg -f '+SRC_FILE)
        print('Created CBZ in',PUBLISH_FOLDER+'/'+self.PROJ_NAME)
        os.system('mogrify -resize '+self.CBZ+'x'+self.CBZ+' '+PUBLISH_FOLDER+'/JPG/*.jpg')
        os.system('zip -r '+PUBLISH_FOLDER+'/'+self.PROJ_NAME+'.cbz '+PUBLISH_FOLDER+'/JPG')
        os.system('mogrify  -fuzz 50% -trim +repage '+PUBLISH_FOLDER+'/JPG/*.jpg')

    #Web and email ready...
    def site(self, PUBLISH_FOLDER, WEBSITE_FOLDER):
        #os.rmdir(website_folder+self.PROJ_NAME.lower())
        self.dir_create(WEBSITE_FOLDER+self.PROJ_NAME.lower())
        os.system('rm -r '+WEBSITE_FOLDER+self.PROJ_NAME.lower()+'/*.jpg')
        os.system('cp -r '+PUBLISH_FOLDER+'/JPG '+WEBSITE_FOLDER+self.PROJ_NAME.lower()+'/')

        
    def front_cover(self, SRC_FILE, PUBLISH_FOLDER):
        self.dir_create(PUBLISH_FOLDER)
        
    def cover(self, SRC_FILE, PUBLISH_FOLDER, COVER_OFFSET):
        self.dir_create(PUBLISH_FOLDER)
        os.system('gs -o '+PUBLISH_FOLDER+'/'+self.PROJ_NAME+'.cs_cover.pdf -sDEVICE=pdfwrite \
        -dPDFSETTINGS=/printer -f '+SRC_FILE)
        os.system('gs -o '+PUBLISH_FOLDER+'/'+self.PROJ_NAME+'.front.pdf -sDEVICE=pdfwrite \
        -dPDFSETTINGS=/printer -dFIXEDMEDIA -dDEVICEWIDTHPOINTS=504 \
        -dDEVICEHEIGHTPOINTS=738 -c "<</PageOffset [-'+str(513+COVER_OFFSET)+' 0]>> \
        setpagedevice" -f '+SRC_FILE)
        print('Created Cover in',PUBLISH_FOLDER+'/'+self.PROJ_NAME)