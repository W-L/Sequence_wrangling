#Rscript to calculate the GC content of a sequence with a sliding window approach
args<-commandArgs(TRUE)

sequence_path<-args[1]
window_size<-as.numeric(args[2])
window_step<-as.numeric(args[3])

clean_seq<-function(seq_path){
    raw<-read.csv(seq_path,header=F)
    raw2<-raw[-1,]
    ifelse(dim(raw)[2]==2 | dim(raw)[2]==3,raw3<-raw2$V1,raw3<-raw2)
    clean_seq<-paste(raw3,collapse = "")
    return(clean_seq)
}

count_GC<-function(base){
    if(is.na(base)==T){return(0)}
    ifelse(base=="G" | base=="C" | base=="c" | base=="g",return(1),return(0))
}

GC<-function(seq,size,step){
    start<-1
    len<-nchar(seq)
    M<-matrix(ncol=1)

    while (start<len){
        win<-substr(seq,start=start,stop=start+size-1)
        win_sep<-strsplit(win,split="")
        win_sep1<-win_sep[[1]]
        win_n<-sapply(win_sep1,count_GC)
        win_res<-(sum(win_n)/length(win_n))*100
        M<-rbind(M,win_res)
        rownames(M)[length(rownames(M))]<-paste("win_",start,sep="")
        start<-start+step
    }
    tidy_names<-make.names(rownames(M))
    tidy_numbers<-unname(M[-1,1])
    M_frame<-data.frame(names=tidy_names[-1],GC=tidy_numbers)
    return(M_frame)
}

#run the two main functions
sequence<-clean_seq(seq_path = sequence_path)
GC_content<-GC(seq=sequence,size=window_size,step=window_step)
#get name for file
spl<-strsplit(sequence_path,"/")
spl2<-spl[[1]][length(spl[[1]])]

#either write to file or stdout

#write.table(GC_content,file=paste("size",window_size,"_","step",window_step,"_",spl2,".gc",sep=""),quote=F,row.names=F)
spl2
GC_content

#cleanup
rm(list=ls())
