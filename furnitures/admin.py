'''
CREATING A NEW DATABASE
-----------------------
Read explanation here: https://flask-sqlalchemy.palletsprojects.com/en/2.x/contexts/

In the terminal navigate to the project folder just above the miltontours package
Type 'python' to enter the python interpreter. You should see '>>>'
In python interpreter type the following (hitting enter after each line):
    from miltontours import db, create_app
    db.create_all(app=create_app())
The database should be created. Exit python interpreter by typing:
    quit()
Use DB Browser for SQLite to check that the structure is as expected before 
continuing.

ENTERING DATA INTO THE EMPTY DATABASE
-------------------------------------

# Option 1: Use DB Browser for SQLite
You can enter data directly into the cities or tours table by selecting it in
Browse Data and clicking the New Record button. The id field will be created
automatically. However be careful as you will get errors if you do not abide by
the expected field type and length. In particular the DateTime field must be of
the format: 2020-05-17 00:00:00.000000

# Option 2: Create a database seed function in an Admin Blueprint
See below. This blueprint needs to be enabled in __init__.py and then can be 
accessed via http://127.0.0.1:5000/admin/dbseed/
Database constraints mean that it can only be used on a fresh empty database
otherwise it will error. This blueprint should be removed (or commented out)
from the __init__.py after use.

Use DB Browser for SQLite to check that the data is as expected before 
continuing.
'''

from flask import Blueprint
from . import db
from .models import Category, Product, Order
import datetime


bp = Blueprint('admin', __name__, url_prefix='/admin/')

