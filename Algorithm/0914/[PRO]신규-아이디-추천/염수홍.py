import re
def solution(new_id):
    # 1단계 
    new_id = new_id.lower() 
    
    # 2단계
    new_id = re.sub(r"[^a-zA-Z0-9-_.]","", new_id)
    
    # 3단계
    new_id = re.sub('(([.])\\2{1,})', '.', new_id)

    # 4단계
    new_id = new_id.strip('.')
    
    # 5단계
    if len(new_id) == 0:
        new_id = 'a'

    # 6단계
    new_id = new_id[:15]
    if new_id[-1] == '.':
        new_id = new_id[:-1]
        
    # 7단계
    if len(new_id) < 3:
        print(new_id)
        new_id  = new_id + (new_id[-1] * (3-len(new_id)))

    return new_id