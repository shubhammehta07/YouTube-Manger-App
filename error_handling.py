import json


def load_data():
    try:
        with open('youtube.txt','r') as file:
            return json.load(file)
        # mtlb file me jo data h usko load kroo
        #here all videos load in json formate
    except FileNotFoundError:
        return []  
    
def save_videos_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)
# json.dump() mtlb file me kyaa likhna haie...
        #videos likhna h or file me se likhna haie

def list_all_videos(videos):
    print('\n')
    print('*'*60)
    for index,video in enumerate(videos,start=1):
        print(f"{index} .{video['name']} duration :- {video['time']}")
    print('\n')
    print('*'*60)

def add_videos(videos):
    name=input("enter video name :-")
    time=input("Enter video duration time :-")
    videos.append({'name':name,'time':time})
    save_videos_helper(videos)

def update_videos(videos):
    list_all_videos(videos)
    index=int(input("Enter vedio number for updating :-"))
    if 1<=index <=len(videos):
        name=input('Enter vedio name :-')
        time=input('Enter video duration time :-')
        videos[index-1]={'name':name,'time':time}
        save_videos_helper(videos)
    else:
        print('Invalid Syntax')

def delete_videos(videos):
    list_all_videos(videos)
    index=int(input('Enter video number for deleting :-'))
    if 1<= index <=len(videos):
        del videos[index-1]
        save_videos_helper(videos)
    else:
        print('Invalid Synatx')

def main():
    videos=load_data()
    while True:
        print("\n Youtube Manger || chooose an option")
        print("1. List all youtube videos")
        print("2. Add a youtube videos")
        print("3. Update a youtube videos details")
        print("4. Delete a youtube videos")
        print("5. Exit a app ")
        choice=input("Enter your option :- ",)

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_videos(videos)
            case "3":
                update_videos(videos)
            case "4":
                delete_videos(videos)
            case '5':
                break
            case _:
                print("Invalid Syntax")


if __name__=="__main__":
    main()
