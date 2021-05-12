import requests
import json
import urllib
file=open('C://Users//Noa Azuz//Desktop//Studies//KnowledgeAndData//matala-4//dests.txt', encoding='UTF-8') 
file=file.read()
city=file.splitlines()
address=str()
distance=dict()
api_key=
lst_km=list()#רשימה שתשמור בתוכה את כל המרחקים מתל אביב
location=dict()#ריספונס
Location=dict()
TLV_far_away=dict()
for place in city:# לולאה להבאת הנתנוים מהרשת ויצירת מילון עם המידע הרלוונטי
    address=place

    try:
        url="https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s"%(address,api_key)
        response=requests.get(url)
        if not response.status_code==200:#בדיקת הקוד לצורך הבנה היכן הבעיה 
            print("HTTP error", response.status_code)
        else:
            try: 
                location[address]=response.json()
                Location[address]=location[address]['results'][0]['geometry']['location']
            except:
                print("request false")
    except:
        print("request false")

    
    serviceurl='https://maps.googleapis.com/maps/api/distancematrix/json?'
    distance['origins']='תל אביב'
    distance['destinations']=address
    distance['key']=api_key
    url_1=serviceurl+urllib.parse.urlencode(distance)
    response_1=requests.get(url_1).json()
   
    info=tuple()#יצירת טאפל להכלת המידע 
    km=response_1['rows'][0]['elements'][0]['distance']['text']#נתיב להגעת המידע מהמילון שהתקבל
    time=response_1['rows'][0]['elements'][0]['duration']['text']
    #רוחב
    latitude=location[address]['results'][0]['geometry']['location']['lat']
    #אורך
    longitude=location[address]['results'][0]['geometry']['location']['lng']
    info=(km,time,'lat=',latitude,'lng=',longitude)#הכנסת המידע על המרחק בקילונטרים,זמן נסיעה, רוחב ואורך
    TLV_distance=dict()#יצירת מילון שיכיל את הטאפל
    
    TLV_distance[place]=info#מילון עבור כל עיר עם מילת קוד השווה לעיר והטאפל עם המידע הרלוונטי
#    print(TLV_distance)#הדפסת המילונים
    
    lst_distance=list()#יצירת רשימה שתחזיק בתוכנה את המילונים שיצרתי
    i=0   
    for place in city:#יצרתי רשימה עם המילונים שהתבקשתי להדפיס למסך כדי לשמור את המידע ושלא ידרס
        lst_distance.append(dict())
        lst_distance[i][place]=info
        i=i+1
    lst_km.append(km)#הוספת המרחק בקילומטר לרשימת המרחקים
    TLV_far_away[km]=address#מילון המחזיק בתוכו את שם מרחק העיר כמפתח ושם העיר כערך

farAway=0
VeryFar=0
far=list()#רשימה המחזיקה בתוכה את המרחקים הגדולים ביותר מתל אביב
j=0       
while len(far)<3:#היה צריך לבחור את 3 המחרקים הכי רחוקים 
    big=max(lst_km)#שמירת המקסימום מרחק מהרשימה
    if lst_km[j]==big :
        farAway=lst_km[j]#שמירת הערך הכי גבוה 
        VeryFar=farAway           
        lst_km.remove(farAway)#הורדת המקסימום שנמצא מרשימת הקילומטרים
        far.append(VeryFar)#הוספת המקסימות לרשימת המרחקים הגדולים מתא
    if j==len(lst_km)-1:#בכל פעם בגלל שאני מבצעת הסרה הגודל של רשימת הקילומטרים קטן
        j=0
    else:    
        j=j+1
p=0
while p<3:#לולאה שמתאימה בין המרחק הכי גדול לבין שם העיר שאותה מייצג
    if far[p] in TLV_far_away.keys():
        print(TLV_far_away[far[p]])
        p=p+1