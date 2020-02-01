 string longestPalindrome(string s) {
        if(s.length()==0)
            return "";
        int n=s.length()*2 + 3;
        int k=0,C=0,R=0,P[n],i,mir;
        vector <char> a;
    
         a.push_back('$');
        P[0]=0;
        P[n-1]=0;
        for(i=1;i<n-1;i++)
        {
            P[i]=0;
            if(i%2==0)
                a.push_back(s[k++]);

            else
                a.push_back('#');
        }
        a.push_back('@');
        string str(a.begin(),a.end());
        cout<<str<<endl;
        for(i=1;i<n-1;i++)
        {
            mir=C*2 - i;
            if(i<R)
                P[i] = min(R-i,P[mir]);
            while(str[i+(P[i]+1)]==str[i-(P[i]+1)])
                P[i]++;
            if(P[i]>P[C])
            {
                C=i;
                R=i+P[i];
            }
             cout<<C<<" "<<P[i]<<endl; 
             
        }
        string temp = string(str.begin()+(C-P[C]),str.begin()+(C+P[C]));
     string res="";
        for(i=0;i<temp.length();i++)
        {
            if(temp[i]!='#')
                res = res + temp[i];
        }
        return res;
    }