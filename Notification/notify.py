dataArray = [
    {
        "id": 30,
        "username": "Ruth.Nduta",
        "email": "ruthnduta891@gmail.com",
        "messages": [
            {
                "receipient_id": 45,
                "read": False,
                "user_id": 30
            },
            {
                "receipient_id": 3,
                "read": False,
                "user_id": 30
            },
            {
                "receipient_id": 112,
                "read": False,
                "user_id": 30
            }
        ]
    },
    {
        "id": 31,
        "username": "Pascaline.Chumba",
        "email": "pjerono56@gmail.com",
        "messages": []
    },
    {
        "id": 45,
        "username": "Josephbill",
        "email": "josephbill00@gmail.com",
        "messages": [
            {
                "msg_id": 3,
                "read": True,
                "user_id": 45
            }
        ]
    },
    {
        "id": 26,
        "username": "Simon.Thuo",
        "email": "simonthuo85@gmail.com",
        "messages": []
    },
    {
        "id": 112,
        "username": "Christine.Kiage",
        "email": "christinekiage@gmail.com",
        "messages": [
                  {
                "msg_id": 45,
                "read": False,
                "user_id": 27
            },
            {
                "msg_id": 3,
                "read": False,
                "user_id": 27
            },
            {
                "msg_id": 112,
                "read": False,
                "user_id": 27
            }
            ]
    }]

def solution(ArrayOfUsers,targetid):
       # ArrayCopy=[user for user in ArrayOfUsers]
        matching_recipients_id=[]        
        for i in range(len(ArrayOfUsers)):                                                                                                
         if ArrayOfUsers[i]["id"]==targetid:
             matching_data= ArrayOfUsers[i]["messages"]                          
             for a in range(len(matching_data)):
                 matching_recipients_id.append(matching_data[a]["receipient_id"])                 
                 for b in range(len(matching_recipients_id)):                                   
       
                      if ArrayOfUsers[i]["id"]==matching_recipients_id[b]:
                         print(ArrayOfUsers[i])
                   
        
# def order_by_key(data,key):    
    # return sorted(data, key=lambda x: x[key])
print(solution(dataArray,30)) 