# function to put some seed data in the database
@bp.route('/dbseed/')
def dbseed():
    sofa = Category(name='Sofas', description='Couche, Lounge, Sofa', image='''sofas/SofaCategory.jpg''')
    table = Category(name='Tables & Desks', description='Table, Desk', image='''tables/TableCategory.jpg''')
    chair = Category(name='Chairs', description= 'Office Chair, Outdoor Chair', image='''chairs/ChairCategory.jpg''')
    wardrobe = Category(name='Wardrobes', description='Wardrobe, Cupboard', image='''wardrobes/WardrobeCategory.jpg''')
    bed = Category(name='Beds', description='Bed', image='''beds/BedCategory.jpg''')
    office = Category(name='Office', description='Office', image='''office/OfficeCategory.jpg''')
    bookcase = Category(name='Bookcases & Shelves', description='Bookcase, Shelf', image='''bookcases/BookcaseCategory.jpg''')
    outdoor = Category(name='Outdoor Furnitures', description='Outdoor Furniture', image='''outdoor/OutdoorCategory.jpg''')
      
    try:
        db.session.add(sofa)
        db.session.add(bed)
        db.session.add(bookcase)
        db.session.add(chair)
        db.session.add(table)
        db.session.add(wardrobe)
        db.session.add(office)
        db.session.add(outdoor)
        db.session.commit()
    except:
        return 'There was an issue adding the categories in dbseed function'

    # Sofa
    p1 = Product( name='3-seat sofa', short_description='Fabric 3 Seater Sofa Bed',\
        description='Fabric 3 Seater Sofa Bed',\
        image='''sofas/Sofa1.jpg''', price=1230, size='W 205cm X D 97cm X H 80cm', category_id= sofa.id)
    p2 = Product( name='2-seat sofa', short_description='Finlay 2 Seater Sofa',\
        description='Classic interior design, over hundred fabrics',\
        image='''sofas/Sofa2.jpg''', price=599, size='W 163cm x D 89cm x H 83cm', category_id= sofa.id)
    p3 = Product( name='Sofa set', short_description='Grey Sofa set',\
        description='Thick foam. The 3 piece suite is perfect for houses.',\
        image='''sofas/Sofa3.jpg''', price=2599, size='1 Seater: W 850cm x D 910cm x H 1010cm, 3 Seater: W 1990cmx D 910cm x H 1010cm', category_id= sofa.id)
    p4 = Product( name='3-seat sofa', short_description='Fabric 3 Seater Sofa Bed',\
        description='Fabric 3 Seater Sofa Bed',\
        image='''sofas/Sofa4.jpg''', price=1230, size='W 205cm X D 97cm X H 80cm', category_id= sofa.id)
    p5= Product( name='2-seat sofa', short_description='Finlay 2 Seater Sofa',\
        description='Classic interior design, over hundred fabrics',\
        image='''sofas/Sofa5.jpg''', price=599, size='W 163cm x D 89cm x H 83cm', category_id= sofa.id)
    p6= Product( name='Sofa set', short_description='Grey Sofa set',\
        description='Thick foam. The 3 piece suite is perfect for houses.',\
        image='''sofas/Sofa6.jpg''', price=2599, size='1 Seater: W 850cm x D 910cm x H 1010cm, 3 Seater: W 1990cmx D 910cm x H 1010cm', category_id= sofa.id)
    p7 = Product( name='3-seat sofa', short_description='Fabric 3 Seater Sofa Bed',\
        description='Fabric 3 Seater Sofa Bed',\
        image='''sofas/Sofa7.jpg''', price=1230, size='W 205cm X D 97cm X H 80cm', category_id= sofa.id)
    p8 = Product( name='2-seat sofa', short_description='Finlay 2 Seater Sofa',\
        description='Classic interior design, over hundred fabrics',\
        image='''sofas/Sofa8.jpg''', price=599, size='W 163cm x D 89cm x H 83cm', category_id= sofa.id)
    p9 = Product( name='Sofa set', short_description='Grey Sofa set',\
        description='Thick foam. The 3 piece suite is perfect for houses.',\
        image='''sofas/Sofa9.jpg''', price=2599, size='1 Seater: W 850cm x D 910cm x H 1010cm, 3 Seater: W 1990cmx D 910cm x H 1010cm', category_id= sofa.id)

    # Bed
    p10 = Product( name='Queen Bed', short_description='Wooden Queen Bed',\
        description='Wooden Queen Bed. Made with natural cotton',\
        image='''beds/Bed1.jpg''', price=2000, size='210 cm x 210 cm', category_id= bed.id)
    p11 = Product( name='King Bed', short_description='Japanese King Bed',\
        description='Japanese King Bed. Material: Solid Pine Wood',\
        image='''beds/Bed2.jpg''', price=2990, size='240 cm x 210 cm', category_id= bed.id)
    p12 = Product( name='Navy Bed', short_description='Double Bed',\
        description='Modern classic design. Non toxic paint',\
        image='''beds/Bed3.jpg''', price=1590, size='195 cm x 210 cm', category_id= bed.id)
    p13 = Product( name='Queen Bed', short_description='Wooden Queen Bed',\
        description='Wooden Queen Bed. Made with natural cotton',\
        image='''beds/Bed4.jpg''', price=2000, size='210 cm x 210 cm', category_id= bed.id)
    p14 = Product( name='King Bed', short_description='Japanese King Bed',\
        description='Japanese King Bed. Material: Solid Pine Wood',\
        image='''beds/Bed5.jpg''', price=2990, size='240 cm x 210 cm', category_id= bed.id)
    p15 = Product( name='Navy Bed', short_description='Double Bed',\
        description='Modern classic design. Non toxic paint',\
        image='''beds/Bed6.jpg''', price=1590, size='195 cm x 210 cm', category_id= bed.id)
    p16 = Product( name='Queen Bed', short_description='Wooden Queen Bed',\
        description='Wooden Queen Bed. Made with natural cotton',\
        image='''beds/Bed7.jpg''', price=2000, size='210 cm x 210 cm', category_id= bed.id)
    p17 = Product( name='King Bed', short_description='Japanese King Bed',\
        description='Japanese King Bed. Material: Solid Pine Wood',\
        image='''beds/Bed8.jpg''', price=2990, size='240 cm x 210 cm', category_id= bed.id)
    p18= Product( name='Navy Bed', short_description='Double Bed',\
        description='Modern classic design. Non toxic paint',\
        image='''beds/Bed9.jpg''', price=1590, size='195 cm x 210 cm', category_id= bed.id)
    
    # Bookcase
    p19 = Product(name='Ladder bookcase', short_description='White Ladder Bookcase',\
        description='Supper stylish; fabulous for the any rooms',\
        image='''bookcases/Bookcase1.jpg''', price=310, size='W 60cm X D 60cm X H 160cm', category_id= bookcase.id)
    p20 = Product(name='Classic bookcase', short_description='2 Drawer 4 Shelf Bookcase',\
        description='Natural variations in wood tone',\
        image='''bookcases/Bookcase2.jpg''', price=790, size='W 41cm X D 110cm X H 200cm', category_id= bookcase.id)
    p21 = Product(name='8-Cube Bookcase', short_description='8-Cube Bookcase Oak and Black',\
        description='Elegant design to compliment your room',\
        image='''bookcases/Bookcase3.jpg''', price=990, size='W 74cm X D 40cm X H 143cm', category_id= bookcase.id)
    p22 = Product(name='Ladder bookcase', short_description='White Ladder Bookcase',\
        description='Supper stylish; fabulous for the any rooms',\
        image='''bookcases/Bookcase4.jpg''', price=310, size='W 60cm X D 60cm X H 160cm', category_id= bookcase.id)
    p23 = Product(name='Classic bookcase', short_description='2 Drawer 4 Shelf Bookcase',\
        description='Natural variations in wood tone',\
        image='''bookcases/Bookcase5.jpg''', price=790, size='W 41cm X D 110cm X H 200cm', category_id= bookcase.id)
    p24 = Product(name='8-Cube Bookcase', short_description='8-Cube Bookcase Oak and Black',\
        description='Elegant design to compliment your room',\
        image='''bookcases/Bookcase6.jpg''', price=990, size='W 74cm X D 40cm X H 143cm', category_id= bookcase.id)
    p25 = Product(name='Ladder bookcase', short_description='White Ladder Bookcase',\
        description='Supper stylish; fabulous for the any rooms',\
        image='''bookcases/Bookcase7.jpg''', price=310, size='W 60cm X D 60cm X H 160cm', category_id= bookcase.id)
    p26 = Product(name='Classic bookcase', short_description='2 Drawer 4 Shelf Bookcase',\
        description='Natural variations in wood tone',\
        image='''bookcases/Bookcase8.jpg''', price=790, size='W 41cm X D 110cm X H 200cm', category_id= bookcase.id)
    p27 = Product(name='8-Cube Bookcase', short_description='8-Cube Bookcase Oak and Black',\
        description='Elegant design to compliment your room',\
        image='''bookcases/Bookcase9.jpg''', price=990, size='W 74cm X D 40cm X H 143cm', category_id= bookcase.id)

    # Chair
    p28 = Product(name='Gaming Chair', short_description='Red Gaming Chair',\
        description='Adjustable seat height; Comfortable and stylist design',\
        image='''chairs/Chair1.jpg''', price=299, size='W 68cm X D 70cm X H 132cm', category_id= chair.id)
    p29 = Product(name='Armchair', short_description='Grey with a plain wood frame',\
        description='This chair is super comfortable. It can be used in living areas, bedrooms or any small spaces.',\
        image='''chairs/Chair2.jpg''', price=140, size='W 68cm X D 60cm X H 94cm', category_id= chair.id)
    p30 = Product(name='Baby Chair', short_description='High Chair Feeding Table For Baby',\
        description='Height adjustable support rod. Easy installation and Disassembly ',\
        image='''chairs/Chair3.jpg''', price=400, size='Item Weight : 3 KG', category_id= chair.id)
    p31 = Product(name='Gaming Chair', short_description='Red Gaming Chair',\
        description='Adjustable seat height; Comfortable and stylist design',\
        image='''chairs/Chair4.jpg''', price=299, size='W 68cm X D 70cm X H 132cm', category_id= chair.id)
    p32 = Product(name='Armchair', short_description='Grey with a plain wood frame',\
        description='This chair is super comfortable. It can be used in living areas, bedrooms or any small spaces.',\
        image='''chairs/Chair5.jpg''', price=140, size='W 68cm X D 60cm X H 94cm', category_id= chair.id)
    p33 = Product(name='Baby Chair', short_description='High Chair Feeding Table For Baby',\
        description='Height adjustable support rod. Easy installation and Disassembly ',\
        image='''chairs/Chair6.jpg''', price=400, size='Item Weight : 3 KG', category_id= chair.id)
    p34 = Product(name='Gaming Chair', short_description='Red Gaming Chair',\
        description='Adjustable seat height; Comfortable and stylist design',\
        image='''chairs/Chair7.jpg''', price=299, size='W 68cm X D 70cm X H 132cm', category_id= chair.id)
    p35 = Product(name='Armchair', short_description='Grey with a plain wood frame',\
        description='This chair is super comfortable. It can be used in living areas, bedrooms or any small spaces.',\
        image='''chairs/Chair8.jpg''', price=140, size='W 68cm X D 60cm X H 94cm', category_id= chair.id)
    p36 = Product(name='Baby Chair', short_description='High Chair Feeding Table For Baby',\
        description='Height adjustable support rod. Easy installation and Disassembly ',\
        image='''chairs/Chair9.jpg''', price=400, size='Item Weight : 3 KG', category_id= chair.id)

    # Table & Desk
    p37 = Product(name='Study Desk', short_description='Wooden Brown Study Desk',\
        description='Good design with plenty of storage',\
        image='''tables/Table1.jpg''', price=300, size='W 60cm x D 12cm x H 140cm', category_id= table.id)
    p38 = Product(name='Dining Table', short_description='Rectangular Dining Table',\
        description='A big dining table fits up to 8 persons',\
        image='''tables/Table2.jpg''', price=709, size='W 210cm X D 105cm X H 77cm', category_id= table.id)
    p39 = Product(name='Computer Desk', short_description='Desk with Shelves & Drawers (Black)',\
        description='Modern design with multiple shelves and spacious drawers',\
        image='''tables/Table3.jpg''', price=499, size='W 50cm X L 120cm X H 1430cm', category_id= table.id)
    p40 = Product(name='Study Desk', short_description='Wooden Brown Study Desk',\
        description='Good design with plenty of storage',\
        image='''tables/Table4.jpg''', price=300, size='W 60cm x D 12cm x H 140cm', category_id= table.id)
    p41 = Product(name='Dining Table', short_description='Rectangular Dining Table',\
        description='A big dining table fits up to 8 persons',\
        image='''tables/Table5.jpg''', price=709, size='W 210cm X D 105cm X H 77cm', category_id= table.id)
    p42 = Product(name='Computer Desk', short_description='Desk with Shelves & Drawers (Black)',\
        description='Modern design with multiple shelves and spacious drawers',\
        image='''tables/Table6.jpg''', price=499, size='W 50cm X L 120cm X H 1430cm', category_id= table.id)
    p43 = Product(name='Study Desk', short_description='Wooden Brown Study Desk',\
        description='Good design with plenty of storage',\
        image='''tables/Table7.jpg''', price=300, size='W 60cm x D 12cm x H 140cm', category_id= table.id)
    p44 = Product(name='Dining Table', short_description='Rectangular Dining Table',\
        description='A big dining table fits up to 8 persons',\
        image='''tables/Table8.jpg''', price=709, size='W 210cm X D 105cm X H 77cm', category_id= table.id)
    p45 = Product(name='Computer Desk', short_description='Desk with Shelves & Drawers (Black)',\
        description='Modern design with multiple shelves and spacious drawers',\
        image='''tables/Table9.jpg''', price=499, size='W 50cm X L 120cm X H 1430cm', category_id= table.id)
    
    # Wardrobe
    p46 = Product(name='Wardrobe Shelving', short_description='White Wardrobe Shelving',\
        description='Easy to assemble.',\
        image='''wardrobes/Wardrobe1.jpg''', price=4800, size='W 45cm X D 20cm X H 240cm', category_id= wardrobe.id)
    p47 = Product(name='3 Doors Wardrobe', short_description='Classic Wooden Wardrobe',\
        description='Includes 5 shelves and one hanging rail.',\
        image='''wardrobes/Wardrobe2.jpg''', price=600, size='W 155cm X L 62cm X H 200cm', category_id= wardrobe.id)
    p48 = Product(name='4 doors Cupboard', short_description='4 Doors 2 Drawers Cupboard',\
        description='4 Doors hanging space above drawers, with Mirrors',\
        image='''wardrobes/Wardrobe3.jpg''', price=1200, size='W 160cm X D 52cm X H 192cm', category_id= wardrobe.id)
    p49 = Product(name='Wardrobe Shelving', short_description='White Wardrobe Shelving',\
        description='Easy to assemble.',\
        image='''wardrobes/Wardrobe4.jpg''', price=4800, size='W 45cm X D 20cm X H 240cm', category_id= wardrobe.id)
    p50 = Product(name='3 Doors Wardrobe', short_description='Classic Wooden Wardrobe',\
        description='Includes 5 shelves and one hanging rail.',\
        image='''wardrobes/Wardrobe5.jpg''', price=600, size='W 155cm X L 62cm X H 200cm', category_id= wardrobe.id)
    p51 = Product(name='4 Doors Cupboard', short_description='4 Doors 2 Drawers Cupboard',\
        description='4 doors hanging space above drawers, with Mirrors',\
        image='''wardrobes/Wardrobe6.jpg''', price=1200, size='W 160cm X D 52cm X H 192cm', category_id= wardrobe.id)
    p52 = Product(name='Wardrobe Shelving', short_description='White Wardrobe Shelving',\
        description='Easy to assemble.',\
        image='''wardrobes/Wardrobe7.jpg''', price=4800, size='W 45cm X D 20cm X H 240cm', category_id= wardrobe.id)
    p53 = Product(name='3 Doors Wardrobe', short_description='Classic Wooden Wardrobe',\
        description='Includes 5 shelves and one hanging rail.',\
        image='''wardrobes/Wardrobe8.jpg''', price=600, size='W 155cm X L 62cm X H 200cm', category_id= wardrobe.id)
    p54 = Product(name='2 Drawers Cupboard', short_description='Big Size Cupboard with Mirror',\
        description='4 doors hanging space above drawers, with Mirrors',\
        image='''wardrobes/Wardrobe9.jpg''', price=1200, size='W 160cm X D 52cm X H 192cm', category_id= wardrobe.id)
    
    # Office
    p55 = Product(name='Workstation Desks', short_description='4-Person Workstation Desks',\
        description='The perfect open plan office desk option for 4 persons ',\
        image='''office/Office1.jpg''', price=1999, size='Height: 74cm, Total length: 240cm, Total width: 163cm, Table top thickness: 2.5cm', category_id= office.id)
    p56 = Product(name='Corner Desk', short_description='Corner Workstation Black Walnut',\
        description='The shelf\'s weight capacity is 10 kg and the desktop\'s is 55 kg',\
        image='''office/Office2.jpg''', price=349, size='(W 150cm x D 150cm) x D 50cm x H 74cm', category_id= office.id)
    p57 = Product(name='Office Shelving', short_description='A freestanding shelving with storage',\
        description='Universal Office Storage Shelving Shelves Racks',\
        image='''office/Office3.jpg''', price=790, size='W 260cm X D 45cm X H 190cm', category_id= office.id)
    p58 = Product(name='Workstation Desks', short_description='4-Person Workstation Desks',\
        description='The perfect open plan office desk option for 4 persons ',\
        image='''office/Office4.jpg''', price=1999, size='Height: 74cm, Total length: 240cm, Total width: 163cm, Table top thickness: 2.5cm', category_id= office.id)
    p59 = Product(name='Corner Desk', short_description='Corner Workstation Black Walnut',\
        description='The shelf\'s weight capacity is 10 kg and the desktop\'s is 55 kg',\
        image='''office/Office5.jpg''', price=349, size='(W 150cm x D 150cm) x D 50cm x H 74cm', category_id= office.id)
    p60 = Product(name='Office Shelving', short_description='A freestanding shelving with storage',\
        description='Universal Office Storage Shelving Shelves Racks',\
        image='''office/Office6.jpg''', price=790, size='W 260cm X D 45cm X H 190cm', category_id= office.id)
    p61 = Product(name='Workstation Desks', short_description='4-Person Workstation Desks',\
        description='The perfect open plan office desk option for 4 persons ',\
        image='''office/Office7.jpg''', price=1999, size='Height: 74cm, Total length: 240cm, Total width: 163cm, Table top thickness: 2.5cm', category_id= office.id)
    p62 = Product(name='Corner Desk', short_description='Corner Workstation Black Walnut',\
        description='The shelf\'s weight capacity is 10 kg and the desktop\'s is 55 kg',\
        image='''office/Office8.jpg''', price=349, size='(W 150cm x D 150cm) x D 50cm x H 74cm', category_id= office.id)
    p63 = Product(name='Office Shelving', short_description='A wooden shelving with big storage',\
        description='Universal Office Storage Shelving Shelves Racks',\
        image='''office/Office9.jpg''', price=790, size='W 260cm X D 45cm X H 190cm', category_id= office.id)

    # Outdoor
    p64 = Product(name='Garden Sunbed', short_description='Round Sunbed With Seat Cushion',\
        description='This outdoor funiture is perfect for casual rest and entertaining inside and outside',\
        image='''outdoor/Outdoor1.jpg''', price=1790, size='Diameter in circle: 28, 25, 22, 19, 16', category_id= outdoor.id)
    p65 = Product(name='Hanging Chair', short_description='Garden Hanging Chair Swings',\
        description='Waterproof, Resistant from outdoor rain, sunshine, snow, etc',\
        image='''outdoor/Outdoor2.jpg''', price=190, size='H 4m x W 2.5m', category_id= outdoor.id)
    p66 = Product(name='Lounge Set', short_description='5-seater L shape Outdoor Lounge',\
        description='Made of PE wicker and aluminium. Cushion covers: Water-resistant and UV resistant polyester.',\
        image='''outdoor/Outdoor3.jpg''', price=1359, size='2x Middle Sofas : W70xD82xH67cm; 3x Corner Sofas : W82xD82xH67cm; 1x Square Shape Coffee Table : W70xD70xH30cm', category_id= outdoor.id)
    p67 = Product(name='Garden Sunbed', short_description='Round Sunbed With Seat Cushion',\
        description='This outdoor funiture is perfect for casual rest and entertaining inside and outside',\
        image='''outdoor/Outdoor4.jpg''', price=1790, size='Diameter in circle: 28, 25, 22, 19, 16', category_id= outdoor.id)
    p68 = Product(name='Hanging Chair', short_description='Garden Hanging Chair Swings',\
        description='Waterproof, Resistant from outdoor rain, sunshine, snow, etc',\
        image='''outdoor/Outdoor5.jpg''', price=190, size='H 4m x W 2.5m', category_id= outdoor.id)
    p69 = Product(name='Lounge Set', short_description='5-seater L shape Outdoor Lounge',\
        description='Made of PE wicker and aluminium. Cushion covers: Water-resistant and UV resistant polyester.',\
        image='''outdoor/Outdoor6.jpg''', price=1359, size='2x Middle Sofas : W70xD82xH67cm; 3x Corner Sofas : W82xD82xH67cm; 1x Square Shape Coffee Table : W70xD70xH30cm', category_id= outdoor.id)
    p70 = Product(name='Garden Sunbed', short_description='Round Sunbed With Seat Cushion',\
        description='This outdoor funiture is perfect for casual rest and entertaining inside and outside',\
        image='''outdoor/Outdoor7.jpg''', price=1790, size='Diameter in circle: 28, 25, 22, 19, 16', category_id= outdoor.id)
    p71 = Product(name='Hanging Chair', short_description='Garden Hanging Chair Swings',\
        description='Waterproof, Resistant from outdoor rain, sunshine, snow, etc',\
        image='''outdoor/Outdoor8.jpg''', price=190, size='H 4m x W 2.5m', category_id= outdoor.id)
    p72 = Product(name='Lounge Set', short_description='5-seater L shape Outdoor Lounge',\
        description='Made of PE wicker and aluminium. Cushion covers: Water-resistant and UV resistant polyester.',\
        image='''outdoor/Outdoor9.jpg''', price=1359, size='2x Middle Sofas : W70xD82xH67cm; 3x Corner Sofas : W82xD82xH67cm; 1x Square Shape Coffee Table : W70xD70xH30cm', category_id= outdoor.id)
    try:
        db.session.add(p1)
        db.session.add(p2)
        db.session.add(p3)
        db.session.add(p4)
        db.session.add(p5)
        db.session.add(p6)
        db.session.add(p7)
        db.session.add(p8)
        db.session.add(p9)
        db.session.add(p10)
        db.session.add(p11)
        db.session.add(p12)
        db.session.add(p13)
        db.session.add(p14)
        db.session.add(p15)
        db.session.add(p16)
        db.session.add(p17)
        db.session.add(p18)
        db.session.add(p19)
        db.session.add(p20)
        db.session.add(p21)
        db.session.add(p22)
        db.session.add(p23)
        db.session.add(p24)
        db.session.add(p25)
        db.session.add(p26)
        db.session.add(p27)
        db.session.add(p28)
        db.session.add(p29)
        db.session.add(p30)
        db.session.add(p31)
        db.session.add(p32)
        db.session.add(p33)
        db.session.add(p34)
        db.session.add(p35)
        db.session.add(p36)
        db.session.add(p37)
        db.session.add(p38)
        db.session.add(p39)
        db.session.add(p40)
        db.session.add(p41)
        db.session.add(p42)
        db.session.add(p43)
        db.session.add(p44)
        db.session.add(p45)
        db.session.add(p46)
        db.session.add(p47)
        db.session.add(p48)
        db.session.add(p49)
        db.session.add(p50)
        db.session.add(p51)
        db.session.add(p52)
        db.session.add(p53)
        db.session.add(p54)
        db.session.add(p55)
        db.session.add(p56)
        db.session.add(p57)
        db.session.add(p58)
        db.session.add(p59)
        db.session.add(p60)
        db.session.add(p61)
        db.session.add(p62)
        db.session.add(p63)
        db.session.add(p64)
        db.session.add(p65)
        db.session.add(p66)
        db.session.add(p67)
        db.session.add(p68)
        db.session.add(p69)
        db.session.add(p70)
        db.session.add(p71)
        db.session.add(p72)
        db.session.commit()
    except:
        return 'There was an issue adding a product in dbseed function'

    return 'DATA LOADED'


