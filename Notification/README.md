Company X has a mobile app with a chat feature interface preceded by a contacts list screen before accessing the chat screen.
This list has an issue with prompt notification i.e. when the logged-in user to the app access the list, no notification icons nor a tag index are indicating what messages may be unread from the different contacts. 
The list is generated using the following JSON response example. 
 [    {    id : 7 , name: “Joseph” , email: “josephbill00@gmail.com” , messages: [ ] } ,  { …… }  ]

Prepare an algorithm that fulfills the following notations : 
The JSON objects with unread messages should be ordered first i.e. a bias on whether the user list has unread messages belonging to the logged-in users 
                 -.  In the input block :: unread messages will be indicated as false , read messages will be represented as true or empty.
The assumption on the range is the JSON response can have 1…..n objects. 
The listing should be unique to the logged-in user.  



Sample Input 

Logged in user : id : 30 

JSON response without sort 
let dataArray = [
    {
        "id": 30,
        "username": "Ruth.Nduta",
        "email": "ruthnduta891@gmail.com",
        "messages": [
            {
                "receipient_id": 45,
                "read": false,
                "user_id": 30
            },
            {
                "receipient_id": 3,
                "read": false,
                "user_id": 30
            },
            {
                "receipient_id": 112,
                "read": false,
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
                "read": true,
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
                "read": false,
                "user_id": 27
            },
            {
                "msg_id": 3,
                "read": false,
                "user_id": 27
            },
            {
                "msg_id": 112,
                "read": false,
                "user_id": 27
            }
            ]
    }]


      


Expected output for user 30 on listing 


let dataArray = [
      {
        "id": 45,
        "username": "Josephbill",
        "email": "josephbill00@gmail.com",
        “Tag”: “unread”,
        "messages": [
            {
                "msg_id": 3,
                "read": true,
                "user_id": 45
            }
        ]
    },
    {
        "id": 112,
        "username": "Christine.Kiage",
        "email": "christinekiage@gmail.com",
        “Tag”: “unread”,
        "messages": [
                  {
                "msg_id": 45,
                "read": false,
                "user_id": 112
            },
            {
                "msg_id": 3,
                "read": false,
                "user_id": 112
            },
            {
                "msg_id": 20,
                "read": false,
                "user_id": 112
            }
            ]
    },


    {
        "id": 31,
        "username": "Pascaline.Chumba",
        "email": "pjerono56@gmail.com",
        "messages": []
        “Tag”: “unread”


    },


    {
        "id": 26,
        "username": "Simon.Thuo",
        "email": "simonthuo85@gmail.com",
        “Tag”: “read”,
        "messages": []
    }
   ]


def function(arrayofusers, targetid)

Function solution(arrayofusers,targetid)


Time complexity expectations : O(n) or O(log n)










—---------------------------------------------------------
