class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] A = nums1,B = nums2;

        if(A.length>B.length){
            A = nums2;
            B = nums1;
        }

        int l = 0,r = A.length-1;
        int half = (A.length+B.length)/2;
        while(true){
            int i = l + (r - l)>=0?l + (r - l) / 2:-1;
            int i2 = half - i -2;
            int Aleft = i>=0?A[i]:Integer.MIN_VALUE;
            int Aright = i+1<A.length?A[i+1]:Integer.MAX_VALUE;
            int Bleft =     i2>=0?B[i2]:Integer.MIN_VALUE;
            int Bright = i2+1<B.length?B[i2+1]:Integer.MAX_VALUE;
            if(Aleft<=Bright && Bleft<=Aright){
                if((A.length+B.length)%2 ==0){
                    return ((double)Math.max(Aleft,Bleft)+Math.min(Aright,Bright))/2;
                } else {
                    return Math.min(Aright,Bright);
                }
            } else if (Aleft>Bright){
                r = i-1;
            } else {
                l = i+1;
            }
        }           
        // B=[1,2]
        // A=[3]
        // l,r             l   r
        // [3]             [1  2]
        //  m

        // 1-0-2

        // Aleft = 3
        // Aright inf

        // Bleft = -Inf
        // Bright = 1

        // r = -1
        // l = 0
        // -1/2





    //     1   2   3   4   5   6   7   8   9


    //         A                               B
        
        
    //         m
    //     l           r                   l   m           r
    //     [3  5   6   7]                  [1  2   4   8   9]

    //     4-1 -2= 1

    //     3,5

    //     1,2

    //     5<4 no 2<6 yes

    //     5<4 no -> move left 
    //     if Aleft>Bright -> move left
    //     else if Bleft>Aright  :
    //         move right


    //     l   m       r
    //     1   2   4   5               3


    //     l,r                 l   l
    //     3                   1   2   4   5



    // m = 2

    // 2-0-2

    // Aleft<2 no

    // r = -1

    // 0-1
    // -1/2
    // -1

    // 2+1-2 = 1




        
    }
}
