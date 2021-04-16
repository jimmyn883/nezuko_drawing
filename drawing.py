''' Purpose: demonstrate simple drawing commands '''

# Below is code made using Pillow package on Pycharm !

from PIL import Image, ImageDraw, ImageFont


def picture():

    # replace dimensions and background as you see fit
    WIDTH  = 575
    HEIGHT = 600

    DIMENSIONS = [ WIDTH, HEIGHT]


    BACKGROUND_COLOR = "darkblue"

    # create image of appropriate size
    im = Image.new( 'RGB', DIMENSIONS, BACKGROUND_COLOR )

    # get a drawable canvas of image im
    canvas = ImageDraw.Draw( im )



    # put your drawing commands here

    '''
    background
    '''
    # GROUND
    x = 0
    y = 450
    w = 600
    h = 200
    xy = [(x, y), (x + w, y + h)]
    canvas.rectangle(xy, fill='darkgreen', outline='black')

    # tree back, middle
    x = 200
    y = 0
    w = 30
    h = 450
    xy = [(x, y), (x + w, y + h)]
    canvas.rectangle(xy, fill='saddlebrown', outline='black')

    # tree back, middle
    x = 300
    y = 0
    w = 40
    h = 470
    xy = [(x, y), (x + w, y + h)]
    canvas.rectangle(xy, fill='saddlebrown', outline='black')


    # tree back, right
    x = 500
    y = 0
    w = 50
    h = 500
    xy = [(x, y), (x + w, y + h)]
    canvas.rectangle(xy, fill='saddlebrown', outline='black')

    # tree front, right behind head
    p0 = (450, 0)
    p1 = (500, 560)
    p2 = (450, 560)
    p3 = (400, 0)
    seq = [p0, p1, p2, p3]
    canvas.polygon(seq, fill='saddlebrown', outline='black')


    # tree front, left
    p0 = (50, 0)
    p1 = (0,580)
    p2 = (100, 580)
    p3 = (150, 0)
    seq = [p0, p1, p2, p3]
    canvas.polygon(seq, fill = 'saddlebrown', outline  = 'black')




    '''
      HAIR
      '''
    # Circle of hair behind head
    x = 310
    y = 135
    w = 145
    h = 140
    xy = [(x, y), (x + w, y + h)]
    canvas.ellipse(xy, fill=(30, 30, 30), outline='black')


    # HIGHEST Hair
    # top of hair
    p0 = (385, 135)
    p1 = (380, 134)
    p2 = (350, 139)
    p3 = (340, 143)
    p4 = (330, 150)
    p5 = (320, 160)
    p6 = (310, 170)
    # first dip
    p7 = (285, 205)
    p8 = (270, 210)
    p9 = (275, 210)
    # first hump
    p10 = (215, 215)
    p11 = (200, 220)
    p12 = (185, 230)
    # second dip
    p13 = (165, 238)
    p14 = (150, 241)
    p15 = (135, 239)
    # second hump (START red)
    p16 = (100, 235)
    p17 = (90, 235)
    p18 = (80, 238)
    # end point to hair
    p19 = (50, 300)
    # bottom side of hair (END red after these two)
    p20 = (80, 280)
    p21 = (90, 275)
    # bottom point right of hair (connects to ear)
    p22 = (175, 298)
    p23 = (400, 300)
    seq = [p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23]
    canvas.polygon(seq, fill = (30, 30, 30), outline = 'black')


    # Hair on Top 1
    p0 = (295, 210)
    # first dip
    p1 = (235, 230)
    p2 = (225, 230)
    # first hump (START red)
    p3 = (165, 220)
    p4 = (155, 220)
    p5 = (130, 230)
    # end point to hair
    p6 = (105, 255)
    # bottom side of hair (END red after p9)
    p7 = (130, 240)
    p8 = (155, 235)
    p9 = (165, 235)
    p10 = (215, 260)
    p11 = (295, 240)
    seq = [p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11]
    canvas.polygon( seq, fill = (30, 30, 30), outline = 'black')


    # Hair on Top 2
    p0 = (315, 220)
    # first dip
    p1 = (235, 245)
    p2 = (225, 248)
    p3 = (215, 248)
    p4 = (208, 246)
    p5 = (205, 245)
    p6 = (195, 244)
    # first half of big dip
    p7 = (160, 254)
    p8 = (150, 255)
    # second-half of big dip (red)
    p9 = (130, 255)
    p10 = (110, 254)
    p11 = (75, 234)
    p12 = (65, 228)
    p13 = (62, 225)
    # first hair spike curled up
    p14 = (50, 225)
    p15 = (50, 200)
    p16 = (47, 200)
    p17 = (30, 228)
    p18 = (30, 233)
    p19 = (45, 245)
    # start second hair
    p20 = (35, 245)
    p21 = (25, 240)
    p22 = (20, 230)
    p23 = (18, 250)
    p24 = (30, 260)
    # start 3rd hair
    p25 = (17, 266)
    p26 = (13, 270)
    p27 = (8, 280)
    p28 = (18, 270)
    p29 = (19, 270)
    # start 4th hair
    p30 = (15, 275)
    p31 = (12, 280)
    p32 = (10, 295)
    p33 = (13, 290)
    p34 = (25, 280)
    # underside upward curve
    p35 = (35, 275)
    p36 = (70, 272)
    p37 = (130, 280)
    p38 = (160, 275)
    p39 = (175, 273)
    # back trace for 5th hair
    p40 = (130, 280)
    p41 = (70, 272)
    p42 = (50, 285)
    p43 = (40, 295)
    p44 = (38, 310)
    p45 = (43, 315)
    p46 = (48, 310)
    # underside of entire hair (END red after p47
    p47 = (130, 300)
    p48 = (175, 298)
    p49 = (200, 270)
    p50 = (300, 265)
    p51 = (325, 240)
    p52 = (333, 232)
    p53 = (340, 232)
    seq = [p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26, p27, p28,p29, p30, p31, p32, p33, p34, p35, p36, p37, p38, p39, p40, p41, p42, p43, p44, p45, p46, p47, p48, p49, p50, p51, p52, p53]
    canvas.polygon(seq, fill=(30, 30, 30), outline='black')


    # Hair in front of face on botton
    p0 = (452, 220)
    p1 = (470, 248)
    p2 = (470, 300)
    p3 = (400, 300)
    p4 = (400, 180)
    seq = [p0, p1, p2, p3, p4]
    canvas.polygon( seq , fill=(30, 30, 30), outline='black')


    # Hair in front of face on top
    p0 = (448, 235)
    p1 = (455, 245)
    p2 = (460, 248)
    p3 = (470, 248)
    p4 = (480, 250)
    p5 = (500, 265)
    p6 = (480, 240)
    p7 = (470, 238)
    p8 = (460, 228)
    p9 = (452, 220)
    seq = [p0, p1, p2, p3, p4, p5, p6, p7, p8, p9]
    canvas.polygon(seq, fill=(30, 30, 30), outline='black')



    '''
    HAIR COLORED RED
    '''
    # HIGHEST Hair
    # second hump (START red)
    p13 = (165, 238)
    p14 = (150, 241)
    p15 = (135, 239)
    p16 = (100, 235)
    p17 = (90, 235)
    p18 = (80, 238)
    # end point to hair
    p19 = (50, 300)
    # bottom side of hair (END red after these two)
    p20 = (80, 280)
    p21 = (90, 275)
    seq = [p13, p14, p15, p16, p17, p18, p19, p20, p21]
    canvas.polygon(seq, fill='darkorange', outline='black')


    # Hair on Top 1
    # first hump (START red)
    p3 = (165, 220)
    p4 = (155, 220)
    p5 = (130, 230)
    # end point to hair
    p6 = (105, 255)
    # bottom side of hair (END red after p9)
    p7 = (130, 240)
    p8 = (155, 235)
    p9 = (165, 235)
    seq = [p3, p4, p5, p6, p7, p8, p9]
    canvas.polygon(seq, fill='darkorange', outline='black')


    # Hair on Top 2
    # second-half of big dip (red)
    p9 = (130, 255)
    p10 = (110, 254)
    p11 = (75, 234)
    p12 = (65, 228)
    p13 = (62, 226)
    # first hair spike curled up
    p14 = (54, 222)
    p15 = (50, 200)
    p16 = (47, 200)
    p17 = (30, 228)
    p18 = (30, 233)
    p19 = (45, 245)
    # start second hair
    p20 = (35, 245)
    p21 = (25, 240)
    p22 = (20, 230)
    p23 = (18, 250)
    p24 = (30, 260)
    # start 3rd hair
    p25 = (17, 266)
    p26 = (13, 270)
    p27 = (8, 280)
    p28 = (18, 270)
    p29 = (19, 270)
    # start 4th hair
    p30 = (15, 275)
    p31 = (12, 280)
    p32 = (10, 295)
    p33 = (13, 290)
    p34 = (25, 280)
    # underside upward curve
    p35 = (35, 275)
    p36 = (70, 272)
    p37 = (130, 280)
    p38 = (160, 275)
    p39 = (175, 273)
    # back trace for 5th hair
    p40 = (130, 280)
    p41 = (70, 272)
    p42 = (50, 285)
    p43 = (40, 295)
    p44 = (38, 310)
    p45 = (43, 315)
    p46 = (48, 310)
    p47 = (130, 300)
    p48 = (175, 298)
    seq = [p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26, p27, p28,p29, p30, p31, p32, p33, p34, p35, p36, p37, p38, p39, p40, p41, p42, p43, p44, p45, p46, p47, p48]
    canvas.polygon(seq, fill='darkorange', outline='black')



    '''
    HAIR FLOWER
    '''
    # first petal
    p0 = (450, 180)
    p1 = (455, 170)
    p2 = (455, 160)
    p3 = (460, 170)
    p4 = (460, 183)
    p5 = (458, 188)
    # second petal
    p6 = (460, 183)
    p7 = (465, 178)
    p8 = (465, 185)
    p9 = (463, 193)
    p10 = (460, 196)
    p11 = (454, 200)
    seq = [p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11]
    canvas.polygon(seq, fill=(255, 213, 239), outline='Hotpink')



    '''
    WHITE PART OF HER FACE
    '''
    # top left face
    p0 = (350, 180)
    # middle top face
    p1 = (390, 182)
    # top right face
    p2 = (420, 185)
    p3 = (430, 187)
    p4 = (440, 191)
    p5 = (445, 198)
    # bottom right face
    p6 = (435, 240)
    p7 = (430, 250)
    p8 = (425, 255)
    p9 = (415, 262)
    # middle bottom face
    p10 = (390, 265)
    # bottom left face
    p11 = (360, 262)
    p12 = (340, 255)
    p13 = (325, 240)
    p14 = (333, 232)
    p15 = (340, 232)
    seq = [p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15]
    canvas.polygon(seq, fill='OldLace', outline='black')



    '''
    CHEEK BLUSH
    '''
    # left cheek blush
    x = 350
    y = 230
    w = 20
    h = 20
    xy = [(x, y), (x + w, y + h)]
    canvas.ellipse(xy, fill=(255, 232, 230))
    # right cheek blush
    x = 414
    y = 233
    w = 19
    h = 19
    xy = [(x, y), (x + w, y + h)]
    canvas.ellipse(xy, fill=(255, 232, 230))



    '''
    EYES
    '''
    # left eye
    for x in range(370, 378):
        for y in range(220, 232):
            seq = [x, y]
            canvas.point(seq, fill='Black')
    # right eye
    for x in range(420, 428):
        for y in range(220, 232):
            seq = [x, y]
            canvas.point(seq, fill='Black')
    # left eye lash
    x = 378
    y = 216
    w = 3
    h = 3
    xy = [(x, y), (x + w, y + h)]
    canvas.rectangle(xy, fill='Black')
    # right eye lash
    x = 428
    y = 216
    w = 3
    h = 3
    xy = [(x, y), (x + w, y + h)]
    canvas.rectangle(xy, fill='Black')
    # left eyebrow
    # top of left eyebrow
    p0 = (358, 203)
    p1 = (368, 198)
    p2 = (378, 198)
    # bottom of left eyebrow
    p3 = (378, 197)
    p4 = (368, 197)
    p5 = (358, 202)
    seq = [p0, p1, p2, p3, p4, p5]
    canvas.polygon(seq, fill='black')
    # right eyebrow
    # top of right eyebrow
    p0 = (413, 203)
    p1 = (423, 198)
    p2 = (433, 198)
    # bottom of right eyebrow
    p3 = (433, 197)
    p4 = (423, 197)
    p5 = (413, 202)
    seq = [p0, p1, p2, p3, p4, p5]
    canvas.polygon(seq, fill='black')



    '''
    BACK FOOT SOCKS
    '''

    # highest sock
    x = 320
    y = 430
    w = 40
    h = 30
    xy = [(x, y), (x + w, y + h)]
    canvas.ellipse(xy, fill=(50, 50, 50))

    # second highest sock
    x = 315
    y = 444
    w = 50
    h = 30
    xy = [(x, y), (x + w, y + h)]
    canvas.ellipse(xy, fill=(50, 50, 50))

    # third highest sock
    x = 283
    y = 455
    w = 90
    h = 30
    xy = [(x, y), (x + w, y + h)]
    canvas.ellipse(xy, fill=(50, 50, 50))

    # 2nd lowest to left
    x = 285
    y = 465
    w = 70
    h = 30
    xy = [(x, y), (x + w, y + h)]
    canvas.ellipse(xy, fill=(50, 50, 50))

    # lowest sock to right (round)
    x = 295
    y = 463
    w = 60
    h = 40
    xy = [(x, y), (x + w, y + h)]
    canvas.ellipse(xy, fill=(50, 50, 50))



    '''
    LEGS
    '''
    p0 = (310, 370)
    p1 = (340, 450)
    p2 = (370, 540)
    p3 = (410, 530)
    p4 = (385, 450)
    p5 = (350, 370)
    seq = [p0, p1, p2, p3, p4, p5]
    canvas.polygon(seq, fill='OldLace', outline='black')



    '''
    SHIRT
    '''
    # right side of shirt BOTTOM PORTION
    p0 = (330, 280)
    p1 = (350, 270)
    p2 = (380, 260)
    p3 = (430, 285)
    # bottom of shirt, top right curve
    p4 = (430, 380)
    p5 = (510, 380)
    p6 = (518, 398)
    p7 = (520, 410)
    # bottom of shirt, underside curve
    p8 = (500, 440)
    p9 = (480, 465)
    p10 = (460, 478)
    p11 = (440, 480)
    p12 = (420, 478)
    p13 = (390, 465)
    p14 = (320, 380)
    seq = [p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14,]
    canvas.polygon(seq, fill= 'mistyrose', outline = 'Hotpink')


    # left side of shirt BOTTOM PORTION
    p0 = (320, 380)
    p1 = (50, 380)
    p2 = (40, 390)
    # left most curve of shirt
    p3 = (30, 415)
    p4 = (19, 430)
    p5 = (20, 435)
    # first low
    p6 = (80, 465)
    p7 = (100, 469)
    p8 = (120, 468)
    # first high
    p9 = (200, 450)
    p10 = (220, 450)
    # second low
    p11 = (290, 460)
    p12 = (300, 460)
    p13 = (320, 458)
    p14 = (330, 455)
    p15 = (345, 445)
    p16 = (360, 430)
    seq = [p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16]
    canvas.polygon( seq , fill= 'mistyrose', outline = 'Hotpink')


    # right side of shirt TOP PORTION
    p0 = (330, 280)
    p1 = (350, 270)
    p2 = (380, 260)
    p3 = (430, 285)
    # bottom of shirt, top right curve
    p4 = (430, 380)
    p5 = (500, 390)
    p6 = (508, 398)
    p7 = (508, 410)
    # bottom of shirt, underside curve
    p8 = (500, 420)
    p9 = (480, 445)
    p10 = (460, 458)
    p11 = (440, 460)
    p12 = (420, 458)
    p13 = (390, 445)
    p14 = (320, 380)
    seq = [p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, ]
    canvas.polygon(seq, fill='pink', outline='Hotpink')


    # left side of shirt TOP PORTION
    p0 = (320, 380)
    p1 = (70, 380)
    p2 = (60, 390)
    # left most curve of shirt
    p3 = (50, 415)
    p4 = (39, 425)
    p5 = (40, 430)
    # first low
    p6 = (80, 445)
    p7 = (100, 449)
    p8 = (120, 448)
    # first high
    p9 = (200, 430)
    p10 = (220, 430)
    # second low
    p11 = (290, 440)
    p12 = (300, 440)
    p13 = (320, 438)
    p14 = (330, 435)
    p15 = (345, 425)
    p16 = (350, 418)
    seq = [p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16]
    canvas.polygon(seq, fill='pink', outline='Hotpink')



    '''
    neck/chest outside of shirt
    '''
    p0 = (325, 266)
    p1 = (425, 333)
    xy = [p0, p1]
    a1 = 230
    a2 = 315
    canvas.pieslice(xy, a1, a2, fill='OldLace', outline='Hotpink')

    p0 = (400, 282)
    p1 = (335, 325)
    xy = [p0, p1]
    canvas.line(xy, fill='hotpink')



    '''
    Green waist
    '''
    # top of band
    p0 = (325, 330)
    p1 = (400, 330)
    p2 = (430, 325)
    # bottom of band
    p3 = (430, 335)
    p4 = (400, 343)
    p5 = (324, 338)
    seq = [p0, p1, p2, p3, p4, p5]
    canvas.polygon(seq, fill='green', outline='black')



    '''
    white band on stomach
    '''
    # top of band (starting from top right)
    p0 = (430, 335)
    p1 = (400, 343)
    p2 = (324, 338)
    # bottom of band (starting from left)
    p3 = (320, 380)
    p4 = (340, 395)
    p5 = (370, 410)
    p6 = (380, 413)
    p7 = (405, 411)
    p8 = (415, 408)
    p9 = (430, 400)
    seq = [p0, p1, p2, p3, p4, p5, p6, p7, p8, p9]
    canvas.polygon(seq, fill='white', outline='black')



    '''
    STOMACH CHECKERS
    '''
    # top right
    p0 = (430, 335)
    p1 = (400, 343)
    p2 = (400, 365)
    p3 = (430, 365)
    seq = [p0, p1, p2, p3]
    canvas.polygon(seq, fill='lightcoral', outline='black')

    # Top left
    p0 = (370, 342)
    p1 = (340, 340)
    p2 = (340, 365)
    p3 = (370, 365)
    seq = [p0, p1, p2, p3]
    canvas.polygon(seq, fill='lightcoral', outline='black')

    # middle left
    p0 = (340, 365)
    p1 = (310, 375)
    p2 = (310, 373)
    p3 = (340, 395)
    seq = [p0, p1, p2, p3]
    canvas.polygon(seq, fill='lightcoral', outline='black')

    # middle middle
    p0 = (370, 365)
    p1 = (400, 365)
    p2 = (400, 395)
    p3 = (370, 395)
    seq = [p0, p1, p2, p3]
    canvas.polygon(seq, fill='lightcoral', outline='black')

    # middle right
    p0 = (430, 365)
    p1 = (460, 365)
    p2 = (460, 395)
    p3 = (430, 395)
    seq = [p0, p1, p2, p3]
    canvas.polygon(seq, fill='lightcoral', outline='black')

    #bottom right
    p0 = (400, 395)
    p1 = (430, 395)
    p2 = (430, 400)
    p3 = (411, 409)
    p4 = (403, 411)
    p5 = (400, 410)
    seq = [p0, p1, p2, p3, p4, p5]
    canvas.polygon(seq, fill='lightcoral', outline='black')

    # bottom right
    p0 = (370, 395)
    p1 = (340, 395)
    p2 = (340, 395)
    p3 = (370, 409)

    seq = [p0, p1, p2, p3]
    canvas.polygon(seq, fill='lightcoral', outline='black')



    '''
    orange knot
    '''
    # band across waist
    x = 320
    y = 365
    w = 150
    h = 15
    xy = [(x, y), (x + w, y + h)]
    canvas.rectangle(xy, fill='orange', outline='black')
    # circular knot in center
    x = 375
    y = 360
    w = 25
    h = 25
    xy = [(x, y), (x + w, y + h)]
    canvas.ellipse(xy, fill='orange', outline='black')



    '''
    BROWN COAT
    '''
    # Right side brown coat underneath
    # top right
    p0 = (525, 370)
    p1 = (550, 390)
    # Underside
    p2 = (540, 385)
    p3 = (520, 383)
    p4 = (510, 385)
    p5 = (480, 390)
    p6 = (430, 400)
    p7 = (420, 350)
    seq = [p0, p1, p2, p3, p4, p5, p6, p7]
    canvas.polygon(seq, fill=(50, 50, 50), outline='black')

    # Right Side Brown Coat
    p0 = (410, 270)
    p1 = (490, 310)
    # backtrace
    p2 = (430, 280)
    # bahind bulge of coat
    p3 = (460, 285)
    p4 = (470, 285)
    p5 = (490, 290)
    p6 = (500, 295)
    p7 = (520, 310)
    # right side curve
    p8 = (525, 312)
    p9 = (540, 330)
    p10 = (540, 350)
    p11 = (525, 370)
    p12 = (440, 370)
    p13 = (420, 350)
    seq = [p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13]
    canvas.polygon(seq, fill=(50, 50, 50), outline='black')


    # left side brown coat
    # top of left shoulder
    p0 = (355, 268)
    p1 = (330, 268)
    p2 = (310, 273)
    # arm fold/dip
    p3 = (290, 280)
    p4 = (255, 295)
    p5 = (250, 295)
    p6 = (240, 291)
    p7 = (220, 292)
    p8 = (170, 299)
    p9 = (120, 298)
    # left-most curved side of coat
    p10 = (60, 290)
    p11 = (45, 295)
    p12 = (43, 305)
    p13 = (45, 310)
    p14 = (50, 320)
    p15 = (80, 345)
    # sharp turn for underside of coat
    p16 = (60, 370)
    p17 = (50, 400)
    p18 = (70, 395)
    p19 = (100, 395)
    # dip on the underside of the coat
    p20 = (180, 408)
    p21 = (200, 410)
    p22 = (220, 408)
    p23 = (250, 405)
    p24 = (270, 400)
    p25 = (320, 380)
    p26 = (335, 350)
    # curve over shoulders
    p27 = (352, 300)
    p28 = (352, 280)
    p29 = (350, 270)
    p30 = (350, 270)
    seq = [p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26, p27, p28, p29, p30]
    canvas.polygon(seq, fill=(50, 50, 50), outline='black')



    '''
    Details on brown coat
    '''
    # left arm under coat
    p0 = (255, 295)
    p1 = (253, 296)
    # start of arm dent
    p2 = (220, 320)
    p3 = (210, 322)
    p4 = (195, 325)
    p5 = (120, 325)
    # other arm indent to right
    p6 = (205, 322)
    p7 = (260, 335) # last point of elbow indent
    seq = [p0, p1, p2, p3, p4, p5, p4, p3, p2, p6, p7, p6, p2]
    canvas.polygon(seq, fill=(50, 50, 50), outline='black')


    # left arm chicken wing
    p0 = (80, 345)
    p1 = (120, 380)
    p2 = (150, 390)
    p3 = (180, 390)
    p4 = (200, 385)
    p5 = (230, 378)
    p6 = (260, 360)
    p7 = (290, 325)
    p8 = (275, 360)
    p9 = (300, 335)
    seq = [p0, p1, p2, p3, p4, p5, p6, p7, p6, p8, p9, p8, p6, p5, p4, p3, p2, p1]
    canvas.polygon(seq, fill=(50, 50, 50), outline='black')



    '''
    BAMBOO
    '''
    # bamboo stick in mouth
    p0 = (355, 248)
    p1 = (435, 250)
    p2 = (433, 268)
    p3 = (355, 265)
    seq = [p0, p1, p2, p3]
    canvas.polygon(seq, fill=(103, 193, 118), outline = 'black')
    # red ribbon on bamboo stick
    p0 = (358, 255)
    p1 = (358, 260)
    p2 = (355, 260)
    p3 = (338, 253)
    p4 = (335, 250)
    seq = [p0, p1, p2, p3,p4 ]
    canvas.polygon(seq , fill = 'red', outline = 'black')



    '''
    FORWARD FOOT SOCKS
    '''

    # bottom ellipse sock forward foot
    x = 345
    y = 517
    w = 80
    h = 30
    xy = [(x, y), (x + w, y + h)]
    canvas.ellipse(xy, fill=(50, 50, 50))

    # middle ellipse sock forward foot
    x = 339
    y = 500
    w = 80
    h = 35
    xy = [(x, y), (x + w, y + h)]
    canvas.ellipse(xy, fill=(50, 50, 50))

    # 2nd to top ellipse sock forward foot
    x = 340
    y = 490
    w = 75
    h = 30
    xy = [(x, y), (x + w, y + h)]
    canvas.ellipse(xy, fill=(50, 50, 50))

    # highest sock ellipse forward foot
    x = 344
    y = 480
    w = 70
    h = 35
    xy = [(x, y), (x + w, y + h)]
    canvas.ellipse(xy, fill=(50, 50, 50))

    # lowest lowest sock
    x = 353
    y = 520
    w = 40
    h = 40
    xy = [(x, y), (x + w, y + h)]
    canvas.ellipse(xy, fill=(50, 50, 50))



    '''
    FORWARD SHOE
    '''
    # bottom left of shoe
    p0 = (365, 558)
    p1 = (395, 520)
    # tip of shoe
    p2 = (405, 517)
    p3 = (415, 516)
    # bottom side of shoe
    p4 = (425, 523)
    p5 = (426, 534)
    p6 = (390, 572)
    # back curve of shoe
    p7 = (375, 573)
    p8 = (369, 572)
    seq = [ p0, p1, p2, p3, p4, p5, p6, p7, p8]
    canvas.polygon( seq, fill = 'dimgrey', outline = 'black')


    '''TEXT'''

    coord = (25, 25)
    s = 'NEZUKO'
    yourFont = ImageFont.truetype(r'C:\Users\System-Pc\Desktop/arial.ttf', 70)
    canvas.text(coord, s, font = yourFont, fill='Pink')

    # return the art
    return im

if ( __name__ == "__main__" ) :

    im = picture()

    im.show()

    im.save( 'myart.jpg' )
