class Solution:
    def read(self, buf, n):
        buf4=['']*4
        read=0     #kepp track of read words
        while read<n:
            count= read4(buf4) #file ne read karse inot buff4 and count ni andar no.of char apse
            if not count:break  #condition will check ke tame end of file aii gaya ke nai
            count=min(count,n-read)  #je charcter baki che e read karva mate ni condition che
            buf[read:]=buf4[:count]  #buff4 na content buff ma apiya che
            read+=count
        return(read)
