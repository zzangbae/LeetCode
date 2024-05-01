class Solution(object):
    def validMountainArray(self, arr):
        
        # when arr.length == 1 -> How?
        l = len(arr)
        up = False
        down = False
        _switch = True  # up상황.
        for i in range(0, l - 1):
            # up
            if(_switch):
                if(arr[i] < arr[i + 1]):
                    up = True
                elif(arr[i] == arr[i + 1]):
                    return False
                else:
                    _switch = False
                    if(i == l - 2):
                        down = True
            # down
            else:
                if(arr[i] > arr[i + 1]):
                    down = True
                else:
                    return False
                
        
        if up and down:
            return True
        
        return False
                
                
                
                
                
                
        