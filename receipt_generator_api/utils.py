from reportlab.platypus  import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from .data import DATA


 

class GenerateReceipt:
    styles = getSampleStyleSheet()
    
    def __init__(self,data):
        self.data = data
    
    def convert(self):
        data=[]
        x=[]
        for i in self.data:
        
            x.append([i for i in i.keys()]) 
            data.append([y for y in i.values()])
        data.insert(0,x[0])
        return data
    
    def title(self):
        title_style = self.styles[ "Heading1" ]
        title_style.alignment = 1
        title = Paragraph( "Dakka Nig Lmt" , title_style )
        return title
    
    def construct_table(self):
        style = TableStyle(
        [
            ( "BOX" , ( 0, 0 ), ( -1, -1 ), 1 , colors.black ),
            ( "GRID" , ( 0, 0 ), ( 4 , 4 ), 1 , colors.black ),
            ( "BACKGROUND" , ( 0, 0 ), ( 3, 0 ), colors.gray ),
            ( "TEXTCOLOR" , ( 0, 0 ), ( -1, 0 ), colors.whitesmoke ),
            ( "ALIGN" , ( 0, 0 ), ( -1, -1 ), "CENTER" ),
            ( "BACKGROUND" , ( 0 , 1 ) , ( -1 , -1 ), colors.beige ),
        ]
    )   
        table = Table( self.convert() , style = style )
        return table
    
    def generate_pdf(self):
        x = []
        for  i in range (1,11):
            pdf = SimpleDocTemplate( f"receipt-{i}.pdf", pagesize = A4 )
            x.append(pdf)
            y = [i.build([ self.title() , self.construct_table() ]) for i in x]
        theList = [f"receipt-{i}.pdf" for i in range(1,11)]
        return theList