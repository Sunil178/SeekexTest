import java.util.*;

public class MySolution{
    static class ball{
        int vol;
        int quantity;
        String color;
        ball(int vol){
            quantity = 0;
            vol = this.vol;
        }
        ball(int vol, int quantity){
            quantity = this.quantity;
            vol = this.vol;
        }
    }
    static void calc(HashMap<Character, Integer> buckets, HashMap<String, ball> hm){
        int allBalls = 0;
        int ballsUsed = 0;
        HashMap<Character, Integer> ans = new HashMap<>();
        for(char c = 'A'; c <= 'C'; c++){
            ans.put(c, 0);
        }
        int n = hm.size();
        ball[] ballVol = new ball[n];
        int i = 0;
        for(String color:hm.keySet()){
            ball temp = hm.get(color);
            ballVol[i] = new ball(temp.vol, temp.quantity);
            allBalls += temp.quantity;
            ballVol[i].quantity = temp.quantity;
            ballVol[i].vol = temp.vol;
            ballVol[i].color = color;
            i++;
        }
        char buck = 'A';
        Arrays.sort(ballVol, Comparator.comparingInt(a -> (a.vol * a.quantity)));
        int req = 0;
        for(int cap : buckets.values()){
            int tempCap = cap;
            int count = 0;
            HashMap<String, Integer> ballCount = new HashMap<>();
            for(int j = 0; j < n; j++){
                int currVol = ballVol[j].vol;
                int currNum = ballVol[j].quantity;
                
                if(currVol*currNum <= tempCap){
                    tempCap -= (currNum*currVol);
                    ballCount.put(ballVol[j].color, currNum);
                    ans.put(buck, ans.get(buck)+currNum);
                    ballVol[j].quantity = 0;
                    count += currNum;
                }
                else{
                    req = tempCap/currVol;
                    ballCount.put(ballVol[j].color, req);
                    ballVol[j].quantity -= req;
                    tempCap -= (req*currVol);
                    ans.put(buck, ans.get(buck)+req);
                    count += req;
                }
                if(tempCap == 0)
                    break;
            }
            System.out.println("=============");
            System.out.println(buck+":"+ans.get(buck));
            System.out.println(ballCount);
            buck++;
            ballsUsed += count;
        }
        if(ballsUsed == 0) {
            System.out.println("We cannot add this balls.");
        }else if(ballsUsed < allBalls) {
            System.out.println("We can add only "+req+" of this balls.");
        }
        System.out.println(ans);
    }
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        HashMap<String, ball> hm = new HashMap<>();
        HashMap<Character, Integer> buckets = new HashMap<>();
        for(char c = 'A'; c <= 'C'; c++){
            int capacity = s.nextInt();
            buckets.put(c, capacity);
        }
        while(true){
            String ballColor = s.next();
            int ballSize = s.nextInt();
            if(hm.size() == 3 && !hm.containsKey(ballColor)){
                System.out.println("balls full");
                break;
            }
            if(hm.containsKey(ballColor)){
                System.out.println("ball already exists");
            }else {
                ball temp = new ball(ballSize);
                temp.vol = ballSize;
                hm.put(ballColor, temp);
            }
        }
        while(true){
            String ballColor = s.next();
            if(ballColor.equals("-1"))
                break;
            int ballQuantity = s.nextInt();
            if(!hm.containsKey(ballColor)){
                System.out.println("ball not found");
                continue;
            }
            hm.get(ballColor).quantity += ballQuantity;
            calc(buckets, hm);
        }
    }
}